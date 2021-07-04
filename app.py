import streamlit as st
import requests
import pandas as pd
import plotly.express as px
#import plotly.graph_objects as go
import datetime

# Create a dropdown menu or selection using streamlit sidebar function

selection = st.sidebar.selectbox('Select a Stock Ticker', ['AMZN'])

# select dates
today = datetime.date.today()
previous = today - datetime.timedelta(days = 8000)
start_date = st.sidebar.date_input('Start date', previous)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date: `%s`' %(start_date, end_date))
else:
    st.sidebar.error('Error: End date must not be before start date')

# get the url from Alpha Vantage and change demo with API key
apikey = open(r'api_key.txt')
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AMZN&outputsize=full&apikey=apikey' 
r = requests.get(url)
data = r.json()
df = pd.DataFrame(data[f'Time Series (Daily)']).T
df = df.rename(columns = {'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})

for i in df.columns:
    df[i] = df[i].astype(float)

df.index = pd.to_datetime(df.index)
df = df.iloc[::-1]

# Plot the stock price data

fig = px.line(df['High'])
fig.update_layout(
    title="Amazon Stock Historical Price Data",
    xaxis_title="Date",
    yaxis_title="Price",
    legend_title="AMZN",
    font=dict(
        family="sans serif",
        size=20,
        color="Blue"
    )
)

st.plotly_chart(fig, use_container_width=False)
progress_bar = st.progress(0)
