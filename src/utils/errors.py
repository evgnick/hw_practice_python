from enum import Enum


class BaseErrorMessage(Enum):

    def message(self, actual, expected=None):
        return self.value.format(actual, expected)


class GlobalErrorMessage(BaseErrorMessage):
    WRONG_STATUS_CODE = "Wrong status code. Actual: {}, expected: {}"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected. Actual: {}, expected: {}"
    VALIDATION_ERROR = "Validation schema error: {}"
    WRONG_DELETE_FIELD = "The field doesn't exist: {}"


class CaseErrorMessage(BaseErrorMessage):
    WRONG_PRIORITY = "Unacceptable priority level: {}. Permissible values: {}"
