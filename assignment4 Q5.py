#creating a employee class

class Employee:

    def __init__(self,n,s):
        self.name=n
        self.salary=s

    #printing the details of the employees

    def print_details(self):
        print(self.__dict__)

#creating objects of the class

e1=Employee('Mehak',40000)
e2=Employee('Ashok',50000)
e3=Employee('viren',60000)

#updating the salary of mehak

e1.salary=70000

#printing details of employee e1

e1.print_details()

#deleting the record of employee named viren

del e3

#code ends here