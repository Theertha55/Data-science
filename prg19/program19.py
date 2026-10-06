import pandas as pd



details={
    'name':['a','b','c','d','e'],
    'occupation':['A1','A1','A1','B1','B1'],
    'salary':[20,30,40,27,23],
}
df=pd.DataFrame(details)
print(df)
occ_average_age=df.groupby('occupation')['salary'].mean()
print("average salary per occupation:")
print(occ_average_age)