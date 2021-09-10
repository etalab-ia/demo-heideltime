from datetime import datetime
import xml.etree.ElementTree as ET

import streamlit as st

from python_heideltime import Heideltime

default_input = """
Quelle a été la profondeur des nappes chez moi, cette année ?
"""

st.sidebar.header("heideltime parameters")
document_type = st.sidebar.selectbox("document type", ["NEWS", "NARRATIVES"])
language = st.sidebar.selectbox("language", ["ENGLISH", "GERMAN", "FRENCH"], 2)
interval_tagger = st.sidebar.checkbox("interval tagger", True)
document_time = st.sidebar.date_input("document time")


heideltime_parser = Heideltime()
heideltime_parser.set_document_type(document_type)
heideltime_parser.set_language(language)
heideltime_parser.set_interval_tagger(interval_tagger)
heideltime_parser.set_document_time(document_time.strftime("%Y-%m-%d"))

st.header("Input")

input = st.text_area("Une question ?", default_input)

st.write(f"> {input}")


st.header("Result")


@st.cache
def get_result(input):
    return heideltime_parser.parse(input)


result = get_result(input)

st.subheader("Raw")
st.write(
    f"""```
{ result }
```"""
)


st.subheader("Detected dates")
xml = ET.fromstring(result)
dates = [el for el in xml.iter() if el.tag == "TIMEX3"]
st.table(
    [
        {"text": date.text, "type": date.attrib["type"], "value": date.attrib["value"]}
        for date in dates
    ]
)
