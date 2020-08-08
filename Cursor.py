from pyhdb.cursor import Cursor


class Cur(object):

    def __init__(self, connection):
        self.conn = connection.get_connection()
        self.cursor = connection.get_cursor()

    def get_cursor(self):
        try:
            return self.cursor

        except Cursor as err:
            print("Error in get cursor is {0}".format(err))

    def close_cursor(self):
        try:
            self.cursor.close()

        except Cursor as err:
            print("Error in close cursor is {0}".format(err))

