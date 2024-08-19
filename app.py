from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def en():
    return render_template('en.html')

@app.route('/pt')
def pt():
    return render_template('pt.html')

@app.route('/esp')
def esp():
    return render_template('esp.html')

if __name__ == '__main__':
    app.run(debug=True)