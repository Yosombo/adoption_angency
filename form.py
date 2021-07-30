from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, DateTimeField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, Optional, URL


class AddNewPet(FlaskForm):

    name = StringField('Name', validators=[
                       InputRequired(message='Enter pet name')])

    species = SelectField('Species', choices=['Dog', 'Cat', 'Donkey'], validators=[
        InputRequired()])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[
        NumberRange(min=0, max=30), Optional()
    ])

    notes = TextAreaField('More information')


class EditPet(FlaskForm):

    name = StringField('Name', validators=[
                       InputRequired(message='Enter pet name')])

    species = SelectField('Species', choices=['Dog', 'Cat', 'Donkey'], validators=[
        InputRequired()])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[
        NumberRange(min=0, max=30), Optional()
    ])

    notes = TextAreaField('More information')
    available = BooleanField('Available')
