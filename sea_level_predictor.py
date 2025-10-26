import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    plt.figure(figsize=(10,6))
    plt.scatter(x, y, label="Original Data", alpha=0.6)

    # --- First line of best fit (all data) ---
    slope_all, intercept_all, r_all, p_all, std_err_all = linregress(x, y)
    x_extended = pd.Series(range(int(x.min()), 2051))
    y_extended = slope_all * x_extended + intercept_all
    plt.plot(x_extended, y_extended, color='red', label='Fit: All Data')

    # --- Second line of best fit (from 2000 onward) ---
    df_recent = df[df["Year"] >= 2000]
    x_recent = df_recent["Year"]
    y_recent = df_recent["CSIRO Adjusted Sea Level"]

    slope_recent, intercept_recent, r_recent, p_recent, std_err_recent = linregress(x_recent, y_recent)
    x_recent_extended = pd.Series(range(2000, 2051))
    y_recent_extended = slope_recent * x_recent_extended + intercept_recent
    plt.plot(x_recent_extended, y_recent_extended, color='green', label='Fit: 2000–Present')

    # --- Labels and title ---
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
