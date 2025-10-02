import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="SDG9 Assistant", page_icon="💬")

st.title("💬 SDG9 Assistant")
st.write("Chat with the bot about resilient infrastructure, sustainable industrialization, and innovation.")

# Dialogflow Messenger embed
html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
    <df-messenger
      intent="WELCOME"
      chat-title="SDG9_Assistant"
      agent-id="371cfe48-d365-4014-8a1a-d60b773b460a"
      language-code="en">
    </df-messenger>
    """,
    height=500,
)
