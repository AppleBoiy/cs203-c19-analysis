import pandas as pd

df = pd.read_csv('../../data/data.csv')
#from ranking2
top_5_C = ['California','Texas','Florida','New York','Illinois']
less_5_C = ['Vermont','District of Columbia','Wyoming','South Dakota','North Dakota']

#clfn = df[(df['Province/State'] == 'California')].sort_values(by='Date')

#print(clfn)


#make .csv file top 5 and less 5 in dist
rank = 1
for i in top_5_C :
    file_name = "rank_TOP_" + str(rank) + "_" + i + ".csv"
    path = 'dist/' + file_name
    temp_file = df[(df['Province/State'] == i)].sort_values(by='Date')
    temp_file.reset_index(drop=True, inplace=True)
    temp_file.to_csv(path, index=False)
    rank += 1



rank = 1
for i in less_5_C :
    file_name = "rank_LESS_" + str(rank) + "_" + i + ".csv"
    path = 'dist/' + file_name
    temp_file = df[(df['Province/State'] == i)].sort_values(by='Date')
    temp_file.reset_index(drop=True, inplace=True)
    temp_file.to_csv(path, index=False)
    rank += 1