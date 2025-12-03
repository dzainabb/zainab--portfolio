import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


gold_df = pd.read_csv('gold_price.csv')
gold_df['Date'] = pd.to_datetime(gold_df['Date'])


gold_df = gold_df.sort_values('Date')


gold_df['Ordinal'] = gold_df['Date'].map(pd.Timestamp.toordinal)

last_date = gold_df['Date'].max()
cutoff_date = last_date - pd.DateOffset(years=10)

train_df = gold_df[gold_df['Date'] < cutoff_date]
test_df = gold_df[gold_df['Date'] >= cutoff_date]

x_train = train_df['Ordinal'].values
y_train = train_df['Value'].values


forecast_end = last_date + pd.DateOffset(years=10)
future_dates = pd.date_range(start=last_date, end=forecast_end, freq='MS')
future_ordinals = future_dates.map(pd.Timestamp.toordinal)


plt.figure(figsize=(14, 8))

plt.plot(gold_df['Date'], gold_df['Value'], color='black', label='Actual Price', linewidth=2)

for deg in range(1, 10):
    # Fit polynomial
    coeffs = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coeffs)

    # Forecast over future 10 years
    future_pred = model(future_ordinals)

    # Plot forecast
    plt.plot(
        future_dates,
        future_pred,
        label=f'Poly Degree {deg}',
        linewidth=1.5
    )

plt.title("Gold Price Forecasting Using Polynomial Fits (Degrees 1–9)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Gold Price (USD/oz)")
plt.legend()
plt.grid(True)
plt.show()
