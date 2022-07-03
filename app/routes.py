from app import app
from flask import redirect, render_template, url_for, flash
from app.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        flash('hello!')
    return render_template('index.html', form=form)
