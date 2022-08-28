def full_name_resolver(obj, info):
	try:
		payload = {
			"success": True,
			"name": {
				"first_name": "Austin",
				"last_name": "Howard"
			}
		}
	except Exception as error:
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload
