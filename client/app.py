from flask import Flask, render_template, request, Response

from cache_client.cache_client import cache_client


app = Flask(__name__)


@app.route("/api/storage/", methods=["GET", "POST"])
def storage():
    if request.method == "GET":
        key = request.args.get("key")
        value = cache_client.get(key)
        # if not value: get it from db and save it to cache
        return Response(value, status=200)

    if request.method == "POST":
        for k, v in request.form.items():
            cache_client.set(k, v)
        return Response(status=200)


# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
