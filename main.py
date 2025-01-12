import string
from random import choice
from random import shuffle

Intro = """Password Generator
password must include: 
1 Upper Case
1 Lower Case
1 Digit 
1 Special Character
Minimum  Length is 6 total Characters
Maximum  Length is 16 total Characters"""

class RandPass:
    def __init__(self):
        print(Intro)
        self.upper = 0
        self.lower = 0
        self.digits = 0
        self.char = 0
        self.password = []

    def askfor_char(self):
        flag = False
        while not flag:
            print('\n')
            self.upper = int(input("How many Uppercase Characters: "))
            if 1 <= self.upper <= 13:
                flag = True
            else:
                print('Please select a number between 1 and 13')

        flag = False
        while not flag:
            self.lower = int(input("How many Lowercase Characters: "))
            if 1 <= self.lower <= 13:
                flag = True
            else:
                print('Please select a number between 1 and 13')

        flag = False
        while not flag:
            self.digits = int(input("How many Digits: "))
            if 1 <= self.digits <= 13:
                flag = True
            else:
                print('Please select a number between 1 and 13')

        flag = False
        while not flag:
            self.char = int(input("How many Special Characters: "))
            if 1 <= self.char <= 13:
                flag = True
            else:
                print('Please select a number between 1 and 13')

    def selection_char(self):
        for _ in range(self.upper):
            self.password.append(choice(string.ascii_uppercase))
        for _ in range(self.lower):
            self.password.append(choice(string.ascii_lowercase))
        for _ in range(self.digits):
            self.password.append(choice(string.digits))
        for _ in range(self.char):
            self.password.append(choice(string.punctuation))
        shuffle(self.password)
        pass_string = ''

        shuffle(self.password)
        for i in self.password:
            pass_string += i
        return pass_string

    def check_valid(self):
        # Directly check the total length condition
        return 6 <= (self.char + self.upper + self.lower + self.digits) <= 16

gen_p = RandPass()
t = False

while not t:
    gen_p.askfor_char()
    t = gen_p.check_valid()
    if not t:
        print('Invalid amount of characters selected, Please try again')

print('Your password is:   ', gen_p.selection_char())
