import pandas as pd
import pmdarima as pm

def find_best_sarima_order(file_path):
    # Load data
    data = pd.read_csv(file_path)
    data['Created Date'] = pd.to_datetime(data['Created Date'], format='%d/%m/%Y')
    daily_registrations = data.groupby('Created Date').size()

    # Ensure a continuous date index
    all_dates = pd.date_range(start=daily_registrations.index.min(), end=daily_registrations.index.max(), freq='D')
    daily_registrations = daily_registrations.reindex(all_dates, fill_value=0)

    # Using auto_arima to find the best SARIMA order
    auto_model = pm.auto_arima(daily_registrations, seasonal=True, m=7,  # Assuming weekly seasonality
                               start_p=0, start_q=0, max_p=3, max_q=3,
                               start_P=0, start_Q=0, max_P=3, max_Q=3,
                               information_criterion='aic', trace=True,
                               error_action='ignore', suppress_warnings=True)

    return auto_model.order, auto_model.seasonal_order

# Example usage
file_paths = ['/Users/Mathi/Desktop/D19.csv', '/Users/Mathi/Desktop/D21.csv', '/Users/Mathi/Desktop/GP21.csv', '/Users/Mathi/Desktop/MSE21.csv',
              '/Users/Mathi/Desktop/NP21.csv', '/Users/Mathi/Desktop/SRM22.csv', '/Users/Mathi/Desktop/SRM23.csv']

for file_path in file_paths:
    order, seasonal_order = find_best_sarima_order(file_path)
    print(f"Best SARIMA order for {file_path}: {order}, Seasonal Order: {seasonal_order}")
