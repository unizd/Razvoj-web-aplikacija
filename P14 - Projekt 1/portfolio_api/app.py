from flask import Flask, jsonify, request, abort

app = Flask(__name__)

about = {'about': 'Web, Flask & Angular developer.'}

portfolio_list = [
    {
        'id': 1,
        'title': u'Python aplikacija',
        'description': u'Web aplikacija za potrebe kolegija OWS'
    },
    {
        'id': 2,
        'title': u'Java aplikacija',
        'description': u'Java Desktop aplikacija (Java FX)'
    },
	{
        'id': 3,
        'title': u'Web stranica',
        'description': u'Statična HTML, CSS web stranica'
    }
]

contact = {'contact': '23 000 Zadar, developer@developer.com'}

# (About) O meni 
@app.route('/api/v1/about', methods=['GET'])
def get_about():
    return jsonify(about)


# (Portfolio) Dohvat cijelog portfelja
@app.route('/api/v1/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(portfolio_list)

	
# (Portfolio) Dodavanje u portfelj
@app.route('/api/v1/portfolio', methods=['POST'])
def create_portfolio():
    if not request.json or not 'title' in request.json:
        abort(400)
    portfolio_item = {
        'id': portfolio_list[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    portfolio_list.append(portfolio_item)
    return jsonify({'portfolio_item': portfolio_item}), 201


# (Contact) Kontakt
@app.route('/api/v1/contact', methods=['GET'])
def get_contact():
    return jsonify(contact)


if __name__ == '__main__':
    app.run(debug=True)