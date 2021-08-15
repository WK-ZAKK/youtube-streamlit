import streamlit as st
import numpy as np
import pandas as pd
import os
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.075)

'Done!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condistion = st.slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味: ', text
# 'コンディション: ', condistion




# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたが好きな数字は', option, '教えてください'

# if st.checkbox('show Image'):
#     img = Image.open(r'C:\Users\tk112\Desktop\udemy\MYPROJECT\media\images\ぴーまん.jpg')
#     st.image(img, caption='ピーマン', use_column_width=True) 