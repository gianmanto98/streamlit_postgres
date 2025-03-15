import streamlit as st
from qwen_model import QwenGenerator

# Initialize the model
qwen = QwenGenerator()

st.title("Qwen Text Generator")

# User input for question
question = st.text_area("Enter your question:", "What is Big Thought's favorite color?")

# Generate response when button is clicked
if st.button("Generate Answer"):
    with st.spinner("Generating..."):
        response = qwen.generate_answer(question)
        st.success("Generated Answer:")
        st.write(response)

# Allow user to change max tokens
max_tokens = st.slider("Set Max Tokens", min_value=50, max_value=500, value=100, step=10)
qwen.set_max_tokens(max_tokens)

st.text(f"Current model: {qwen.get_current_model()}")
