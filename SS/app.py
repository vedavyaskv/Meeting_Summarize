# # app.py

# import streamlit as st
# import requests
# import time

# # --- Part 1: Functions to Call Hugging Face APIs ---

# # This function queries the Hugging Face API for a specific model.
# def query_api(payload, model_url):
#     """Sends a request to the Hugging Face Inference API."""
#     # Retrieve the API key from Streamlit's secrets
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {"Authorization": f"Bearer {api_key}"}
    
#     # Make the API request
#     response = requests.post(model_url, headers=headers, json=payload)
    
#     # Handle potential errors from the API
#     if response.status_code != 200:
#         # Sometimes the model needs to load, so we wait and retry.
#         if "is currently loading" in response.text:
#             st.info("Model is loading, please wait...")
#             time.sleep(20) # Wait 20 seconds
#             response = requests.post(model_url, headers=headers, json=payload)
#         else:
#             st.error(f"Error from API: {response.text}")
#             return None
            
#     return response.json()



# def transcribe_audio(file):
#     """Transcribes audio using OpenAI's Whisper model on Hugging Face."""
#     # We need to get the file's content type and raw bytes
#     content_type = file.type
#     audio_bytes = file.getvalue()
    
#     api_key = st.secrets["HF_API_KEY"]
    
#     # Add the "Content-Type" to our headers
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": content_type 
#     }
    
#     # The URL for the powerful Whisper model
#     model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    
#     response = requests.post(model_url, headers=headers, data=audio_bytes)

#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Whisper model is loading, this can take a moment...")
#             time.sleep(30) # Whisper is a large model, give it more time
#             response = requests.post(model_url, headers=headers, data=audio_bytes)
#         else:
#             st.error(f"Error during transcription: {response.text}")
#             return None
    
#     return response.json()


# # --- Part 2: Building the Streamlit User Interface ---

# st.set_page_config(layout="wide")
# st.title("AI Meeting Summarizer 🎙️")
# st.write("Upload your meeting audio file, and I'll provide a transcript and a summary with action items.")

# # File uploader allows user to add their own audio
# uploaded_file = st.file_uploader(
#     "Choose an audio file (.mp3, .wav, .m4a)", 
#     type=['mp3', 'wav', 'm4a', 'ogg']
# )


# # --- Part 3: Main Logic to Process the File ---

# if uploaded_file is not None:
#     st.audio(uploaded_file, format='audio/ogg')
    
#     # A button to start the process
#     if st.button("Generate Summary"):
#         with st.spinner("Step 1: Transcribing audio... this may take a few minutes."):
#             # Call the transcription function
#             transcript_result = transcribe_audio(uploaded_file)
        
#         # Check if the transcription was successful
#         if transcript_result and "text" in transcript_result:
#             transcript = transcript_result["text"]
#             st.subheader("✅ Transcription Complete")
#             st.text_area("Full Transcript", transcript, height=200)

#             # Prompt for the summarization model
#             prompt = f"""
#             Summarize the following meeting transcript.
#             Your summary should have two distinct sections:
#             1.  **Key Decisions:** A bulleted list of the most important decisions made.
#             2.  **Action Items:** A bulleted list of tasks assigned to individuals or the team.

#             Transcript:
#             "{transcript}"
#             """

#             # This is the correctly integrated summarization section
#             with st.spinner("Step 2: Generating summary and action items..."):
#                 # Define the LLM for summarization
#                 summarizer_model_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

#                 # Call the summarizer function with both arguments
#                 summary_result = query_api({
#                     "inputs": prompt,
#                     "parameters": {"min_length": 100, "max_length": 300} # Adjust length as needed
#                 }, summarizer_model_url) 

#             if summary_result:
#                 summary = summary_result[0]['summary_text']
#                 st.subheader("✅ Summary & Action Items")
#                 st.write(summary)
        
#         # This is the correctly integrated else block for when transcription fails
#         else: 
#             st.error("Transcription failed. Please try again or with a different file.")

# app.py

