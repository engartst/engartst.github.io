import geopy.distance
import pandas as pd
df = pd.read_csv('coordsWithDistSorted.csv')
#print(df['Town'])
print(df.iloc[0, 0])
print(len(df.index))
for i in range(len(df.index)):
    house = (36.0770819, -78.8668914)
    town = df.iloc[i][1], df.iloc[i][2]
    #distance = geopy.distance.geodesic(house, town).miles
    #df.loc[i, 'Distance'] = distance
    m_distance = abs(house[0]-town[0]) + abs(house[1]-town[1])
    print(m_distance)
    df.loc[i, 'Manhattan_Distance'] = m_distance

#for index, row in df.iterrows():
    #print(geopy.distance.geodesic(row['Longitude'], row['Latitude']))

#coords_1 = (52.2296756, 21.0122287)
#coords_2 = (52.406374, 16.9251681)
#print geopy.distance.geodesic(coords_1, coords_2).km

df.to_csv('coordsWithDistSortedMan.csv')
