import seaborn as sns

tips = sns.load_dataset('tips')

# distibuted chart
sns.distplot(tips['total_bill']) # bin with trend line(Kernel density estimation)

sns.distplot(tips['total_bill'], kde= False) # bin without trend line(KDE)

sns.distplot(tips['total_bill'],kde=False,bins=20) # 20 bins, defining bin size

# jointplot - allows to compare 2 measures
#KIND
#“scatter”
#“reg”
#“resid”
#“kde”
#“hex”
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')

#pairplot
# which takes entire dataframes to plot the chart on available measures
sns.pairplot(tips)

# hue represents the grouping element and legend, palette will give you option to select the color combination
sns.pairplot(tips,hue='sex',palette='coolwarm')

#rug plt
# Draw dash mark for every values for distribution
sns.rugplot(tips['total_bill'])




