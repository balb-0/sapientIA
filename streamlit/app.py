import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pmdarima as pm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Function to evaluate the model
def evaluate_model(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return mae, rmse, mape

# Function to process data
@st.cache_data
def load_and_process_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        # Load the default dataset
        df = pd.read_csv('data/default_dataset.csv')

    # Data treatment steps
    df = df[['Ano', 'Mês', 'UEN', 'Vl Liquido Final']]
    df.dropna(inplace=True)
    df['Ano'] = df['Ano'].astype(int)
    df['Mês'] = df['Mês'].astype(int)
    df['Vl Liquido Final'] = df['Vl Liquido Final'].astype(str)
    df['Vl Liquido Final'] = df['Vl Liquido Final'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    df['Vl Liquido Final'] = df['Vl Liquido Final'].astype(float)
    df['UEN'] = df['UEN'].astype('category')
    df.rename(columns={'Ano': 'year', 'Mês': 'month'}, inplace=True)
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
    df.sort_values('date', inplace=True)
    agg_df = df.groupby(['date', 'UEN'])['Vl Liquido Final'].sum().reset_index()
    return agg_df

# Main function
def main():
    st.title('SARIMAX Forecasting App')

    # File upload
    uploaded_file = st.file_uploader('Upload a CSV file (optional)', type='csv')

    # Load and process data
    agg_df = load_and_process_data(uploaded_file)

    # UEN selection
    UEN_list = agg_df['UEN'].unique()
    selected_UEN = st.selectbox('Select UEN', UEN_list)

    # Forecasting
    if st.button('Run Forecast'):
        # Filter data for the selected UEN
        UEN_df = agg_df[agg_df['UEN'] == selected_UEN].copy()
        UEN_df.set_index('date', inplace=True)
        UEN_df.sort_index(inplace=True)

        if len(UEN_df) < 24:
            st.warning(f"Not enough data for UEN {selected_UEN}. Please select another UEN.")
        else:
            # Split into training and testing sets
            train_size = int(len(UEN_df) * 0.8)
            train_data = UEN_df.iloc[:train_size]
            test_data = UEN_df.iloc[train_size:]

            # Endogenous variable
            endog_train = train_data['Vl Liquido Final']
            endog_test = test_data['Vl Liquido Final']

            # Fit SARIMA model
            try:
                with st.spinner('Training the SARIMAX model...'):
                    stepwise_model = pm.auto_arima(endog_train, start_p=1, start_q=1,
                                                   max_p=3, max_q=3, m=12,
                                                   start_P=0, seasonal=True,
                                                   d=None, D=1, trace=False,
                                                   error_action='ignore',
                                                   suppress_warnings=True,
                                                   stepwise=True)

                    model = SARIMAX(endog_train, order=stepwise_model.order, seasonal_order=stepwise_model.seasonal_order)
                    model_fit = model.fit(disp=False)

                # Forecasting
                predictions_test = model_fit.forecast(steps=len(endog_test))
                predictions_future = model_fit.forecast(steps=12)

                # Evaluate model
                mae, rmse, mape = evaluate_model(endog_test, predictions_test)

                st.success(f"Model trained successfully! MAE: {mae:.2f}, RMSE: {rmse:.2f}, MAPE: {mape:.2f}%")

                # Plotting
                fig, ax = plt.subplots(figsize=(12, 6))

                # Plot actual data from test set
                ax.plot(endog_test.index, endog_test, label='Actual Values (Test Set)', color='blue', marker="o")

                # Plot predicted data for test set
                ax.plot(endog_test.index, predictions_test, label='Predicted Values (Test Set)', linestyle='--', color='green', marker="o")

                # Plot forecast for next 12 months
                future_dates = pd.date_range(endog_test.index[-1] + pd.DateOffset(months=1), periods=12, freq='MS')
                ax.plot(future_dates, predictions_future, label='Future Forecast (12 months)', linestyle='--', color='red', marker="o")

                # Vertical line to mark the end of testing
                ax.axvline(x=endog_test.index[-1], color='black', linestyle=':', label='Train/Test Split')

                ax.grid(True, linestyle="-", which="major", color="black", linewidth="0.5")
                ax.set_title(f'UEN {selected_UEN} - Forecast')
                ax.set_xlabel('Date')
                ax.set_ylabel('Vl Liquido Final')
                ax.legend(loc='upper left')

                st.pyplot(fig)

                # Prepare forecast data for download
                forecast_df = pd.DataFrame({
                    'Date': future_dates,
                    'Forecasted Vl Liquido Final': predictions_future
                })
                csv = forecast_df.to_csv(index=False).encode('utf-8')

                # Download button
                st.download_button(
                    label="Download Forecast as CSV",
                    data=csv,
                    file_name=f'forecast_UEN_{selected_UEN}.csv',
                    mime='text/csv',
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Run the app
if __name__ == '__main__':
    main()
