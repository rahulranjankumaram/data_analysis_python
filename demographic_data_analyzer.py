import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rahulranjankumaram/data_analysis_python/refs/heads/main/adult_data.csv')

print('representation of people of each race')
data = pd.Series(df['race'])
print(data.value_counts())

print('\naverage age of men')
d1 = df[df['sex']==' Male']['age'].mean()
print(round(d1,1))

print('\npercentage of people with bachelors degree')
d2 = df['education'].value_counts(normalize=True)[' Bachelors']*100
print(round(d2,1))

print('\npercentage of people with advanced education earning >50K')
advance = df['education'].isin([' Bachelors',' Masters',' Doctorate'])
d3 = df[advance]['salary'].value_counts(normalize=True)[' >50K']*100
print(round(d3,1))

print('\npercentage of people without advanced education earning >50K')
d4 = df[~advance]['salary'].value_counts(normalize=True)[' >50K']*100
print(round(d4,1))

print('\nminimum hours per week')
mh = df['hours-per-week'].min()
print(mh)

print('\npercentage of people working for minimum hours earns >50K')
mw = df[df['hours-per-week']==mh]
d5 = mw['salary'].value_counts(normalize=True)[' >50K']*100
print(round(d5,1))

print('\ncountry with highest percentage of people earning >50K')
country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
data1 = (country_salary[' >50K']*100).sort_values(ascending=True)
print(data1.idxmax(),':',round(data1.max(),1))

print('\nmost popular occupation for people earning >50K in india')
in_occupation = df[(df['native-country'] == ' India') & (df['salary'] == ' >50K')]
print(in_occupation['occupation'].value_counts().idxmax())
