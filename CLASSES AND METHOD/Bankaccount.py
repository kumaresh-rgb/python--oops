class BankAccount:
    def __init__(self, name, age, profession, salary, balance=0):
        print("Account created successfully")
        self.name = name
        self.age = age
        self.profession = profession
        self.salary = salary
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Balance amount is zero")
        elif amount <= self.balance:
            self.balance -= amount
            print("Transaction processed")
        else:
            print("Insufficient balance")

Account1 = BankAccount(name="kumaresh", age=34, profession="broke", salary=30000)

Account1.deposit(5000)
Account1.withdraw(2)




class Product:
    def __init__(self, name, quantity):
        print("Product created successfully")
        self.name = name
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.quantity}"

    def change_quantity(self, new_quantity):
        print("Quantity updated")
        self.quantity = new_quantity


class ShoppingList:
    def __init__(self, title):
        print("Shopping list created successfully")
        self.title = title
        self.items = []

    def __str__(self) -> str:
        return f"{self.title}, {len(self.items)}"

    def add(self, item):
        if isinstance(item, Product):
            self.items.append(item)
            print("New item added to the shopping list")
        else:
            print("Invalid item. Please provide a valid Product object.")

    def show(self):
        print(f"Total items in the shopping list '{self.title}': {len(self.items)}")
        for item in self.items:
            print(f"Item: {item.name}, Quantity: {item.quantity}")


List1 = ShoppingList("Electronics")
print(List1)
List1.show()

Product1 = Product("Mobile", 200)
Product2 = Product("Tablet", 200)
Product3 = Product("Cables", 200)
Product4 = Product("Accessories", 200)

List1.add(Product1)
List1.add(Product2)
List1.add(Product3)
List1.add(Product4)

print(List1)
List1.show()


Product1.change_quantity(300)
print(List1)
List1.show()
