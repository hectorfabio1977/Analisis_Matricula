import pandas as pd

Data_set = pd.read_csv('Ciencia_de_Datos\MentalHealthSurvey.csv')
#Nulos = Data_set.isnull().sum()
#Duplicados = Data_set.duplicated().sum()

#print(Nulos)
#print(Data_set.info())
#print(Data_set.head())
print(Data_set.describe())


