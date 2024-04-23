import streamlit as st
import openai
from openai import AsyncOpenAI
from openai import OpenAI
import os
import time

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=st.secrets["API_key"],
)

async def generate_response(question, context):
    model = "gpt-4-0125-preview"
    #model - "gpt-3.5-turbo"

    completion = await client.chat.completions.create(model=model, 
        messages=[{"role": "user", "content": question}, 
                {"role": "system", "content": context}])
    return completion.choices[0].message.content


async def app():
    # Create two columns
    col1, col2 = st.columns([1, 4])

    # Display the image in the left column
    with col1:
        st.image("wvsu-logo.jpg")

    # Display the title in the right column
    with col2:
        st.title("A Teaching Co-pilot Powered by OpenAI")

    with st.expander("Click to display developer information."):
        text = """Prof. Louie F. Cervantes, M. Eng. (Information Engineering) \n
            CCS 229 - Intelligent Systems
            Department of Computer Science
            College of Information and Communications Technology
            West Visayas State University
            """
        st.text(text)
        link_text = "Click here to visit [openAI](https://openai.com)"
        st.write(link_text)

    context = """You are a teaching co-pilot designed to assist educators in various classroom tasks. 
    When responding to prompts, prioritize providing resources and strategies that directly benefit teachers.
    Remember, your primary function is to empower teachers and enhance their effectiveness in the classroom."""


    st.subheader("Empower Your Teaching with AI! The OpenAI Teacher Copilot")
    text = """Unleash creativity and personalize learning in your classroom with 
    the OpenAI Teacher Copilot, a revolutionary data app powered by OpenAI's 
    cutting-edge large language model, ChatGPT 4. This AI co-pilot 
    equips educators with a treasure trove of ideas and resources to spark 
    student engagement, tackle challenging concepts, differentiate instruction, 
    design formative assessments, and seamlessly integrate technology into 
    lessons, all while saving educators time and boosting their teaching potential."""
    st.write(text)

    options = ['K1', 'K2', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 
    'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
  
    yearlevel = st.selectbox(
    label="Select year level:",
    options=options,
    index=7  # Optionally set a default selected index
    )

    topic = st.text_input("Please input the topic: ")

    options = ['Generate engaging learning activities', 
    'Suggest alternative explanations for a concept students find challenging', 
    'Provide differentiation strategies to cater to learners with varying needs',
    'Create formative assessment ideas to gauge student understanding',
    'Offer resources for incorporating technology into the classroom']
    
    # Create the combobox (selectbox) with a descriptive label
    selected_option = st.selectbox(
    label="Choose a task for the teaching co-pilot:",
    options=options,
    index=0  # Optionally set a default selected index
    )

    question = selected_option + " for year level " + yearlevel + " on topic " + topic

    # Create a checkbox and store its value
    checkbox_value = st.checkbox("Check this box to input a custom prompt.")

    # Display whether the checkbox is checked or not
    if checkbox_value:
        # Ask the user to input text
        question = st.text_input("Please input a prompt (indicate year level and topic): ")

    # Button to generate response
    if st.button("Generate Response"):

        if question and context:            
            if topic:

                progress_bar = st.progress(0, text="The AI teacher co-pilot is processing the request, please wait...")
                response = await generate_response(question, context)
                st.write("Response:")
                st.write(response)

                # update the progress bar
                for i in range(100):
                    # Update progress bar value
                    progress_bar.progress(i + 1)
                    # Simulate some time-consuming task (e.g., sleep)
                    time.sleep(0.01)
                # Progress bar reaches 100% after the loop completes
                st.success("AI teacher co-pilot task completed!") 
            else:
                st.error("Please enter a topic.")   
        else:
            st.error("Please enter both question and context.")

#run the app
if __name__ == "__main__":
    import asyncio
    asyncio.run(app())
