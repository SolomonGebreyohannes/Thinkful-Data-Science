from bs4 import BeautifulSoup
import requests 
import pandas as pd 
import sqlite3 as lite 
import csv  

# Get data 
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)
soup = BeautifulSoup(r.content)

hlist = soup.findAll('tr', attrs=('class', 'tcont'))
hlist = hlist[:93] 

countries = []
for l in hlist:     
	countries.append([l.contents[1].string, l.contents[3].string, l.contents[9].string, l.contents[15].string, l.contents[21].string]) 

countries_df = pd.DataFrame(countries) 
countries_df.columns = ['Country', 'Year', 'Total', 'Men', 'Women']
 
countries_df['Total'] = [int(i) for i in countries_df['Total']]
countries_df['Men'] = [int(i) for i in countries_df['Men']] 
countries_df['Women'] = [int(i) for i in countries_df['Women']] 

# Store data  
con = lite.connect('education.db')
cur = con.cursor() 

countries_df.to_csv('school_expectancy.csv', header=True, index=False)
with con:
    cur.execute('drop table if exists school_expectancy')
    cur.execute('CREATE TABLE school_expectancy (cName, year, tYears, mYears, fYears)')

with open('school_expectancy.csv') as inputFile:
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        line_db = [line[0], line[1], line[2], line[3], line[4]]
        with con:
            cur.execute('INSERT INTO school_expectancy (cName, year, tYears, mYears, fYears) VALUES (?, ?, ?, ?, ?);', line_db)

# Get and store another data 
with con: 
    cur.execute('drop table if exists gdp')
    cur.execute('CREATE TABLE gdp (country_name text, _1999 numeric, _2000 numeric, _2001 numeric, _2002 numeric, _2003 numeric, _2004 numeric, _2005 numeric, _2006 numeric, _2007 numeric, _2008 numeric, _2009 numeric, _2010 numeric)')

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile)     
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-5]) + '");')

# Combine 
with con:
    cur.execute('drop table if exists combined')
    cur.execute('CREATE TABLE combined (country, gdp, totalyears)')

with con:
    cur.execute('INSERT INTO combined (country, gdp, totalyears) SELECT gdp.country_name, _2005, Tota FROM gdp JOIN school_years ON gdp.country_name = school_expectancy.country_name;')
 
combined_df = pd.read_sql_query("SELECT * FROM combined", con, index_col = "country")

combined_df.dropna(inplace=True) 
combined_df = combined_df[combined_df['gdp'] != ''] 

# TODO: Analysis 
