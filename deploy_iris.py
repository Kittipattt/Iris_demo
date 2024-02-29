import pickle
import warnings

import streamlit as st

warnings.filterwarnings("ignore")
from PIL import Image

pickle_in = open("model_iris.pkl","rb")
classifier = pickle.load(pickle_in)

def predict_iris_variety(sepal_lenght,sepal_width,petal_lenght,petal_width):
    prediction = classifier.predict([[sepal_lenght,sepal_width,petal_lenght,petal_width]])
    print(prediction)
    return prediction

def Input_Output():
    st.title("Iris Variety Prediction")
    st.image("https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.lac.inpe.br%2F~rafael.santos%2FDocs%2FCAP394%2FWholeStory-Iris.html&psig=AOvVaw0dHqp9AXzkHOyhGO6pEE1L&ust=1709288407697000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNDz29Sp0IQDFQAAAAAdAAAAABAE", width=600)
    
    st.markdown("You are using Streamlit...",unsafe_allow_html=True)
    sepal_lenght = st.text_input("Enter Sepal Lenght" , ".")
    sepal_width = st.text_input("Enter Sepal Width" , ".")
    petal_lenght = st.text_input("Enter Petal Lenght" , ".")
    petal_width = st.text_input("Enter Petal Width" , ".")
    
    result = ""
    if st.button("click here to Predict"):
        result = predict_iris_variety(sepal_lenght, sepal_width, petal_lenght, petal_width)
        st.balloons()
    st.success('The output is {}'.format(result))
    
if __name__ == '__main__' :
    Input_Output()     