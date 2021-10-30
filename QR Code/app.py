from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('registration.html')
    
if __name__ == "__main__":
    app.run(debug=True)