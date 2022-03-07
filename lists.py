# creating variables
student1 = "Drew"
student2 = "Noelia"
# creating a list
students_111 = ["Drew", "Brandon", "Dusan", "Brandan"]
students_490 = ["Seth", "Jordan", "Joyce"]
# looping through a list
# for i in student_list:
#     print(i)


# for i in range(len(students_111)):
#     print(students_111[i])

birch_students = [students_111, students_490]
# print(birch_students)

for l in birch_students:
    for s in l:
        print(s)

# dictionaries vs lists
# create a dictionary
student = {
    "first_name": "Jenny",
    "id_number": 417481844,
    "email": "fddfsaf@byui.edu",
    "grade": 95
}
student2 = {
    "first_name": "Jonny",
    "id_number": 55115,
    "email": "asdf@byui.edu",
    "grade": 60,
    "images": ["img1.png", "img2.png"]
}
awesome_students = [student, student2]

student_name = input("please enter the student's name to see their grade: ")

for student in awesome_students:
    if student['first_name'] == student_name:
        print(f"{student['first_name']}'s grade is {student['grade']}%")

random_picker_item = {
    "title": "Teams class 2-14",
    "data": ['Landon', 'Andre', 'Drew', 'Noelia', 'Brendan', 'Jared', 'Jacob'] 
}
random_items = {
    "title": "awesome colors",
    "data": []
}

all_lists = [random_picker_item, random_items]
# print(all_lists)

comma_separated_string = input("please enter a list of stuff separated by commas: ")
string_without_spaces = comma_separated_string.replace(" ", "")
user_list = string_without_spaces.split(',')
print(string_without_spaces)
print(comma_separated_string)
print(user_list)
for user in user_list:
    print(user)
print(user_list[1])

def get_item_in_list(list, value):
    for i in list:
        if i['name'] == value:
            return i['price']

ice_creams = [{'name': 'Vanilla', 'price': 4.99}, 
{'name': 'Strawberry'}, 
{'name': 'Chocolate'}]
print(get_item_in_list(ice_creams, 'Vanilla'))


favorite_numbers = [234,5236,3,8,45,3456,124,4,6,62,2432,-2356]

print(favorite_numbers)
print(favorite_numbers[::2])

first_name = "Nathan"
print(first_name[2:])