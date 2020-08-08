import os
from random import randint


class UserData:

    def __init__(self):
        """
        Create base data structures and execute read functions to populate those data structures

        """
        self.first_names = []
        self.last_names = []
        self.countries = []
        self.cities = []
        self.phone_number = set()

        # Read all the data into data structures
        self.read_first_names()
        self.read_last_names()
        self.read_countries()
        self.read_cities()

    def read_first_names(self):
        try:
            f = open("files/first_names.txt", "r")
            for x in f.readlines():
                self.first_names.append(x)
            f.close()

        except FileNotFoundError as error:
            print("Not able to open file {0}".format(error))

        # print(self.first_names)

    def read_last_names(self):
        try:
            f = open("files/last_names.txt", "r")
            for x in f.readlines():
                self.last_names.append(x)
            f.close()

        except FileNotFoundError as error:
            print("Not able to open file {0}".format(error))

        # print(self.last_names)

    def read_countries(self):
        try:
            f = open("files/countries.txt", "r")
            for x in f.readlines():
                self.countries.append(x)
            f.close()

        except FileNotFoundError as error:
            print("Not able to open file {0}".format(error))

        # print(self.countries)

    def read_cities(self):
        try:
            f = open("files/cities.txt", "r")
            for x in f.readlines():
                self.cities.append(x)
            f.close()

        except FileNotFoundError as error:
            print("Not able to open file {0}".format(error))

        # print(self.cities)

    def gen_phone_number(self):
        range_start = 10 ** (10 - 1)
        range_end = (10 ** 10) - 1
        flag = True
        ph_number = 0
        while flag:
            ph_number = randint(range_start, range_end)
            # print("phone number is {0}".format(ph_number))
            if ph_number not in self.phone_number:
                self.phone_number.add(ph_number)
                flag = False
        return ph_number
