# my_age = 27
# my_name = "mohammad"
#
# print("Hello", my_name, "My Age is", my_age)
# print(f"hello {my_name} my age is {my_age}")
#
# name = input("What is your name?")
# print(name)
#
# num_1, num_2 = input("Enter 2 Numbers: ").split()
# num_1 = int(num_1)
# num_2 = int(num_2)
#
# sum_1 = num_1 + num_2
# minus = num_1 - num_2
# multiplie = num_1 * num_2
# quotient = num_1 / num_2
# remainder = num_1 % num_2
#
# print("{} + {} = {}".format(num_1, num_2, sum_1))
# print("{} - {} = {}".format(num_1, num_2, minus))
# print("{} * {} = {}".format(num_1, num_2, multiplie))
# print("{} / {} = {}".format(num_1, num_2, quotient))
# print("{} % {} = {}".format(num_1, num_2, remainder))

# drink = str(input("Pick Coke or Pepsi: "))
#
# if drink.__eq__("Coke"):
#     print("Coke")
# elif drink == "Pepsi":
#     print("Pepsi")
# else:
#     print("Water")
# print("Is 6 Even: ", ((6 % 2) == 0))

# your_float = float(input("Enter a float: "))
# print("Rounded to 2 decimals : {:.2f}".format(your_float))


# for i in range(5):
#     print("i= ", i)
# print("\n")
# for i in range(2, 5):
#     print("j= ", i)


# tree_height = int(input("How much tall is tree: "))
# spaces = tree_height - 1
# hashes = 1
# stump_spaces = tree_height - 1

# while tree_height != 0:
#     for i in range(spaces):
#         print(' ', end="")
#     for i in range(hashes):
#         print("#", end="")
#     print()
#     spaces -= 1
#     hashes += 2
#     tree_height -= 1
# for i in range(stump_spaces):
#     print(' ', end="")
# print("#")

# samp_string = "This is a very important string"
#
# print(samp_string[0])
# print(samp_string[-1])
# print(samp_string[0:4])
# print(samp_string[8:])
# print("Every Other: ", samp_string[0:-1:2])
# print("Reverse: ", samp_string[::-1])

# norm_string = input("Enter Message: ")
# secret_string = ""
# for char in norm_string:
#     secret_string += str(ord(char))
# print("Secret Message = ", secret_string)
# norm_string = ""
# for i in range(0, len(secret_string) - 1, 2):
#     norm_string += chr(int(secret_string[i] + secret_string[i + 1]))
# print(norm_string)

# rand_string = "         this is string     "
# # rand_string = rand_string.lstrip()
# # print(rand_string)
# # rand_string = rand_string.rstrip()
# # print(rand_string)
# rand_string = rand_string.strip()
# # print(rand_string)
# # rand_string = rand_string.capitalize()
# # print(rand_string)
# rand_string = rand_string.upper()
# print(rand_string)
# rand_string = rand_string.lower()
# print(rand_string)

# a_list = ["Dog", "Snack", "Fish"]
# print(", ".join(a_list))

# str_toabs = input("Enter string: ")
# org_str = str_toabs.upper()
# list_word = org_str.split()
# for i in list_word:
#     print(i[0], end="")
# print()

# def mult_divide(num_1, num_2):
#     return (num_1 * num_2), (num_1 / num_2)
# mult, divide = mult_divide(20, 5)
# print("mul =", mult)
# print("divide = ", divide)

# def sum_all(*args):
#     sum_num = 0
#     for num in args:
#         sum_num += num
#     return sum_num
# print("sum = ", sum_all(1, 2, 3, 4))

# even_list = [i*2 for i in range(11)]
# for i in even_list:
#     print(i, end=", ")
# print()
# import math
#
# num_list = [1, 2, 3, 4]
# lis_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in num_list]
# for k in lis_values:
#     print(k, end=", ")
# print()

# my_dic = {"f_name": "mm", "l_name": "mgb", "age": "27", "city": "isfahan"}
# print(my_dic.values())
# print(my_dic.keys())
# print("city is in list :", "city" in my_dic)
# print(my_dic["city"])
# for k, v in my_dic.items():
#     print(k, v)
# print(my_dic.get("address", "Not in list"))
# print(my_dic.get("city", "Not in list"))
# del my_dic["city"]
# my_dic.clear()

