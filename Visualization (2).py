#!/usr/bin/env python
# coding: utf-8

# In[22]:


#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt



# In[17]:


Arbnb = pd.read_csv("C:\DataisGood\Airbnb.csv")


# In[18]:


print(Arbnb)


# In[14]:


list_of_column_names = list(Arbnb.columns)
print(list_of_column_names)


# In[24]:


# Scatter plot with room type against price
plt.scatter(Arbnb['room_type'], Arbnb['price'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('room_type')
plt.ylabel('price')
 
plt.show()


# In[26]:


plt.bar(Arbnb['room_type'], Arbnb['price'])
 
plt.title("Bar Chart")
 
# Setting the X and Y labels
plt.xlabel('room_type')
plt.ylabel('price')
 
# Adding the legends
plt.show()


# In[ ]:
# Plot the proce value in boxplot.

Arbnb.boxplot(by='room_type',column=['price'])
Arbnb.boxplot




# In[5]:


# histogram of reviews_per_month
plt.hist(Arbnb['reviews_per_month'])
 
plt.title("Histogram")
 
# Adding the legends
plt.show()


# In[23]:


import seaborn as sns
HR = pd.read_csv("C:\DataisGood\HR.csv")

HR_List = list(HR.columns)
print(HR_List)
HR=HR.iloc[2:10, :]
print(HR)

sns.lineplot(HR['Salary'], HR['Position'])
 
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')
 
plt.show()

HR.boxplot(by='Position',column=['Salary'])
sns.set_style("whitegrid")



# In[28]:


HR1 = pd.read_csv("C:\DataisGood\HR.csv")
# read  SAL
 
# count plot on single categorical variable MALE VS FEMALE
sns.countplot(x ='Sex', data = HR1)
 
# Show the plot
plt.show()


# In[55]:





# In[ ]:




