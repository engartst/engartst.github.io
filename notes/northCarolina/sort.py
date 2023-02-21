import pandas as pd

df = pd.read_csv('coordsWithDist.csv')

df.sort_values('Distance').to_csv("coordsWithDistSorted.csv")
