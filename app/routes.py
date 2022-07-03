from app import app, db
from flask import redirect, render_template, url_for, flash
from app.forms import HelloForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    messages = User.query.order_by(User.timestamp).all()
    if form.validate_on_submit():
        if form.secret_code.data != '123':
            flash('暗号不正确，你应该说："风骚大吉鲁"！')
            return redirect(url_for('index'))
        user = User(name=form.name.data, message=form.message.data)
        db.session.add(user)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
