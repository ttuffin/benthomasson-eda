import pytest
import os
import subprocess
from ..utils import CLIRunner, TESTS_PATH


@pytest.fixture(scope="function")
def init_webhook_client():
    cwd = os.path.join(TESTS_PATH, "event_source_webhook")
    result = subprocess.run(["docker-compose", "up", "-d"], cwd=cwd)
    yield result
    subprocess.run(["docker-compose", "down", "-v"], cwd=cwd)


def test_webhook_source_sanity(init_webhook_client):
    ruleset = os.path.join(TESTS_PATH, "event_source_webhook", "test_webhook_rules.yml")
    result = CLIRunner(rules=ruleset).run()

    assert "'msg': 'SUCCESS'" in result.stdout.decode()
    assert "'ping': 'pong'" in result.stdout.decode()
    assert "'User-Agent': 'webhook_client/1.0.1'" in result.stdout.decode()
