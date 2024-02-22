def application(environment, start_response):
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return ["<h1>こんにちは！</h1>".encode("utf-8")]

