from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.models import Puppy
from website.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies',__name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add_puppy', methods = ['GET','POST'])
def add():
    form = AddForm()
    
    if form.validate_on_submit():
        
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form = form)

@puppies_blueprint.route('/list')
def list():

    puppies = Puppy.query.all()
    print(puppies)
    return render_template('list.html', puppies = puppies)


@puppies_blueprint.route('/delete_puppy', methods= ['GET','POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    
    return render_template('delete.html', form = form)