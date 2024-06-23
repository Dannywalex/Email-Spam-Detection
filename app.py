import streamlit as st
import pickle



feature_extraction = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email Spam Detection")
input_email = st.text_input("Enter the message")

if st.button('Predict'):



  #1. preprocess
  input_mail = ["Ok lar... Joking wif u oni..."]
  #2.vectorize
  input_data_feature = feature_extraction.transform([input_email])
  #3.predict
  prediction = model.predict(input_data_feature)
  #4.Display
  if prediction[0] == 1:
   st.header("Not Spam")
  else:
   st.header("Spam")
