import streamlit as st
import requests #send data to AI

api_key = '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' #authentication key needed
api_link = "https://openrouter.ai/api/v1/chat/completions" #api acess website
headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"} #setup to allow your api key
#----------------------------------------------------


#FUNCTION TO SEND DATA TO OPENROUTER
def ask_ai(content):
   """Send prompt to AI and return only the text content."""
   data = {
       "model": "openai/gpt-3.5-turbo",
       "messages": [{"role": "user", "content": content}],
       "max_tokens": 250, #free version limited tokens
       "temperature": 0.7 #how real it looks
   }
   response = requests.post(api_link, headers=headers, json=data) #post means send data
   if response.status_code == 200:
       return response.json()['choices'][0]['message']['content']
   else:
       st.write('Error')




with st.sidebar:
    name = st.text_input('Enter your full name')
    st.divider()
    number = st.text_input('Enter your phone number')
    st.divider()
    address = st.text_input('Enter your home address')
    st.divider()
    if st.toggle('Email (Optional)'):
        email = st.text_input('Enter your email')

    if st.toggle('Photo (Optional)'):
        photo = st.file_uploader('Choose an image type', type=['jpg','jpeg','png'])

    st.divider()
    skills = st.text_area('Enter your key skills',placeholder='Examples: \nPhotography \nVideography \nArts and Craft \nPainting')
    st.divider()
    work = st.text_area('Enter your work experience',placeholder='Examples: \nSydney, Australia: 2010-2019 (Remote) \nBoston, US: 2020-2025')
    st.divider()
    education = st.text_area('Describe education',placeholder='Examples: \nUniversity of Idaho: Class of 2015 \nBritish Columbia: Class of 2019')



prof_summary = f'''
Design a professional summary for my CV. Make it 3-4 lines using the information given below
My key skills: {skills}
My work experience: {work}
My education: {education}




'''

skills_question = f'''create a bulleted list with just one line sentence for each skill provided below:
{skills}

'''
work_question = f'''

Create a professional description of my work expreience below using the format:
Employer/Organization
Start-end date
Job title
Responsibilities/Achievements (bullet points)
My work experience:

'''

education_question = f'''

Create an education outline in this format for each section:
Course Title
Start year - End Year
School or course provider
with information provided below, no prompt text
{education}

'''

if st.sidebar.button('Generate CV'):

    st.info('My Professional Summary')
    prof_reponse = ask_ai(prof_summary)
    st.write(prof_reponse)


    st.divider()
    st.info('My Key Skills')
    skills_reponse = ask_ai(skills_question)
    st.write(skills_reponse)


    st.divider()
    st.info('My Work Experience')
    work_reponse = ask_ai(work_question)
    st.write(work_reponse)

    st.divider()
    st.info('My Education')
    education_reponse = ask_ai(education_question)
    st.write(education_reponse)

