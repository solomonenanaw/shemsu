from flask import Flask, render_template
from flask import sqlalchemy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

if __name__ == '__main__':
    app.run(debug=True)
