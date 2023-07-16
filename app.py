import streamlit as st
from PIL import Image, ImageFilter
import os

# create a folder image
if not os.path.exists('images'):
    os.makedirs('images')

def save_images(image):
    img = Image.open(image)
    img.save(f'images/{image.name}.png')

st.title(' Image Processing App')

upload = st.file_uploader(
    label='upload your image',
    type=['png','jpg','jpeg']
) 
if upload is not None:
    save_images(upload)
    img =Image.open(upload)
    coll,col2 = st.columns(2)

        
    
    filters = ['contour','emboss','edge_enhance','blur','smooth','sharpen']
    option = st.sidebar.selectbox( 'Select a filter',filters)
    coll.image( upload,caption='Uploaded /image', use_column_width=True)
    if option == 'contour':
        col2.image(img.filter(ImageFilter.CONTOUR), caption='Contour Filter', use_column_width=True)
    if option == 'emboss':
        col2.image(img.filter(ImageFilter.EMBOSS), caption='Emboss Filter', use_column_width=True)
    if option == 'blur':
        col2.image(img.filter(ImageFilter.BLUR), caption='Blur Filter', use_column_width=True)
    if option == 'smooth':
        col2.image(img.filter(ImageFilter.SMOOTH), caption='Smooth Filter', use_column_width=True)
    if option == 'sharpen':
        col2.image(img.filter(ImageFilter.SHARPEN), caption='Sharpen Filter', use_column_width=True)
    if option == 'edge_enhance':
        col2.image(img.filter(ImageFilter.EDGE_ENHANCE), caption='Edge_enhance Filter', use_column_width=True)
