# ml-forecasting
This project is a demonstration of forecasting, a subset of regression, which is a supervised learning method. This forecasting algorithm is integrated in a web app. This project was done primarily in Python, but also uses Jupyter Notebook.

## General Info
- Web App
  - File Info
    - [app.py](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/app.py) compiles the individual pages into a multipage web app.
    - [multiapp.py](https://github.com/Evan-Lehmann/ml-forecastingn/blob/main/multiapp.py) acts as a framework that allows multipage web apps.
    - [app_pages](https://github.com/Evan-Lehmann/ml-forecastingn/tree/main/app_pages) contains the different pages of the web app.  
  - Page Info
    - [model.py](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/app_pages/model.py) 
      - The page displays the original dataset, which the model was initially fitted on. The model will forecast for the selected number of months.
      - The trained model file is in the repo and can be found [here](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/forecast.pkl) 
      - See [Algorithm](##Algorithm) for more info on the algorithm.
    - [dashboard.py](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/app_pages/dashboard.py)
      - Dashboard with descriptive charts and statistics from the original data.
        - STL Decomposition (Seasonal and Trend Decomposition using Loess), a time series decomposition method, was used to decompose the the time series into trend, noise, and seasonal components. More information on this technique can be found [here](https://en.wikipedia.org/wiki/Decomposition_of_time_series)
- Jupyter Notebook  
  - The Jupyter Notebook, [ml_classification.ipynb](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/ml_clustering.ipynb), is where the model was constructed and is also used for exploratory purposes.
- Dataset
  - The original dataset can be found on Kaggle, [here](https://www.kaggle.com/hemil26/gold-rates-1985-jan-2022). 

## Algorithm
- The forecasting algorithm used is Holt's Linear Trend (also called double exponential smoothing)
  - This algorithm is an extension of single exponential smoothing (SES), which is a univariate forecasting method the produces forecasts using weighted averages from the past. As the observations get older, the weights decrease exponentially. 
    - SES uses the parameter *smoothing constant* to determine the degree to which past observations have on forecasts. The higher the value, the more influence past observations have.
  - Holt's Linear Trend employs two *smoothing constants* at each period, which helps it handle trends better than single exponential smoothing.

## Usage
- [app.py](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/app.py)
  - The web app can be launched locally by entering: 

    ```
    streamlit run app.py
    ```

## Dependencies

- Python Version:

 ```
 Python 3.10.1
 ```
 
- Python Packages:

 ```
 pip install -r requirements.txt
 ```

## Screenshots

 
## License 
This project is licensed under the [MIT license](LICENSE).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)