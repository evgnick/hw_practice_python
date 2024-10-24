from pydantic import BaseModel, ValidationError
from requests import Response
from src.utils.errors import GlobalErrorMessage


class ResponseValidations:

    def __init__(self, response: Response) -> object:
        self.response = response

    def assert_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, \
            GlobalErrorMessage.WRONG_STATUS_CODE.message(self.response.status_code, expected_status_code)
        return self

    def assert_schema(self, schema: BaseModel):
        try:
            data = self.response.json()
            if isinstance(data, list):
                for item in data:
                    schema.model_validate(item)
            else:
                schema.model_validate(data)
        except ValidationError as e:
            raise AssertionError(GlobalErrorMessage.VALIDATION_ERROR.message(e))
        return self

    def assert_json(self):
        pass


validation = ResponseValidations