# import streamlit as st
# import requests
# import time

# # --- Part 1: Functions to Call Hugging Face APIs ---

# # This function queries the Hugging Face API for a specific model.
# def query_api(payload, model_url):
#     """Sends a request to the Hugging Face Inference API."""
#     # Retrieve the API key from Streamlit's secrets
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {"Authorization": f"Bearer {api_key}"}
    
#     # Make the API request
#     response = requests.post(model_url, headers=headers, json=payload)
    
#     # Handle potential errors from the API
#     if response.status_code != 200:
#         # Sometimes the model needs to load, so we wait and retry.
#         if "is currently loading" in response.text:
#             st.info("Model is loading, please wait...")
#             time.sleep(20) # Wait 20 seconds
#             response = requests.post(model_url, headers=headers, json=payload)
#         else:
#             st.error(f"Error from API: {response.text}")
#             return None
            
#     return response.json()



# def transcribe_audio(file):
#     """Transcribes audio using OpenAI's Whisper model on Hugging Face."""
#     # We need to get the file's content type and raw bytes
#     content_type = file.type
#     audio_bytes = file.getvalue()
    
#     api_key = st.secrets["HF_API_KEY"]
    
#     # Add the "Content-Type" to our headers
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": content_type 
#     }
    
#     # The URL for the powerful Whisper model
#     model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    
#     response = requests.post(model_url, headers=headers, data=audio_bytes)

#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Whisper model is loading, this can take a moment...")
#             time.sleep(30) # Whisper is a large model, give it more time
#             response = requests.post(model_url, headers=headers, data=audio_bytes)
#         else:
#             st.error(f"Error during transcription: {response.text}")
#             return None
    
#     return response.json()


# # --- Part 2: Building the Streamlit User Interface ---

# st.set_page_config(layout="wide")
# st.title("AI Meeting Summarizer 🎙️")
# st.write("Upload your meeting audio file, and I'll provide a transcript and a summary with action items.")

# # File uploader allows user to add their own audio
# uploaded_file = st.file_uploader(
#     "Choose an audio file (.mp3, .wav, .m4a)", 
#     type=['mp3', 'wav', 'm4a', 'ogg']
# )


# # --- Part 3: Main Logic to Process the File ---

# if uploaded_file is not None:
#     st.audio(uploaded_file, format='audio/ogg')
    
#     # A button to start the process
#     if st.button("Generate Summary"):
#         with st.spinner("Step 1: Transcribing audio... this may take a few minutes."):
#             # Call the transcription function
#             transcript_result = transcribe_audio(uploaded_file)
        
#         # Check if the transcription was successful
#         if transcript_result and "text" in transcript_result:
#             transcript = transcript_result["text"]
            
#             # --- START: NEW TRANSLATION & SUMMARIZATION LOGIC ---

#             st.subheader("✅ Transcription Complete")
#             st.text_area("Original Transcript (Detected Language)", transcript, height=150)

#             # NEW STEP: Translate the transcript to English
#             with st.spinner("Step 2: Translating to English..."):
#                 translator_model_url = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-hi-en"
#                 translation_payload = {"inputs": transcript}
#                 translation_result = query_api(translation_payload, translator_model_url)

#             if translation_result:
#                 english_transcript = translation_result[0]['translation_text']
#                 st.subheader("✅ Translation Complete")
#                 st.text_area("English Transcript", english_transcript, height=150)

#                 # Prompt for the summarization model using the ENGLISH transcript
#                 prompt = f"""
#                 Summarize the following meeting transcript.
#                 Your summary should have two distinct sections:
#                 1.  **Key Decisions:** A bulleted list of the most important decisions made.
#                 2.  **Action Items:** A bulleted list of tasks assigned to individuals or the team.

#                 Transcript:
#                 "{english_transcript}"
#                 """

#                 # This is the correctly integrated summarization section
#                 with st.spinner("Step 3: Generating summary and action items..."):
#                     summarizer_model_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#                     summary_result = query_api({
#                         "inputs": prompt,
#                         "parameters": {"min_length": 50, "max_length": 250}
#                     }, summarizer_model_url) 

