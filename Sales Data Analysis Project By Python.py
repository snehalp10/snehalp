#!/usr/bin/env python
# coding: utf-8

# #                   Sales Data Analysis
# 

# # Import libraries
# 

# In[6]:


#Data manipulation
import numpy as np
import pandas as pd

#Data visualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# # Dataset

# In[7]:


df = pd.read_excel("D:\Snehal\DS\DATASET\superstore_sales.xlsx")


# In[5]:


df


# In[6]:


#show no.of rows and columns
df.shape


# In[7]:


#show first five records by default
df.head()


# In[8]:


#show last 5 records by default
df.tail()


# In[9]:


#coulmns present in dataset
df.columns


# In[10]:


#shows the summary of the data
df.info()


# In[11]:


#checking missing values
df.isnull().sum()


# In[12]:


#getting discription of statistical summary
df.describe()


# Exploratory Data Analysis

# In[13]:


df['order_date'].min()


# In[14]:


df['order_date'].max()


# In[17]:


#getting month year from dataset
df['month_year'] = df['order_date'].apply(lambda x : x.strftime('%Y-%m'))
df['month_year']


# In[21]:


df.groupby('month_year').sum()


# In[24]:


#grouping month year
df_trend = df.groupby('month_year').sum()['sales'].reset_index()
df_trend


# In[29]:


plt.figure(figsize=(15,6))
plt.plot(df_trend['month_year'],df_trend['sales'],color='#b80045')
plt.xticks(rotation='vertical',size = 8)
plt.show


# In[36]:


#grouping product names column
prod_sales = pd.DataFrame(df.groupby('product_name').sum()['sales'])
prod_sales


# In[37]:


#sorting prod_sales column
prod_sales.sort_values('sales',ascending = False)


# In[38]:


#top 10 product names by sales 
prod_sales[:10]


# In[40]:


#
most_sell_prod = pd.DataFrame(df.groupby('product_name').sum()['quantity'])
most_sell_prod


# In[41]:


most_sell_prod.sort_values('quantity',ascending=False)


# In[42]:


sns.countplot(df['ship_mode'])


# In[8]:


cat_subcat_profit = pd.DataFrame(df.groupby(['category','sub_category']).sum()['profit'])
cat_subcat_profit


# In[10]:


cat_subcat_profit.sort_values(['category','profit'],ascending = False)


# # END

# In[ ]:




