# Answers from Dev-sprint1

# Name: Ceceilia Allwein


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Internet!"


@app.route("/world")
def world():
	return "Hello, World"


if __name__ == "__main__":
    app.run(port=5000)


