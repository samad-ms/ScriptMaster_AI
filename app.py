import streamlit as st
from utils import generate_script

# Applying Styling
st.markdown("""
<style>
    .main-container {
        max-width: 800px;
        margin: auto;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
    }
    .header-title {
        color: #333333;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #007bff;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        cursor: pointer;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stSlider > div {
        padding-top: 1rem;
    }
    .sidebar-container {
        background-color: #f0f0f5;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .sidebar-title {
        text-align: center;
        color: #333333;
        font-family: 'Helvetica Neue', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    # Creating Session State Variable
    if 'API_Key' not in st.session_state:
        st.session_state['API_Key'] = ''
    
    st.markdown('<h1 class="header-title">YouTube Script Writing Tool</h1>', unsafe_allow_html=True)
    
    # Captures User Inputs
    prompt = st.text_input('Please provide the topic of the video', key="prompt", placeholder="Enter video topic...")
    video_length = st.text_input('Expected Video Length (in minutes)', key="video_length", placeholder="Enter video length...")
    creativity = st.slider('Creativity Level (0 LOW || 1 HIGH)', 0.0, 1.0, 0.2, step=0.1)
    
    submit = st.button("Generate Script")
    
    if submit:
        if st.session_state['API_Key']:
            search_result, title, script = generate_script(prompt, video_length, creativity, st.session_state['API_Key'])
            st.success('Script generated successfully!')
            
            # Display Title
            st.subheader("Title")
            st.write(title)
            
            # Display Video Script
            st.subheader("Your Video Script")
            st.write(script)
            
            # Display Search Engine Result
            st.subheader("Search Results")
            with st.expander('Show Search Results'):
                st.info(search_result)
        else:
            st.error("Please provide an API key.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<h2 class="sidebar-title">API Key</h2>', unsafe_allow_html=True)
st.session_state['API_Key'] = st.sidebar.text_input("Enter your OpenAI API key", type="password")
st.sidebar.image('./youtube.svg', use_column_width=True)
