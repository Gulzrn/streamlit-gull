import os
import subprocess
import streamlit as st

# Start Flask app in the background
if "flask_started" not in st.session_state:
    st.session_state["flask_started"] = True
    subprocess.Popen(["python", "app.py"])

st.title("Flask + Streamlit Deployment")
st.write("Your Flask app is running on Heroku-style PaaS!")

st.markdown("[Open Flask App](http://localhost:5000)")
