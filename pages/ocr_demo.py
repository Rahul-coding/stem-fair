import streamlit as st
from ocr_utils import analyze
from jsonpath_ng import JSONPath, parse
import json
image = "./images/real.jpg"

on = st.toggle('Use backup file')
data = 0
parsed = ''

st.title("Extracting Text")
st.write("**Using Oracles OCI vision service**")
if on:
        image = "./images/backup.jpg"   
        st.image('./images/backup.jpg')
else:
    image = "./images/real.jpg"
    st.image('./images/real.jpg')

if st.button('Analyze'):
    if on:
        image = "./images/backup.jpg"   
        st.image('./images/backup.jpg')
    else:
        image = "./images/real.jpg"
        st.image('./images/real.jpg')
    data = analyze(image)   
    with open('./text/real.txt','w') as extract:
     extract.write(str(data))

    with open('./text/real.txt', 'r') as json_file:
        json_data = json.load(json_file)

    expression = parse('pages[*].lines[*].text')
    match = expression.find(json_data)

    for match in expression.find(json_data):
        parsed += match.value

    #print(parsed) 
    with open('./text/real.txt', 'w') as save:
        save.write(str(parsed))  
else:
    st.write(data)

     