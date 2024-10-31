from http import HTTPStatus

import pytest
from src.config.base_test import BaseTest
from src.utils.response_validations import validation
from src.services.case.models.case_model import Case
from tests.conftest import response_logging


class TestCase(BaseTest):

    def test_create_test_case(self, case_generator, response_logging):
        response = self.api_case.create_testcase(case_generator.set_id(5).build())
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.OK) \
            .assert_schema(Case)

    def test_update_test_case(self, case_generator, response_logging):
        response = self.api_case.update_testcase_by_id(7, case_generator.set_name("IVAN").build())
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.NOT_FOUND)

    def test_delete_test_case(self, response_logging):
        response = self.api_case.delete_testcase_by_id(1)
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.OK)

    def test_get_test_case(self, response_logging):
        response = self.api_case.get_testcase_by_id(1)
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.OK) \
            .assert_schema(Case)

    def test_get_test_case_list(self, response_logging):
        response = self.api_case.get_testcase_list()
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.OK) \
            .assert_schema(Case)

    def test_response_validations(self, response_logging):
        response = self.api_case.get_testcase_list()
        response_logging(response)
        validation(response) \
            .assert_status_code(HTTPStatus.OK) \
            .assert_schema(Case) \
            .assert_json(response.json())

    @pytest.mark.parametrize("delete_key", [
        "name", "description", "steps", "expected_result", "priority"
    ])
    def test_check_create_case_without_required_field(self, delete_key, case_generator, response_logging):
        fields = case_generator.build()
        del fields[delete_key]

        response = self.api_case.create_testcase(fields)
        response_logging(response)
        validation(response) \
            .assert_status_code(422)
