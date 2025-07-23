from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_utils import JobIndex

app = Flask(__name__)
CORS(app)

job_index = JobIndex()

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    user_query = data.get("query", "")
    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    result = job_index.query_jobs(user_query)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)