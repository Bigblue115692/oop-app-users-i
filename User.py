# your User class goes here
class Users():
    #think of what a user would need to have attribute wise
    def __init__(self, name, email_address, drivers_license):
        self.name = name
        self.email = email_address
        self.license = drivers_license
    
    def introduce(self):
        print(f"Hello, my weird name is {self.name}")

weird_person = Users("Jimmy", "hello@gmail.com", "666")
messed_up_guy = Users("Dan", "hi@gmail.com", "6666")

weird_person.introduce()
messed_up_guy.introduce()