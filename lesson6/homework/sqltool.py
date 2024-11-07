import requests
url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
response = requests.get(url)
type(response)
data = response.json()
type(data)
sitenames = []
for items in data['records']:
    sitenames.append([items['sitename'],items['datacreationdate'],items['county'],items['aqi'],items['pm2.5'],items['status'],items['latitude'],items['longitude']])
sitenames = list(sitenames)
print(sitenames)


sql = '''
CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
	county TEXT,
    
	aqi INTEGER,
	status TEXT,
	pm25 NUMERIC,
	date TEXT,
	lat NUMERIC,
	lon NUMERIC
);
'''

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("AQI.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute(sql)

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
    
