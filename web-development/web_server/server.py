from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')

def write_to_csv(data):
   with open('database.csv', newline='', mode='a') as database:
      writer = csv.writer(database, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writerow([data["email"], data["subject"], data["message"]])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
   if request.method == 'POST':
      try:
         data = request.form.to_dict()
         write_to_csv(data)
         return redirect('/contact_done.html')
      except:
         return 'Check the values and try again.'
   else:
      return 'Something went wrong, try again.'

@app.route('/<section>')
def page_html(section):
   return render_template(section)