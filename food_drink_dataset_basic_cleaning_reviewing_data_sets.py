#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

from collections import Counter


# In[145]:


df_cities = pd.read_csv('dim_cities.csv')

df_respondents = pd.read_csv('dim_repondents.csv')

surveys = pd.read_csv('fact_survey_responses.csv')

df_cities.info()


# In[146]:


df_cities_missing_value = df_cities.isnull().sum()
df_cities_missing_value


# No Null Value, No need to drop or edit Data Set for Cities Data Frame

# In[147]:


df_respondents.info()


# No missing value in dataset for respondents

# In[149]:


df_respondents.head(), 


# there are no values in numbers except Respondent_ID and age range, while we keep age range as is for our analysis,
# we do not need to make any changes in respondent_ID, it will be useful to connect other datasets in our Data model in Power BI

# For now, in this example, I have prepared only one visualization for energy drink uses, brand awareness and typical consumer behavior using PIE chart
# 
# As I will be preparing POWER BI dashboard, here we will not focus on visualization, instead I will post data relationaship models using
# different techniques in Data analysis using python to predict different variables in data set

# In[81]:


consume_frequency_list = surveys['Consume_frequency'].unique().tolist()
consume_time_list = surveys['Consume_time'].unique().tolist()
consume_reason_list = surveys['Consume_reason'].unique().tolist()
Heard_before_list = surveys['Heard_before'].unique().tolist()
brand_perception_list = surveys['Brand_perception'].unique().tolist()
general_perception_list = surveys['General_perception'].unique().tolist()


# In[82]:


#Considering 7 days in a week and based on frequency as responded by respondents, following is mapped for responses

response_mapping = {
    '2-3 times a week': 3,
    '2-3 times a month': 2,
    'Rarely': 1,
    'Daily': 5,
    'Once a week': 4
}

surveys['consume_frequency_num'] = surveys['Consume_frequency'].map(response_mapping)

consume_frequency_num_list = surveys['consume_frequency_num'].unique().tolist()

surveys.head()



# # Consumption Habits, Awareness and Perception about brand

# In[94]:


# Counters for each dataset
frequency_counter = Counter(surveys['Consume_frequency'])
reason_counter = Counter(surveys['Consume_reason'])
time_counter = Counter(surveys['Consume_time'])
General_perception_counter = Counter(surveys['General_perception'])

# a 2x2 grid for the subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Data for all the subplots
counters = [frequency_counter, reason_counter, time_counter, General_perception_counter]

# Labels for each subplot
titles = ['Frequency', 'Reason to Drink', 'Consume Time', 'General Perception']

#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Explode slices
explode = [(0.1, 0, 0, 0, 0), (0, 0.1, 0, 0, 0), (0, 0, 0.1, 0), (0, 0, 0, 0.1)]

# Looping through each subplot and creating a pie chart
for i, ax in enumerate(axs.flat):
    labels, counts = zip(*counters[i].items())
    
    # Create the pie chart with customizations
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode = explode[i])
    ax.add_artist(plt.Circle((0, 0), 0.70, fc='white'))
    ax.axis('equal')  # Equal aspect ratio ensures that each pie chart is circular.
    ax.set_title(titles[i])


# a legend
fig.legend(labels, loc='upper right', bbox_to_anchor=(0.9, 0.9))

# Adjusted layout
plt.tight_layout()

# Displayed the grid of pie charts
plt.show()


# ## Outcome/Evaluation:
# 
# How often do customers consume energy Drinks?
# A. 34.9~ 35% customers prefer to consume drinks 2-3 times a week
# while
# B. 13.5% and 16.1% customers consume it daily and weekly respectively.
# 
# 
# What are the reasons to consume energy drinks?
# 
# 91.02% gave a different positive reasons to consume energy drinks like to combat fatigue(24.3%), to enhance sports performance (16%), to boost performance (15.1%) and to increase energy and focus (being the top most reason among consumers with 35.7%)
# 
# How do customers typically consume energy drinks based on data?
# 
# With more than 60% respondents, customers typically consume drinks to stay awake during work/study (34.1%) and before exercise (31.5%), while 19.9% (~20%) of them consume for mental alertness and 14.5% consume it throughout the day.
# 
# 
# 
