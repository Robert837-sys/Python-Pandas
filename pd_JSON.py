import pandas as pd 
df=pd.read_json('data.json')
print(df.to_string())
# Tip: use to_string() to print the entire DataFrame.