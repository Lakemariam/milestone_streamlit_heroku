# Streamlit on Heroku

This project shows the simple way of creating a web app using python liberaries such as pandas, plotly, and streamlit.
And also shows how to deploy the web app on Heroku cloud platform. To do this we can follow five steps. 
The [deployed stock price web app](https://milestone-streamlit-heroku.herokuapp.com/) 
that can be used for checking monthly stock prices of Amazon (AMZN) since 2000.

## Step 1: Streamlit APP
- Fork a cloned repository from [The Data Incubator](https://github.com/thedataincubator/streamlit-framework) to use some of the default settings of `Procfile`, `requirements.txt`, and `setup.py`. 
- pip install streamlit
- import python liberaries into `app.py`
- streamlit run `app.py`

## Step 2: Create Heroku Account
- Create a Heroku account and create new app or 
- Create Heroku application with `heroku create app-name` from terminal
- log into heroku: `heroku login` 
- `git init`
- `heroku git:remote -a milestone-streamlit-heroku`
- `git add .`
- `git commit -am "heroku deployment"`
- Deploy to Heroku: `git push heroku main`
- The final deployed web app is `https://milestone-streamlit-heroku.herokuapp.com/`

## Step 3: Get data from API and put it in pandas
- Use the `requests` library to grab some data from Alpha Vantage API. The data is in JSON.
- Got API key for the url
- Create a `pandas` dataframe with the data.
- Columns are dictionary so spliting them and renaming is necessary
- Read the JSON file in pandas and convert it to pandas sataframe

## Step 4: Plot pandas data
- use plotly to plot the stock monthly price data for Amazon (AMZN)

"# stock-tick-price-streamlit-heroku" 
"# milestone_streamlit_heroku" 
"# milestone_streamlit_heroku" 
