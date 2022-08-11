
# '''Create a class called “Group_leader” that inherits from the class “Students” that 
# we created in the practical session today. (Initialize the class and let it&nbsp; 
# take an argument of the list of students under the group leader. Let the 
# parent class take care of the other arguments'''


class Students:
    def __init__(self, first_name,last_name,email):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email


class Group_leader(Students):
    students_list = []

    def __init__(self, first_name,last_name,email, list1 = None): 
        super().__init__(first_name,last_name,email)

        if list1 is not None:
                self.students_list = list1

## Define a method that adds students to the list of student under the group leader
    def add_students(self, students):
        for student in students:
            self.students_list.append(student)
        

    def add_student(self, student):
        self.students_list.append(student)


## Define a method that removes students from the list of students under the group leader
    def remove_student(self, student_name):
        for student in self.students_list:
            self.students_list.remove(student)

    def remove_students(self, students):
        for student in students:
                self.students_list.remove(student)



## Define a method that prints out the full names of students in the list of students under group leader



## Create 3 more instances of the parent class we defined in the practical session
Student1 = Students('bukola','ajayi','bukolam.ajayi@gmail.com')
Student2 = Students('Israel','Ayomide','Israelayomide@gmail.com')
Student3 = Students('kike','jola','kikejola@gmail.com')


## Create 2 instances of the sub class you created
leader1 = Group_leader('ore','ojo', 'oreojo@gmail,com', ['shola'])
leader2 = Group_leader('bola','rayols', 'bolarayola@gmail,com', ['shola','samson'])



##Add 2 students each to the list of students under the instances of your subclass.
students = ['tola','shade']
leader1.add_students(students)

print(leader1.students_list)














  







