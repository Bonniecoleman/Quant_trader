import pymysql

con = pymysql.connect(
    user = 'root',
    passwd = 'Rlaqjatjd1!',
    host = '127.0.0.1',
    db = 'shop',
    charset = 'utf8'
)

mycursor = con.cursor()

query = """
select * from products;
"""

mycursor.execute(query)
data = mycursor.fetchall()
con.close()

for row in data:
    print(row)
