class ValidationSchemas:
    DayCreateSchema = {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "integer"
            },
            "date": {
                "type": "string"
            },
            "day_energy": {
                "type": "string",
                "enum": ["energetic", "strong", "relaxed", "tired"]
            },
            "period_day_correct": {
                "type": "boolean"
            },
            "training_type": {
                "type": "string",
                "enum": ["out", "home", "skip"]
            },
        },
        "required": ["user_id", "date", "day_energy", "period_day_correct", "training_type"],
        "additionalProperties": False
    }