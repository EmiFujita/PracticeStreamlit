import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバー')

'Start!!'
latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    time.sleep(0.01)
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    


left_column, right_column = st.columns(2)




button = left_column.button('右に注目')

if button:
    right_column.write('Hello')


exp1 = st.expander('FAQ')
exp1.write('お問い合わせ内容')
exp2 = st.expander('FAQ2')
exp2.write('お問い合わせ内容2')

text = st.text_input(
    '趣味を教えてください',
)
condition = st.slider('あなたの今の調子は？', 0, 10, 5)


'あなたの趣味は、',text,'です'
'コンディション：', condition


#if st.checkbox('Show Image'):
#    img = Image.open('dog.jpg')
#    st.image(img, caption='wanwan', use_column_width = True)