# import os
# with open("text.txt", mode="w", encoding="utf-8") as my_file:
#     my_file.write("random text\n more random text")
#
# with open("text.txt", encoding="utf-8") as my_file:
#     print(my_file.read())
# print(my_file.closed)
# print(my_file.name)
# print(my_file.mode)
# # os.rename("text.txt", "my_data.txt")
# # os.remove("my_data.txt")
# # os.mkdir("mydir")
# # os.chdir("mydir")
# # print("current dir :", os.getcwd())
# # os.chdir("..")
# # os.rmdir("mydir")
#
# with open("text.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print("Line :", line_num, " : ", line, end="")
#         line_num += 1


# class person:
#     def __init__(self, fullname="", age=0, height=0):
#         self.fullname = fullname
#         self.age = age
#         self.height = height
#     def getpersoninfo(self):
#         print(self.fullname, self.age, self.height)
#
# def main():
#     pers = person("mohammad mogh", 27, 170)
#     pers.getpersoninfo()
#
# main()

# class Square:
#     def __init__(self, height="0", width="0"):
#         self.height = height
#         self.width = width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if value.isdigit():
#             self.__height = value
#         else:
#             print("wrong height")
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if value.isdigit():
#             self.__width = value
#         else:
#             print("wrong width")
#
#     def get_area(self):
#         return int(self.__width) * int(self.__height)
#
# def main():
#     sq = Square()
#     height = input("height: ")
#     width = input("width: ")
#     sq.height = height
#     sq.width = width
#     print(sq.get_area())
#
# main()

# import random
# import math
#
#
# class Warrior:
#     def __init__(self, name="Warrior", health=0, attk_max=0, block_max=0):
#         self.name = name
#         self.health = health
#         self.attk_max = attk_max
#         self.block_max = block_max
#
#     def attack(self):
#         att_amt = self.attk_max * (random.random() + .5)
#         return att_amt
#
#     def block(self):
#         block_amt = self.block_max * (random.random() + .5)
#         return block_amt
#
#
# class Battle:
#     def start_fight(self, warrior1, warrior2):
#         while True:
#             if self.get_attack_result(warrior1, warrior2) == "Game Over":
#                 break
#             if self.get_attack_result(warrior2, warrior1) == "Game Over":
#                 break
#
#     def get_attack_result(self, warrior_a, warrior_b):
#         warrior_a_att_amt = warrior_a.attack()
#         warrior_b_block_amt = warrior_b.block()
#         damage_to_warrior_b = math.ceil(warrior_a_att_amt - warrior_b_block_amt)
#         warrior_b.health = warrior_b.health - damage_to_warrior_b
#         print("{} attack {} and deals {} damage".format(warrior_a.name, warrior_b.name, damage_to_warrior_b))
#         print("{} is down to {} health".format(warrior_b.name, warrior_b.health))
#
#         if warrior_b.health <= 0:
#             print("{} has died and {} is victorious".format(warrior_b.name, warrior_a.name))
#             return "Game Over"
#         else:
#             return "Next Round"
#
#
# def main():
#     thor = Warrior("Thor", 50, 20, 10)
#     loki = Warrior("Loki", 50, 20, 10)
#     battle = Battle()
#     # battle.get_attack_result2(thor, loki)
#     battle.start_fight(thor, loki)
#
#
# main()