#                 if summary_result:
#                     summary = summary_result[0]['summary_text']
#                     st.subheader("✅ Summary & Action Items")
#                     st.write(summary)
#             else:
#                 st.error("Translation failed.")
            
#             # --- END: NEW TRANSLATION & SUMMARIZATION LOGIC ---

#         # This is the else block for when transcription fails
#         else: 
#             st.error("Transcription failed. Please try again or with a different file.")

# app.py

# app.py

# import streamlit as st
# import requests
# import time

# # --- Part 1: Functions to Call Hugging Face APIs ---

# def query_api(payload, model_url):
#     """Sends a request to the Hugging Face Inference API."""
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {"Authorization": f"Bearer {api_key}"}
    
#     response = requests.post(model_url, headers=headers, json=payload)
    
#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Model is loading, please wait...")
#             time.sleep(20)
#             response = requests.post(model_url, headers=headers, json=payload)
#         else:
#             st.error(f"Error from API: {response.text}")
#             return None
            
#     return response.json()

# def transcribe_audio(file):
#     """Transcribes audio using OpenAI's Whisper model on Hugging Face."""
#     content_type = file.type
#     audio_bytes = file.getvalue()
    
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": content_type 
#     }
    
#     model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    
#     response = requests.post(model_url, headers=headers, data=audio_bytes)

#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Whisper model is loading, this can take a moment...")
#             time.sleep(30)
#             response = requests.post(model_url, headers=headers, data=audio_bytes)
#         else:
#             st.error(f"Error during transcription: {response.text}")
#             return None
    
#     return response.json()


# # --- Part 2: Building the Streamlit User Interface ---

# st.set_page_config(layout="wide")
# st.title("AI Meeting Summarizer 🎙️")
# st.write("Upload your meeting audio file, and I'll provide a transcript and a summary.")

# uploaded_file = st.file_uploader(
#     "Choose an audio file (.mp3, .wav, .m4a)", 
#     type=['mp3', 'wav', 'm4a', 'ogg']
# )


# # --- Part 3: Main Logic to Process the File ---

# if uploaded_file is not None:
#     st.audio(uploaded_file, format='audio/ogg')
    
#     if st.button("Generate Summary"):
#         with st.spinner("Step 1: Transcribing audio... this may take a few minutes."):
#             transcript_result = transcribe_audio(uploaded_file)
        
#         if transcript_result and "text" in transcript_result:
#             transcript = transcript_result["text"].strip()
            
#             st.subheader("✅ Transcription Complete")
#             st.markdown(f"<blockquote>{transcript}</blockquote>", unsafe_allow_html=True)

#             # Prompt is created directly from the original transcript
#             prompt = f"""
#             Summarize the following meeting transcript into two sections: "Key Decisions" and "Action Items".

#             Transcript:
#             "{transcript}"
#             """

#             with st.spinner("Step 2: Generating summary..."):
#                 summarizer_model_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#                 summary_result = query_api({
#                     "inputs": prompt,
#                     "parameters": {"min_length": 50, "max_length": 250}
#                 }, summarizer_model_url) 

#             if summary_result:
#                 summary = summary_result[0]['summary_text']
#                 st.subheader("✅ Summary Complete")
#                 st.write(summary)
                
