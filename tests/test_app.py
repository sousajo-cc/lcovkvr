import hashlib
import os


def generate_key():
    return hashlib.sha1(os.urandom(10)).hexdigest()


def test_insert_should_respond_201(client):
    cov = "97.4"
    key = generate_key()
    assert client.put("/set/" + key, data={"value": cov}).status_code == 201


def test_insert_20_keys_should_respond_201_and_get_also(client):
    cov = "927.4"
    keys = [generate_key() for _ in range(20)]
    for k in keys:
        r = client.put("/set/" + k, data={"value": cov})
        assert r.status_code == 201

    for k in keys:
        assert client.get("/get/", data={"commit_hash": k}).status_code == 201
