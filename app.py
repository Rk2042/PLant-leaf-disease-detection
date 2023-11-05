# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name)

# Load your ML models here
model1 = tf.keras.models.load_model("my_model.h5")
model2 = tf.keras.models.load_model("my_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    # Receive image data from the frontend
    image_data = request.files['image'].read()
    image = process_image(image_data)  # Implement image preprocessing as needed

    # Use your models for prediction
    prediction1 = model.predict(image)
    prediction2 = model.predict(image)

    return jsonify({
        'model1_prediction': prediction1.tolist(),
        'model2_prediction': prediction2.tolist()
    })

if __name__ == '__main__':
    app.run()
