#!/usr/bin/env python
# coding: utf-8

# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[322]:


arrst = pd.read_csv('Daily_Arrests.csv')


# In[323]:


arrst.info()
arrst.head()


# In[324]:


#organize by date of arrest
arrst_datesort = arrst.sort_values(by='ARREST DATE')

#create the graph and make it pretty with labels and colors
sns.countplot(x = "ARREST DATE", data = arrst_datesort, palette="Greens_d")
plt.xticks(rotation=90)
plt.xlabel("ARREST DATE")
plt.title("Total Arrest Count for Mont. Co. PD by Date from 07/07/21 - 08/06/21")


# In[309]:


arrst_datesort['ARREST DATE'].value_counts()


# In[325]:


#organize the values by age
arrst_agesort = arrst.sort_values(by='AGE')
arrst_agesort = arrst_agesort.groupby(['AGE']).count()
arrst_agesort = arrst_agesort.reset_index()

#create variables for the bar graph
x1 = arrst_agesort['AGE']
y1 = arrst_agesort['OFFENSE']

#create graph and fix labels, title, etc
sns.barplot(x = x1, y = y1, data = arrst_agesort, palette="Blues_d", errwidth = .010)
plt.xticks(rotation=90)
spacing = 1.200
plt.title('Total offenses by age for Mont. Co. PD from 07/07/21 - 08/06/21')


# In[312]:


print(np.mean(arrst['AGE']), np.min(arrst['AGE']), np.max(arrst['AGE'])) 
# average age of offenses is 34.9, min 16, max 79


# In[326]:


sns.boxplot(x = x1, data = arrst_agesort, palette="Blues_d")
plt.title('Distribution of total offenses by age for Mont. PD from 07/07/21 - 08/06/21')


# In[373]:


#organize the values by the city
arrst_citysort = arrst.copy()
arrst_citysort['CITY'] = arrst_citysort['CITY'].str.title()
arrst_citysort = arrst_citysort.groupby(['CITY']).count()
arrst_citysort = arrst_citysort.reset_index()

#create variables for the bar graph
x2 = arrst_citysort['CITY']
y2 = arrst_citysort['OFFENSE']

#create graph and fix labels, title, etc
sns.set(rc={"figure.figsize":(30, 4)})
sns.barplot(x = x2, y = y2, data = arrst_citysort, palette="cool")
plt.xticks(rotation=90)
plt.title('Total offenses by city for Mont. Co. PD from 07/07/21 - 08/06/21')


# In[344]:


arrst_citysort.groupby(['CITY']).count()


# In[ ]:




