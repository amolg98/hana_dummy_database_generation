import uuid
import time
import pyhdb
from random import uniform
from random import randint
from Cursor import Cur
from Connection import Conn
from userData import UserData
from pictures import Pictures
import datetime
import Constants


class GenerateDummyData(object):

    def __init__(self, cursor, conn, user_data, pictures_data):
        self.conn = conn
        self.cur = cursor
        self.user_data = user_data
        self.pictures_data = pictures_data

        self.pictures = pictures_data.pictures
        self.first_names = user_data.first_names
        self.last_names = user_data.last_names
        self.countries = user_data.countries
        self.cities = user_data.cities
        self.phone_number = set()
        self.user_id = []

    @staticmethod
    def generate_user_table(self):
        pass

    def write_data(self, sql, parameters=None):
        try:
            if parameters is None:
                self.cur.cursor.execute(sql)
            else:
                self.cur.cursor.execute(sql, parameters)

        except Exception as err:
            print("Error in write data is {0}".format(err))

    def get_data(self, sql):
        """

        :param sql:
        :return:
        """
        try:
            # Execute a SQL string
            # e.g. sql = "SELECT * from CUSTOMERS"
            print("sql in get data is {0}".format(sql))
            self.cur.cursor.execute(sql)

            # Fetch all results from the cursor into a sequence,
            # display the values as column name = value pairs,
            # and then close the connection
            row_set = self.cur.cursor.fetchall()
            print("row_set length is {0}".format(len(row_set)))
            return row_set

        except Exception as err:
            print("Error in get data is {0}".format(err))

    def delete_record(self, sql):
        """

        :param sql:
        :return:
        """
        try:
            # Execute a SQL string
            # sql = "delete from {0} where {1}".format(table, condition)
            self.cur.cursor.execute(sql)
            a = self.cur.cursor.fetchone()
            print("a is {0}".format(a))

        except Exception as err:
            print("Error in delete is {0}".format(err))

    def create_table(self, table, values):
        """

        :type values: object
        :param table:
        :return:
        """
        try:
            if not isinstance(values, list):
                # Raise a custom exception
                raise
            v = ""
            for i in range(0, len(values)-1):
                if not isinstance(values[i], dict):
                    raise
                v = v + " {0} {1}({2}) {3}, ".format(
                    values[i]['col_name'],
                    values[i]['type'],
                    values[i]['size'],
                    values[i]['special']
                )

            v = v + "{0} ({1})".format(
                values[len(values)-1]['special condition'],
                values[len(values)-1]['col_name'])

            sql = "CREATE TABLE {0} (  {1} )".format(table, v)
            print("sql statement is {0}".format(sql))

            # sql = "CREATE TABLE AGENTS " \
            #    "(AGENT_CODE varchar(6) NOT NULL," \
            #    "AGENT_NAME varchar(40) DEFAULT NULL, " \
            #    "WORKING_AREA varchar(35) DEFAULT NULL,"\
            #    "COMMISSION decimal(10,2) DEFAULT NULL,"\
            #    "PHONE_NO varchar(15) DEFAULT NULL,"\
            #    "COUNTRY varchar(25) DEFAULT NULL, " \
            #    "PRIMARY KEY (AGENT_CODE))"

            self.cur.cursor.execute()

        except Exception as err:
            print("Error in create table is {0}".format(err))

    def get_table_data(self, table, print_flag):
        try:
            sql = "SELECT * from {0}".format(table)

            print("sql is {0}".format(sql))

            row_set = self.get_data(sql)
            if print_flag:
                for row in row_set:
                    for col in range(len(row)):
                        print("{0} : {1}".format(row_set[0][col], row[col]))
                    print("")

            return row_set

        except Exception as err:
            print("Error in get table data is {0}".format(err))

    def write_customers_data(self, user_data):
        """
        Write data to table "CUSTOMERS"
        :return:
        """
        try:
            user_id = uuid.uuid1()
            first_name = (self.first_names[randint(0, len(self.first_names) - 1) % len(self.first_names)]).rstrip()
            last_name = (self.last_names[randint(0, len(self.last_names) - 1) % len(self.last_names)]).rstrip()
            phone_num = user_data.gen_phone_number()
            sql = "INSERT INTO {0} VALUES (\'{1}\', \'{2}\',\'{3}\',\'{4}\')".format(
                "CUSTOMERS",
                user_id,
                first_name,
                last_name,
                phone_num
            )
            self.write_data(sql)

            # print("Data written to Customers table")

        except Exception as err:
            print("Error in write customer data is {0}".format(err))

    def get_customers_data(self, print_flag):
        try:
            return self.get_table_data("CUSTOMERS", print_flag)

        except Exception as err:
            print("Error in get customer data is {0}".format(err))

    def write_workers_data(self, user_data):
        """
        Write data to table "AGENTS"
        :return:
        """
        try:
            worker_id = uuid.uuid1()
            worker_first_name = (self.first_names[randint(0, len(self.first_names) - 1) % len(self.first_names)]).rstrip()
            worker_last_name = (self.last_names[randint(0, len(self.last_names) - 1) % len(self.last_names)]).rstrip()
            worker_name = "{0} {1}".format(worker_first_name, worker_last_name)
            working_area = (self.cities[randint(0, len(self.cities)-1) % len(self.cities)]).rstrip()
            commission = round((uniform(2.5, 10)) * (randint(0, 100)), 2)
            phone_num = user_data.gen_phone_number()
            country = (self.countries[randint(0, len(self.countries)-1) % len(self.countries)]).rstrip()

            sql = "INSERT INTO {0} VALUES (\'{1}\', \'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\')".format(
                "WORKERS",
                worker_id,
                worker_name,
                working_area,
                commission,
                phone_num,
                country
            )
            self.write_data(sql)
            # print("Data written to Workers table")

        except Exception as err:
            print("Error in write worker data is {0}".format(err))

    def get_workers_data(self, print_flag):
        try:
            return self.get_table_data("WORKERS", print_flag)

        except Exception as err:
            print("Error in get worker data is {0}".format(err))

    def write_orders_data(self, cust_id, worker_id):
        """
        Write data to table "ORDERS"
        :return:
        """
        try:

            order_id = uuid.uuid1()
            order_amount = round((uniform(5, 10))*(randint(0, 100)), 2)
            advance_amount = round((uniform(2.5, 5))*(randint(0, 100)), 2)
            order_date = ""
            cust_id = cust_id
            worker_id = worker_id
            order_desc = Constants.order_desc

            sql = "INSERT INTO {0} VALUES (\'{1}\', \'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\')".format(
                "ORDERS",
                order_id,
                order_amount,
                advance_amount,
                order_date,
                cust_id,
                worker_id,
                order_desc
            )
            self.write_data(sql)
            # print("Data written to Workers table")

        except Exception as err:
            print("Error in write customer data is {0}".format(err))

    def get_orders_data(self, print_flag):
        try:
            return self.get_table_data("ORDERS", print_flag)

        except Exception as err:
            print("Error in get order data is {0}".format(err))

    def create_dataset(self, customers_set, workers_set):
        try:
            # Write to orders tables using customers and workers table
            count = 0
            for w in workers_set:
                for c in customers_set:
                    # print("customer id - {0}, worker id - {1}".format(c[0], w[0]))
                    self.write_orders_data(c[0], w[0])
                    count += 1
                    if count == 10000:
                        count = 0
                        self.conn.commit_connection()

        except Exception as err:
            print("Error in create dataset is {0}".format(err))

    def set_pictures_data(self):
        try:
            pic_id = uuid.uuid1()
            pic_details = self.pictures[randint(0, len(self.pictures)-1)]

            insert_blob_tuple = (pic_id, pic_details)

            sql = """INSERT INTO PICTURES (PIC_ID, PIC_DETAILS) VALUES (?, ?)"""

            # self.cur.cursor.execute(sql, insert_blob_tuple)
            self.write_data(sql, insert_blob_tuple)

        except pyhdb.connection.Error as err:
            print("Error in set_pictures_data is {0}".format(err))

        except Exception as err:
            print("Error in set_pictures_data is {0}".format(err))


