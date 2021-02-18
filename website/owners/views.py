from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.models import Owner
from website.models import Puppy
from website.owners.forms import AddForm, DeleteForm

owners_blueprints = Blueprint('owners',__name__,template_folder='templates/owners')


@owners_blueprints.route('/add_owner', methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():

       

        name = form.name.data
        pup_id = form.pup_id.data
        puppyIds = Puppy.query.filter_by(id = pup_id).first()

        if puppyIds:

            new_owner = Owner(name, pup_id)
            db.session.add(new_owner)
            db.session.commit()

            return redirect(url_for('puppies.list'))
        
        else:
            return render_template('error.html')
    
    return render_template('add_owner.html', form = form)

@owners_blueprints.route('/delete_owner', methods=['GET','POST'])
def delete():

    form = DeleteForm()

    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.pup_id.data
        puppyIds = Puppy.query.filter_by(id = puppy_id).first()
        if name and puppy_id == puppyIds.id:        
            owner_del = Owner.query.filter_by(name = name, puppy_id = puppy_id).first()

            db.session.delete(owner_del)
            db.session.commit()

            return redirect(url_for('puppies.list'))
        
        else:
            return render_template('error.html')
    
    
    return render_template('delete_owner.html', form = form)