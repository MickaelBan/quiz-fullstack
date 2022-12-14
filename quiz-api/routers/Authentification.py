from flask import Blueprint, Flask,request
from flask_cors import CORS
from services import authentification as AuthentService


authentification = Blueprint('Authentification', __name__)


@authentification.route('/login', methods=['POST'])
def PostLogin():
	return AuthentService.ChekLogin()
	
	