def main():
    start_time = time.time()
    user_data = UserData()
    pictures_data = Pictures()
    conn = Conn("localhost", 30015, "SYSTEM", "Frsd1234!")
    cursor = Cur(conn)
    m = GenerateDummyData(cursor=cursor, conn=conn, user_data=user_data, pictures_data=pictures_data)

    try:
        '''for i in range(0, 20000):
            m.write_customers_data(user_data)
        conn.commit_connection()

        print("Customer data written!!")
        # m.delete_record()

        for i in range(0, 4000):
            m.write_workers_data(user_data)
        conn.commit_connection()

        print("Worker data written!!")'''

        cust_row_set = m.get_customers_data(0)
        worker_row_set = m.get_workers_data(0)

        # m.create_dataset(cust_row_set, worker_row_set)
        # m.get_orders_data(0)

        time_start = datetime.datetime.now()
        t1 = time_start
        for i in range(0, 4000):
            if (i % 1000) == 0:
                conn.commit_connection()
                t2 = datetime.datetime.now()
                print("Time taken to commit 1000 records is {}".format(t2 - t1))
                t1 = t2
                print("1000 written")
            m.set_pictures_data()
        conn.commit_connection()

        time_end = datetime.datetime.now()
        print("Time taken to commit 1000 records is {}".format(time_end - time_start))

        # m.set_pictures_data()
        print("Data written to Pictures table")

        conn.commit_connection()
        return

    except Exception as err:
        print("Error is {0}".format(err))

    finally:
        cursor.close_cursor()
        conn.commit_connection()
        conn.close_connection()
        print(" --- {0} seconds --- ".format(time.time() - start_time))


if __name__ == '__main__':
    main()