#                 # Export functionality
#                 st.subheader("⬇️ Export Results")
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.download_button(
#                         label="Download Transcript",
#                         data=transcript,
#                         file_name="transcript.txt",
#                         mime="text/plain"
#                     )
#                 with col2:
#                     st.download_button(
#                         label="Download Summary",
#                         data=summary,
#                         file_name="summary.txt",
#                         mime="text/plain"
#                     )
#             else:
#                 st.error("Summarization failed.")
        
#         else: 
#             st.error("Transcription failed. Please try again or with a different file.")
# app.py

# import streamlit as st
# import requests
# import time

# # --- Part 1: Functions to Call Hugging Face APIs ---

# def query_api(payload, model_url):
#     """Sends a request to the Hugging Face Inference API."""
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {"Authorization": f"Bearer {api_key}"}
    
#     response = requests.post(model_url, headers=headers, json=payload)
    
#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Model is loading, please wait...")
#             time.sleep(20)
#             response = requests.post(model_url, headers=headers, json=payload)
#         else:
#             st.error(f"Error from API: {response.text}")
#             return None
            
#     return response.json()

# def transcribe_audio(file):
#     """Transcribes audio using OpenAI's Whisper model on Hugging Face."""
#     content_type = file.type
#     audio_bytes = file.getvalue()
    
#     api_key = st.secrets["HF_API_KEY"]
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": content_type 
#     }
    
#     model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    
#     response = requests.post(model_url, headers=headers, data=audio_bytes)

#     if response.status_code != 200:
#         if "is currently loading" in response.text:
#             st.info("Whisper model is loading, this can take a moment...")
#             time.sleep(30)
#             response = requests.post(model_url, headers=headers, data=audio_bytes)
#         else:
#             st.error(f"Error during transcription: {response.text}")
#             return None
    
#     return response.json()


# # --- Part 2: Building the Streamlit User Interface ---

# st.set_page_config(layout="wide")
# st.title("AI Meeting Analyzer 🎙️")
# st.write("Upload your meeting audio file for a transcript, summary, and keywords.")

# uploaded_file = st.file_uploader(
#     "Choose an audio file (.mp3, .wav, .m4a)", 
#     type=['mp3', 'wav', 'm4a', 'ogg']
# )


# # --- Part 3: Main Logic to Process the File ---

# if uploaded_file is not None:
#     st.audio(uploaded_file, format='audio/ogg')
    
#     if st.button("Analyze Meeting"):
#         # Step 1: Transcription
#         with st.spinner("Step 1: Transcribing audio... this may take a few minutes."):
#             transcript_result = transcribe_audio(uploaded_file)
        
#         if transcript_result and "text" in transcript_result:
#             transcript = transcript_result["text"].strip()
            
#             st.subheader("✅ Transcription Complete")
#             st.markdown(f"<blockquote>{transcript}</blockquote>", unsafe_allow_html=True)

#             # Step 2: Summarization
#             summary_prompt = f'Summarize the following meeting transcript into two sections: "Key Decisions" and "Action Items".\n\nTranscript:\n"{transcript}"'
#             with st.spinner("Step 2: Generating summary..."):
#                 summarizer_model_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#                 summary_result = query_api({
#                     "inputs": summary_prompt,
#                     "parameters": {"min_length": 50, "max_length": 250}
#                 }, summarizer_model_url) 

#             # Step 3: Keyword Extraction (NEW FEATURE)
#             with st.spinner("Step 3: Extracting keywords..."):
#                 keyword_model_url = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"
#                 keyword_result = query_api({"inputs": transcript}, keyword_model_url)

#             # Displaying the results
#             if summary_result:
#                 summary = summary_result[0]['summary_text']
#                 st.subheader("✅ Summary Complete")
#                 st.write(summary)
#             else:
#                 st.error("Summarization failed.")

#             if keyword_result:
#                 st.subheader("🔑 Key Phrases")
#                 # The model returns a list of dictionaries, so we format it
#                 keywords = [f"`{item['word']}`" for item in keyword_result]
#                 st.markdown(", ".join(keywords))
                
#                 # Full Keywords data to be used in download button
#                 keywords_text = "\n".join([item['word'] for item in keyword_result])
#             else:
#                 st.error("Keyword extraction failed.")

#             # Export functionality if both summary and keywords were successful
#             if summary_result and keyword_result:
#                 st.subheader("⬇️ Export Results")
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.download_button("Download Transcript", transcript, "transcript.txt", "text/plain")
#                 with col2:
#                     st.download_button("Download Summary", summary, "summary.txt", "text/plain")
#                 with col3:
#                     st.download_button("Download Keywords", keywords_text, "keywords.txt", "text/plain")
        
#         else: 
#             st.error("Transcription failed. Please try again or with a different file.")
# app.py

import streamlit as st
import requests
import time

# --- NEW: Function to load local CSS file ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- Part 1: Functions to Call Hugging Face APIs ---

def query_api(payload, model_url):
    """Sends a request to the Hugging Face Inference API."""
    api_key = st.secrets["HF_API_KEY"]
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.post(model_url, headers=headers, json=payload)
    
    if response.status_code != 200:
        if "is currently loading" in response.text:
            st.info("Model is loading, please wait...")
            time.sleep(20)
            response = requests.post(model_url, headers=headers, json=payload)
        else:
            st.error(f"Error from API: {response.text}")
            return None
            
    return response.json()

def transcribe_audio(file):
    """Transcribes audio using OpenAI's Whisper model on Hugging Face."""
    content_type = file.type
    audio_bytes = file.getvalue()
    
    api_key = st.secrets["HF_API_KEY"]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": content_type 
    }
    
    model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    
    response = requests.post(model_url, headers=headers, data=audio_bytes)

    if response.status_code != 200:
        if "is currently loading" in response.text:
            st.info("Whisper model is loading, this can take a moment...")
            time.sleep(30)
            response = requests.post(model_url, headers=headers, data=audio_bytes)
        else:
            st.error(f"Error during transcription: {response.text}")
            return None
    
    return response.json()


