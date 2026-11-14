import streamlit as st

def show_about():
    st.title("About ELI-X")
    st.markdown("""
        ### ELI-X: Explain Like I'm X

        ELI-X is an interactive web application built with Streamlit and powered by Google's Gemini AI. 
        Its mission is to make the world's most complex information accessible to everyone by breaking it down 
        into clear, simple, and understandable explanations—perfect for curious minds of any age.

        Whether you're trying to grasp abstract scientific concepts, understand how everyday technology works, 
        or simply want a straightforward answer to a complicated question, ELI-X delivers simplified summaries 
        in seconds.

        **Key Features:**
        - **Simple Explanations:** Tailored to be easily understood, regardless of the topic.
        - **AI-Powered:** Utilizes the advanced Gemini model for accurate and concise content.
        - **User-Friendly:** An intuitive interface designed for quick and easy interaction.
        - **Extensive Knowledge:** Explore topics with our dynamic example prompts.
        - **Streaming Responses:** Get answers instantly as they are generated.
    """)
    st.markdown("---")
    st.markdown("Made by [bruzz-bruzz](https://github.com/bruzz-bruzz)")

show_about()
