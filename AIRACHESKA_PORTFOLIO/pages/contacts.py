import streamlit as st

st.set_page_config(page_title="📞 Contact", layout="wide")

# Beautiful Contact Styling
st.markdown("""
<style>
.contact-hero {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    padding: 3rem;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}
.contact-info {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 2rem;
    border-radius: 20px;
    margin: 1rem 0;
}
.sub-header {
    font-size: 2rem;
    color: #2563eb;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("# 📞 Contact Aira Cheska")

# Hero Contact Card
st.markdown("""
<div class="contact-hero">
    <h1>📱 Let's Connect!</h1>
    <h2>Aira Cheska Villamor</h2>
    <p><strong>BSCS 3rd Year | DEBESMSCAT</strong></p>
</div>
""", unsafe_allow_html=True)

# Contact Details
st.markdown('<h2 class="sub-header">📍 Contact Information</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="contact-info">
        <h3>📱 Mobile Number</h3>
        <h1><strong>0985-795-2537</strong></h1>
        <p>📲 Text or Call anytime!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-info">
        <h3>✉️ Email</h3>
        <h2><strong>villamorairacheska@gmail.com</strong></h2>
        <p>💌 Professional inquiries welcome</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="contact-info">
    <h3>📍 Address</h3>
    <p><strong>Jamorawon, Milagros<br>Masbate, Philippines</strong></p>
</div>
""", unsafe_allow_html=True)

# Interactive Contact Form
st.markdown('<h2 class="sub-header">💌 Send Message</h2>', unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("👤 Your Name", placeholder="Enter your name")
        email = st.text_input("📧 Your Email", placeholder="your.email@example.com")
    
    with col2:
        subject = st.selectbox("📋 Subject", 
                             ["General Inquiry", "Academic Collaboration", 
                              "Tech Project", "Just Saying Hi!"])
    
    message = st.text_area("💬 Message", 
                          placeholder="Hi Aira! I'd love to connect about...", 
                          height=150)
    
    col1, col2, col3 = st.columns([1,1,2])
    
    submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
    
    if submitted:
        if name and email and message:
            st.success("✅ **Message Sent Successfully!** 🎉")
            st.balloons()
            st.markdown(f"""
            **Thank you {name}!** 
            
            I'll reply to **{email}** within 24 hours 📧
            """)
        else:
            st.error("❌ Please fill in **all fields** before sending!")

# Social Links (Optional)
st.markdown("### 🔗 Find Me Online")
col1, col2 = st.columns(2)
with col1:
    st.info("📧 **Primary:** villamorairacheska@gmail.com")
with col2:
    st.success("📱 **Fastest:** 0985-795-2537")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <h3>© 2025 Aira Cheska Villamor</h3>
    <p>🎓 BSCS 3rd Year | DEBESMSCAT | Masbate</p>
</div>
""", unsafe_allow_html=True)