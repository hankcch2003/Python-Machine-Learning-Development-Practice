import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

st.write("Hello StreamLit")
name = st.text_input("Enter your Name")
st.write(f"Hello {name}")


st.title("Number Input")
n1 = st.number_input("Enter first Number:", value = 0)
n2 = st.number_input("Enter Second Number:", value = 0)
sum_result = n1 + n2
st.write(f"The sum is : {sum_result}")


def colorIndex(colorData, findColor="紅色"):
    index = -1
    for i in range(len(colorData)):
        if colorData[i] == findColor:
            return i
    return index

st.title("請選元素")
data = ["紅色","藍色","綠色"]
option_selectbox = st.selectbox("你喜歡甚麼顏色：", ["紅色", "藍色", "綠色"])
st.write("你選擇的顏色是：", option_selectbox, colorIndex(data, option_selectbox))


st.title("Data Plot")
data = pd.DataFrame({"x": np.arange(1, 101), "y": np.random.randn(100).cumsum()})
st.line_chart(data)
st.line_chart(data, x = "x", y = "y")