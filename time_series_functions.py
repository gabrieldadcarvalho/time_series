import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def moving_average(df, window_size):
    """
    This function calculates the moving average of a time series data frame.

    Parameters
    ----------
    df : pandas.DataFrame
        The input data frame containing the time series data.
    window_size : int
        The size of the moving average window.

    Returns
    -------
    pandas.DataFrame
        The data frame with the moving averages.

    """
    averages = df.rolling(window=window_size).mean()

    # Plotting the moving average
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df.iloc[:, 0], label="Original Data")
    plt.plot(
        averages.index,
        averages.iloc[:, 0],
        label=f"Moving Average (Window Size: {window_size})",
    )
    plt.title(f"Moving Averages (Window Size: {window_size})")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"moving_averages_{window_size}.png")
    plt.show()


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
    import plotly.express as px

    DATA_FRAME_SEM_TENDENCIA = DF[VALUES].diff().dropna()
    DATA_FRAME_SEM_TENDENCIA.index = DF.iloc[1:].index
    GRAFICO_SEM_TENDENCIA = px.line(x=DF[TIME][1:], y=DATA_FRAME_SEM_TENDENCIA)
    GRAFICO_SEM_TENDENCIA.update_layout(
        title=f"Gráfico de Vendas Sem Tendência - D(Yt) = Yt - Yt-1", xaxis_title=TIME
    )
    GRAFICO_SEM_TENDENCIA.write_image("grafico_sem_tendencia.png")
    return DATA_FRAME_SEM_TENDENCIA


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
    import plotly.express as px

    DATA_FRAME_SEM_SAZONALIDADE = DF[VALUES].diff(SEASONAL_PERIOD).dropna()
    GRAFICO_SEM_TENDENCIA = px.line(
        x=DATA_FRAME[TIME][SEASONAL_PERIOD:], y=DATA_FRAME_SEM_SAZONALIDADE
    )
    GRAFICO_SEM_TENDENCIA.update_layout(
        title=f"Gráfico de Vendas Sem Sazonalidade", xaxis_title=TIME
    )
    GRAFICO_SEM_TENDENCIA.write_image("grafico_sem_sazonalidade.png")
    return DATA_FRAME_SEM_SAZONALIDADE


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
    import plotly.express as px

    DATA_FRAME_SEM_SAZONALIDADE_TENDENCIA = (
        DF[VALUES].diff(SEASONAL_PERIOD).diff().dropna()
    )
    GRAFICO_SEM_SAZONALIDADE_TENDENCIA = px.line(
        x=DATA_FRAME[TIME][SEASONAL_PERIOD + 1 :],
        y=DATA_FRAME_SEM_SAZONALIDADE_TENDENCIA,
    )
    GRAFICO_SEM_SAZONALIDADE_TENDENCIA.update_layout(
        title=f"Gráfico de Vendas Sem Sazonalidade e Tendência", xaxis_title=TIME
    )
    GRAFICO_SEM_SAZONALIDADE_TENDENCIA.write_image(
        "grafico_sem_sazonalidade_e_tendencia.png"
    )
    return DATA_FRAME_SEM_SAZONALIDADE_TENDENCIA


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
    N = len(DF)
    ACF = []
    lags = list(range(H + 1))

    for lag in lags:
        Sxy = 0
        Sxx = 0
        for i in range(lag, N):
            Sxy += (DF.iloc[i] - DF.mean()) * (DF.iloc[i - lag] - DF.mean())
            Sxx += (DF.iloc[i] - DF.mean()) ** 2

        ACF.append(Sxy / Sxx)

    # Removendo o primeiro elemento da lista (autocorrelação no atraso 0)
    ACF = ACF[1:]

    # Criando o gráfico de autocorrelação com Plotly Express
    fig = px.bar(x=lags[1:], y=ACF, labels={"x": "Lag", "y": "Autocorrelation"})
    fig.update_layout(
        title="Função de Autocorrelação (ACF)",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
    )

    # Salvando o gráfico em um arquivo .png
    fig.write_image(save_path)

    return ACF


def graph_color(DF, VALUE, TIME):
    """
    This function creates a line plot of the time series data grouped by year, and saves the plot as an image file.

    Parameters
    ----------
    DF : pandas.DataFrame
        The input data frame containing the time series data.
    VALUE : str
        The name of the column containing the time series values.
    TIME : str
        The name of the column containing the time stamps.

    Returns
    -------
    None
        The function saves the line plot as an image file.

    """
    import plotly.graph_objects as go

    # Convertendo a coluna de tempo para o tipo datetime
    DF[TIME] = pd.to_datetime(DF[TIME])

    # Extraindo o ano da coluna de tempo
    DF["Ano"] = DF[TIME].dt.year

    # Agrupando os dados pelo ano
    GRUPO_ANO = DF.groupby("Ano")

    # Criando um objeto de figura para o gráfico
    GRAFICO_COR_POR_ANO = go.Figure()

    # Iterando sobre cada ano e adicionando uma linha ao gráfico
    for year, group in GRUPO_ANO:
        GRAFICO_COR_POR_ANO.add_trace(
            go.Scatter(x=group[TIME], y=group[VALUE], mode="lines", name=f"Ano {year}")
        )

    # Atualizando o layout do gráfico
    GRAFICO_COR_POR_ANO.update_layout(
        title="Evolução de Vendas por Ano",
        xaxis_title="Mês",
        yaxis_title="Vendas",
        showlegend=True,
    )

    # Salvando o gráfico como uma imagem
    GRAFICO_COR_POR_ANO.write_image("vendas_por_ano_colorido.png")
