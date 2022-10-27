import json
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
app=Flask(__name__)
## Load the model
MODEL_Path = 'classmodel.h5'
model = load_model(MODEL_PATH)
# scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data=request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
#     output=regmodel.predict(new_data)
#     print(output[0])
#     return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    # final_input=scalar.transform(np.array(data).reshape(1,-1))
    final_input = np.array(data).reshape(1,-1)
    print(final_input)
    output=regmodel.predict(final_input)[0]
    if output == 1:
        x = "86 percent chances of having heart disease"
    else:
        x = "86 percent chances of not having heart disease"
    return render_template("home.html",prediction_text="You have {}".format(x))

if __name__=="__main__":
    app.run(debug=True)