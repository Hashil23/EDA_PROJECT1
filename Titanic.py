import pandas as pd
#load dataset
data="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(data)

#inspect data
print(df.describe())