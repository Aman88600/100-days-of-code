# Importing Pandas
import pandas as pd
# Reading the csv file
df = pd.read_csv('salaries_by_college_major.csv')
#print(df.shape)
#print(df.isna())
#print(f"Columns = {df.columns}")
#print(df.tail())
clean_df = df.dropna()
#print(clean_df.tail())
#print(clean_df['Starting Median Salary'].max())
#print(clean_df['Starting Median Salary'].idxmax())
#print(clean_df['Undergraduate Major'].loc[43])
#print(clean_df.loc[43])

# Which Carrier has the highest mid carrier salary
all_mid_carrier_salaries = clean_df['Mid-Career Median Salary']
#print(f'Highest mid carrier salary = ${all_mid_carrier_salaries.max()}')
#print(f'row with the highest mid carrier salary = {all_mid_carrier_salaries.idxmax()}')
row = all_mid_carrier_salaries.idxmax()
print(f'College Major with the highest mid carrier salary = {clean_df["Undergraduate Major"].loc[row]}')
print(f'Starting Median Salary = {clean_df["Starting Median Salary"].loc[row]}')
print(f'Mid-Career Median Salary = {clean_df["Mid-Career Median Salary"].loc[row]}')
print(f'Mid-Career 10th Percentile Salary = {clean_df["Mid-Career 10th Percentile Salary"].loc[row]}')
print(f'Mid-Career 90th Percentile Salary = {clean_df["Mid-Career 90th Percentile Salary"].loc[row]}')

# Which Carrie has the lowest starting salary and how much do people earn with it
all_starting_salaries = clean_df['Starting Median Salary']
row = all_starting_salaries.idxmin()
print(f'College Major with the lowest starting salary = {clean_df["Undergraduate Major"].loc[row]}')
print(f'Starting Median Salary = {clean_df["Starting Median Salary"].loc[row]}')
print(f'Mid-Career Median Salary = {clean_df["Mid-Career Median Salary"].loc[row]}')
print(f'Mid-Career 10th Percentile Salary = {clean_df["Mid-Career 10th Percentile Salary"].loc[row]}')
print(f'Mid-Career 90th Percentile Salary = {clean_df["Mid-Career 90th Percentile Salary"].loc[row]}')

# which major has the lowerst mid carrier salary and how much people can expect to earn form it
all_mid_carrier_salaries = clean_df['Mid-Career Median Salary']
#print(f'Highest mid carrier salary = ${all_mid_carrier_salaries.max()}')
#print(f'row with the highest mid carrier salary = {all_mid_carrier_salaries.idxmax()}')
row = all_mid_carrier_salaries.idxmin()
print(f'College Major with the lowest mid carrier salary = {clean_df["Undergraduate Major"].loc[row]}')
print(f'Starting Median Salary = {clean_df["Starting Median Salary"].loc[row]}')
print(f'Mid-Career Median Salary = {clean_df["Mid-Career Median Salary"].loc[row]}')
print(f'Mid-Career 10th Percentile Salary = {clean_df["Mid-Career 10th Percentile Salary"].loc[row]}')
print(f'Mid-Career 90th Percentile Salary = {clean_df["Mid-Career 90th Percentile Salary"].loc[row]}')

# Calculating the difference between 90th percetile and 10th percentile
spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]

print(clean_df.sort_values('Mid-Career 90th Percentile Salary').tail())

clean_df.insert(1, "Spread", spread_col)
print(clean_df.sort_values('Spread').tail())



# Group By
print(clean_df.groupby('Group')['Starting Median Salary'].mean())













