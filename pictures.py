import binascii
import os
import base64


class Pictures:

    def __init__(self):
        self.pictures = []
        self.read_pictures_data()

    def read_pictures_data(self):
        try:
            for x in os.listdir("pictures"):
                file_path = os.path.abspath("pictures/{0}".format(x))
                # print("file is {0}".format(x))
                # print("file is {0}".format(file_path))
                if os.path.isfile(file_path):
                    # f = open(file_path, mode="rb")
                    with open(file_path, 'rb') as f:
                        data = f.read()

                        """f_img = binascii.hexlify(data)
                        data_img = bytes.decode(f_img)"""

                    # binary_data = bytearray(data)
                    # str_data = base64.b64encode(data)

                    # print("type of character is {0}".format(binary_data[0]))
                    # print("character is {0}".format(binary_data[0]))
                    self.pictures.append(data)
                    f.close()

        except Exception as error:
            print("Not able to open file {0}".format("in pictures with some file "))

        # print(self.pictures)
