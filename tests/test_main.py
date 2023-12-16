def test_main(client):
    got = client.get("/")

    assert got.status_code == 200
    assert got.json() == {"message": "Hello World"}
