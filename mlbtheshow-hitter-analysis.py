#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('live_series_hitters.csv')
print(df)


# In[5]:


import pandas as pd
df = pd.read_csv('live_series_hitters.csv')

# Remove unnecessary columns
df.drop(['Unnamed: 0', 'uuid'], axis=1, inplace=True)

# Remove duplicate entries
df.drop_duplicates(inplace=True)


# In[6]:


print(df)


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('live_series_hitters.csv')

# Histogram for 'ovr' distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['ovr'], kde=True)
plt.title('Distribution of Overall Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('Frequency')
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('live_series_hitters.csv')

# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[15]:


# Scatter plot for 'ovr' vs 'CLU'
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['ovr'], y=df['CLU'])
plt.title('Overall Rating vs Clutch')
plt.xlabel('Overall Rating')
plt.ylabel('Clutch')
plt.show()

# Scatter plot for 'ovr' vs 'POW R'
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['ovr'], y=df['POW R'])
plt.title('Overall Rating vs Power Right')
plt.xlabel('Overall Rating')
plt.ylabel('Power Right')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['ovr'], y=df['SPD'])
plt.title('Overall Rating vs Speed')
plt.xlabel('Overall Rating')
plt.ylabel('Speed')
plt.show()


# In[20]:


df = pd.read_csv('live_series_hitters.csv')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Group players by position
grouped_by_position = df.groupby('pos').mean(numeric_only=True)

# Plot distribution of key attribute by position using box plots
plt.figure(figsize=(12, 6))
sns.boxplot(x='pos', y='POW R', data=df)
plt.title('Distribution of Power Right by Position')
plt.show()

# Violin plot for another key attribute by position
plt.figure(figsize=(12, 6))
sns.violinplot(x='pos', y='SPD', data=df)
plt.title('Distribution of Speed by Position')
plt.show()


# In[2]:


df = pd.read_csv('live_series_hitters.csv')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Analyze the distribution of attributes across rarity levels
rarity_groups = df.groupby('rarity').mean(numeric_only=True)

# Visualize the differences in attribute distributions across rarity levels
plt.figure(figsize=(12, 6))
sns.boxplot(x='rarity', y='ovr', data=df, order=['Common', 'Bronze', 'Silver', 'Gold', 'Diamond'])
plt.title('Distribution of Overall Rating by Player Rarity')
plt.show()

# Compare 'STA', 'DUR', 'FLD', 'SPD', 'POW R', and 'POW L'
attributes_to_compare = ['STA', 'DUR', 'FLD', 'SPD', 'POW R', 'POW L']
for attr in attributes_to_compare:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='rarity', y=attr, data=df, order=['Common', 'Bronze', 'Silver', 'Gold', 'Diamond'])
    plt.title(f'Distribution of {attr} by Player Rarity')
    plt.show()


# In[ ]:




