import tensorflow as tf
import numpy as np
import cv2

def load_model():
    return tf.keras.models.load_model("../Models/saved_model/")

def predict_image(img_bytes, model):
    arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224)) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return int(np.argmax(pred))
