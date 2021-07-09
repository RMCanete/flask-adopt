"""Adoption Agency application."""

from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2118@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'asdfghjkl'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """List pets"""

    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added a {new_pet.species} named {new_pet.name}.")
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route(f'/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    """Edit a pet"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Updated {pet.name}")

        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)

@app.route(f"/<int:id>/delete", methods=['POST'])
def delete_tag(id):
    """Delete a pet"""
    
    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)
    db.session.commit()

    return redirect(f'/')
