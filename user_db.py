""" Create a user database (login, password, and last login timestamp) class (see problems 7-5 and 9-12) that manages a system requiring users to log in before access to resources is allowed. This database class manages its users, loading any previously saved user information on instantiation and providing accessor functions to add or update database information. If updated, the database will save the new information to disk as part of its deallocation (see __del__())."""
#data to be store
# - username
# - password
# - last_login
import time
import sys



db = {}

class User_db:
	def __init__(self,username,password,last_login):
		self.username = username
		self.password = password
		self.last_login = last_login

	def show_user_credential(self):
		print("Username:",self.username)
		print("password:",self.password)
		print("login time:",self.last_login)

	def new_user(self):
		username = input("Hi,please enter your desired username: ")
		while True:
			if (username) in db:
				prompt = 'name taken, try another: '
				continue
			else:
				break
		password = input('password: ')
		db[username] = password
	
	def old_user(self):
		username = input('username: ')
		password = input('password: ')
		passwd = db.get(username)
		if passwd == password:
			print ('welcome back', username)
		else:
			print ('login incorrect')


	def show_menu(self):
		prompt = input('(N)ew User Login\n(E)xisting User Login\n(Q)uit\nEnter choice: ')
		if prompt == 'n' :
			User_db.new_user(self)
		if prompt == 'e':
			User_db.old_user(self)
		if prompt == 'q':
			sys.exit()

uday = User_db("Uday","password",time.time())
uday.show_menu()
print(db)

"""if __name__ == '__main__':
	uday = User_db("Uday","gurinder",time.time())
	uday.show_menu()
	print(db)"""
