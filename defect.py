import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL import Image

st.set_page_config('DEFECT AI', page_icon='🤡', layout='wide')

st.title("AI POWERED DEFECT ANALYSIS🤖 AI Assistant🦅 ")
st.header(":blue[Prototype of automated structural defect analyzer using AI]🗝️")
st.subheader(':red[AI powered structural defect analysis using Streamlit that allows users to upload the image of ant structural defects and to get suggestions and recommendations for repar and rebuilt]🐍' )

with st.expander('About the app'):
    st.markdown(f'''This app helps to detect the defects like cracks, misalignments and provide 
                - **Defect Detection**
                - **Recommendation**
                - **Suggestions for improvements** ''')
    
import os

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)
input_image = st.file_uploader('Upload your file here ⤷', 
                 type = ['png', 'jpeg', 'jpg'])

img = ''

if input_image:
    img = Image.open(input_image).convert('RGB')
    st.image(img, caption="Uploaded successfully✅")
    
    
prompt = f''' You are an quality and civil engineer. You need to analyze the input image and provide necessary details
for the below questions in bullet points(maximum 3 points for each question)

1.Identify the type of structural defect in the given image like cracks, bends..
2.When does cracks like this appear?
3.Explain the severity level of cracks like this.
4.Can it be repaired?
5.What measures can be taken to avoid such incidents in future?
6.Analyse if these cracks can cause future problems.
7.Give suggestions to repair the cracks without any complications.
8.Does cost plays a important factor in appearence of these kind of cracks? explain.
9.Estimate the cost of total repair of the defect in Rupees.
10.List out the materials to fix the defect.'''

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def generative_result(prompt, img):
    result = model.generate_content(f''' Using the given {prompt}
                                  and give the image {img}
                                  analyze te=he image and give the results as per
                                  the given prompt''')

    return result.text

submit = st.button('Analyze the image 🤖')

if submit:
    with st.spinner('Results loading...'):
        response = generative_result(prompt, img)
        
        st.markdown('## :green[Results]')
        st.write(response)