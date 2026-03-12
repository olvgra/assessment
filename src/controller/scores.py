from flask import Flask, request, jsonify

from src.dao.scores import init_db
from src.service.scores import insert_score, get_score_by_id

app = Flask(__name__)

@app.before_request
def setup():
    init_db()

@app.post("/scores")
def add_score():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be JSON."}), 400

    first_name = body.get("First Name", "").strip()
    if not first_name:
        return jsonify({"error": "'First Name' is required and must be a non-empty string."}), 400

    second_name = body.get("Second Name", "").strip()
    if not second_name:
        return jsonify({"error": "'Second Name' is required and must be a non-empty string."}), 400

    score = body.get("Score")
    if score is None:
        return jsonify({"error": "'Score' is required."}), 400

    new_id = insert_score(first_name, second_name, score)
    return jsonify({"id": new_id, "First Name": first_name, "Second Name": second_name, "Score": score}), 201


@app.get("/scores/<id>")
def get_score(id: int):
    record = get_score_by_id(id)
    if record is None:
        return jsonify({"error": f"No score found for ID '{id}'."}), 404
    return jsonify(record), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)