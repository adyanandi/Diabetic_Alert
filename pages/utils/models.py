# This file provides functions for loading machine learning models, making predictions,
# and loading model accuracies from a JSON file 

import os
import pickle
import numpy as np
import json
from tensorflow.keras.models import load_model as keras_load_model
import streamlit as st
import lightgbm

def load_model(comb):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, '..', 'models', 'modelPima')
    model_path_pkl = os.path.join(models_dir, f'model_{"_".join(comb)}.pkl')
    model_path_h5 = os.path.join(models_dir, f'model_{"_".join(comb)}.h5')

    if os.path.exists(model_path_pkl):
        with open(model_path_pkl, 'rb') as f:
            model = pickle.load(f)
        return model
    elif os.path.exists(model_path_h5):
        model = keras_load_model(model_path_h5)
        return model
    else:
        st.error("Model for the selected feature combination does not exist.")
        return None
    
def predict_diabetes(model, features):
    features_array = np.array([features])
    prediction = model.predict(features_array)
    return prediction


 
def load_accuracies(json_file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, '..', 'models')
    file_path = os.path.join(models_dir, json_file)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    with open(file_path, 'r') as file:
        return json.load(file) 