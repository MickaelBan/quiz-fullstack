from flask import jsonify


class Question():
    def __init__(self, title: str, position: str, text: str, image: str, possibleAnswers):
        self.title = title.replace("'", "''")
        self.position = position
        self.text = text.replace("'", "''")
        self.image = image.replace("'", "''")
        self.possibleAnswers = possibleAnswers

    @staticmethod
    def ParseRequestToQuestion(request):
        js = request.get_json()
        return Question(title=js['title'],
                        position=js['position'],
                        text=js['text'],
                        image=js['image'],
                        possibleAnswers=js['possibleAnswers'])

    def parseQuestionToJson(self) -> str:
        json = {"title": self.title, "position": self.position, "text": self.text,
                "image": self.image, "possibleAnswers": self.possibleAnswers}
        return jsonify(json)
