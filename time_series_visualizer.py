import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

f='https://raw.githubusercontent.com/rahulranjankumaram/data_analysis_python/refs/heads/main/fcc-forum-pageviews.csv'
df = pd.read_csv(f)

bottom = df['value'].quantile(0.025)
top = df['value'].quantile(0.975)
df = df[(df['value'] >= bottom) & (df['value'] <= top)]

def draw_line_plot(df):
    dfl = df.copy()
    plt.figure(figsize=(9,6))
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(dfl['date'],dfl['value'])
    return plt.show()

def draw_bar_plot(df):
    dfbar = df.copy()
    dfbar['date'] = pd.to_datetime(dfbar['date'])
    dfbar['year'] = dfbar['date'].dt.year
    dfbar['month'] = dfbar['date'].dt.month
    month_order = {
      1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',
      11:'Nov',12:'Dec'}
    dfbar['month'] = dfbar['month'].map(month_order)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    dfbar['month'] = pd.Categorical(dfbar['month'],categories=month_order, ordered=True)
    plt.figure(figsize=(16,6))
    sns.barplot(data=dfbar,x='year',y='value',hue='month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views')
    plt.legend(title='Months')
    return plt.show()

def draw_box_plot(df):
    dfbox = df.copy()
    month_order = {
    1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',
      11:'Nov',12:'Dec'}
    dfbox['date'] = pd.to_datetime(dfbox['date'])
    dfbox['year'] = dfbox['date'].dt.year
    dfbox['month'] = dfbox['date'].dt.month
    dfbox['month'] = dfbox['month'].map(month_order)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    dfbox['month'] = pd.Categorical(dfbox['month'],categories=month_order, ordered=True)
    fig,axes=plt.subplots(1,2,figsize=(16,6))
    sns.boxplot(ax=axes[0],x='year',y='value',data=dfbox)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(ax=axes[1],x='month',y='value',data=dfbox)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    return plt.show()

draw_line_plot(df)
draw_bar_plot(df)
draw_box_plot(df)