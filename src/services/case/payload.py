from src.services.case.models.priority import Priority
from src.utils.errors import CaseErrorMessage
import itertools


class CasePayloadGenerator:
    _id_counter = itertools.count(1)

    def __init__(self):
        self._data = {}
        self._reset()

    def set_id(self, id_: int = None):
        if id_ is None:
            id_ = next(self._id_counter)
        self._data["id"] = id_
        return self

    def set_name(self, name: str = "Название"):
        self._data["name"] = name
        return self

    def set_description(self, description: str = "Описание"):
        self._data["description"] = description
        return self

    def set_steps(self, steps=None):
        if steps is None:
            steps = ["Шаг 1", "Шаг 2", "Шаг 3"]
        self._data["steps"] = steps
        return self

    def set_expected_result(self, expected_result: str = "Ожидаемый результат"):
        self._data["expected_result"] = expected_result
        return self

    def set_priority(self, priority: Priority = Priority.LOW):
        if not isinstance(priority, Priority):
            raise ValueError(CaseErrorMessage.WRONG_PRIORITY.message(priority, [p.value for p in Priority]))
        self._data["priority"] = priority.value
        return self

    def _reset(self):
        self.set_id()
        self.set_name()
        self.set_description()
        self.set_steps()
        self.set_expected_result()
        self.set_priority()
        return self

    def build(self):
        return self._data
