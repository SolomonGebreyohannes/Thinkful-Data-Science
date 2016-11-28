import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:

    cur = con.cursor()

    # Create tables
    cur.execute('DROP TABLE IF EXISTS cities')
    cur.execute('DROP TABLE IF EXISTS weather')
    cur.execute('CREATE TABLE cities(name text, state text)')
    cur.execute('CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)')
  
    # Insert data 
    cur.execute("INSERT INTO cities VALUES('New York City', 'NY')")
    cur.execute("INSERT INTO cities VALUES('Boston', 'MA')")
    cur.execute("INSERT INTO cities VALUES('Chicago', 'IL')")
    cur.execute("INSERT INTO cities VALUES('Miami', 'FL')")
    cur.execute("INSERT INTO cities VALUES('Dallas', 'TX')")
    cur.execute("INSERT INTO cities VALUES('Seattle', 'WA')")
    cur.execute("INSERT INTO cities VALUES('Portland', 'OR')")
    cur.execute("INSERT INTO cities VALUES('San Francisco', 'CA')")
    cur.execute("INSERT INTO cities VALUES('Los Angeles', 'CA')")

    cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January', 62)")
    cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', 59)")
    cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', 59)")
    cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', 84)")
    cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', 77)")
    cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', 61)")
    cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', 63)") 
    cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', 64)") 
    cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', 75)")   
    
    # Join 
    cur.execute("SELECT name, state, year, warm_month, cold_month average_high FROM cities JOIN weather ON name = city")
    tjoins = cur.fetchall()  	    
 
    # Warmest cities in july from the joined table 
    print "The cities that are warmest in July are:"
    for tjoin in tjoins:
	if tjoin[3]=='July':
	   print tjoin[0],",",tjoin[1]    	
	 
    
    










    
