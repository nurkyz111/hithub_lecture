#OOP

class Dog:
#аттрибуты класса
    amount_of_legs = 4
    amount_of_tails = 1
    def __init__(self, name, vozrast,color):
        self.name = name
        self.age = vozrast
        self.color = color

    def bark(self):
        print("Woof")

    def eat(self, food):
          if food == 'bones':
           print('Mmm delicious!')
        else:
           print('I dont want it')

    def birthday(self):
          print("Today is my birthday")
    self.age += 1

    def get_dog_info(self):
        print(f'Woof! My name is {self.name},'
              f'I am {self.age}years old and i am {self.color}')

    def be_friend(self, friend):
        self.friend = friend
        friend.friend = self


экземпляры класса
eva = Dog('Eva', 5, 'black')
print(eva.name, eva.age, eva.color)
rex = Dog('Rex', 4,'white')
print(rex.name, rex.age, rex.color)

print(eva.amount_of_legs, rex.amount_of_legs, eva.amount_of_tails, rex.amount_of_tails)

eva.eat('bones')
print(eva.age)

eva.birthday()
print(eva.age)
get_dog_info()



class Car:
    amount_of_heels = 4
    amount_of_wipers = 2
    amount_of_pedal = 1

    def __init__(self, model, price, year, mileage, color, volume, oil):
        self.model = model
        self.price = price
        self.year = year
        self.mileage = mileage
        self.color = color
        self.volume = volume
        self.oil = oil

    def get_car_info(self):
        print(f'Model-{self.model}')
        print(f'Price-{self.price}')
        print(f'Year-{self.year}')
        print(f'Mileage-{self.mileage}')
        print(f'Color-{self.color}')
        print(f'Volume-{self.volume}')
        print(f'Oil-{self.oil}')

    def horn(self):
        print("Beep")

    def drive(self):
        try:
            if self.oil < 20:
                raise Exception
            self.mileage += 100
            self.price -= 100
            self.oil -= 20
        except Exception:
            print("Cannot drive anymore")

bmw = Car('BMW', '$7000', '2020', '20000', 'green', '2.3', '40')
print(bmw.model, bmw.price, bmw.year, bmw.mileage, bmw.color, bmw.volume, bmw.oil)

print(bmw.amount_of_heels, bmw.amount_of_wipers, bmw.amount_of_pedal)
get_car_info()
print('Было', bmw.mileage, bmw.price, bmw.oil)
bmw.drive()
print('Стало', bmw.mileage, bmw.price, bmw.oil)
bmw.drive()
print('Стало', bmw.mileage, bmw.price, bmw.oil)
bmw.drive()





class Student:
    teacher = 'Nurkyz'


    def __init__(self, name):
        self.name = name
        self.test_score = []

    def add_grade(self, grade):
        self.test_score.append(grade)

student_1 = Student('Azim')
student_2 = Student('Syimyk')

student_1.add_grade(90)
print(student_1.test_score)
student_1.add_grade(100)
print(student_1.test_score)
student_2.add_grade(110)

print( 'eto Syimyk', student_2.test_score)



class House:
    sewerage = True
    gas = False
    electricity = True
    furniture = 'Table'

    def __init__(self, area, price, address, year):
        self.area = area
        self.price = price
        self.address = address
        self.year = year


    def get_house_info(self):
        print(f'Area-{self.area}')
        print(f'Price-{self.price}')
        print(f'Address-{self.address}')
        print(f'Year-{self.year}')







house = House('100', '45000$', 'Djal', '2019')
print(house.area, house.price, house.address, house.year)
house.get_house_info()


from datetime import datetime
 class User:

    def __init__(self, username, firstname, secondname,phonenumber, email, date_joined):
        self.Username = username
        self.firstname = firstname
        self.secondname = secondname
        self.phonenumber = phonenumber
        self.email = email
        self.date_joined = datetime.now()
          self.followers = []
          self.following = []
#
        def __str__

    def get_user_info(self):
        print(f'Username - {self.username}\n'
              f'First name - {self.first-name}\n'
              f'Second name{self.second_name}')

    def follow(self,user):
        self.

user_1 = User('username-1', 'Nurkyz', 'Bektashova', '+996708824055', 'bektawovanurkyz@gmail.com')
user_2 = User('username -2', 'Alihan', 'Alimov', '+996702347687', 'alimovalihan.mail.ru')
user_3 = User('username-3', 'Nur', 'Bektashova', '+996708824055', 'bektawovanurkyz@gmail.com')



class Student:
    def __init__(self, name, surnname, age, phone, languages):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.languages = languages
        self.prog_languages = []
    def learn_prog_languages(self, language):
        self.prog_languages.append(language)
        if "Python" in self.prog_languages and "JavaScript" in self.prog_languages:
            print("I am full stack developer")
        elif "Python" in self.prog_languages:
            print("I am backend developer")
        elif "JavaScript" in self.prog_languages:
            print("I am frontend developer")




nurkyz = Student('Nurkyz', 'bektashova', '26', '0708824055', ['russian,english'])
adilet = Student('Adilet', 'Adiletov', '23', '+996700700700', ['kyrgyz', 'russian'])

nurkyz.learn_prog_language('Python')
nurkyz.learn_prog_language('JavaScript')




