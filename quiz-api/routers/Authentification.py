from flask import Blueprint, Flask,request
from flask_cors import CORS
from services import jwt_utils as jwt
import json


Authentification = Blueprint('Authentification', __name__)


@Authentification.route('/login', methods=['POST'])
def PostLogin():
	payload = request.get_json()
	if payload['password'] == "flask2023":
		token = jwt.build_token()
		return json.dumps({"token": token}),200
	else :
		return 'Unauthorized', 401
	
	