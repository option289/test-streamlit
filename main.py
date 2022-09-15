import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
   latest_iteration.text(f"Iteration{i+1}")
   bar.progress(i+1)
   time.sleep(0.2)
st.title('Streamlit　入門')
st.write("DataFrame")

df=pd.DataFrame({
   "1" : [1, 4, 6, 7],
   "2" : [5, 120, 22, 26]
}
)
st.table(df.style.highlight_max(axis=0))

"""

# r
## t
### s

```python

print

```

"""

df=pd.DataFrame(
   np.random.rand (15,4),
   columns=["f", "u", "c", "k"]
)
df
st.line_chart(df)
st.area_chart(df)

st.bar_chart(df)

df=pd.DataFrame(
   np.random.rand (50,2)/[50,50]+[33,117],
   columns=["lat", "lon"]
)
df
st.map(df)


st.write("Display Image")
if st.checkbox("show "):
    img=Image.open("thumbnail.jpg")
    st.image(img,caption="sex",use_column_width=True)

option=st.selectbox(
     "tell me fucking number",
     list(range(0,10))
)
"your number",option,"yeah"

option2 = st.text_input("what is your hobby")
"your hobby is ",option2

let=st.slider("what is your condition",0,100,50)
"your condition",let

left_column,right_column=st.columns(2)
button=left_column.button("display words on right column")
if button:
   right_column.write("yes!!!!")

expander=st.expander("question")
expander.write("about question")

option3 = st.text_input("what is your luck")
let2=st.slider("what is your power",0,100,50)


"your power",let2
"your luck is ",option3
