import streamlit as st
from openai import OpenAI

client = OpenAI()

football_map = {
    'Jersey': "fan made jersey", 
    'Playing Card': "football card",
    'Poster': "poster",
}

cricket_map = {
    'Jersey': "fan made jersey", 
    'Playing Card': "cricket card",
    'Poster': "poster",
}


def page1():
    st.title("OpenAI Sports Fan Art Generator")
    st.info("""
            This app generates posters, fan made jerseys and playing card concepts for Cricket and Football.\
            
            ### Usage Information
            - You can create fan art for **Indian Premier League** 🏏 and **UEFA Champions League** ⚽ teams.
            - You can create **fan made jerseys** 👕 , **playing cards** 🎴 and **posters** 🖼️.
            - The supported image sizes are 1024x1024, 1024x1792 amd 1792x1024.
            - You can create upto 4 images at once and the app also accepts special requests if you have any.
            - Currently this app has all the IPL teams and some of the UCL teams.  
            """)
    
    st.image('demo.png')

def page2():
    st.title("Champions League Fan Art Generator ⚽")
    st.info("""#### NOTE: You can download images by \
            right clicking on the image and selecting save image as option.""")
    
    with st.form(key="form"):
        team = st.selectbox("Enter your favorite team: ", ('Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich', 'Paris Saint Germain', 'Juventus', 'AC Milan', 'Inter Milan', 'Borussia Dortmund'))
        type = st.selectbox("What kind of fan art do you want?", ('Jersey', 'Playing Card', 'Poster'))
        extraprompt = st.text_input(label="Any special requests (Optional)")
        size = st.selectbox("Select size of the images", ('1024x1024', '1024x1792', '1792x1024'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='Submit')

    prompt = f"""Generate a {football_map[type]} for a player from {team} in the UEFA Champions League."""

    for idx in range(num_images): 
        if submit_button:
            if team:
                response = client.images.generate(
                model="dall-e-3",
                prompt=prompt+extraprompt,
                size=size,
                quality="standard",
                n=1,
                )


                image_url = response.data[0].url
                st.image(image_url, caption=f"Generated image: {idx+1}")


def page3():
    st.title("IPL Fan Art Generator🏏")
    st.info("""#### NOTE: You can download images by \
            right clicking on the image and selecting save image as option.""")
    
    with st.form(key="form"):
        team = st.selectbox("Enter your favorite team: ", ('Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore', 'Delhi Capitals', 'Punjab Kings', 'Sunrisers Hyderabad', 'Kolkata Knight Riders', 'Gujarat Titans', 'Rajasthan Royals', 'Lucknow Super Giants'))
        type = st.selectbox("What kind of fan art do you want?", ('Jersey', 'Playing Card', 'Poster'))
        extraprompt = st.text_input(label="Any special requests (Optional)")
        size = st.selectbox("Select size of the images", ('1024x1024', '1024x1792', '1792x1024'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='Submit')

    prompt = f"""Generate a {cricket_map[type]} for a player from {team} in the Indian Premier League."""

    for idx in range(num_images): 
        if submit_button:
            if team:
                response = client.images.generate(
                model="dall-e-3",
                prompt=prompt+extraprompt,
                size=size,
                quality="hd",
                style="vivid",
                n=1,
                )


                image_url = response.data[0].url
                st.image(image_url, caption=f"Generated image: {idx+1}")
