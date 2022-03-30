import streamlit as st
import pandas as pd
from statsmodels.iolib.smpickle import load_pickle
import altair as alt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#initialize original raw dataset
def dataset():
    gold = pd.read_csv(r"data/annual_gold_rate.csv") 
    return gold

#clean data
def clean(data):
    data = data[["Date", "USD"]]
    return data

#create app page
def app():
    st.header("Model")

    #display original data
    gold = clean(dataset())
    
    st.subheader("Original Dataset")
    st.dataframe(gold)

    #allow data to be downloaded
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    gold_csv = convert_df(gold)
    
    st.download_button(
        label="Download data as a CSV",
        data=gold_csv,
        file_name='gold.csv',
        mime='text/csv',
    )

    st.subheader("Forecast New Data")

    #additional cleaning
    temp_gold = gold.copy()
    temp_gold.index = temp_gold["Date"]
    temp_gold = temp_gold.drop(columns=["Date"])

    temp_gold.index = pd.to_datetime(temp_gold.index, format="%Y")
    temp_gold.index.freq = temp_gold.index.inferred_freq

    #divide into train and test
    split_num = int(round(len(temp_gold)*0.7, 0))
    train = temp_gold.iloc[:split_num]
    test = temp_gold.iloc[split_num:]

    #choose how many months to forecast for
    months = st.slider(label="Select the number of months to forecast", min_value=1, max_value=15, value=5)

    #initialize and fit model
    holts = ExponentialSmoothing(train, trend="mul")
    holts = holts.fit(optimized=True)
    
    #forecast new data
    temp_forecast = holts.forecast(len(test) + months)
    temp_forecast = pd.DataFrame(temp_forecast[len(test):].round(2))
    temp_forecast.columns = ["USD"]

    temp_forecast["Date"] = temp_forecast.index
    temp_forecast = temp_forecast[["Date", "USD"]]
    temp_forecast["Date"] = temp_forecast["Date"].dt.strftime("%Y")
    temp_forecast = temp_forecast.reset_index(drop=True)

    st.dataframe(temp_forecast)

    forecast_csv = convert_df(temp_forecast)
    st.download_button(
        label="Download data as a CSV",
        data=forecast_csv,
        file_name='forecast.csv',
        mime='text/csv',
    )

    #clean and plot 
    gold["Type"] = "Observed"
    gold["Date"] = pd.to_datetime(gold["Date"].copy(), format="%Y")
    
    temp_forecast["Type"] = "Forecast"
    temp_forecast["Date"] = pd.to_datetime(temp_forecast["Date"].copy())

    historical_forecast_concat = pd.concat([gold, temp_forecast], axis=0)
    forecast_chart = alt.Chart(historical_forecast_concat).mark_line().encode(
        x="Date",
        y="USD",
        color=alt.Color("Type:N",  scale=alt.Scale(domain=["Observed", "Forecast"], range=["steelblue", "peru"]))
    ).properties(
        title='Annual Gold Price (USD) per Ounce',
        width=750,
        height=450
    ).configure_axis(
        labelFontSize=16,
        titleFontSize=16
    ).configure_title(
        fontSize=16
    ).interactive()

    st.altair_chart(forecast_chart)
