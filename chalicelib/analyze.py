def analyze(body: dict, model):
    if body.get("multiples"):
        response = model.predict(body["data"])
        return response
    response = model.predict([body["data"]])
    return response
