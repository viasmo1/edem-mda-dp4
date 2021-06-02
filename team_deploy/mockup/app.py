# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:46:20 2021

@author: guill
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
import base64

# Aquí cargaríamos nuestros modelos

#model1 = pickle.load(open('iri.pkl', 'rb'))  # rb -> read and binary

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/prediction', methods=['POST'])
def home():
    imagebase64 = request.form['base64image']
    
    # Aquí guardaríamos el resultado (prediccion) de cada modelo:
    #pred = model1.predict(image)
    
    #Después creariamos un array con todos los resultados de los modelos
    
    return render_template('prediction.html', data=imagebase64)


if __name__ == "__main__":
    app.run(debug=True)



