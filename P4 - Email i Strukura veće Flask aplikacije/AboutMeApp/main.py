from flask import Flask, render_template, request, redirect
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
import validators
import json

app = Flask(__name__)
app.debug = True
app.secret_key = b'xen_o7q536_*88^j-)m$pyyp*gmq$()8!p*ral@+k5+_=^jnjd'

# Postavke za email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = Config.email_username
app.config['MAIL_PASSWORD'] = Config.email_password
mail = Mail(app)

csrf = CSRFProtect(app)


@app.route("/")
def index():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("index.html", name = ime_i_prezime)


@app.route("/education")
def obrazovanje():
	return render_template("education.html")


@app.route("/bankAccount")
def bankovni_racun():
	ime_banke = Config.banka
	broj_racuna = Config.iban	
	
	if not validators.iban(broj_racuna):
		broj_racuna = "Neispravan IBAN!"
	
	return render_template("bankAccount.html", banka=ime_banke, iban=broj_racuna)


@app.route("/skills")
def vjestine():
	return render_template("skills.html")


@app.route("/comments", methods=['get', 'post'])
def komentari():
	
	komentari = []
	poruka = ''
	
	# Učitavamo komentare iz datoteke
	with open('komentari.json', mode='r', encoding='utf-8') as json_datoteka:
		komentari = json.load(json_datoteka)
		json_datoteka.close()
	
	ime = ''
	komentar = ''
	
	# Ako je metoda POST onda podatke validiramo i spremamo
	if request.method == 'POST':
		ime = request.form["ime"]
		komentar = request.form["komentar"]
		
		if len(ime)<3 or len(komentar)<3:
			ispravan_unos = False
			poruka = 'Pogrešan unos.'
		else:
			ispravan_unos = True
			poruka = 'Uspješan unos.'
			
		# Zapisujemo komentare u datoteku
		if ispravan_unos:
			with open('komentari.json', mode='w', encoding='utf-8') as json_datoteka:
				komentari.append({"ime": ime, "komentar": komentar})
				json.dump(komentari, json_datoteka)
				json_datoteka.close()
				
				# Da ne radi dupli POST prilikom refreshanja stranice
				# (https://en.wikipedia.org/wiki/Post/Redirect/Get)
				return redirect("/comments")
	
	# Prikazujemo podatke
	return render_template("comments.html", komentari=komentari, poruka=poruka, ime=ime, komentar=komentar)

	
@app.route("/contact", methods=['get', 'post'])
def kontakt():
	pass

	
# Funkcija za slanje emaila
def send_email(to, subject, body, **kwargs):
	msg = Message(subject, sender=Config.email_username, recipients=[to])
	msg.body = body
	mail.send(msg)

if __name__ == "__main__":
	app.run()
