import sqlite3

class loginDB():

    def __init__(self):
        #Initialize db class variables
        self.connection = sqlite3.connect('LoginCredentials.db')
        self.cur = self.connection.cursor()


    def ___del___(self):
        #close sqlite3 connection
        self.connection.close()

    def addUser(self, newUserName, newPassword):
        with self.connection:
            self.cur.execute(" INSERT INTO LoginInfo VALUES (:username, :password)", {'username': newUserName, 'password': newPassword})
            self.connection.commit()

    def CheckDBCred(self, userID, passCode):
        self.cur.execute("SELECT * FROM LoginInfo WHERE username=:username AND password=:password", {'username': userID, 'password':passCode})
        return self.cur.fetchall()

    def DeleteUser(self, userID, passCode):
        with self.connection:
            self.cur.execute("DELETE from LoginInfo WHERE username=:username AND password=:password", {'username': userID, 'password':passCode})
            self.connection.commit()

    def commit(self):
        #commit changes to database
        self.connection.commit()



# conn = sqlite3.connect('LoginCredentials.db')

# cursor = conn.cursor()

## create a table now

# cursor.execute("""CREATE TABLE LoginInfo (
#     username text,
#     password text
# )""")

##ADD data to table
# cursor.execute(" INSERT INTO LoginInfo VALUES ('hamzam', '9035712357')")
# cursor.execute(" INSERT INTO LoginInfo VALUES ('freddiev', '4692267036')")
# conn.commit()
##run query
# cursor.execute("SELECT * FROM LoginInfo WHERE username='hamzam'")

##three ways to cycle through query
## 1. fetchone()  --- gets the first occurance
## 2. fetchmany(*int*) --- gets that many occurances
## 3. fetchall() --- gets all the occurancs

# print(cursor.fetchone()[1])

# conn.commit() ## commits the current changes


# conn.close() ##good to close connection at end
