import requests
import sqlite3 as lite
import datetime
import collections
import pandas as pd 
import matplotlib.pyplot as plt  

api_key = ''  
url = 'https://api.forecast.io/forecast/' + api_key

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

end_date = datetime.datetime.now()

# Store temperature data 
con = lite.connect('weather.db')
cur = con.cursor()

cities.keys()
with con:
    cur.execute('drop table if exists daily_temp')
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, city1 REAL, city2 REAL, city3 REAL, city4 REAL, city5 REAL);')

query_date = end_date - datetime.timedelta(days=30) 

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1) 

for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) 
    while query_date < end_date:
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))
        with con:
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))
        query_date += datetime.timedelta(days=1) 

con.close()

# Profile temperature data  
df = pd.read_sql_query("SELECT * FROM daily_temp", con, index_col = "day_of_reading")
for i in df.columns:
    print("Range:", i, max(df[i])-min(df[i]))
for i in df.columns: 
    print("Mean:", i, df[i].mean())
for i in df.columns: 
    print("Variance:", i, df[i].variance())

plt.plot(df)
plt.show()   


