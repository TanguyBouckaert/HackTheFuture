# streamlit_app.py
import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Needs to be imported by api"
spacy_streamlit.visualize(models, default_text)