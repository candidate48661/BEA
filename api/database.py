import sqlite3


class Database:
    name = ""

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, type TEXT, number TEXT, name TEXT,"+
            " first_name TEXT, address TEXT, birthdate TEXT, latitude FLOAT, longitude FLOAT)")
        self.connection.commit()
        self.connection.close()
        self.name=db;

    def get_max_id(self):
        self.connection = sqlite3.connect(self.name)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM accounts ORDER BY id DESC LIMIT 1")
        rows = self.cursor.fetchall()
        self.connection.close()
        if len(rows) == 0:
            return 0
        return int(rows[0]["id"])

    def post(self, account_type, number, name, first_name, address, birthdate, latitude, longitude):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO accounts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (account_type, number, name,
                                                                                           first_name, address,
                                                                                           birthdate, latitude,
                                                                                           longitude))
        self.connection.commit()
        self.connection.close()

    def view(self):
        self.connection = sqlite3.connect(self.name)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM accounts")
        rows = self.cursor.fetchall()
        self.connection.close()
        return rows

    def get(self, id):
        self.connection = sqlite3.connect(self.name)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM accounts  WHERE id=?", (id,))
        result = self.cursor.fetchall()
        self.connection.close()
        if len(result) == 0:
            return ""
        return result[0]

    def delete(self, id):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM accounts WHERE id=?", (id,))
        self.connection.commit()
        self.connection.close()

    def put(self, id, account_type, number, name, first_name, address, birthdate, latitude, longitude):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("UPDATE accounts SET type=?, number=?, number=?, first_name=?, address=?, birthdate=?,"+
                            " latitude=?, latitude=? WHERE id=?",
                            (account_type, number, name, first_name, address, birthdate, latitude, longitude, id))
        self.connection.commit()
        self.connection.close()

    def init_dummy_db(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO accounts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", ("Credit",
                                                                                           "BE 1234 5678 9876 5432",
                                                                                           "John",
                                                                                           "Smith",
                                                                                           "Limelette",
                                                                                           "12/02/1968",
                                                                                           None,
                                                                                           None))
        self.cursor.execute("INSERT INTO accounts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", ("Credit",
                                                                                           "BE 5844 3021 3235 9473",
                                                                                           "Mike",
                                                                                           "Wood",
                                                                                           "Genval",
                                                                                           "16/04/1977",
                                                                                           None,
                                                                                           None))
        self.cursor.execute("INSERT INTO accounts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", ("Credit",
                                                                                           "BE 1456 9826 1074 0275",
                                                                                           "Sam",
                                                                                           "Simpson",
                                                                                           "Leuven",
                                                                                           "28/06/1991",
                                                                                           None,
                                                                                           None))
        self.connection.commit()
        self.connection.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

