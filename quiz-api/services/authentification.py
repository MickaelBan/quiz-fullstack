
from flask import request
from services import jwt_utils as jwt


def ChekLogin():
	payload = request.get_json()
	if payload['password'] == "flask2023":
		token = jwt.build_token()
		return {"token": token},200
	else :
		return 'Unauthorized', 401
	
	