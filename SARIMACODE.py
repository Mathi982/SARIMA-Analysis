import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt
import matplotlib.pyplot as plt

# Replace with whatever datsets you want to use
file_paths = ['/Users/Mathi/Desktop/D19.csv', '/Users/Mathi/Desktop/D21.csv', '/Users/Mathi/Desktop/GP21.csv',
              '/Users/Mathi/Desktop/MSE21.csv', '/Users/Mathi/Desktop/NP21.csv', '/Users/Mathi/Desktop/SRM22.csv',
              '/Users/Mathi/Desktop/SRM23.csv']
sarima_orders = [(0, 1, 2), (1, 1, 1), (1, 1, 1), (0, 0, 1), (0, 1, 2), (1, 0, 0), (2, 0, 2)]
seasonal_orders = [(2, 0, 0, 7), (3, 0, 0, 7), (1, 0, 1, 7), (0, 0, 0, 7), (0, 0, 1, 7), (0, 0, 0, 7), (0, 0, 0, 7)]
# Make sure there are as many orders as there are datasets

# Loop through each file and perform the analysis
for file_path, sarima_order, seasonal_order in zip(file_paths, sarima_orders, seasonal_orders):
    # Load the data
    data = pd.read_csv(file_path)
    data['Created Date'] = pd.to_datetime(data['Created Date'], format='%d/%m/%Y')
    daily_registrations = data.groupby('Created Date').size()

    # Ensure a continuous date index
    all_dates = pd.date_range(start=daily_registrations.index.min(), end=daily_registrations.index.max(), freq='D')
    daily_registrations = daily_registrations.reindex(all_dates, fill_value=0)

    # Splits the data into training and testing sets. You can change the forecast to whenever you want the forecast to begin from
    train_size = int(len(daily_registrations) * 0.8)
    train, test = daily_registrations[:train_size], daily_registrations[train_size:]

    # Define the model
    model = SARIMAX(train, order=sarima_order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False)

    # Forecast
    forecast = model_fit.forecast(steps=len(test))

    # Create a date range for the forecast starting from the first date in the test set
    forecast_dates = test.index

    # Assign the date range as the index of the forecast
    forecast.index = forecast_dates

    # Plotting
    plt.figure(figsize=(15, 6))
    plt.plot(train.index, train, label='Training Data', color='blue')
    plt.plot(test.index, test, label='Actual Test Data', color='green')
    plt.plot(forecast.index, forecast, label='Forecast', color='red')
    plt.title(f'SARIMA Model Forecast from 80% Threshold for {file_path.split("/")[-1]}')
    plt.xlabel('Date')
    plt.ylabel('Number of Registrations')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculates the RMSE and MAE, the closer the values are to 0, the more accurate the forecast
    rmse = sqrt(mean_squared_error(test, forecast))
    mae = mean_absolute_error(test, forecast)
    print(f'RMSE for {file_path.split("/")[-1]}: {rmse}')
    print(f'MAE for {file_path.split("/")[-1]}: {mae}')
