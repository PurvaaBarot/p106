import plotly_express as px
import csv
import numpy as np

def getdatasource(path):
    x=[]
    y=[]
    with open (path) as f:
        data=csv.DictReader(f)
        
        for i in data:
            x.append(float(i["Coffee"]))
            y.append(float(i["sleep"]))

    return {"xdata" : x, "ydata" : y}

def findcorelation(data):
    c=np.corrcoef(data["xdata"] , data["ydata"])
    print("corelation coeficient is= ", c[0][1])         

def setup():
    path="cups of coffee vs hours of sleep.csv"  

    data=getdatasource(path)
    findcorelation(data)

setup()         