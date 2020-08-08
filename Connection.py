import pyhdb
from pyhdb import Connection


class Conn:

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = pyhdb.connect(self.host, self.port, self.user, self.password)

    def get_connection(self):
        try:
            return self.conn

        except Connection as err:
            print("Error in get connection is {0}".format(err))

    def get_cursor(self):
        try:
            return self.conn.cursor()

        except Connection as err:
            print("Error in get cursor is {0}".format(err))

    def commit_connection(self):
        try:
            self.conn.commit()

        except Connection as err:
            print("Error in commit connection is {0}".format(err))

    def close_connection(self):
        try:
            self.conn.close()

        except Connection as err:
            print("Error in close connection is {0}".format(err))

