from werkzeug.exceptions import HTTPException

class CustomError(HTTPException):
    code = 418
    description = "Um erro genérico ocorreu."

    def __init__(self, description=None, response=None, custom_data=None):
        super().__init__(description, response)