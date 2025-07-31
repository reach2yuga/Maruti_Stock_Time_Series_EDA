What is Time Series Data¶
Time series data is a sequence of data points in chronological order that is used by businesses to analyze past data and make future predictions. These data points are a set of observations at specified times and equal intervals, typically with a datetime index and corresponding value. Common examples of time series data in our day-to-day lives include:

Measuring weather temperatures
Measuring the number of taxi rides per month
Predicting a company’s stock prices for the next day
Components of Time Series
Time series data consist of four components:

Trend Component: This is a variation that moves up or down in a reasonably predictable pattern over a long period.

Seasonality Component: is the variation that is regular and periodic and repeats itself over a specific period such as a day, week, month, season, etc.,

Cyclical Component: is the variation that corresponds with business or economic 'boom-bust' cycles or follows their own peculiar cycles, and

Random Component: is the variation that is erratic or residual and does not fall under any of the above three classifications.

To make this concept more clear here is a visual interpretation of the various components of the Time Series. You can view the original diagram with its context, here.



[Source](https://www.atap.gov.au/tools-techniques/travel-demand-modelling/6-forecasting-evaluation)
Dataset
In this notebook, we’ll use it to analyze stock prices of Maruti and perform some basic time series operations. Maruti Suzuki India Limited, formerly known as Maruti Udyog Limited, is an automobile manufacturer in India. It is a 56.21% owned subsidiary of the Japanese car and motorcycle manufacturer Suzuki Motor Corporation.[6]As of July 2018, it had a market share of 53% of the Indian passenger car market.



Source - https://www.dsij.in/Portals/0/EasyDNNnews/11202/img-MarutiSuzuki.jpg
Objective
In this notebook, we will introduce some common techniques used in time-series analysis and walk through the iterative steps required to manipulate, visualize time-series data.
