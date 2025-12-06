
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    df_raw = pd.read_csv("../notebooks/Data.csv")
    numeric_cols = df_raw.select_dtypes(include=[np.number]).columns.tolist()

    def remove_outliers_iqr(dataframe, columns, threshold=1.5):
        df_clean = dataframe.copy()
        for col in columns:
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            df_clean = df_clean[
                (df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)
            ]
        return df_clean

    numeric_cols.remove('high_risk_flag')
    df_cleaned = remove_outliers_iqr(df_raw, numeric_cols, threshold=1.5)
    return df_cleaned


def create_corr(df_cleaned):
    numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols.remove('high_risk_flag')

    fig, ax = plt.subplots()
    corr = df_cleaned[numeric_cols].corr()
    sns.heatmap(corr, ax=ax)
    return fig

def create_hist(df_cleaned):
    df_cleaned = df_cleaned.copy()
    df_cleaned['screentime_bucket'] = pd.cut(
        df_cleaned['device_hours_per_day'],
        bins=[0, 3, 6, 9, float("inf")],
        labels=["0-3", "3-6", "6-9", "9+"],
        right=False
    )
    fig, ax = plt.subplots()
    sns.histplot(
        data=df_cleaned,
        x="depression_score",
        hue="screentime_bucket",
        multiple="stack",
        ax=ax
    )
    ax.set_xlabel('Depression')
    ax.set_title('Depression Density based on Screentime')
    return fig

def split_hist(df_cleaned):
    df_cleaned = df_cleaned.copy()
    df_cleaned['screentime_bucket'] = pd.cut(
        df_cleaned['device_hours_per_day'],
        bins=[0, 3, 6, 9, float("inf")],
        labels=["0-3", "3-6", "6-9", "9+"],
        right=False
    )
    # displot is figure-level and returns a FacetGrid
    g = sns.displot(
        data=df_cleaned,
        x="depression_score",
        hue="screentime_bucket",
        col="screentime_bucket"
    )
    fig = g.fig  # get the underlying matplotlib Figure
    return fig
