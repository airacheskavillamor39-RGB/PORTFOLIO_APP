import streamlit as st
from datetime import date

st.set_page_config(page_title="👩 About", layout="wide")

# Custom Styling
st.markdown("""
<style>
.info-card {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 2.5rem;
    border-radius: 20px;
    color: white;
    margin: 1rem 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.personal-card {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    padding: 2.5rem;
    border-radius: 20px;
    color: white;
}
.sub-header {
    font-size: 2rem;
    color: #2563eb;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# 👩 About Aira Cheska Villamor")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="personal-card">
        <h2>📋 Personal Information</h2>
        <h3><strong>Aira Cheska Villamor</strong></h3>
        <p><strong>🎂 Birthdate:</strong> July 11, 2005</p>
        <p><strong>👶 Age:</strong> 20</p>
        <p><strong>📍 Address:</strong></p>
        <p><em>Jamorawon, Milagros<br>Masbate</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h2>🎓 Academic Background</h2>
        <h3><strong>Bachelor of Science in Computer Science</strong></h3>
        <p><strong>🏫 School:</strong> DEBESMSCAT</p>
        <p><strong>📚 Year Level:</strong> 3rd Year</p>
        <p><strong>📍 Location:</strong> Masbate, Philippines</p>
    </div>
    """, unsafe_allow_html=True)

# Interactive Age Calculator
st.markdown('<h2 class="sub-header">🎂 Age Calculator</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    birth_year = st.number_input("Birth Year", 2000, 2010, 2005)
with col2:
    birth_month = st.select_slider("Birth Month", options=range(1,13), value=7)
with col3:
    birth_day = st.number_input("Birth Day", 1, 31, 11)

if st.button("Calculate Age 🎈"):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    st.balloons()
    st.success(f"🎉 You're **{age} years old**!")
    st.metric("Exact Age", f"{age} years")

# Interests & Hobbies
st.markdown('<h2 class="sub-header">💖 Interests</h2>', unsafe_allow_html=True)

interests = [
    "💻 Coding & Programming",
    "📚 Learning new technologies", 
    "🌴 Beach trips in Masbate",
    "🎵 Music & Lo-fi",
    "☕ Coffee & studying"
]

for interest in interests:
    st.success(interest)

st.markdown("---")
st.info("👩‍🎓 Passionate BSCS student ready to make an impact! 🚀")