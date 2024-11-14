# !pip install widgetsnbextension ipywidgets jupyter-js-widgets-nbextension ipympl

# !jupyter nbextension enable --py widgetsnbextension --sys-prefix

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ipywidgets import interactive
from scipy import signal

df_raw = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv",
    usecols=["location", "date", "daily_vaccinations"],
    parse_dates=["date"],
)

df = df_raw[df_raw["location"] == "United States"]

df.set_index("location", inplace=True, drop=True)

df


def make_iplot(window_size, polyorder):
    data_x = df["date"].values
    data_y = df["daily_vaccinations"].values  # original
    data_y_filtered = signal.savgol_filter(data_y, window_size, polyorder)  # smoothed

    # Find peaks (np.greater)
    peak_indexes = signal.argrelextrema(data_y_filtered, np.greater)
    peak_indexes = peak_indexes[0]

    # Find valleys (np.less)
    valley_indexes = signal.argrelextrema(data_y_filtered, np.less)
    valley_indexes = valley_indexes[0]

    # Matplotlib plot
    plt.figure(figsize=(20, 5))
    plt.plot(data_x, data_y, color="grey")  # line plot for the original data
    plt.plot(data_x, data_y_filtered, color="black")  # line plot for the filtered data
    plt.plot(
        data_x[valley_indexes],
        data_y_filtered[valley_indexes],
        "o",
        label="dip",
        color="r",
    )
    plt.plot(
        data_x[peak_indexes],
        data_y_filtered[peak_indexes],
        "o",
        label="peak",
        color="g",
    )
    plt.show()


# this line of code makes the figure appear in the output below
# %matplotlib inline

iplot = interactive(make_iplot, window_size=(1, 100, 2), polyorder=(1, 10, 1))

iplot

# this line of code makes the figure appear in the output below
# %matplotlib inline

iplot = interactive(make_iplot, window_size=(1, 100, 2), polyorder=(1, 10, 1))

iplot
