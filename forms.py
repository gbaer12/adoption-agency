from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField,TextAreaField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL

class PetForm(FlaskForm):
    """Form for adding new Pet"""

    name = StringField('Pet name', validators=[InputRequired()])

    species = SelectField('Species', choices=[('dog','Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[Optional(),NumberRange(min=0, max=30)])

    notes = TextAreaField('Notes',validators=[Optional()])

    available = BooleanField('Available', validators=[Optional()])