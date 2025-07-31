# Databricks notebook source
import pandas as pd
from datetime import datetime
df = pd.read_csv("/Volumes/workspace/default/data/ADANIPORTS.csv")
df.head

# COMMAND ----------

data = df[['Date','Open','High','Low','Close','Volume','VWAP']]

# COMMAND ----------

data.info()

# COMMAND ----------

data['Date'] = data['Date'].apply(pd.to_datetime)
data.set_index('Date',inplace=True)
data.head()

# COMMAND ----------

data['VWAP'].plot(figsize=(10,6),title='Maruti Stock Prices')
plt.ylabel('VWAP')

# COMMAND ----------

from datetime import datetime
my_year = 2019
my_month = 4
my_day = 21
my_hour = 10
my_minute = 5
my_second = 30

# COMMAND ----------

test_date = datetime(my_year, my_month, my_day)
test_date

# COMMAND ----------

test_date = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
print('The day is : ', test_date.day)
print('The hour is : ', test_date.hour)
print('The month is : ', test_date.month)

# COMMAND ----------

print(data.index.max())
print(data.index.min())

# COMMAND ----------

# Earliest date index location
print('Earliest date index location is: ',data.index.argmin())

# Latest date location
print('Latest date location: ',data.index.argmax())

# COMMAND ----------

df_vwap = df[['Date','VWAP']]
df_vwap['Date'] = df_vwap['Date'].apply(pd.to_datetime)
df_vwap.set_index("Date", inplace = True)
df_vwap.head()

# COMMAND ----------

# Slicing on year
vwap_subset = df_vwap['2017':'2020']

# Slicing on month
vwap_subset = df_vwap['2017-01':'2020-12']

#Slicing on day
vwap_subset = df_vwap['2017-01-01':'2020-12-15']

# COMMAND ----------

import matplotlib.pyplot as plt
ax = vwap_subset.plot(color='blue',fontsize=14)
ax.set_xlabel('Date')
ax.set_ylabel('VWAP')

ax.axvspan('2019-01-01','2019-01-31', color='red', alpha=0.3)
ax.axhspan(6500,7000, color='green',alpha=0.3)

plt.show()

# COMMAND ----------

import seaborn as sns
sns.kdeplot(df_vwap['VWAP'],shade=True)

# COMMAND ----------

# Visualising the VWAP 
df_vwap['VWAP'].plot(figsize=(16,8),title=' volume weighted average price')

# COMMAND ----------

import matplotlib.dates as mdates
ax = df_vwap.loc['2018', 'VWAP'].plot(figsize=(15,6))
ax.set_title('Month-wise Trend in 2018'); 
ax.set_ylabel('VWAP');
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'));

# COMMAND ----------

import matplotlib.dates as mdates
ax = df_vwap.loc['2018-10':'2018-11','VWAP'].plot(marker='o', linestyle='-',figsize=(15,6))
ax.set_title('Oct-Nov 2018 trend'); 
ax.set_ylabel('VWAP');
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'));

# COMMAND ----------

from statsmodels.tsa.seasonal import seasonal_decompose

# Ensure your data has a proper datetime index
df_vwap.index = pd.to_datetime(df_vwap.index)

# For weekly data (52 weeks in a year)
result_mul = seasonal_decompose(df_vwap['VWAP'], model='multiplicative', period=52)
result_add = seasonal_decompose(df_vwap['VWAP'], model='additive', period=52)

# Plot the results
result_mul.plot().suptitle('Multiplicative Decomposition', y=1.05)
plt.tight_layout()
plt.show()

result_add.plot().suptitle('Additive Decomposition', y=1.05)
plt.tight_layout()
plt.show()

# COMMAND ----------

## Extract the Components
# Actual Values = Product of (Seasonal * Trend * Resid)
df_reconstructed = pd.concat([result_add.seasonal, result_add.trend, result_add.resid, result_add.observed], axis=1)
df_reconstructed.columns = ['seas', 'trend', 'resid', 'actual_values']
df_reconstructed.tail()

# COMMAND ----------

# First ensure we're working with a fresh copy to avoid SettingWithCopyWarning
df_vwap = df_vwap.copy()

# Convert Date column to datetime if not already
df_vwap['Date'] = pd.to_datetime(df_vwap['Date'])

# Extract datetime components
df_vwap['year'] = df_vwap['Date'].dt.year
df_vwap['month'] = df_vwap['Date'].dt.month
df_vwap['day'] = df_vwap['Date'].dt.day
df_vwap['day_of_week'] = df_vwap['Date'].dt.dayofweek  # Monday=0, Sunday=6
df_vwap['weekday_name'] = df_vwap['Date'].dt.day_name()  # Updated method name

# Set Date column as index
df_vwap.set_index('Date', inplace=True)

# Display the result
df_vwap.head()

# COMMAND ----------

