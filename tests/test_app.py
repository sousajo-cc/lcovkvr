import hashlib
import os
from typing import Any


def generate_key() -> str:
    return hashlib.sha1(os.urandom(10)).hexdigest()


def test_insert_should_respond_201(client: Any) -> None:
    cov = "97.4"
    key = generate_key()
    assert client.put("/set/" + key, data={"value": cov}).status_code == 201


def test_insert_20_keys_should_respond_201_and_get_also(client: Any) -> None:
    cov = "927.4"
    keys = [generate_key() for _ in range(20)]
    for k in keys:
        r = client.put("/set/" + k, data={"value": cov})
        assert r.status_code == 201

    for k in keys:
        assert client.get("/get/", data={"commit_hash": k}).status_code == 201
