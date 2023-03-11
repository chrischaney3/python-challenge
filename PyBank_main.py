#!/usr/bin/env python
# coding: utf-8

# In[47]:


#Import Dependecies
import pandas as pd
import datetime as datetime


# In[48]:


#Read the csvfile
df = pd.read_csv("budget_data.csv")
df.head()


# In[49]:


#Check data info
df.info()


# In[50]:


#The total number of months included in the dataset
total_months = df['Date'].nunique()
print(total_months)


# In[53]:


#The net total amount of "Profit/Losses" over the entire period
net_amount = df['Profit/Losses'].sum()
print(net_amount)


# In[57]:


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
avg_amount = df['Profit/Losses'].mean()
print(avg_amount)


# In[63]:


#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
max_profit = df.max()
min_profit = df.min()
print(max_profit)
print(min_profit)


# In[64]:


#Printing the report
print ("Financial Analysis")
print ("-"*20)
print (f'Total Months: ' +str( total_months))
print (f'Total: $' + str(net_amount))
print (f'Average Change: $' + str(avg_amount))
print (f'Greatest Increase in Profits: ' +str(max_profit))
print (f'Greatest Decrease in Profits: ' +str(min_profit))


# In[ ]:





# In[ ]:




