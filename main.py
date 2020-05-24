from abc import ABCMeta, abstractmethod

class Department:

    def __init__(self, name, code):
        self.name = name
        self.code = code
 
class Employee(metaclass=ABCMeta):

    __workhours = 8

    @abstractmethod
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    #criação do método get_department
    def get_department(self):
        return self.__department.name

    #criação do método set_department com alteração do nome
    def set_department(self, name):
        self.__department.name = name

    @abstractmethod
    def calc_bonus(self):
        pass

    #definição de carga horária de 8h para todos
    def get_hours(self):
        return self.__workhours

class Manager(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15

class Seller(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    #criação do método get_sales e retorno do valor
    def get_sales(self):    
        return self.__sales
    
    #criação do método put_sales e retorno do valor acumulado
    def put_sales(self, sales):     
        self.__sales += sales

    #cálculo do bonus sobre vendas
    def calc_bonus(self):
        return self.__sales * 0.15
