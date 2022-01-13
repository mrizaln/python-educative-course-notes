class Salary:

    def __init__(self, base_pay=0, bonus=0):
        self.__base_pay = base_pay
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus
    
    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_base_pay(self):
        return self.__base_pay

    def set_base_pay(self, base_pay):
        self.__base_pay = base_pay

class Employee:
    
    def __init__(self, name='', base_pay=0, bonus=0):
        self.__name = name 
        self.__salary = Salary(base_pay, bonus)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary.get_base_pay() + self.__salary.get_bonus()

    def set_salary(self, base_pay, bonus):
        self.__salary.set_base_pay(base_pay)
        self.__salary.set_bonus(bonus)
    
    
maiuna = Employee("Maiuna", 1000, 100)
print(maiuna.get_salary())
maiuna.set_salary(1231,23)
print(maiuna.get_salary())