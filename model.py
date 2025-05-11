import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

# Load saved model
model = load_model("churn_model.h5")

def predict_churn(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0][0]
