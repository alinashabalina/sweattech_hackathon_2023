class ValidationSchemas:
    UserCreateSchema = {
        "type": "object",
        "properties": {
            "username": {
                "type": "string"
            },
            "email": {
                "type": "string"
            },
            "password": {
                "type": "string"
            }
        },
        "required": ["email"],
        "additionalProperties": False,
    }