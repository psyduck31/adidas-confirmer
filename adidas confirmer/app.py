from flask import Flask, render_template, request, abort
import os, json, base64, time

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")

@app.route('/event/<string:event_name>')
def event(event_name):
	return render_template('adidas.html')


@app.route("/api/getEvent")
def getEvent():
	return json.dumps({"start": "2020 01 15 20:52:00", "text": "OK!", "images": ["danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg", "danila.jpg"]})


@app.route("/api/eventAnswer", methods=["POST"])
def eventAnswer():
	return "Thank you!"


@app.route("/api/getImage", methods=["POST"])
def getImage():
	try:
		content = request.get_json()
		images = []
		if 'hash' in content:
			result = checkHash(request.headers['referer'].replace(request.headers['origin'], ""), request.headers['User-Agent'], content['hash'])
			if result == True:
				for image in content['images']:
					with open("./static/images/%s" % image, "rb") as img:
						images.append(str(base64.b64encode(img.read())).replace("b'", "").replace("'", ""))
				return json.dumps({"images": images})
			else:
				return json.dumps({"error": "Unauthorized request"})
	except Exception as e:
		return json.dumps({"error": str(e)})
		#return json.dumps({'error': 'bad request'})


def checkHash(path, header, string):
	result = ''
	for i in string:
		if ord(i) + 5 > 126 or ord(i) + 5 <= 25:
			result += chr(ord(i))
		else:
			result += chr(ord(i)+5)
	if header in result:
		result = result.replace(header, "")
		if path in result:
			result = result.replace(path, "").strip()
			if result.isdigit():
				if time.time() - int(result)/1000 < 1:
					return True
			return False
		else:
			return False
	else:
		result = result.replace(header, "")
		print("BAD HEADERS!!!")
		return False
	return result


@app.route("/static/images/<string:something>")
def staticFiles(something):
	return abort(403)



if __name__ == '__main__':
	app.run(debug=True)