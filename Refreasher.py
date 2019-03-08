#Change
'''
#Refreasher Question 1
mark = float(input("Enter the Student's mark: "))
def grading(mark):
    output = ""
    if mark <=49.4:
        output = "Fail"
    if mark >49.4 and mark <=65.4:
        output = "Pass"
    if mark >65.4 and mark <=75.4:
        output = "Credit"
    if mark >75.4 and mark <=84.4:
        output = "Distinction"
    if mark > 84.4 and mark <=100:
        output = "High Distinction"
    print("Student has received a {}".format(output))
try:
    grading(mark)
except:
    print("Error")
'''

'''
#Refreasher Question 2

def factorial_forloop(originalnum):
    num = originalnum
    total = originalnum
    if originalnum >= 0:
        if originalnum == 0:
            total = 1
        while num !=0 and (num-1) !=0:
            total = (total * (num-1))
            num = num-1
    print("The factorial of {} is {}".format(originalnum,total))

originalnum = int(input("Enter whole number your would like the factorial of: "))
try:
    factorial_forloop(originalnum)
except:
    print("Error")

"""
b = a - 1
total = a

while a > 0:
    if b > 0:
        total *= b
        a = b
        b -= 1
    else:
        print("Factorial is:",total)
        break
"""
def calc_thing(value):
    if value ==0 or value ==1:
        return 1
    else:
        return value * calc_thing(value-1)
try:
    print(calc_thing(int(input("Enter num: "))))
except:
    print("error")
'''
'''
#Refreasher QUESTION 3
class Food():

    def __init__(self, desc, price):
        self.description = desc
        try:
            price = float(price)
        except:
            self.cost = 0.0
        else:
            self.cost = price

    def get_details(self):
        return str('The %s will cost %.2f' % (self.description, self.cost))

class Pizza(Food):
    def __init__(self, desc, price, *item_list):

        Food.__init__(self, desc, price)
        self.toppings = []
        for item in item_list:
            self.toppings.append(item)

    def get_details(self):
        return str('The %s will cost %.2f. Toppings are: %s.' % (self.description, self.cost, self.toppings))

brian = Pizza("Large Meatlovers", 11, "Pepperoni", "memes", "cream")

print(brian.get_details())
'''
