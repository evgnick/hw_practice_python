from src.services.case.api_case import CaseAPI


class BaseTest:

    @classmethod
    def setup_method(cls):
        cls.api_case = CaseAPI()
