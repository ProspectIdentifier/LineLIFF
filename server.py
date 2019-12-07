import os
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return "hello world"

@app.route('/contact-list')
def contact_list():
    return render_template('./contact-list.html')

@app.route('/interesting')
def interesting():
    return render_template('./interesting.html')

@app.route('/company-summary')
def company_summary():
    return render_template('./company-summary.html')

if __name__ == '__main__':
    print(app.url_map)
    print(app.blueprints)
    app.run(debug = True, host='0.0.0.0', port=5001, threaded=True)