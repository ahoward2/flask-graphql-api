class Store:
	def __init__(self, initial_users):
		self.users = initial_users

	def add_user(user):
		self.users.append(user)
	
	def print_store(self):
		print(self.users)

	def get_user_by_id(self, id):
		for user in self.users:
			if (user["id"] == id):
				return user

	def get_users(self):
		return self.users

store = Store([
	{
		"id": "1",
		"first_name": "Austin",
		"last_name": "Howard",
	},
	{
		"id": "2",
		"first_name": "Anna",
		"last_name": "Skryd"
	}
])
