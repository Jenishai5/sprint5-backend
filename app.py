from flask import Flask, request, jsonify
from datetime import datetime
from calculator import calculate
from storage import save_entry, load_history

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate_route():
    data = request.json

    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        operation = data.get("operation")

        result, duration = calculate(num1, num2, operation)

        entry = {
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result,
            "timestamp": datetime.now().isoformat(),
            "duration_ms": duration
        }

        save_entry(entry)

        return jsonify(entry)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/history", methods=["GET"])
def history():
    return jsonify(load_history())

@app.route("/help", methods=["GET"])
def help_route():
    return jsonify({
        "message": "Calculator API",
        "endpoints": {
            "POST /calculate": {
                "body": {
                    "num1": 3,
                    "num2": 9,
                    "operation": "plus"
                }
            },
            "GET /history": "Returns all calculations"
        }
    })
