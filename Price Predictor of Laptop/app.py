import streamlit as st
import pickle
import numpy as np


model=pickle.load(open("model.pkl","rb"))
data=pickle.load(open("data.pkl","rb"))

st.title("Laptop Price Predictor")

#brand
company=st.selectbox("Brand",data["Company"].unique())

#type
type=st.selectbox("Type",data["TypeName"].unique())

#Ram
ram=st.selectbox("Ram",[2,4,6,8,16,32,64])

#weight
weight=st.number_input("Weight of laptop")

# Touchscreen
TouchScreen=st.selectbox("TouchScreen",["No","Yes"])

#ips
IPS=st.selectbox("IPS",["No","Yes"])

#ppi
screen_size=st.number_input("Screen_Size")

#resolution
resolution=st.selectbox("Resolution",['1366x768' , '1600x900' , '1920x1080' ,   '2560x1440','2560×1600','2880×1800','3000x2000','3200x1800','3840x2160']) 

#cpu
cpu=st.selectbox("CPU",data["Cpu"].unique())

#gpu
gpu=st.selectbox("GPU",data["Gpu"].unique())

#os
OpSys=st.selectbox("OpSys",data["OpSys"].unique())

#hdd
hdd=st.selectbox("HDD",data["HDD"].unique())

#ssd
ssd=st.selectbox("SSD",data["SSD"].unique())

if st.button("predict Price"):
    PPI=None
    if TouchScreen=="Yes":
        TouchScreen=1
    else:
        TouchScreen=0
    if IPS =="Yes" :
        IPS=1
    else:
        IPS=0
    
    X_res=int(resolution.split("x")[0])
    Y_res=int(resolution.split("x")[1])

    PPI = (((X_res**2) + (Y_res**2))**0.5)/screen_size
    

    query=np.array([company ,type ,	cpu ,ram ,	gpu ,	OpSys ,	weight 	, 	TouchScreen ,PPI,	IPS  ,	hdd ,	ssd])
    query=query.reshape(1,12)
    st.title("The Predicted Price of Laptop is " + str(int(np.exp(model.predict(query)[0]))))









