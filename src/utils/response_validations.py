from pydantic import BaseModel, ValidationError
from requests import Response
from src.utils.errors import GlobalErrorMessage
from deepdiff import DeepDiff


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

    def assert_json(self, expected_json):
        try:
            response_json = self.response.json()
        except ValueError as e:
            raise AssertionError(GlobalErrorMessage.VALIDATION_ERROR.message(e))

        diff = DeepDiff(
            response_json, expected_json, verbose_level=2, ignore_order=True
        )

        if diff:
            error_message = "JSON объекты отличаются:\n"

            if "dictionary_item_added" in diff:
                error_message += "Добавлены следующие элементы:\n"
                for item in diff["dictionary_item_added"]:
                    error_message += f"  {item}\n"

            if "dictionary_item_removed" in diff:
                error_message += "Удалены следующие элементы:\n"
                for item in diff["dictionary_item_removed"]:
                    error_message += f"  {item}\n"

            if "values_changed" in diff:
                error_message += "Изменены следующие значения:\n"
                for key, change in diff["values_changed"].items():
                    error_message += f"  {key}: с '{change['old_value']}' на '{change['new_value']}'\n"

            error_message += f"\nОжидаемый JSON:\n{expected_json}\n"
            error_message += f"Полученный JSON:\n{response_json}"
            raise AssertionError(GlobalErrorMessage.WRONG_JSON_TEXT.message(error_message))

        return self


validation = ResponseValidations
