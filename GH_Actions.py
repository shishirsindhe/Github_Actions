print("Something")



class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def Total_CTC(self):
        total_ctc=0
        total_ctc+=self.salary*12
        return total_ctc

e1=Employee("Bill",26,1000)
e2=Employee("steve",28,4000)
print(e1.salary)
print(e1.Total_CTC())
print(e2.salary)
print(e2.Total_CTC())
