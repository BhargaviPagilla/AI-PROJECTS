import streamlit as st
from tutor import ask_tutor

st.set_page_config(page_title="AI Tutor",page_icon="🎓",layout="wide")

st.markdown("""
<style>
.main{background:#f8f9fb;}
.block-container{padding-top:2rem;}
.card{padding:20px;border-radius:12px;background:#ffffff;border:1px solid #ddd;}
</style>
""",unsafe_allow_html=True)

st.title("🎓 AI Tutor")
st.caption("Learn any topic with Google Gemini + LangChain")

c1,c2=st.columns([1,2])

with c1:
    st.markdown("### 📚 Learning Setup")
    subject=st.selectbox("Subject",["Machine Learning","Python","Java","Data Structures","DBMS","Operating Systems","Computer Networks","Mathematics"])
    topic=st.text_input("Topic","Neural Networks")
    difficulty=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])
    temp=st.slider("Creativity",0.0,1.0,0.4,0.1)

with c2:
    question=st.text_area("💬 Ask your question",height=180,placeholder="Explain backpropagation with an example.")
    if st.button("🚀 Ask AI Tutor",use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Teaching..."):
                ans=ask_tutor(subject,topic,difficulty,question,temp)
            st.success("Lesson Generated")
            st.markdown(ans)
            st.download_button("📥 Download Lesson",ans,file_name="lesson.md")
