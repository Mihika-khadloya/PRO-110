import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

def RandomSet(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=st.mean(dataSet)
    return mean

def ShowFig(meanList):
    df=meanList
    mean=st.mean(df)
    fig=ff.create_distplot([df],["result"],show_hist=False)
    fig.show()

def Setup():
    meanList=[]
    for i in range(0,100):
        means=RandomSet(30)
        meanList.append(means)
    ShowFig(meanList)

Setup()
    
