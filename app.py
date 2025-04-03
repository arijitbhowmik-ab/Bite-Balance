import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")
    
    
#initialize our streamlit app





# st.set_page_config(page_title="Calorie Checker App")
# st.header("BiteBalance")
# # input=st.text_input("Input Prompt: ",key="input")
# uploaded_file=st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
# image=""
# if uploaded_file is not None:
#     image=Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_container_width=True)
    
# submit=st.button("Tell me about total calories")

# input_prompt="""
# You are an expert in nutritionist where you need to see the food items from the image
#                and calculate the total calories, also provide the details of every food items with calories intake
#                is below format

#                1. Item 1 - no of calories
#                2. Item 2 - no of calories
#                ----
#                ----

# after that recmommend which type of exercise need to burn that calorie
#                1. Exercise 1
#                2. Exercise 2
#                -----
#                ----
# """

# if submit:
#     image_data=input_image_setup(uploaded_file)
#     response=get_gemini_response(input_prompt, image_data)
#     st.subheader("The Response is ....")
#     st.write(response)




# Page Configurations
st.set_page_config(page_title="Calorie Checker App", page_icon="🥗", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 100px !important;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
    }
    .stFileUploader {
        text-align: center;
    }
    .response-box {
        background-color: #fff3e0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<p class="title"> BiteBalance - Calorie Checker</p>', unsafe_allow_html=True)

# File Upload Section
uploaded_file = st.file_uploader("📸 Upload Your Meal Image:", type=["jpeg", "jpg", "png"])
image = ""

# Show Image Preview
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

# Submit Button
submit = st.button("🔍 Analyze Calories")

# Input Prompt for AI
input_prompt = """
You are an expert nutritionist. Analyze the food items in the image,
calculate total calorie intake, and provide details in this format:

1.  Item 1 - X calories  
2.  Item 2 - Y calories  
3.  Item 3 - Z calories  
---
 Suggested Exercises to Burn Calories:  
1.  Exercise 1  
2.  Exercise 2  
---
"""

# AI Processing and Response Display
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    
    st.subheader("Calorie Analysis:")
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)











### Health Management APP
# from dotenv import load_dotenv

# load_dotenv() ## load all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load Google Gemini Pro Vision API And get response

# def get_gemini_repsonse(input,image,prompt):
#     model=genai.GenerativeModel('gemini-1.5-flash')
#     response=model.generate_content([input,image[0],prompt])
#     return response.text

# def input_image_setup(uploaded_file):
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    
# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Health App")

# st.header("Gemini Health App")
# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image=""   
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)


# submit=st.button("Tell me the total calories")

# input_prompt="""
# You are an expert in nutritionist where you need to see the food items from the image
#                and calculate the total calories, also provide the details of every food items with calories intake
#                is below format

#                1. Item 1 - no of calories
#                2. Item 2 - no of calories
#                ----
#                ----


# """

# ## If submit button is clicked

# if submit:
#     image_data=input_image_setup(uploaded_file)
#     response=get_gemini_repsonse(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)

