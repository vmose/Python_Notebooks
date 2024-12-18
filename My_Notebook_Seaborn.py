# %%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# %%
tips = sns.load_dataset('tips') #sample dataset from seaborn repository
tips.head()

# %%
#normal distribution
sns.distplot(tips['total_bill'])

# %%
sns.histplot(tips['total_bill']) #histogram

# %%
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter') #scatterplot

# %%
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex') #hexagon grid

# %%
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg') #reg plot

# %%
sns.pairplot(tips) #pair plot for all numerical columns

# %%
sns.pairplot(tips,hue='sex',palette='coolwarm') #pairplot with sex set as a filter

# %%
sns.rugplot(tips['total_bill']) #basic rugplot

# %%
sns.barplot(x='sex',y='total_bill',data=tips) #barplot

# %%
sns.countplot(x='sex',data=tips)   #countplot

# %%
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')  #boxplot

# %%
sns.boxplot(data=tips,palette='rainbow',orient='h') #boxplot oriented horizontally

# %%
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm") #boxplot using 'smoker' as a filter

# %%
sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow') #violin plot

# %%
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')  
#violinplot with 'sex' set as a filter and Set1 colour palette

# %%
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1') 
#violinplot with the two filters expressed within the same set

# %%
sns.stripplot(x="day", y="total_bill", data=tips) #stripplot

# %%
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True) 
#stripplot with jitter=true so that datapoints do not overlap

# %%
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')
#same jitterplot filtered by 'sex'

# %%
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',dodge=True)
#as above but with split filters

# %%
sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", dodge=True)
#swarmplot

# %%
sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)
#combined violinplot and swarmplot

# %%
sns.catplot(x='sex',y='total_bill',data=tips,kind='bar')
#factorplot

# %%
flights = sns.load_dataset('flights')
flights.head(10)
#'flights' dataset from seaborn repository

# %%
y=tips.corr()  #using the 'tips' dataset to create a correlation for the subsequent heatmap
y

# %%
sns.heatmap(y) #heatmap

# %%
sns.heatmap(y,cmap='coolwarm',annot=True) #annotated heatmap with coolwarm color palette

# %%
#creating a crosstabulated dataset from the 'flights' data for the subsequent heatmap
x=flights.pivot_table(values='passengers',index='month',columns='year') 
x

# %%
sns.heatmap(x)

# %%
sns.heatmap(x,cmap='magma',linecolor='white',linewidths=1) #alternative heatmap

# %%
sns.clustermap(x) #clustermap

# %%
sns.clustermap(x,cmap='coolwarm',standard_scale=1) #clustermap with 'coolwarm' gradient

# %%
iris = sns.load_dataset('iris')
iris
#importing 'iris' dataset from seaborn repository

# %%
#pairgrid with seaborn and matplotlib
p = sns.PairGrid(iris)
p.map(plt.scatter)

# %%
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

# %%
sns.pairplot(iris,hue='species',palette='rainbow')
#pairplot with iris dataset and 'species' set as a filter

# %%
f = sns.FacetGrid(tips, col="time",  row="smoker")
f = f.map(plt.hist, "total_bill")
#facetmap

# %%
g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

#tips dataset for facetgrid with time on the columns and smoker on the rows; 'sex' is the chosen filter

# %%
