# from django.test import TestCase

# Create your tests here.


# class product:
#     pass

# p1 = product()
# p1.name = "induleka"
# p1.price = 30
# print(p1.price)

# class product:
#     place = 'infopark'
#     def __init__(athif, place):
#         athif.place = place
#         # print(athif.place)

# p2 = product(product.place)
# print(p2.place)
# p2.place = 'calicut'

# class sps:
#     year = 2021
    
#     def __init__(self, name, age, place):
#         self.name = name
#         self.age = age
#         self.place = place

#     def age_incriment(self):
#         self.age += 1

#     def relocate(self, place):
#         self.place = place

#     def display(self):
#         print("Year: " + str(sps.year))
#         print("name: " + self.name) 
#         print("age: " + str(self.age)) 
#         print("place: " + self.place)
#         print('------------------------')

#     @classmethod
#     def add_year(cls):
#         cls.year = cls.year + 1
#         cls.age_incriment(90)

#     @staticmethod
#     def display_welcome(one):
#         one = one + 10
#         print("=======Welcome=======" + str(one))

    

    

# sps.display_welcome(100)

# abdu = sps('abdulla', 20, 'kannur')
# semeeh = sps('semeeh', 10, 'kottakal')

# abdu.display()
# semeeh.display()

# sps.year = sps.year + 1
# abdu.age_incriment()
# semeeh.age_incriment()
# semeeh.relocate('london')

# sps.add_year()

# abdu.display()
# semeeh.display()

# class Base():
#     def __init__(self):
#         print("base init")

#     def display(self, athif):
#         print("Base Display", + athif)

# class Sub(Base):
#     def __init__(self):
#         print("Sub init")

#     def display(self):
#         print("sub Display")

# x = Sub()
# x.display()