import streamlit as st
import sqlite3
import os
import re
from datetime import datetime

# Title and branding
st.markdown("""
    <h1 style='text-align: center;'>🧠 DIV-AI: Private Smart Assistant</h1>
    <h3 style='text-align: center; color: gray;'>Your data stays on your device. 100% offline, fully private AI.</h3>
""", unsafe_allow_html=True)

# Set page config
st.set_page_config(page_title="DIV-AI", page_icon="🧠", layout="centered")

# Custom CSS for aesthetics
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Create or connect to SQLite database
conn = sqlite3.connect('div_ai_emails.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS user_emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        download_count INTEGER DEFAULT 0,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# Email validation
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Layout sections
page = st.sidebar.selectbox("Navigate", ["Home", "Download", "About", "Privacy Policy"])

if page == "Home":
    st.image("https://i.imgur.com/bjTlyF7.png", use_column_width=True)  # Placeholder image/logo
    st.markdown("""
        ## Welcome to DIV-AI
        **DIV-AI** is a locally running smart assistant designed for privacy, speed, and control.
        
        - ✅ 100% Offline AI Model (2.7B quantized)
        - 🔐 No cloud, no tracking, no surveillance
        - ⚡ Fast, light, and effective
        - 🧰 Works great for productivity, programming help, Q&A, and more

        ---
        #### 🔽 Go to the Download page to get started!
    """)

elif page == "Download":
    st.markdown("## Download DIV-AI")
    st.write("Enter your email to get the download link. This helps us keep track of installs.")

    email = st.text_input("Email address")
    submitted = st.button("Get Download Link")

    if submitted:
        if is_valid_email(email):
            c.execute("SELECT * FROM user_emails WHERE email = ?", (email,))
            result = c.fetchone()

            if result:
                c.execute("UPDATE user_emails SET download_count = download_count + 1, timestamp = CURRENT_TIMESTAMP WHERE email = ?", (email,))
            else:
                c.execute("INSERT INTO user_emails (email, download_count) VALUES (?, 1)", (email,))
            conn.commit()

            st.success("✅ Thank you! Here is your download link:")
            st.markdown("[📦 Download DIV-AI (Google Drive)](https://drive.google.com/file/d/1d0W5N6-Qeh13zZz0xxqUuM4A2rbSmdoB/view?usp=sharing)")
            st.info("**Download link is now available!** Click the button above to download from Google Drive.")
        else:
            st.error("❌ Please enter a valid email address.")

elif page == "About":
    st.markdown("## About DIV-AI")
    st.markdown("""
        DIV-AI is built for those who want the power of AI **without giving up privacy**.
        
        - ⚙️ Powered by Div_v1_Quant (offline 2.7B parameter model)
        - 🧠 Capable of code generation, logical reasoning, Q&A, etc.
        - 🖥️ No GPU required – runs on CPU using optimized quantization
        - 🛠️ Built using Python, GGUF, CTransformers, Tkinter GUI

        ---
        ### Developer
        - Name: Divyansh Pandiit
        - Email: divyanshpandiit@gmail.com

        [GitHub Repo](https://github.com/DivyanshPandit) | [Support](mailto:divyanshpandiit@gmail.com)
    """)

    try:
        st.image("path/to/your_photo.jpg", caption="Divyansh Pandiit", width=200)
    except:
        pass

elif page == "Privacy Policy":
    st.markdown("## 🔒 Privacy Policy")
    st.markdown("""
        **Your Privacy, Guaranteed**

        - This app runs completely **offline** on your machine
        - No data is sent to any external server or cloud
        - We only ask for your email to track download stats (stored securely)
        - We will never sell, share, or misuse your email

        If you have concerns or want your data removed, contact us at [divyanshpandiit@gmail.com](mailto:divyanshpandiit@gmail.com)
    """)

# Close connection
conn.close()