# class Animal:
#     def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
#         self.__birth_type = birth_type
#         self.__appearance = appearance
#         self.__blooded = blooded
#
#     @property
#     def birth_type(self):
#         return self.__birth_type
#
#     @birth_type.setter
#     def birth_type(self, val):
#         self.__birth_type = val
#
#     @property
#     def appearance(self):
#         return self.__appearance
#
#     @appearance.setter
#     def appearance(self, val):
#         self.__appearance = val
#
#     @property
#     def blooded(self):
#         return self.__blooded
#
#     @blooded.setter
#     def blooded(self, val):
#         self.__blooded = val
#
#     def __str__(self):
#         return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birth_type, self.appearance, self.blooded)
#
#
# class Mammal(Animal):
#     def __init__(self, birth_type="born alive",
#                  appearance="hair or fur",
#                  blooded="warm blooded",
#                  nurse_young=True):
#         Animal.__init__(self, birth_type, appearance,blooded)
#         self.__nurse_young = nurse_young
#
#     @property
#     def nurse_young(self):
#         return self.__nurse_young
#
#     @nurse_young.setter
#     def nurse_young(self, val):
#         self.__nurse_young = val
#
#     def __str__(self):
#         return super().__str__() + " and it is {} they nurse their young".format(self.__nurse_young)
#
#
# class Reptile(Animal):
#     def __init__(self, birth_type="born in egg or born alive",
#                  appearance="dry scales",
#                  blooded="cold blooded"):
#         Animal.__init__(self, birth_type, appearance, blooded)
#
#
# def main():
#     animal1 = Animal("born alive")
#     print(animal1.birth_type)
#     print(animal1)
#     mamal1 = Mammal()
#     print(mamal1)
#     print(mamal1.appearance)
#
#     reptile1 = Reptile()
#     print(reptile1)
#
# main()


# class Animal:
#     def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
#         self.__birth_type = birth_type
#         self.__appearance = appearance
#         self.__blooded = blooded
#
#     @property
#     def birth_type(self):
#         return self.__birth_type
#
#     @birth_type.setter
#     def birth_type(self, val):
#         self.__birth_type = val
#
#
# def main():
#     animal1 = Animal("born alive")
#     print(animal1.birth_type)
#     animal1.birth_type = "died"
#     print(animal1.birth_type)
#
#
# main()

# class Time:
#     def __init__(self, hour=0, minute=0, second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def __str__(self):
#         return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
#
#     def __add__(self, other_time):
#         new_time = Time()
#         if self.second + other_time.second >= 60:
#             self.minute += 1
#             new_time.second = (self.second + other_time.second) - 60
#         else:
#             new_time.second = self.second + other_time.second
#
#         if self.minute + other_time.minute >= 60:
#             self.hour += 1
#             new_time.minute = (self.minute + other_time.minute) - 60
#         else:
#             new_time.minute = self.minute + other_time.minute
#
#         if self.hour + other_time.hour >= 24:
#             new_time.hour = (self.hour + other_time.hour) - 24
#         else:
#             new_time.hour = self.hour + other_time.hour
#
#         return new_time
#
#
# def main():
#     time1 = Time(1, 20, 30)
#     print(time1)
#
#     time2 = Time(24, 41, 30)
#     print(time1 + time2)
#
#
# main()

# class MySum:
#     @staticmethod
#     def getSume(*args):
#         sum_1 = 0
#         for i in args:
#             sum_1 += i
#
#         return sum_1
#
# def main():
#     print("Sum", MySum.getSume(1,2,3,4,5))
#
# main()

# def random_func(name:str, age: int, weight: float) -> str:
#     return "My name is{} and my age is {} and my weight is {}".format(name, age, weight)
#
# print(random_func("mamad", 44, 50.0))

# def is_odd(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# def check_list(list, func):
#     odd_list = []
#     for i in list:
#         if func(i):
#             odd_list.append(i)
#     return odd_list
#
# a_list = range(1, 20)
#
# print(check_list(a_list, is_odd))

# sum1 = lambda x, y: x + y
#
# print("sum :", sum1(2, 3))
# import random
#
# print(list(map((lambda x: x * 2), range(1, 11))))
#
# print([x for x in [random.randint(1, 1001) for i in range(5)] if x % 9 == 0])
#
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#         return True
#
# def gen_primes(max_numer):
#     for num1 in range(2, max_numer):
#         if is_prime(num1):
#             yield num1
#
# prime = gen_primes(50)
# print(next(prime))
# print(next(prime))

# import threading
# import random
# import time
#
# def execute_thread(i):
#     print("T {} s at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
#     rand_sleep_time = random.randint(1, 4)
#     time.sleep(rand_sleep_time)
#     print("T {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
#
# for i in range(10):
#     thread = threading.Thread(target=execute_thread, args=(i,))
#     thread.start()
#     print("a t:", threading.active_count())
#     print("t o:", threading.enumerate())