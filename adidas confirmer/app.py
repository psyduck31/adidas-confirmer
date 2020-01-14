from flask import Flask, render_template, request
import os, json, base64

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")

@app.route('/event/')
def event():
	return render_template('adidas.html')


@app.route("/api/getEvent")
def getEvent():
	return json.dumps({"start": "2020 01 15 01:12:15", "text": "OK!", "images": ["danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg"]})


@app.route("/api/eventAnswer", methods=["POST"])
def eventAnswer():
	return "Thank you!"


@app.route("/api/getImage", methods=["POST"])
def getImage():
	try:
		content = request.get_json()
		images = []
		for image in content['images']:
			with open("./static/images/%s" % image, "rb") as img:
				images.append(str(base64.b64encode(img.read())).replace("b'", "").replace("'", ""))
		return json.dumps({"images": images})
	except Exception as e:
		return json.dumps({"error": str(e)})
		#return json.dumps({'error': 'bad request'})



if __name__ == '__main__':
	app.run(debug=True)