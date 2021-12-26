import yfinance as yf
import pandas as pd
import streamlit as st


def appRun():

    # Creates title of app
    st.markdown("<h1 style='text-align: center; color: maroon;'>AggieQuant Stock Screener</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>By: Kyle Welch ('23)</h4>", unsafe_allow_html=True)

    # Downloads stock data
    name = st.text_input("Type ticker here (Ex: TSLA)", "TSLA")
    symbol = yf.Ticker(name)

    df = symbol.info

    print(df)

    # Add company name and logo
    col3, col4 = st.columns([1, 8])
    col3.image(df['logo_url'], width=60)
    col4.header(df['longName'])

    # Creates price chart
    df2 = symbol.history(period='max')
    st.line_chart(df2['Close'])

    # Prints company description
    st.write(df['longBusinessSummary'])

    # Print key financial metrics
    col1, col2 = st.columns(2)


    col1.header("EV/EBITDA")
    col1.write(df['enterpriseToEbitda'])

    col1.header("BETA")
    col1.write(df['beta'])

    col1.header("ROE")
    col1.write(df['returnOnEquity'])

    col2.header('FORWARD PE')
    col2.write(df['forwardPE'])

    col2.header("PEG")
    col2.write(df['pegRatio'])

    col2.header("ROA")
    col2.write(df['returnOnAssets'])

