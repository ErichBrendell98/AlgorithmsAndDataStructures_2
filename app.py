from flask import Flask, render_template, redirect, request

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

@app.route('/')
def home():
    return render_template('result.html')

@app.route('/result', methods = ['POST'])
def result():
    input_text = request.form.get('input')
    print(input_text)
    return redirect('/')

if __name__ in "__main__":
    app.run(debug=True)