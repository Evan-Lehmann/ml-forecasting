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
      - The page displays the original dataset, which the model was initially fitted on. The model will forecast for the selected number of years.
      - The trained model file is in the repo and can be found [here](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/forecast.pkl) 
      - See [Algorithm](##Algorithm) for more info on the algorithm.
    - [dashboard.py](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/app_pages/dashboard.py)
      - Dashboard with descriptive charts and statistics from the original data.
        - STL Decomposition (Seasonal and Trend Decomposition using Loess), a time series decomposition method, was used to decompose the the time series into trend, noise, and seasonal components. More information on this technique can be found [here](https://en.wikipedia.org/wiki/Decomposition_of_time_series)
- Jupyter Notebook  
  - The Jupyter Notebook, [ml_classification.ipynb](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/ml_clustering.ipynb), is where the model was constructed and is also used for exploratory purposes.
- Dataset
  - The original dataset can be found on Kaggle, [here](https://www.kaggle.com/hemil26/gold-rates-1985-jan-2022). 

## <a name="algorithm">Algorithm</a>
- The forecasting algorithm used is Holt's Linear Method, also called double exponential smoothing.
  - Double exponential smoothing is an extension of single exponential smoothing
    - Single exponential smoothing (SES) is a forecasting technique used with univariate data. 
      - SES assumes that data has no trend or seasonality/cyclicality.
      - SES uses a weighted sum of past observations to make forecasts. As observations get older, their weights decrease exponentially. 
      - SES's only parameter is α, which is known as the smoothing coefficient. Alpha's value is between 0 and 1, and it controls the rate at which past observations decay.
      - SES Formula: yₜ = αxₜ + (1 - α)yₜ₋₁ 
        - Notaion: α: smoothing factor, t: time period
  - Double exponential smoothing differs from SES because it adds a trend component
    - This makes double exponential smoothing appropriate when trends are present in a time series
  - Double exponential smoothing techniques are commonly used in marketing and finance to make short-term forecast on time series with trend.
  - Double exponential smoothing additive method forecasting formula: ŷᵧ₊ₙ = lₜ + nbₜ
    -  Level Formula: lₜ = (1 - α)lₜ₋₁ + αx₁
    -  Trend Formula: bₜ = (1 - β)bₜ₋₁ + β(lₜ - lₜ₋₁)
    -  Model Formula: yᵧ₊ₙ = lₜ + bₜ
    -  Notation: α: level smoothing constant, β: trend smoothing constant, t: observed time units, n: number of time units to forecast for
  - Double exponential smoothing additive method forecasting formula: ŷᵧ₊ₙ = lₜ + (ϕ¹ + ϕ² + ϕʰ)nbₜ
    -  Level Formula: lₜ = (1 - α)lₜ₋₁ + αx₁
    -  Trend Formula: bₜ = (1 - β)bₜ₋₁ + β(lₜ - lₜ₋₁)
    -  Model Formula: yᵧ₊ₙ = lₜ + bₜ
    -  Notation: α: level smoothing constant, β: trend smoothing constant, t: observed time units, n: number of time units to forecast for, ϕ: daming coefficient
  
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

 ## <a name="demo">Deployed Demo</a>
 - A deployed demonstration of this app can be found at https://ml-forecasting-app.herokuapp.com/. The app was hosted using Heroku, a cloud platform used to work with applications. 
 - Deployment Dependencies 
    - [Procfile](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/Procfile) is used to declare the commands run by the application's dynos. 
    - [setup.sh](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/setup.sh) is used to add shell commands.
    - [.slugignore](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/.slugignore) is used to remove files after code is pushed to Heroku.
    - [runtime.txt](https://github.com/Evan-Lehmann/ml-forecasting/blob/main/runtime.txt) is used to declare the Python version used. 
 
## License 
This project is licensed under the [MIT license](LICENSE).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
