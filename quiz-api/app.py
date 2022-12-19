from flask import Flask
from flask_cors import CORS
from routers import QuizRouter,AuthentRouter,EngineRouter

app = Flask(__name__)
CORS(app)

from model import engine
engine.__init__()

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

#ajout des routes
app.register_blueprint(QuizRouter)
app.register_blueprint(AuthentRouter)
app.register_blueprint(EngineRouter)



if __name__ == "__main__":
    app.run()