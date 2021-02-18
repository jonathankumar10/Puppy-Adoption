from website import app
from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField
from website.models import Puppy

class SubmitForm(FlaskForm):
    submit = SubmitField('Click here!!') 


@app.route('/', methods=['GET','POST'])
def index():
    form = SubmitForm()

    if form.validate_on_submit():
        puppies = Puppy.query.all()
        print(puppies)
        return render_template('list.html', puppies = puppies)
    return render_template('home.html', form= form) 

if __name__ == '__main__':
    app.run(debug=True)