
from flask import request,json
from services import jwt_utils as jwt
from functools import wraps

def Login():	
	payload = request.get_json()
	if payload['password'] == "flask2023":
		token = jwt.build_token()
		response = {"token": token}
		response.headers.add('Access-Control-Allow-Origin', '*');
		return (response, 200)
	else:
		return 'Unauthorized - bad password', 401


def token_required(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		auth = request.headers.get('Authorization')
		if auth is None : 
			return 'Unauthorized - need to log in',401
		token = auth.split()[1]
		try :			
			if not jwt.decode_token(token) == jwt.payload_sub_admin:
				return 'Unauthorized - wrong token',401
			else :
				return f(*args, **kwargs)
		except jwt.JwtError as jE:
			return 'Unauthorized - ' + jE.message,401
	return decorator
