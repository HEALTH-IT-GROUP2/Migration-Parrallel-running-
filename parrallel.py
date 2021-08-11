import mysql.connector
from variables import *

# import kenya

try:
    print("n")
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='afyaehms',
                                         user='root',
                                         password='')

    cursor = connection.cursor(buffered=True)
    print(connection)

    # cursor.execute(insert_to_patient)

    last_row = "SELECT * FROM afya.patient ORDER BY patient_id DESC LIMIT 1"
    connection.commit()
    cursor.execute(last_row)
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
    # connection.commit()

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

last_row = []
# DATABASE KENYAEMR
try:
    connection_afya = mysql.connector.connect(host='localhost', port='3306', database='afya', user='root', password='')
    print("n")
    connection2 = mysql.connector.connect(host='localhost',
                                          port='3306',
                                          database='kenya',
                                          user='root',
                                          password='')

    cursor1 = connection2.cursor(buffered=True)
    cursor_ = connection_afya.cursor(buffered=True)

    print(connection2)
    last = "SELECT * FROM afya.patient ORDER BY patient_id DESC LIMIT 1"
    connection_afya.commit()
    last = cursor_.execute(last)
    print(type(last))

    result = cursor_.fetchall()

    for x in result:
        print(type(x))
        last_row = x

    hey = cursor1.execute(real_migrate_patient, last_row)
    connection2.commit()
    print(hey)

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
