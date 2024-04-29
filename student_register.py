'''
This program allows a user to register students for an exam venue.
'''

number_of_students = int(input("How many students are registering?"))

'''
This code adds the student id's to the register form to then be used
for the students to sign in.
'''
for i in range(number_of_students):
    student_id = input("What's the student id of this student?: ")
    with open('reg_form.txt', 'a') as file:
        file.write(f"{student_id} .......\n")


