# # TODO class attribute method

# class BankAccount:
#     interestpercent=1.3
#     account=0

#     def __init__(self, name, age, profession, salary, balance=0):
#         print("Account created successfully")
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.salary = salary
#         self.balance = balance
#         BankAccount.account+=1

#     def totalinterest(self):
#             interest=self.balance*BankAccount.interestpercent
#             return interest 


# c1=BankAccount.interestpercent
# print(c1)


# c2=BankAccount(2,2,2,2,2)
# print(c2.totalinterest())

# c3=BankAccount(3,3,3,3,3)
# print(c3.totalinterest())

# print(BankAccount.account)



# TODO CLASS METHOD PRACTICE


# class Developer:
#     # TODO CLASS ATTRIBUTE
#     limit=3 

#     def __init__(self,  balance=0):
#         print("Account created  successfully")
       
#         self.skill = []
#         self.balance = balance

    


#     def addskills(self ,skills):
#         if len(self.skill)<Developer.limit:
#             self.skill.append(skills)
#         else:
#             print("cannot be add more than three")

#     def __str__(self) -> str:
#         return f"{self.skill},{self.balance}"
    

#     @classmethod
#     def setlimit(cls,update_limit):
#         Developer.limit=update_limit



# dev1=Developer(3)
# print(dev1)
# print(Developer.limit)
# dev1.addskills("python")
# dev1.addskills("python1")
# dev1.addskills("python2")
# dev1.addskills("python3")
# print(dev1)



# dev2=Developer(3)
# print(dev1)
# dev2.setlimit(4)
# print(Developer.limit)
# dev2.addskills("python")
# dev2.addskills("python1")
# dev2.addskills("python3")
# dev2.addskills("python3")
# dev2.addskills("python3")
# print(dev2)


# TODO assignment

class Player:
    Max_heart = 3

    def __init__(self, name):
        self.name = name
        self.Max_heart = Player.Max_heart  # Set initial Max_heart value for each player

    def lose_heart(self):
        if (Player.Max_heart) <= 0:
            print("Game Over??")
        else:
            Player.Max_heart -= 1
              # Update default Max_heart for "kanmani"

    @classmethod
    def set_limit(cls, update_limit):
        Player.Max_heart = update_limit

    def __str__(self):
        return f"{self.name},{Player.Max_heart}"


p1 = Player("pooja")
print(p1)  # Output: pooja,3,3
p1.lose_heart()
print(p1)  # Output: pooja,2,2

p2 = Player("kanmani")
print(p2)  # Output: kanmani,3,3
p2.lose_heart()
p2.lose_heart()
p2.lose_heart()
print(p2)  # Output: kanmani,3,2
