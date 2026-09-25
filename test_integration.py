import os
import time

import pytest
import requests

BASE_URL = os.environ.get("BASE_URL")


@pytest.mark.skipif(not BASE_URL, reason="BASE_URL is not set")
def test_health_endpoint():
    for _ in range(10):
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=2)
            break
        except requests.ConnectionError:
            time.sleep(1)
    else:
        pytest.fail("app did not start in time")

    assert response.status_code == 200
    assert response.text == "ok"
