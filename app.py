from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('numbers')
        numbers = [int(num.strip()) for num in data.split(',')]
        
        # Gerar o gráfico de pizza
        plt.pie(numbers, labels=numbers, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Gráfico de Pizza')
        plt.savefig('static/pie_chart.png')
        plt.close()
        
        return render_template('chart.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
