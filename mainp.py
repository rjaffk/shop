import mysql.connector
from mysql.connector import errorcode
import LogWindow

def create_database():
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        cursor.execute("USE {}".format(db_name))
        cursor.execute("""CREATE TABLE IF NOT EXISTS `users` (id INT(2) AUTO_INCREMENT,
            name VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(20) NOT NULL,
                role TINYINT NOT NULL, PRIMARY KEY(id))""")
        cursor.execute("""INSERT INTO users (name, password,role)
            values('Ivan', '1234',1), ('Anna', 'qwert', 2), ('Jane', '123qwe',2)""")
        con.commit()
        LogWindow.logwin()


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            LogWindow.logwin()
        else:
            print("Failed creating database: {}".format(err))

try:
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
    cursor = con.cursor()
    db_name = 'admin_b'
    create_database()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)

else:
    cursor.close()
    con.close()
