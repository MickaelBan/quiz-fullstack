from flask import Blueprint
from services import authentification as AuthService
from services import engine as EngineService

database = Blueprint('DBRouter', __name__)

@database.route('/rebuild-db',methods=['POST'])
@AuthService.token_required
def PostRebuildDB():
    return EngineService.rebuil_DB()
