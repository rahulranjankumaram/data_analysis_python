import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/rahulranjankumaram/data_analysis_python/refs/heads/main/medical_examination.csv')

df['overweight'] = (df['weight']/((df['height']/100)**2)>25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot(df):

     df_cat = pd.melt(df, id_vars = ['cardio'],
     value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])
     
     df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index()
     df_cat = df_cat.rename(columns={0:'total'})

     fig_out = sns.catplot(x='variable',y='total',hue='value',col='cardio',data=df_cat,
     kind='bar',order=['cholesterol','gluc','smoke','alco','active','overweight'])
     
     fig = fig_out
     return plt.show()
draw_cat_plot(df)

def draw_heat_map(df):
     
     df_heat = df[
          (df['ap_lo'] <= df['ap_hi']) &
          (df['height'] >= df['height'].quantile(0.025)) &
          (df['height'] <= df['height'].quantile(0.975)) &
          (df['weight'] >= df['weight'].quantile(0.025)) &
          (df['weight'] <= df['weight'].quantile(0.975))]
     
     corr = df_heat.corr()

     mask = np.triu(np.ones_like(corr,dtype=bool))

     fig = plt.subplots(figsize=(12,8))

     sns.heatmap(corr,mask=mask,annot=True,fmt='0.1f',center=0,vmin=-0.2,vmax=0.8,linewidths=1)
     return plt.show()
draw_heat_map(df)
