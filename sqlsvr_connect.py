server = 'cl-lsg-sqlsvr.database.windows.net'
database = 'master'
username = 'lsg-admin'
password = 'L0gicSurface'

# failed to connect because python is 32bit and odbc drive 64bit on Windows 64 bit.
def connect_via_odbc():
    import pyodbc
    driver= '{ODBC Driver 13 for SQL Server}'
    #cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cnxn =pyodbc.connect('Data Source=(localdb)\ProjectsV13;Initial Catalog=HenryRes;Integrated Security=True')
    cursor = cnxn.cursor()
    cursor.execute("SELECT count(*) FROM dbo.Well_Location")
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()


def connect_via_pymssql():
    import pymssql
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    #conn = pymssql.connect(server='gis-db-03.vss.lcl', user='sde', password='logicadmin', database='MuneerTest')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM dbo.Well_Location')
    row = cursor.fetchone()
    while row:
        print str(row[0]) + " " + str(row[1]) + " " + str(row[2])
        row = cursor.fetchone()


if __name__ == '__main__':
    # connect_via_odbc()
    connect_via_pymssql()

