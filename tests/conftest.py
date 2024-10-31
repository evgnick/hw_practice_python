import pytest
from requests import Response
from loguru import logger
from curlify2 import Curlify
from src.services.case.payload import CasePayloadGenerator


@pytest.fixture()
def case_generator():
    return CasePayloadGenerator()


@pytest.fixture()
def response_logging():
    def _response_logging(response: Response):
        logger.info("Запрос на ручку: " + str(response.request.url))
        if response.request.body:
            if isinstance(response.request.body, bytes):
                logger.debug("Тело запроса: " + response.request.body.decode("utf-8"))
            else:
                logger.debug("Тело запроса: " + response.request.body)
        logger.debug("Заголовки запроса: " + str(response.request.headers))
        logger.info("Код ответа: " + str(response.status_code))
        logger.debug("Тело ответа: " + response.text)
        logger.debug("Curl: " + Curlify(response.request, compressed=True).to_curl())

    return _response_logging
