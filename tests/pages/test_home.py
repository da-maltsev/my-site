def test_ok(client):
    got = client.get("/")

    assert got.status_code == 200
    assert got.template.name == "home/index.html"
    assert "text/html" in got.headers["Content-Type"]
