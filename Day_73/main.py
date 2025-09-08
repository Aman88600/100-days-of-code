import pandas as pd
df = pd.read_csv('QueryResults.csv')
# First five rows
print(df.head())

# Last Five rows
print(df.tail())

# Number of rows and columns
print(df.shape)

# Number of entries in each column
print(df.count())

# Counting programming languages
print(df.groupby('TAG').sum())
print(df.groupby('TAG').count())

df['DATE'] = pd.to_datetime(df['DATE'])
print(df['DATE'].head())

# Rehshape
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

import matplotlib.pyplot as plt

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=column)

plt.legend(fontsize=16)
plt.title('6-Month Rolling Average of StackOverflow Posts', fontsize=16)
plt.grid(True)

plt.show()  # Show the second figure
