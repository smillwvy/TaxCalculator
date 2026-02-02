
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  return render_template("index.html")

@app.route("/api/calcTax", methods=["POST"])
def calcTax():
  """
  Expects JSON like: {"a": <number>, "b": <number>, "c": <number>}
  Returns: {"taxIncome": <number>, "taxSavings": <number>, "taxOnBonus": <number>}
  """
  data = request.get_json(silent=True)

  if not data or "a" not in data or "b" not in data or "c" not in data:
    return jsonify({"error1": "Income can not be blank"}), 400
  

  try:
    a = float(data["a"])
    b = float(data["b"])
    c = float(data["c"])

    if a < 0 or b < 0 or c < 0:
      return jsonify({"error2": "Please provide positive income"}), 400
  
    tax_income = 20/100*a
    tax_bonus = 20/100*c

    if b < 1000:
      return jsonify({"taxIncome": tax_income, "taxSavings": 0, "taxOnBonus": tax_bonus}), 200
    
    return jsonify({"taxIncome": tax_income, "taxSavings": 15/100*(b-1000), "taxOnBonus": tax_bonus}), 200
    
  except (ValueError, TypeError):
    return jsonify({"error4": "Both incomes must be numerical"}), 400

  
@app.route("/api/saveTax", methods=["POST"])
def commit_sum():
  data = request.get_json(silent=True)
  
  try:
    a = float(data["a"])
    b = float(data["b"])
    c = float(data["c"])
    
    # this is where we save the inputs in a db
    #import db_manager
    #db_manager.addIncomes(1, a, b, c)

    return jsonify({"message": "Saved"}), 200
    
  except (ValueError, TypeError):
    return jsonify({"error": "Error saving"}), 400


if __name__ == "__main__":
    app.run(debug=True)
