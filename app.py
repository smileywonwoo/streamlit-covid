import streamlit as st
import pandas as pd
import numpy as np

st.title('전세계 코로나 데이터')

coronaDf = pd.read_csv('covid_19_clean_complete.csv')

st.dataframe(data=coronaDf)
coronaDf['Date'] = pd.to_datetime(coronaDf['Date'])
latestDf= coronaDf[coronaDf['Date'] == max(coronaDf['Date'])]
lastest_country_sum = latestDf.groupby(['Country/Region'])['Confirmed','Deaths','Recovered'].sum().reset_index()
lastest_country_sum = lastest_country_sum.sort_values(['Confirmed'], ascending=False).reset_index(drop=True)
st.dataframe(data=lastest_country_sum)

st.write("## 시간에 따른 확진자, 사망자, 회복자 시각화")

date_Status = coronaDf.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum()
date_Status.sort_index()

st.line_chart(data=date_Status)