from flask import Flask,request
from flask_cors import CORS
from routers import QuizRouter,AuthentificationRouter


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"


#ajout des route Quiz
app.register_blueprint(QuizRouter)
app.register_blueprint(AuthentificationRouter)


if __name__ == "__main__":
    app.run()