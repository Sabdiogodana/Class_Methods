class Student:
      school = "Akirachix"
      def __init__(self,first_name,last_name,age,country): 
                 self.first_name = first_name
                 self.last_name = last_name
                 self.age = age
                 self.country = country
     

      def greet(self):
          return f"Hello {self.name} welcome to {self.school} How is {self.country}"

      def full_name(self):
          return f"Hello {self.first_name} {self.last_name} is your full name"

      def  initials(self):
          return f" Your initials are {self.first_name[0]} {self.last_name[0]}" 

      def year_of_birth(self,):
          year = 2022 - self.age
          return f"Your were born {self.year}"

      

                


