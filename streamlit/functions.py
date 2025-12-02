import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data():
	df_raw = pd.read_csv("~/insy6500/projects/insy6500_project/notebooks/Data.csv")
	numeric_cols = df_raw.select_dtypes(include=[np.number]).columns.tolist()
	def remove_outliers_iqr(dataframe, columns, threshold=1.5):
    		df_clean = dataframe.copy()
    		for col in columns: #first find interquartile range for each column
        		Q1 = df_clean[col].quantile(0.25)
        		Q3 = df_clean[col].quantile(0.75)
        		IQR = Q3 - Q1
        
        		# create upper and lower limits
        		lower_bound = Q1 - threshold * IQR
        		upper_bound = Q3 + threshold * IQR
        
        		# git rid of outliers
        		df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    
    		return df_clean

	# remove outliers from data
	numeric_cols.remove('high_risk_flag')
	df_cleaned = remove_outliers_iqr(df_raw, numeric_cols, threshold=1.5)
	return df_cleaned


def create_corr(df_cleaned):
	numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns.tolist()
	numeric_cols.remove('high_risk_flag')
	corr = df_cleaned[numeric_cols].corr()
	sns.heatmap(corr)
	fig = plt.show
	return fig
