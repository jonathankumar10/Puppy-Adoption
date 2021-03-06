from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of the Owner: ')
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')
    

class DeleteForm(FlaskForm):

    name = StringField('Name of the Owner: ')
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Delete Owner') 