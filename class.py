class Phone:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

samsung_1 = Phone("Z-Fold", "Fold-6" ,"Grey")
samsung_2 = Phone("Galaxy","s21", "Silver")
samsung_3 = Phone("Galaxy","S22","Gold")
iphone = Phone("iphone", "16-Pro-max", "Gold")
print(f"The brand name is {samsung_1.brand},The model name is {samsung_1.model},The color name is {samsung_1.color}")
print(f"The brand name is {samsung_2.brand},The model name is {samsung_2.model},The color name is {samsung_2.color}")
print(f"The brand name is {samsung_3.brand},The model name is {samsung_3.model},The color name is {samsung_3.color}")
print(f"The brand name is {iphone.brand},The model is {iphone.model},The color name is {iphone.color}")



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
      print(f"Hello my name is {self.name},and i am {self.age}years old")
    def lifestyle(self):
      print(f"{self.name} goes to the gym alot and is living healthy")
p1 =Person("Zara", "15")
print("Function call")
p1.intro()
p1.lifestyle()


class Child(Person):
    def __init__(self,name, age):
      Person. __init__(self,name,age)
      super(). __init__(name, age)
      self.gradyear = 2020
      self.fav_color =color
    def convocation(self):
        print(f"Welcome everyone to{self.name}'s {self.gradyear} Convocation amd her favorite color is {self.fav.color}")
       


x =Child("Amina", "12")
x.intro()
print(x.gradyear,x.favcolor)




