import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[(
    (df["value"] <= df["value"].quantile(0.975)) &
    (df["value"] >= df["value"].quantile(0.025))
)]


def draw_line_plot():
    # Draw line plot
    x = df.index
    y= df['value']
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.plot(x,y)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["year"] = df.index.year
    df["month"] = df.index.month
    df_bar = df.groupby(["year", "month"])["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(
        kind="bar",
        figsize=(10, 6)
    ).figure

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=month_names)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0] , hue="year")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1] , hue="month")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    axes[0].ticklabel_format(style='plain', axis='y')
    axes[1].ticklabel_format(style='plain', axis='y')

    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig