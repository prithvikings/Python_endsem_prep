"""create a class name staff inside the class create two methods __init__ and show details(). in init method initialize role,
dept and of an employee and in show details print the details of the employee create another class teacher which is inherited from staff class.
inside teacher class create __init method initialize the variable name and age call the init of the staff class inside teacher class create an object of teacher class and print the values"""
class Staff:
    def __init__(self, role, dept,salary):
        self.role = role
        self.dept = dept
        self.salary =salary

    def show_details(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)


class Teacher(Staff):
    def __init__(self, name, age, role, dept):
        super().__init__(role, dept)
        self.name = name
        self.age = age

    def display_teacher_details(self):
        print("Teacher's Name:", self.name)
        print("Teacher's Age:", self.age)
        self.show_details()


# Creating an object of the Teacher class
teacher_obj = Teacher("John Doe", 35, "Math Teacher", "Mathematics")
teacher_obj.display_teacher_details()

 