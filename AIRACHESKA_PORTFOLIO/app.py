import streamlit as st

st.set_page_config(
    page_title="Aira Cheska Villamor - Portfolio", 
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
.main-header {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 1rem;
}
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🎓 Aira Cheska Villamor</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <h2>👋 Welcome to My Portfolio</h2>
    <p><strong>3rd Year BSCS Student | DEBESMSCAT</strong></p>
    <p>📍 Jamorawon, Milagros, Masbate</p>
    <p>💻 Passionate about Computer Science & Technology</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Navigate using the sidebar** 📂

**Pages included:**
- 🏠 **Home** - Introduction & Quick Info
- 👩 **About** - Personal & Academic Details  
- 📞 **Contact** - Get in touch with me!

---
**✨ BSCS 3rd Year Student Portfolio - Made with Streamlit**
""")

st.balloons()