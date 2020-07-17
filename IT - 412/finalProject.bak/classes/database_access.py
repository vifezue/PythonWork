import pymysql


class DB_Connect():
    """A simple class for connecting to a database and performing queries"""

    def __init__(self, passed_db_username, passed_db_password, passed_database):
        """Initialize name and age variables/attributes"""
        self.passed_db_username = passed_db_username
        self.passed_db_password = passed_db_password
        self.passed_database = passed_database
        self.conn = None

    def __connect(self):
        """Creates connections to the database when they are needed"""
        self.conn = pymysql.connect(host='localhost',
                                    user=self.passed_db_username,
                                    password=self.passed_db_password,
                                    db=self.passed_database,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)

    def executeQuery(self, passed_query):
        """Executes a database query for Inserts, Updates, and Deletes"""
        try:

            if not self.conn:
                self.__connect()

            with self.conn.cursor() as cursor:
                self.conn
                cursor.execute(passed_query)

        except:
            self.conn.close()

    def executeSelectQuery(self, passed_query):
        """Executes a SELECT database query and returns the results as a tuple-like structure"""
        try:

            if not self.conn:
                self.__connect()

            with self.conn.cursor() as cursor:
                cursor.execute(passed_query)

            return cursor.fetchall()

        except:
            self.conn.close()
