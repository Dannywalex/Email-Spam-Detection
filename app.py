import streamlit as st
import pickle
import os

vectorizer_path = r'C:\Users\MRS AKINBUSOYE\PycharmProjects\ML\email-spam Detection\pythonProject\vectorizer.pkl'
model_path = r'C:\Users\MRS AKINBUSOYE\PycharmProjects\ML\email-spam Detection\pythonProject\model.pkl'

# check if the required files exist
if os.path.exists(vectorizer_path) and os.path.exists(model_path):

 feature_extraction = pickle.load(open(vectorizer_path,'rb'))
 model = pickle.load(open(model_path,'rb'))
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
else:
 st.error("Required files are missing. Ensure 'vectorizer.pkl' and 'model.pkl' are in correct path.")
