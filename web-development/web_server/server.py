from flask import Flask, render_template, url_for
app = Flask(__name__)

#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None, post_id=None):
#   return render_template('index.html', name=username, post_id=post_id)

#@app.route('/<username>')
#def hello_world(username=None):
#   return render_template('index.html', name=username)

# probando la reutilizacion de acuerdo al valor ingresado
@app.route('/')
def main():
   return render_template('index.html')


@app.route('/<section>')
def page_html(section):
   return render_template(section)