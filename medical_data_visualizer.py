import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df = df.assign(overweight=np.where(df["weight"]/((df["height"]/100)**2) > 25, 1, 0))

# 3
columns = ["smoke","alco","active","cardio","overweight"]

for col in columns:
    df[col] = np.where(df[col] == 1, 1, 0)


for col in ["cholesterol", "gluc"]:
    df[col] = np.where(df[col] == 1, 0, 1)  


# 4
def draw_cat_plot():
    # 5
    columns = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns)


    # 6
    cat_plot = sns.catplot(
        data=df_cat,
        kind="count",
        x="variable",
        hue="value",
        col="cardio"
    )
    
    cat_plot.set_axis_labels("variable", "total")
    cat_plot.set_titles("Cardio = {col_name}")

    # 8
    fig = cat_plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()
    

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        cbar_kws={"shrink": 0.5}
    )

    # 16
    fig.savefig('heatmap.png')
    return fig