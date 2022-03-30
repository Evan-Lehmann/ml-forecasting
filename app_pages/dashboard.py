import streamlit as st
import pandas as pd
import numpy as np
from app_pages.model import dataset, clean
import altair as alt
from statsmodels.tsa.seasonal import STL
from fredapi import Fred
import os 

def app():
    st.header("Dashboard")
    
    #decompose data
    decomp_gold = clean(dataset())
    decomp_gold["Date"] = pd.to_datetime(decomp_gold["Date"], format="%Y")
    decomp_gold.index = decomp_gold["Date"]
    decomp_gold["Type"] = "original"

    stl = STL(decomp_gold["USD"], robust=True, period=12)
    res = stl.fit()

    temp_gold = clean(dataset())
    temp_gold["Type"] = "Observed"
    temp_gold["Date"] = pd.to_datetime(temp_gold["Date"].copy(), format="%Y")

    #choose decomposition component to plot
    choose_component = st.selectbox(
        "Select a decomposition component to graph.",
        ("Trend", "Residual", "Cyclicality")
    )

    #deal with trend component
    trend_x = res.trend.index
    trend_y = res.trend.values
    trend = pd.concat([pd.DataFrame(trend_x), pd.DataFrame(trend_y)], axis=1)
    trend.columns = ["Date", "USD"]
    trend["Type"] = "Trend"
    trend = pd.concat([trend, temp_gold], axis=0)

    #deal with residual component
    res_x = res.resid.index
    res_y = res.resid.values
    resids = pd.concat([pd.DataFrame(res_x), pd.DataFrame(res_y)], axis=1)
    resids.columns = ["Date", "USD"]
    resids["Type"] = "Residual"
    resids = pd.concat([resids, temp_gold], axis=0)

    #deal with cyclicality component
    cyclical_x = res.seasonal.index
    cyclical_y = res.seasonal.values
    cyclicality = pd.concat([pd.DataFrame(cyclical_x), pd.DataFrame(cyclical_y)], axis=1)
    cyclicality.columns = ["Date", "USD"]
    cyclicality["Type"] = "Cyclicality"
    cyclicality = pd.concat([cyclicality, temp_gold], axis=0)

    #plot decomposed data
    if choose_component == "Trend":
        temp_component = trend
    elif choose_component == "Residual":
        temp_component = resids
    else:
        temp_component = cyclicality

    decomp_chart = alt.Chart(temp_component).mark_line().encode(
        x="Date",
        y="USD",
        color=alt.Color("Type:N",  scale=alt.Scale(domain=["Observed", choose_component], range=["steelblue", "goldenrod"]))
    ).properties(
        title=f'Annual Gold Price (USD) per Ounce {choose_component}',
        width=750,
        height=450
    ).configure_axis(
        labelFontSize=16,
        titleFontSize=16
    ).configure_title(
        fontSize=16
    ).interactive()

    st.altair_chart(decomp_chart)

    #select external feature from api
    select_external = st.selectbox(
        "Select a feature to compare with Annual Gold Price (USD) per Ounce.",
        ("Urban Consumer CPI", "Gold Ore PPI", "Gold Export Price", "Jewelry Retail Sales")
    )

    #call API and return external data
    key = str(os.environ.get("api_key"))
    fred = Fred(api_key=key)

    cpi = fred.get_series('CPIAUCSL')
    ppi = fred.get_series('WPU10210501')
    gold_export = fred.get_series('IQ12260')
    jewelry = fred.get_series('MRTSSM44831USS')

    external_mapping = {"Urban Consumer CPI": cpi, "Gold Ore PPI":ppi, "Gold Export Price":gold_export, "Jewelry Retail Sales":jewelry}
    
    #deal with external feature data
    external_df = pd.DataFrame(external_mapping[select_external])
    external_df = external_df.reset_index()
    external_df.columns = ["Date", "USD"]

    external_df["Gold"] = pd.to_datetime(external_df["Date"].copy(), format="%Y")
    external_df["Type"] = select_external
    external_df = pd.concat([external_df, temp_gold], axis=0)

    #plot original data with external feature
    external_chart = alt.Chart(external_df).mark_line().encode(
        x="Date",
        y="USD",
        color=alt.Color("Type:N",  scale=alt.Scale(domain=["Observed", select_external], range=["steelblue", "forestgreen"]))
    ).properties(
        title=f'Annual Gold Price (USD) per Ounce with {select_external}',
        width=750,
        height=450
    ).configure_axis(
        labelFontSize=16,
        titleFontSize=16
    ).configure_title(
        fontSize=16
    ).interactive()   

    st.altair_chart(external_chart)

    st.dataframe()




    