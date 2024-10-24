import requests
from src.services.case.endpoints import CaseEndpoints
from src.services.case.payload import CasePayloadGenerator


class CaseAPI:

    def __init__(self):
        self.endpoint = CaseEndpoints()

    def create_testcase(self, generator: CasePayloadGenerator = None):
        response = requests.post(
            url=self.endpoint.create_testcase,
            json=generator
        )
        return response

    def get_testcase_list(self):
        response = requests.get(
            url=self.endpoint.get_testcases_list
        )
        return response

    def get_testcase_by_id(self, case_id):
        response = requests.get(
            url=self.endpoint.get_testcases_by_id(case_id)
        )
        return response

    def update_testcase_by_id(self, case_id, generator: CasePayloadGenerator = None):
        response = requests.put(
            url=self.endpoint.update_testcase(case_id),
            json=generator
        )
        return response

    def delete_testcase_by_id(self, id_):
        response = requests.delete(
            url=self.endpoint.delete_testcase(id_)
        )
        return response
