#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt #visualisation data 
import seaborn as sns 


# # Load the dataset

# In[12]:


df = pd.read_excel(r"Finacial_Data.xlsx")


# In[4]:


## understanding the dataset 
df


# In[5]:


df.head()


# In[6]:


df.info()


# In[ ]:





# In[9]:


df.dropna()  # Drop rows with any NaN values
df = df.dropna(axis=1, how='all')  # Drop columns where all values are NaN



# In[10]:


df.info()


# In[11]:


print(df.isnull().sum())  # Shows count of missing values in each column


# In[12]:


#describe() method returns description of data in the dataframe (i.e count, mean, std,)
df.describe()


# In[13]:


df[['Account_Key', 'Sort on Type']].describe()


# In[ ]:





# In[18]:


df.info()


# In[21]:


df


# ##A. Distribution of Different Types of Transactions

# In[18]:


plt.figure(figsize=(12, 6))
sns.countplot(y=df["Type"], order=df["Type"].value_counts().index, palette="coolwarm")
plt.xlabel("Count")
plt.ylabel("Transaction Type")
plt.title("Distribution of Transaction Types")
plt.show()


# ##### from above bar chart- The company primarily manages its cash flow through Operating Activities, meaning its profitability and liquidity depend heavily on its core business operations.

# In[6]:


plt.figure(figsize=(18, 10))  # Increase figure size for better readability

sns.barplot(x="SubAccount", y="Sort on Type", hue="ValueType", data=df, palette="coolwarm")

plt.xlabel("SubAccount")  #X-axis represents transaction types
plt.ylabel("Sort on Type") # Y-axis represents their corresponding values
plt.title("Revenue vs. Expenses Over Time")

plt.xticks(rotation=45, ha="right")  # Rotate X-axis labels for better visibility....ticks	The positions where you want the labels to appear (default: auto).
plt.legend(title="Value Type")

plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 6))

# Calculate value counts as percentages
type_counts = df["Type"].value_counts(normalize=True) * 100  # Convert to percentage

# Create the countplot but set y-ticks manually
ax = sns.countplot(y=df["Type"], order=type_counts.index, palette="coolwarm")

# Update x-axis labels to show percentages
total = len(df)  # Total number of rows in the dataset
for p in ax.patches:
    percentage = f"{(p.get_width() / total) * 100:.1f}%"  # Convert count to percentage
    ax.annotate(percentage, (p.get_width(), p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=12, color='black', xytext=(5, 0),
                textcoords='offset points')

plt.xlabel("Percentage (%)")  # Change X-axis label
plt.ylabel("Transaction Type")
plt.title("Distribution of Transaction Types (in %)")
plt.show()


# In[16]:


filtered_df = df[df["Type"] == "Cash flows from Operating Activities"]
print(filtered_df)


# In[8]:


plt.figure(figsize=(25, 15))
df["Account"].value_counts().plot(kind="bar", color="skyblue")
plt.xlabel("Account")
plt.ylabel("Frequency")
plt.title("Cash Flow by Account Type")
plt.xticks(rotation=45)
plt.show()



# In[26]:


# Expense Breakdown
def expense_breakdown(df):
    expense_data = df[df['Type'] == 'Cash flows from Operating Activities']
    expense_summary = expense_data.groupby("SubAccount")["ValueType"].count().sort_values(ascending=False)
    plt.figure(figsize=(12, 5))
    sns.barplot(x=expense_summary.index, y=expense_summary.values, palette="Blues")
    plt.xticks(rotation=90)
    plt.xlabel("Expense Type")
    plt.ylabel("Count")
    plt.title("Top Operating Expenses")
    plt.show()
    return expense_summary

print("Expense Breakdown:")
print(expense_breakdown(df))


# In[ ]:





# In[24]:


# Sorting & Filtering
def sort_filter_analysis(df):
    sorted_df = df.sort_values(by=["Sort on Type", "Sort on SubType"])
    print(sorted_df.head(10))

print("Sorted & Filtered Data:")
sort_filter_analysis(df)


# In[7]:


plt.figure(figsize=(12, 6))
sns.countplot(y=df["Account"], order=df["Account"].value_counts().index, palette="viridis")

plt.xlabel("Count")
plt.ylabel("Account")
plt.title("Transaction Count by Account", fontsize=14, color="red")

plt.show()


# In[16]:


df.to_csv("Cleaned_Financial_Data.csv", index=False)


# In[15]:


import os
print(os.getcwd())  # Prints the current working directory


# In[ ]:




