# Time Series Analysis in Python

This repository contains Python code for performing various time series analysis tasks. Below are the details of the functions provided:

## Functions

### `moving_average`

This function calculates the moving average of a time series data frame.

```python
def moving_average(DF, WINDOW_SIZE):
    """
    This function calculates the moving average of a time series data frame.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.
    WINDOW_SIZE : int
        The size of the moving average window.

    Returns
    -------
    pandas.DataFrame
        The data frame with the moving averages.
    """
#Function code here 
 ```

# `remove_trend This` 
function removes the linear trend from a time series data frame.

```python
def remove_trend(DF, VALUES, TIME):
    """
    This function removes the linear trend from a time series data frame.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.

    Returns
    -------
    pandas.DataFrame
        The data frame with the linear trend removed.
    """
    #Function code here 
```


# `remove_sazonality`
This function removes the seasonal component from a time series data frame.

```python
def remove_sazonality(DF, SEASONAL_PERIOD, VALUES, TIME):
    """
    This function removes the seasonal component from a time series data frame.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.
    SEASONAL_PERIOD : int
        The period of the seasonal component to be removed.

    Returns
    -------
    pandas.DataFrame
        The data frame with the seasonal component removed.
    """
    #Function code here 
```
# `remove_sazonality_and_trend`
This function removes the seasonal and linear trend components from a time series data frame.

```python
def remove_sazonality_and_trend(DF, SEASONAL_PERIOD, VALUES, TIME):
    """
    This function removes the seasonal and linear trend components from a time series data frame.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.
    SEASONAL_PERIOD : int
        The period of the seasonal component to be removed.
    VALUES : str
        The name of the column containing the time series values.
    TIME : str
        The name of the column containing the time stamps.

    Returns
    -------
    pandas.DataFrame
        The data frame with the seasonal and linear trend components removed.
    """
    #Function code here 
```
    

# `autocorrelation`
This function calculates the autocorrelation function (ACF) of a time series data frame.

```python
def autocorrelation(DF, H, save_path):
    """
    This function calculates the autocorrelation function (ACF) of a time series data frame.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.
    H : int
        The maximum lag value for the ACF.
    save_path : str
        The path and filename where the ACF plot should be saved.

    Returns
    -------
    numpy.ndarray
        The ACF values.
    """
    #Function code here 
```

## Requirements
* Python 3.x
* Pandas
* Plotly Express
* Plotly Graph Objects
