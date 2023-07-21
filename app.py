from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretysecret1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """Show Adoption Homepage."""

    pets = Pet.query.all()
    return render_template('homepage.html',  pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    """Show Add new pet form."""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(new_pet)
        db.session.commit()

        flash(f'{new_pet.name} has been Added.')
        
        return redirect('/')
    
    else:
        return render_template('add_new_pet.html', form=form)
    
@app.route('/<int:id>')
def show_pet_details(id):
    """Show page with pet details."""

    pet = Pet.query.get_or_404(id)

    return render_template('pet_details.html', pet=pet)
    
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    """Show form to edit pet."""

    pet = Pet.query.get_or_404(id)

    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f'{pet.name} has been updated.')

        return redirect('/')
    
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
    
@app.route('/<int:id>/delete', methods=['POST'])
def delete_pet(id):

    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)
    db.session.commit()

    return redirect('/')