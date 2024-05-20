#Medical_data_visualizer

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['BMI'] = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['BMI'] > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    # 6
    df_cat = df_cat.groupby(['cardio'], as_index=False, sort= True).value_counts()
    df_cat = df_cat.rename(columns = {'count':'total'})
    df_cat = df_cat.sort_values(by = 'variable', ascending = True)
    # 7
    sns.catplot(x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar', data = df_cat)
    # 8
    fig = sns.catplot(x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar', data = df_cat).fig
    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df.where((df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)))    
    df_heat = df_heat.drop('BMI', axis = 1)
    # 12
    corr = df_heat.corr()
    # 13
    masked = (np.triu(np.ones_like(corr, dtype=bool)))
    # 14
    fig, ax = plt.subplots(figsize=(10, 8))
    # 15
    sns.heatmap(data=corr, mask=masked, annot = True, fmt = '.1f', cmap = 'YlOrRd')
    # 16
    fig.savefig('heatmap.png')
    return fig
    