# --- Part 2: Building the Streamlit User Interface ---

st.set_page_config(layout="wide")

# Apply the custom CSS
local_css("style.css")

st.title("AI Meeting Analyzer 🎙️")
st.write("Upload your meeting audio file for a transcript, summary, and keywords.")

uploaded_file = st.file_uploader(
    "Choose an audio file (.mp3, .wav, .m4a)", 
    type=['mp3', 'wav', 'm4a', 'ogg']
)


# --- Part 3: Main Logic to Process the File ---

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/ogg')
    
    if st.button("Analyze Meeting"):
        # Step 1: Transcription
        with st.spinner("Step 1: Transcribing audio... this may take a few minutes."):
            transcript_result = transcribe_audio(uploaded_file)
        
        if transcript_result and "text" in transcript_result:
            transcript = transcript_result["text"].strip()
            
            st.subheader("✅ Transcription Complete")
            st.markdown(f"<blockquote>{transcript}</blockquote>", unsafe_allow_html=True)

            # Step 2: Summarization
            summary_prompt = f'Summarize the following meeting transcript into two sections: "Key Decisions" and "Action Items".\n\nTranscript:\n"{transcript}"'
            with st.spinner("Step 2: Generating summary..."):
                summarizer_model_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
                summary_result = query_api({
                    "inputs": summary_prompt,
                    "parameters": {"min_length": 50, "max_length": 250}
                }, summarizer_model_url) 

            # Step 3: Keyword Extraction
            with st.spinner("Step 3: Extracting keywords..."):
                keyword_model_url = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"
                keyword_result = query_api({"inputs": transcript}, keyword_model_url)

            # Displaying the results
            if summary_result:
                summary = summary_result[0]['summary_text']
                st.subheader("✅ Summary Complete")
                st.write(summary)
            else:
                st.error("Summarization failed.")

            if keyword_result:
                st.subheader("🔑 Key Phrases")
                keywords = [f"`{item['word']}`" for item in keyword_result]
                st.markdown(", ".join(keywords))
                
                keywords_text = "\n".join([item['word'] for item in keyword_result])
            else:
                st.error("Keyword extraction failed.")

            # Export functionality
            if summary_result and keyword_result:
                st.subheader("⬇️ Export Results")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.download_button("Download Transcript", transcript, "transcript.txt", "text/plain")
                with col2:
                    st.download_button("Download Summary", summary, "summary.txt", "text/plain")
                with col3:
                    st.download_button("Download Keywords", keywords_text, "keywords.txt", "text/plain")
        
        else: 
            st.error("Transcription failed. Please try again or with a different file.")