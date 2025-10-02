import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="SDG9 Assistant", page_icon="💬", layout="centered")

st.title("SDG9 Assistant")
st.caption("Chat about resilient infrastructure, sustainable industrialization, and innovation.")

# Minimal HTML: Dialogflow Messenger embed
agent_id = "371cfe48-d365-4014-8a1a-d60b773b460a"  # your agent id

html(f"""
  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
  <df-messenger
    intent="WELCOME"
    chat-title="SDG9_Assistant"
    agent-id="{agent_id}"
    language-code="en">
  </df-messenger>
""", height=80)

st.write("Tip: Try **“What is SDG 9?”**, **“Assess my factory”**, or **“Funding”**.")
