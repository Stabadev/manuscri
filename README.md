# Flask Drawing Application

This is a Flask-based web application that allows users to draw digits on a canvas and get predictions on which digit they have drawn. The application also includes a history feature where users can save their drawings and mark predictions as correct or incorrect.

## Features

- **Draw Digits**: Users can draw digits on a canvas using their mouse.
- **Real-time Prediction**: The app predicts the drawn digit in real-time using a pre-trained ONNX model.
- **Prediction History**: Users can save their drawings to a history with the associated prediction, and mark the prediction as correct or incorrect.
- **Interactive Interface**: Users can clear the canvas or save their drawing with dedicated buttons.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Flask
- onnxruntime
- Pillow

### Steps

1. Clone the repository:
    ```bash
    git clone https://your-repository-url.git
    cd your-repository-directory
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000` to use the application.

## Usage

- Draw a digit on the canvas.
- Click **"Terminé"** to save your drawing to the history.
- Click **"Effacer"** to clear the canvas without saving.
- Review your prediction history and mark predictions as correct or incorrect.

## Deployment

To deploy this application on a server or service like Heroku, you need to:

1. Prepare the application for deployment by adding a `Procfile`, `requirements.txt`, and configuring your `app.py` file for production.

2. Deploy the application following the specific service's deployment instructions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

