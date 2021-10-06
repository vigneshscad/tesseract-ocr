import streamlit as st
import cv2 
import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract' #for heroku setup
st.set_option('deprecation.showfileUploaderEncoding',False)           #avoid warnings
st.title("OCR  - Optical Character recognition")
st.text("Upload the image") 

uploaded_file = st.sidebar.file_uploader("Choose an image",type = {"jpg","jpeg","png"})
if(uploaded_file is not None):
  img = Image.open(uploaded_file)
  st.image(img, caption="Uploaded Image", use_column_width=True)
  st.write("")

  if(st.button('Predict')):
    st.write("Result")
    info = pytesseract.image_to_string(img)
    st.title(info)
