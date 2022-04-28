from asyncore import write
from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)
print(__name__)


# To activate the virtual environment
# webserver/Scripts/activate

# @app.route('/path/parameter')
# def function(param=None): Sets the default param = None
#     return render_template(html, html_variable_name = param)

@app.route('/') 
def my_home():
    return render_template('index.html')

# Instead of doing an app.route for each html, we can instead just dynamically add it
# by defining a parameter string: page_name. We can do this because from the html, it
# redirects to /page.html
@app.route('/<string:page_name>') 
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt' ,mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
      with open('database.csv' ,mode='a', newline="") as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow(data.values())

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
                return 'Was not able to save'
    else:
        return 'Something went wrong'
