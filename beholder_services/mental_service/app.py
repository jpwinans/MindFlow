from flask import Flask, Response, request
from language import Completions

app = Flask("Mental Consciousness")

language_completion = Completions()


@app.route("/completions", methods=["POST"])
def completions_create():
    data = request.get_json()

    if data.get("stream"):
        def event_stream():
            response = language_completion.create(data["prompt"], stream=True)

            for chunk in response:
                yield chunk

        return Response(event_stream(), mimetype="text/event-stream")
    else:
        return language_completion.create(data["prompt"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
