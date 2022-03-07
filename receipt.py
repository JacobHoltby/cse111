import csv
from tkinter import N

def main():
    # Index of the phone number column
    # in the dentists.csv file.
    PRODUCT_NUMBER = 0
    NAME = 1
    PRICE = 2
    QUANTITY = 1

    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    products_dict = read_dict("products.csv", PRODUCT_NUMBER)

    # Print the dentists compound dictionary.
    print('All Products')
    print(products_dict)
    print()

    print('Requested Items')

    with open("request.csv", "rt") as request_file:
        request_reader = csv.reader(request_file)
        next(request_reader)

        for row in request_reader:
            product_number = row[PRODUCT_NUMBER]
            request_quantity = row[QUANTITY]

            name = products_dict[product_number][NAME]
            quantity = request_quantity
            price = products_dict[product_number][PRICE]

            #make sure quanitties add up maybe
            print(f'{name}: {quantity} @ {price}')


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()