from operator import ne
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from form import AddNewPet, EditPet
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///animals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "chi21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    animals = Pet.query.all()
    return render_template('home.html', animals=animals)


@app.route('/add', methods=['GET', 'POST'])
def add_animal():
    form = AddNewPet()
    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_animal.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPet(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    return render_template('pet.html', pet=pet, form=form)
