import pandas as pd
file_path ="C:\\Users\\ManishaBheemanpally\\Downloads\\data.csv"
df = pd.read_csv(file_path)
#pd.options.display.max_rows=99
print(df.to_string()) 
#print(df.head())
#print(df.tail())
'''print(df.info())
df.dropna(inplace=True)
df.loc[7,'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
df.drop_duplicates(inplace = True)    
print(df.to_string())'''

