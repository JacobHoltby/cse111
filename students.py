import csv

def main():
    
    STUDENT_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict("students.csv", STUDENT_INDEX)
    
    

    flag = True

    while flag != False:
        inumber = input("Please enter an I-Number (xxxxxxxxx): ")

        inumber = inumber.replace("-", "")
        
        if not inumber.isdigit():
            print("Please enter a valid I-Number.")
        else:
            if len(inumber) < 9:
                print("Invalid I-Number: too few digits.")
            elif len(inumber) > 9:
                print("Invalid I-Number: too many digits")
            else:
                if inumber in student_dict:
                    value = student_dict[inumber]
                    name = value[NAME_INDEX]
                    print(name)
                    flag = False
                else:
                    print("No such student.")

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
    
    dict_student = {} 

    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dict_student[key] = row_list

    return dict_student 


if __name__ == "__main__":
    main()
    