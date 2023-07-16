from flask import Flask, render_template, redirect, url_for, request
import matplotlib.pyplot as plt
import numpy as np
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
            plt.title('Gráfico de Pizza')
            
            # Salvar o gráfico em um arquivo
            chart_path = os.path.join('static', 'pie_chart.png')
            plt.savefig(chart_path)
            plt.close()
            
            return redirect(url_for('chart'))
    
    return render_template('create_chart.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')

if __name__ == '__main__':
    app.run()
