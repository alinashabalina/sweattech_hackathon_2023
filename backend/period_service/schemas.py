class ValidationSchemas:
    DayCreateSchema = {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "integer"
            },
            "day_id": {
                "type": "integer"
            },
            "day_energy": {
                "type": "string",
                "enum": ["energetic", "strong", "weak", "tired"]
            },
            "period_day_correct": {
                "type": "boolean"
            },
            "period_day_set": {
                "type": "integer"
            },
            "training_type": {
                "type": "string",
                "enum": ["out", "home", "skip"]
            }
        },
        "required": ["user_id", "day_energy", "period_day_correct", "training_type"],
        "additionalProperties": False
    }