import streamlit as st
from utils import page_header
from blog_generator import generative_blog
st.set_page_config(page_title= "AI Blog Generator ",page_icon= "📝" ,layout =  "wide")
page_header()
topic = st.text_input("topic")
tone = st.selectbox("Tone" ,
                    ["Professional" ,"Friendly" ,"Technical" ,"Funny","Motivational"])

length = st.selectbox("Length" ,
                    ["short" ,"Medium","Long"])
audience = st.selectbox("Audience",
                        ["Students" ,"Developers" ," Researches ", "Business Owner","General Public"])
temperature = st.slider("Temperature" ,0.0,1.0,0.7,0.1)
if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a topic. ")
    else:
        with st.spinner("Generating..."):
            result = generative_blog(topic,tone,length,audience,temperature)
        st.markdown(result)