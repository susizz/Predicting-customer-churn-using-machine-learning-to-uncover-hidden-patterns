# 📉 Predicting Customer Churn Using Machine Learning

This project uses machine learning to predict whether a customer will churn based on historical data. By identifying churn patterns, businesses can take proactive measures to retain customers. The project includes data processing, modeling using TensorFlow, and deployment through a Streamlit web application.

---

## 🚀 Technologies Used

- **Python 3.8+**
- **TensorFlow 2.x** – for building and training the neural network
- **Pandas, NumPy** – for data manipulation
- **Matplotlib, Seaborn** – for data visualization
- **Scikit-learn** – for preprocessing and evaluation
- **Streamlit** – for building and deploying the interactive web app
- **Joblib / Pickle** – for saving/loading the model

---

## 🧠 Model Overview (TensorFlow)

We built a deep learning model using TensorFlow with the following architecture:

- Input Layer (based on number of features)
- Dense Layers with ReLU activations
- Dropout layers for regularization
- Output Layer with Sigmoid activation for binary classification

Loss: `binary_crossentropy`  
Optimizer: `adam`  
Metrics: `accuracy`

The model is saved as `churn_model.h5` and loaded in `model.py`.

---

## 📁 Project Structure

