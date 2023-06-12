from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/')
def index():
	return ''' <a href="/web1">Challenge #1</a><br>
	<a href="/web2">Challenge #2</a><br>
	<a href="/web3">Challenge #3</a><br>
	<a href="/web4">Challenge #4</a><br>
	<br>
	<a href="https://forms.gle/CcSVsNo2MjEqArcZ9"> Formulario para subir respuestas!</a>
	
	'''

@app.route('/web1', methods=["GET", "POST", "PUT"])
def web1():
	if request.method == 'GET':
		return "Ya googleaste sobre los metodos HTTP?"

	elif request.method == 'POST':
		return "Cada vez mas cerca! Segui intentando"

	elif request.method == 'PUT':
		print(request.data)
		if (request.data):
			return "FLAG: aprender_sobre_protocolos_garpa"
		else:
			return "Que es el body de un request? Agrega cualquier cosa al body del request y proba enviarlo de vuelta"
		
@app.route('/web2')
def web2():
    response = Response()
    response.headers.add('Medio-raro-este-header', '/web2/pss')
    response.data = "No mires siempre el body de un response..."
    return response


@app.route('/web2/pss')
def web2flag():
	return 'FLAG: caminos_ocultos'

@app.route('/web3')
def web3():
	return 'Como le digo Google que no investigue mi pagina web?'

@app.route('/robots.txt')
def web3flag():
	return 'FLAG: domo_arigato_mr_roboto'

@app.route('/web4')
def web4():
	return '''<p>L3dlYjQvYmFzZTY0L2ZsYWc=</p>
	<p>Basico? 64? QUE?</p>
	<!-- Psss...Cyberchef o Burp Suite Decoder.... -->
	'''

@app.route('/web4/base64/flag')
def web4flag():
	return 'FLAG: base64_no_oculta_secretos'

if __name__ == '__main__':
	app.run(debug=False)
