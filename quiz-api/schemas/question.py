question = {
    "type": "object",
    "properties": {
        "title": {"type": ["string", "null"]},
        "position": {"type": ["string", "null"]},
        "text": {"type": ["string", "null"]},
        "image": {"type": ["string", "null"]},
        "possibleAnswers": {
            "type": "array",
            "uniqueItems": True,
            "items":{
                "type":"object",
                "properties": {
                    "text": {"type":"string"},
                    "isCorrect": {"type":"string"}
                }
            }
        }
    },
    "required": [ "text", "image","possibleAnswers"]
}
