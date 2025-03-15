import streamlit as st

# Draw a title and some text to the app:
st.write('''
# This is the document title

This is some _markdown_.
''')

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
st.write(df)  # 👈 Draw the dataframe

x = 10
st.write('x', x)  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.write(fig)  # 👈 Draw a Matplotlib chart


st.write(np.random.randn(2, 4))

from transformers import pipeline

classifier = pipeline('sentiment-analysis')

st.write(classifier.model)