"""Forms for Adoption Agency."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form to add a pet"""

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Pet species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Pet image URL", validators=[Optional(), URL()])
    age = IntegerField("Pet age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Pet notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit a pet"""

    photo_url = StringField("Pet image URL", validators=[Optional(), URL()])
    notes = TextAreaField("Pet notes", validators=[Optional()])
    available = BooleanField("Available for adoption?")
