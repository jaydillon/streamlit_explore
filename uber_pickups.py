import streamlit as st
import pandas as pd
import numpy as np

# Add a title for this App
st.title('Uber Pickups in NYC')

# Fetch data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data 


# Create a text element that and let reader know the data is loading
data_load_state = st.text('Loading data...')
# Load 10,000 rows of the data into dataframe
data = load_data(10000)
# Notify the reader that the data is successfully loaded
data_load_state.text("Done! (using st.cache)")

def highlight_survived(s):
    return ['background-color: #9bf2cb']*len(s)

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.dataframe(data.style.apply(highlight_survived, axis=1))
    # st.dataframe(data.style.applymap(color_test, subset=['Survived']))
    # st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# st.subheader('Map of all pickups')
# st.map(data)
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# Test columns    
col1, col2, col3 = st.columns((1,1,2))

with col1:
     st.write('This is first col')
with col2:
     st.write('This is last col')
with col3:
     st.bar_chart(hist_values)

# Contidiontal formatting


