from flask import Flask, render_template, url_for, request, redirect
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

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
   if request.method == 'POST':
      data = request.form.to_dict()
      with open('database.txt', 'a+') as database:
         database.write(f'From: {data["email"]}; Subject: {data["subject"]}; Message: {data["message"]}\n')
      return redirect('/contact_done.html')
   else:
      return 'Algo salio mal, pa. Proba de nuevo.'

@app.route('/<section>')
def page_html(section):
   return render_template(section)