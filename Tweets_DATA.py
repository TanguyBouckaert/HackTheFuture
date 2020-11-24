# streamlit_app.py
import spacy
import streamlit as st
import pandas as pd


input = "Apple is looking at buying U.K. startup for $1 billion"

nlp = spacy.load("en_core_web_sm")
doc = nlp(input)
#visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

#put stats in obj
textdata = []
labeldata = []
for ent in doc.ents:
    textdata.append([ent.text])
    labeldata.append([ent.label_])
    print("text:" + ent.text, "label:" + ent.label_)


dataf = pd.DataFrame(textdata, columns=[labeldata.pop])
print(labeldata)
print(dataf)

st.line_chart(dataf)
st.bar_chart(dataf)