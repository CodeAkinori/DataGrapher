from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graphpizza', methods=['GET', 'POST'])
def graph_pizza():
    if request.method == 'POST':
        quantidade = int(request.form['quantidade'])
        return render_template('graph_pizza.html', quantidade=quantidade)
    return render_template('graph_pizza.html')


if __name__ == '__main__':
    app.run(debug=True)
