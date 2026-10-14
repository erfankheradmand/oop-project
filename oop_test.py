# class Person:
#     def __init__(self, name, family):
#         self.name = name
#         self.family = family
#
#     def save (self):
#         print(f"person name is {self.name} family is {self.family}")
#     @staticmethod
#     def sample():
#         print('sample')
#
# person1 = Person('erfan', 'kherad')
# person1.save()
#
# person2 = Person('ali', 'fdsds')
# person2.save()
# person1.sample()
# person2.sample()
# Person.sample()

# class Person:
#      def __init__(self, name, family , salary):
#          self.name = name
#          self.family = family
#          self.salary = salary
#
#      def get_name(self):
#          return self.__name
#
#      def set_name(self, new_name):
#          if not isinstance(new_name, str):
#              raise TypeError('new name must be a string')
#          self.__name = new_name
#      def get_salary(self):
#          return self.__salary * 0.9
#      def set_salary(self, new_salary):
#          if not isinstance(new_salary, int ):
#              raise TypeError('new salary must be a float')
#          self.__salary = new_salary
#
#      name = property(get_name, set_name)
#      salary = property(get_salary, set_salary)
# person1 = Person('John', 'Frank' , 1000)
# person1.set_name("mary")
# print(person1.get_name())
# print(person1.get_salary())
# person1.set_salary(2000)
# print(person1.get_salary())


