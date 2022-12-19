from flask import Blueprint
from flask_cors import CORS
from flask_expects_json import expects_json
from schemas import LoginSchema
from services import authentification as AuthentService


authentification = Blueprint('Authentification', __name__)


@authentification.route('/login', methods=['POST'])
@expects_json(LoginSchema)
def PostLogin():
	return AuthentService.Login()
	
	