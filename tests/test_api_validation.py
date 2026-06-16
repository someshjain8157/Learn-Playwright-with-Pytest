import pytest
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))

from utils.excel_reader import (
    get_config,
    get_api_test_data
)

from utils.json_utils import (
    save_actual_response,
    load_expected_response,
    compare_json,
    log_mismatch
)

CONFIG = get_config()

BASE_URL = CONFIG["base_url"]
API_KEY = CONFIG["api_key"]

TEST_DATA = get_api_test_data()


@pytest.mark.parametrize(
    "test_data",
    TEST_DATA,
    ids=[x["testcase_id"] for x in TEST_DATA]
)
def test_api_validation(playwright, test_data):

    request_context = playwright.request.new_context(
        extra_http_headers={
            "x-api-key": API_KEY
        }
    )

    tc_id = test_data["testcase_id"]

    method = str(
        test_data["method"]
    ).upper()

    endpoint = test_data["endpoint"]

    url = f"{BASE_URL}{endpoint}"

    if method == "POST":

        response = request_context.post(
            url,
            data=test_data["payload"]
        )

    elif method == "GET":

        params = {}

        if test_data.get("filters"):

            for item in str(
                test_data["filters"]
            ).split("&"):

                if "=" in item:

                    key, value = item.split(
                        "=",
                        1
                    )

                    params[key] = value

        response = request_context.get(
            url,
            params=params
        )

    else:

        pytest.fail(
            f"Unsupported Method: {method}"
        )

    print("\n")
    print(f"TC_ID   : {tc_id}")
    print(f"METHOD  : {method}")
    print(f"URL     : {response.url}")
    print(f"STATUS  : {response.status}")
    print(f"BODY    : {response.text()}")

    assert response.ok, (
        f"Status={response.status}\n"
        f"Body={response.text()}"
    )

    actual_json = response.json()

    save_actual_response(
        tc_id,
        actual_json
    )

    expected_json = load_expected_response(
        tc_id
    )

    skip_keys = []

    if (
        "skip_keys" in test_data
        and test_data["skip_keys"]
    ):

        skip_keys = [
            key.strip()
            for key in str(
                test_data["skip_keys"]
            ).split(",")
            if key.strip()
        ]

    mismatches = compare_json(
        actual_json,
        expected_json,
        skip_keys
    )

    if mismatches:

        log_mismatch(
            tc_id,
            mismatches,
            actual_json,
            expected_json
        )

        pytest.fail(
            f"Response mismatch. "
            f"Check logs/mismatched.txt"
        )

    request_context.dispose()