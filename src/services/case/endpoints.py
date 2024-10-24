from src.config.base_url import BASE_URL


class CaseEndpoints:

    get_testcases_list = f"{BASE_URL}/testcases"
    create_testcase = f"{BASE_URL}/testcases"
    get_testcases_by_id = lambda self, id_: f"{BASE_URL}/testcases/{id_}"
    update_testcase = lambda self, id_: f"{BASE_URL}/testcases/{id_}"
    delete_testcase = lambda self, id_: f"{BASE_URL}/testcases/{id_}"
