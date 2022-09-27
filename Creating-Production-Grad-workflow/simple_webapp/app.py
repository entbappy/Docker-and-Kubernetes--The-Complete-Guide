from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template("index.html")
    # return jsonify("help")



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="127.0.0.1", port=8080,debug=True)