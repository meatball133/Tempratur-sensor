from django.shortcuts import render
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from django.http import HttpResponse
from django.template import loader
import io
import base64
import numpy as np

Temperature = 69

def index(request):
    fahrenheit = fahrenheit_converter(Temperature)
    template = loader.get_template("./index.html")
    graph = plot()
    return HttpResponse(template.render({"temperature": Temperature, "fahrenheit": fahrenheit, "data": graph}, request))

def plot():
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,2.5))
    plt.style.use('seaborn-v0_8')
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([10, 15, 12, 11, 17, 19, 10])
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 40)
    Y_ = X_Y_Spline(X_)
    my_xticks = ['Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.xticks(x, my_xticks)
    plt.plot(X_, Y_)
    plt.ylabel('Temperature')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph



def fahrenheit_converter(temperature):
    return round((temperature - 32) * 1.8, 4)