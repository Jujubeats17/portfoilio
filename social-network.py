class User:

    def _init_(self, name):
        self.user_name = name
        self.age = 0
        self.interests = []
        self.friends = []

    def Change_username(self,name):
        self.user_name = name

    def age(self,age):
        self.age=age

    def interests(self,interests):
        self.interests=interests

    def friends(self,friends):
        self.friends=friends



class Network:
    def _init_(self,name):
        self.name=name
        self.users=[]

    def name(self,name):
        self.users.append(name)
    def get_users(self):
        return self.users



def main():
    print ("What is your name?")
    user_input=input()

    print ("How old are you")
    user_input=input()

# Runs your program.
if __name__ == '__main__':
    main():
