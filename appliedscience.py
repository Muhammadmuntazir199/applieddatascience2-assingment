# data set i have choosen is olympics 
import pandas
import matplotlib.pyplot as plot
import seaborn
olympicsecnomics = pandas.read_csv(r'C:\Users\faiza\Downloads\olympics-economics.csv')
print(olympicsecnomics.head())
#cleaning the dataset 
print(olympicsecnomics.isnull().sum())
olympicsecnomics.drop_duplicates(inplace=True)
#Bar Chart
plot.figure(figsize=(14, 6))
plot.bar(olympicsecnomics['country'], olympicsecnomics['gold'], color='gold')
plot.ylabel('Gold medals')
plot.xlabel('Country')
plot.xticks(rotation=90)  
plot.show()
#HeatMap
columns_choosen = olympicsecnomics[['gold', 'total', 'gdp', 'population']]
comatrix = columns_choosen.corr()
plot.figure(figsize=(12, 12))
seaborn.heatmap(comatrix, annot=True, cmap='PuOr', linewidths=0.7)
plot.show()
#Scatter Graph
plot.figure(figsize=(8, 8))
plot.scatter(olympicsecnomics['gdp'], olympicsecnomics['gold'], color='red', edgecolor='black')
plot.title('Scatter Plot: GDP vs Gold Medals')
plot.ylabel('Gold medals')
plot.xlabel('GDP')
plot.show()
