import pandas as pd

table = {
    "Name":["mike","mbappe","dembele","olise","kone"],
    "age":[20,21,22,19,20],
    "marks":[90,78,96,57,45]
}

df = pd.DataFrame(table)
print(df)