from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageOps
import numpy as np
import onnxruntime as ort
import io
import base64

app = Flask(__name__)

# Charger le modèle ONNX
model_path = "mnist-12.onnx"
session = ort.InferenceSession(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données de l'image envoyée depuis la requête POST
    image_data = request.form['image']
    image_data = image_data.split(",")[1]  # Enlever l'en-tête 'data:image/png;base64,'
    image = Image.open(io.BytesIO(base64.b64decode(image_data))).convert('L')

    # Redimensionner l'image à 28x28 pixels pour correspondre au modèle MNIST
    image = image.resize((28, 28), Image.Resampling.LANCZOS)
    # Inverser les couleurs pour que le chiffre soit en blanc sur fond noir
    image = ImageOps.invert(image)
    # Normaliser l'image
    image = np.array(image).astype(np.float32) / 255.0
    # Redimensionner pour correspondre à l'entrée du modèle ONNX
    input_image = np.reshape(image, (1, 1, 28, 28))

    # Prédiction du modèle
    ort_inputs = {session.get_inputs()[0].name: input_image}
    ort_outs = session.run(None, ort_inputs)
    logits = ort_outs[0][0]  # Logits pour chaque classe de chiffre

    # Appliquer la fonction softmax pour obtenir des probabilités
    exp_logits = np.exp(logits)
    probabilities = exp_logits / np.sum(exp_logits)

    # Trouver la classe avec la probabilité la plus élevée
    predicted_digit = np.argmax(probabilities)
    prediction_confidence = probabilities[predicted_digit]

    # Retourner la prédiction au format JSON, avec toutes les probabilités
    return jsonify({
        'digit': int(predicted_digit),
        'confidence': float(prediction_confidence),
        'probabilities': probabilities.tolist()  # Convertir en liste pour JSON
    })

if __name__ == '__main__':
    app.run(debug=True)
