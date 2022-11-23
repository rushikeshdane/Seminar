import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import json

df = pd.read_csv('seminar.csv')

st.sidebar.subheader('Evalution Metrics')
st.sidebar.write('1) Presentation of Topic')
st.sidebar.write('2) Communication ')
st.sidebar.write('3) Practical Implementaion ')
st.sidebar.write('4) Accuracy and Depth of Knowledge')

st.sidebar.warning('Note : There is no particular date given for any topic , seminar will be conducted sequentially and you need to be present in each seminar')
st.header('  BADS 501 Third Semester Evalution -2022')
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("111489-teach.json")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",height=220
)


def Table(df):
    fig=go.Figure(go.Table( columnorder = [1,2,3,4],
          columnwidth = [10,28],
            header=dict(values=[' Sr No.','Name','Topic','Subject'],
                        line_color='black',font=dict(color='black',size= 19),height=40,
                        fill_color='#dd571c',#
                        align=['left','center']),
                cells=dict(values=[df['Sr No.'],df.Name, df.Topic ,df.Subject],
                       fill_color='#ffdac4',line_color='grey',height=25,
                           font=dict(color='black', family="Lato", size=16),
                       align='left')))
    fig.update_layout(height=1500, title ={'text': "Seminar Topics", 'font': {'size': 22}},title_x=0.5
                     )
    return st.plotly_chart(fig,use_container_width=True)

Table(df)