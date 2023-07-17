from flask import Flask, render_template, redirect, url_for, request
import matplotlib.pyplot as plt

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_chart', methods=['GET', 'POST'])
def create_chart():
    if request.method == 'POST':
        data = request.form.get('numbers')
        if data:
            numbers = [int(num.strip()) for num in data.split(',')]
            
            # Gerar o gráfico de pizza
            plt.pie(numbers, labels=numbers, autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Pie Chart')
            
            # Salvar o gráfico em um arquivo, para exibição
            chart_path = os.path.join('static', 'img', 'pie_chart.png')
            plt.savefig(chart_path)
            plt.close()
            
            return redirect(url_for('chart'))
    
    return render_template('piechart/create_chart.html')


@app.route('/chart')
def chart():
    return render_template('piechart/chart.html')

@app.route('/chart_bar')
def chart_bar():
    return render_template('barchart/chart_bar.html')


@app.route('/create_bar_chart', methods=['GET', 'POST'])
def create_bar_chart():
    if request.method == 'POST':
        data = request.form.get('numbers')
        if data:
            numbers = [int(num.strip()) for num in data.split(',')]

            # Gerar o gráfico de barras
            plt.bar(range(len(numbers)), numbers)
            plt.xlabel('Categoria')
            plt.ylabel('Valor')
            plt.title('Bar Chart')

            # Salvar o gráfico em um arquivo, para exibição
            chart_path = os.path.join('static', 'img', 'bar_chart.png')
            plt.savefig(chart_path)
            plt.close()

            return redirect(url_for('chart_bar'))

    return render_template('barchart/create_bar_chart.html')


if __name__ == '__main__':
    app.run()
