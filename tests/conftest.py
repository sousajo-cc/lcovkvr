import os
import tempfile
from pathlib import Path
from typing import Any

import pytest

from lcovkv import create_app
from lcovkv.db import init_db, get_db


@pytest.fixture
def app(tmpdir: Path) -> None:
    db_fd, db_path = tempfile.mkstemp()
    p = tmpdir.mkdir("data")
    app = create_app({
        'TESTING': True,
        'DATABASE': p,
    })

    with app.app_context():
        init_db()
        get_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app: Any) -> Any:
    return app.test_client()


@pytest.fixture
def runner(app: Any) -> Any:
    return app.test_cli_runner()
