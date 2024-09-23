from flask import Flask, url_forimport dominatefrom dominate.tags import *app = Flask(__name__)@app.route('/')def home():    doc = dominate.document(title='Home Page')    with doc.head:        link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')    logo_url = url_for('static', filename='logo.png')  # Properly reference the static logo    with doc:        with body(style="background-color: rgb(229, 204, 255);"):            with div(style="text-align: center; margin-top: 50px;"):                h1('Welcome to Na Laochra Aeracha Home Page')                p('Cork LGBTQ+ Inclusive GAA (football) Club')                img(src=logo_url, width="400")  # Use the URL for the static file    return str(doc)if __name__ == '__main__':    app.run(debug=True)