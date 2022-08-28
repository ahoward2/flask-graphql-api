from api.store import store

def getUsers_resolver(obj, info):
	try:
		users = store.get_users()
		payload = {
			"success": True,
			"users": users
		}
	except Exception as error:
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def getUser_resolver(obj, info, id):
	try:
		user = store.get_user_by_id(id)
		payload = {
			"success": True,
			"user": user
		}
	except Exception as error:
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload
