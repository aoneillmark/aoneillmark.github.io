from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/products')
def products():
    return render_template('products.html', active_page='products')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)


    ##aaaaa

# TODO: 
# home page
# project page
# resume page