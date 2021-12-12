from flask import Flask, jsonify, request
import pandas as pd

import config as cfg
import pipeline_predict as pp

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify({"username": "garg"})

#Ruta pred
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #cambiar nombre
    data = data[cfg.FEATURES]

    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": resultado})