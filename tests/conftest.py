import pytest
from src.services.case.payload import CasePayloadGenerator


@pytest.fixture()
def case_generator():
    return CasePayloadGenerator()
