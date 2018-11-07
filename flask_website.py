from flask import Flask, render_template

# store flask aplication into variable
app = Flask(__name__)

# / is decorator pointing to homepage
@app.route('/')
def home():
    return render_template('main_page.html')

# to create 'about' subpage
@app.route('/about/')
def about():
    return 'Webpage content is here!'

if __name__ == '__main__':
    app.run(debug=True)