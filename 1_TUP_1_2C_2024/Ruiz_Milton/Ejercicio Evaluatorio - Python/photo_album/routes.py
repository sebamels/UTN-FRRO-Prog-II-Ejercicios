import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from models import db, Photo
from forms import PhotoForm

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)

@main.route('/add', methods=['GET', 'POST'])
def add_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        image_file = form.image.data

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(UPLOAD_FOLDER, filename))

            photo = Photo(title=title, description=description, image=filename)
            db.session.add(photo)
            db.session.commit()
            flash('Foto agregada con Éxito!', 'success')
            return redirect(url_for('main.index'))

    return render_template('photo_form.html', form=form)

@main.route('/delete/<int:photo_id>', methods=['POST'])
def delete_photo(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    db.session.delete(photo)
    db.session.commit()
    flash('Foto borrada con Éxito!', 'success')
    return redirect(url_for('main.index'))

@main.route('/edit/<int:photo_id>', methods=['GET', 'POST'])
def edit_photo(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    form = PhotoForm(obj=photo)

    if form.validate_on_submit():
        photo.title = form.title.data
        photo.description = form.description.data
        image_file = form.image.data

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(UPLOAD_FOLDER, filename))
            photo.image = filename

        db.session.commit()
        flash('Foto editada con Éxito!', 'success')
        return redirect(url_for('main.index'))

    return render_template('photo_form.html', form=form, photo=photo)
