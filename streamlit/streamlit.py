import streamlit as st
from functions import load_data, create_hist, split_hist
from PIL import Image

st.set_page_config(page_title = 'EDA Project - Digital Lifestyle Benchmark', layout = 'wide')
st.title("Digital Lifestyle Benchmark Data Analysis")
st.write('''
### Project Description

This project strengthens skill sets pertaining to data exploration, cleaning, and analysis. The “real world” data set selected for this project is “Digital 
Lifestyle Benchmark,” a data set found on Kaggle that explores the correlations between mental/emotional wellbeing and social media interaction/studying 
online/screen time.  To begin analysis of the data set, the data was cleaned, meaning null values and outliers were removed if present. Along with this, the 
data columns were properly assigned data types to ensure efficient and easy analysis. Afterwards, hypotheses were drawn regarding the correlations between 
values and tested via data visualization during analysis.''')

df = load_data()

#fig = create_corr(df)
#st.pyplot(fig)

corr = Image.open('corr.png')
st.image(corr, caption = 'Correlation Matrix of Observed Variables')

st.write("""
### Hypotheses
#### When comparing men and women that have the same range of screen time, is there a strong correlation between mental illness and gender? 

We assume that there is a strong correlation between mental illness and gender, 
with mental illness levels sharing a positive correlation with screen time. We 
anticipated that females will on average have higher levels of anxiety, depression, 
and stress.""")

g_a = Image.open('g_a.png') 
g_d = Image.open('g_d.png')
g_s = Image.open('g_s.png')

col1, col2, col3 = st.columns(3)

with col1:
	st.image(g_a, caption = "Gender vs Anxiety")

with col2:
        st.image(g_d, caption = "Gender vs Depression")

with col3:
        st.image(g_s, caption = "Gender vs Stress")

st.write("""These graphs highlight the correlation between gender and anxiety, 
gender and depression, and gender and stress. There is a correlation between gender and 
anxiety, with women having higher levels of anxiety than men; however, there are no strong correlations between gender and depression or gender and stress. There are 
similar connections between gender and depression and gender and stress that 
indicate higher screen times lead to high levels of both depression and stress.""")

st.write("""#### When comparing education levels that have the same range of screen time, is there a strong correlation between mental illness and education level?

We assume that there is a strong correlation between mental illness and education 
level, with mental illness levels sharing a positive correlation with screen time. 
We anticipated that the lower the education level, the higher the mental illness 
reports.
""")

e_a = Image.open('e_a.png')
e_d = Image.open('e_d.png')
e_s = Image.open('e_s.png')

col1, col2, col3 = st.columns(3)

with col1:
        st.image(e_a, caption = "Education vs Anxiety")

with col2:
        st.image(e_d, caption = "Education vs Depression")

with col3:
        st.image(e_s, caption = "Education vs Stress")

st.write("""There is a small correlation between education level and stress. Three 
out of four of the screentime ranges indicate that those with a higher education 
level have lower levels of stress. There are no strong correlations between education versus anxiety/depression; however, all three graphs indicate that higher 
screen times lead to higher levels of these negative emotions.""")

st.write("""#### When comparing age groups with similar screen time, is there a strong correlation between mental illness and age?

We assume that there is a strong correlation between mental illness and age, with 
mental illness levels sharing a positive correlation with screen time. We 
anticipated that teenagers and young adults will have higher levels of 
mental illness in comparison to those older in age. 
""")

a_a = Image.open('a_a.png')
a_d = Image.open('a_d.png')
a_s = Image.open('a_s.png')

col1, col2, col3 = st.columns(3)

with col1:
        st.image(a_a, caption = "Age vs Anxiety")

with col2:
        st.image(a_d, caption = "Age vs Depression")

with col3:
        st.image(a_s, caption = "Age vs Stress")

st.write("""While there are no correlations between age versus depression, anxiety, 
and stress, the three graphs highlight the strong positive correlation between 
higher screen times and mental illnesses.""")

st.write("""#### Is there a correlation between time spent studying online and mental illness?""")

st.write("""We speculate there is a strong positive correlation 
between studying online and mental illness. We assume that more time 
spent studying with a screen will lead to higher levels of mental 
illness.""")

s_a = Image.open('s_a.png')
s_d = Image.open('s_d.png')
s_s = Image.open('s_s.png')

col1, col2, col3 = st.columns(3)

with col1:
        st.image(s_a, caption = "Time Spent Studying Online vs Anxiety")

with col2:
        st.image(s_d, caption = "Time Spent Studying Online vs Depression")

with col3:
        st.image(s_s, caption = "Time Spent Studying Online vs Stress")

st.write("""There is very little variation between the separate time 
spent studying groups. This means that there is no correlation among 
studying online and mental illness, which is contradictory to our 
hypothesis.""")

st.write("""#### What are the effects of social media usage and happiness scores? Is there a correlation?""")

st.write("""We hypothesize there is a strong inverse relationship between happiness and social media usage. In 
this relationship, we assume more time spent on social media will lead to lower happiness scores.""")

h_a = Image.open('h_a.png')
st.image(h_a, caption = "Happiness vs Anxiety")

st.write("""The data indicates there is no variation with happiness 
and depression scores as social media minutes increase, meaning a lack 
of correlation.""")

st.write("""#### Is there a correlation between focus scores and time spent on social media?""")

st.write("""We predict an inverse relationship between focus scores 
and social media usage. In this case, as social media usage 
increases, the focus score will decrease.""")

s_f = Image.open('s_f.png')
st.image(s_f, caption = "Affect of Time Spent on Social Media on Focus")

st.write("""As expected, there is an inverse relationship between 
focus and social media usage; as usage increases focus scores 
decrease.""")

st.write("""#### Do notifications induce higher levels of stress?""")

st.write("""It is hypothesized that a positive correlation lies 
between number of notifications and levels of stress. We expect that 
an increase in notifications will lead to higher levels of 
stress.""")

s_n = Image.open('s_n.png')
st.image(s_n, caption = "Affect of Number of Notifications on Stress")

st.write("""The data proves the hypothesis, there is a positive 
trend between social media usage and stress levels.""")

st.write("""#### What is the correlation between time spent on a device and sleep quality?""")

st.write("""We predict there is an inverse relationship between 
device usage and sleep quality. In this relationship, as device 
hours per day increases, we expect sleep quality levels to 
decrease.""")

sq = Image.open('sq.png')
st.image(sq, caption = "Affect of Device Hours per Day on Sleep Quality")

st.write("""As expected, as device hours increase, sleep quality 
decreases. Indicating there is a strong inverse relationship between 
the two factors, thus proving the hypothesis.""")

st.write("""#### Is there a correlation between depression and screen time?""")
 
st.write("""We expect a strong correlation between depression and 
screen time. It is hypothesized that an increase in screen time will 
showcase a rise in depression scores.""")

if st.button('Click for Stacked Graph'):
	fig = create_hist(df)
	st.pyplot(fig)

if st.button('Click for Split Graph'):
	fig = split_hist(df)
	st.pyplot(fig)

st.write("""This combined bar chart shows higher density levels of 
depression as screen time increases. This indicates a strong 
positive correlation between depression and screen time.""")
