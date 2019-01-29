from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author':'sharon',
        'title':'blog 1',
        'blog': 'my very first',
        'content': 'its ablessing',
        'date_posted': 'jan 20th, 2019'
    },
    {
        'author': 'sharon',
        'title': 'blog 2',
        'blog': 'my very first',
        'content': 'blessings and fun',
        'date_posted': 'jan 21th 2019'     
    }        
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")   




# if __name__ =="__main__":
#     app.run(debug=True)



 