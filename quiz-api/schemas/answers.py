answers = {
    "type": "object",
    "properties": {
        "playerName": {"type": "string"},
        "answers": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        }
    },
    "required": ["playerName","answers"]
}