import os
import sys
import numpy as np 
import pandas as pd
import flask
from flask import Flask, render_template #https://stackoverflow.com/questions/46785507/python-flask-display-image-on-a-html-page/46794505
import pickle
import matplotlib.pyplot as plt
import urllib3
from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')

def index():
 return flask.render_template("index.html")

def ValuePredictor(to_predict_list): 
 to_predict = np.array(to_predict_list) 
 loaded_model = pickle.load(open("model.pkl", "rb"))
 result = loaded_model.predict(to_predict)
 return result[0]

@app.route("/predict", methods = ['POST'])
def result():
 if request.method == 'POST':
    to_predict_list = request.form.to_dict()
    to_predict_list=list(to_predict_list.values())
    print(to_predict_list) #Prints the URLs of the pictures. 
    #result = ValuePredictor(to_predict_list)

    
 return render_template("predict.html", prediction=to_predict_list[0], test=to_predict_list[1])

if __name__ == "__main__":
 app.run(debug=True)