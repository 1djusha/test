import psycopg2

conn = psycopg2.connect(dbname='postgres', user='test', password='123', host='10.220.177.217')
if conn :
    print('+')
cursor = conn.cursor()
cursor.execute('SELECT * FROM playground')
for row in cursor:
    print(row)
cursor.close()
conn.close()
