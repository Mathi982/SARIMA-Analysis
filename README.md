# SARIMA-Analysis

This project uses Python to perform a time series forecasting using the SARIMA (Seasonal AutoRegressive Integrated Moving Average) model on multiple datasets for a client that wanted to see if they could forecast the number of final registrations for a conference based on the way the registrations are being made prior to the stat date of the conference. It involves two sets of code:

* SARIMA Parameters: Determines the optimal SARIMA parameters (order and seasonal order) for each dataset using automatic parameter selection techniques.
* SARIMA Code: Implements the SARIMA model with the best parameters to forecast the registration data.

# SARIMA Parameters

Importing Libraries:
* The SARIMA parameter code imports pandas for data manipulation and pmdarima for automatic SARIMA parameter selection.

find_best_sarima_order Function:
* This function takes a file path as input.
* It loads the dataset, ensures a continuous date index, and utilizes auto_arima from pmdarima to find the best SARIMA parameters.
* The best SARIMA order and seasonal order are returned.

The code iterates through each dataset file path, calls the find_best_sarima_order function, and prints the best SARIMA order and seasonal order for each dataset.

# SARIMA Code

Importing Libraries:
* The SARIMA code imports pandas for data manipulation, numpy for numerical computations, statsmodels for time series analysis, and matplotlib for plotting.

Forecasting with SARIMA:
* The code loops through each dataset file path.
* For each dataset, it loads the data, ensures a continuous date index, and splits the data into training and testing sets.
* It defines the SARIMA model with the best parameters obtained from the SARIMA parameter code.
* The model is fitted to the training data and used to forecast the future registrations.
* Plots are generated to visualize the training data, actual test data, and forecasted values.
* Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) are calculated to evaluate forecast accuracy.


This SARIMA analysis provides insights into the forecasting of conference registrations based on historical data. By determining optimal SARIMA parameters and implementing the SARIMA model, accurate forecasts can be generated to assist conference organizers in planning and decision-making.
