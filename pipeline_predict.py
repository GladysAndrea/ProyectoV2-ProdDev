import joblib
import config as cfg
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
Target_model = joblib.load('Target_pipeline.pkl')

#Funcion para hacer predicciones.
def predict(X):
    predicts = Target_model.predict(X)
    salida = np.exp(predicts)
    print(salida)
    return salida[0]

#predict(X_test)