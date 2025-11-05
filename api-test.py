from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to order management"

@app.route("/get-order/<number>")
def get_order(number):
    response = f"Order number: {number}"
    extras = request.args.get('extras') #get from query params
    if extras:
        response = f"{response}. Extras: {extras}"
    return response

@app.route("/create-order", methods=["POST"])
def create_order():
    data = request.get_json() # get data from body
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)