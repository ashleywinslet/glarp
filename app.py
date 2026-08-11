from flask import Flask, render_template, session, jsonify, request

app = Flask(__name__)
app.secret_key = "gcash-clone-demo-secret"

STARTING_BALANCE = 2516.04


def get_balance():
    if "balance" not in session:
        session["balance"] = STARTING_BALANCE
    return session["balance"]


@app.route("/")
def home():
    return render_template("index.html", balance=get_balance())


@app.route("/api/balance")
def api_balance():
    return jsonify({"balance": get_balance()})


@app.route("/api/send", methods=["POST"])
def api_send():
    data = request.get_json(force=True)
    amount = float(data.get("amount", 0))
    recipient = (data.get("recipient") or "").strip()

    if amount <= 0:
        return jsonify({"ok": False, "error": "Enter a valid amount."}), 400
    if not recipient:
        return jsonify({"ok": False, "error": "Enter a recipient."}), 400

    balance = get_balance()
    if amount > balance:
        return jsonify({"ok": False, "error": "Insufficient balance."}), 400

    balance -= amount
    session["balance"] = balance
    return jsonify({"ok": True, "balance": balance, "recipient": recipient, "amount": amount})


@app.route("/api/cashin", methods=["POST"])
def api_cashin():
    data = request.get_json(force=True)
    amount = float(data.get("amount", 0))

    if amount <= 0:
        return jsonify({"ok": False, "error": "Enter a valid amount."}), 400

    balance = get_balance() + amount
    session["balance"] = balance
    return jsonify({"ok": True, "balance": balance, "amount": amount})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
