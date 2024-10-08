from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        flash('Looks like you have changed your email!')
        session['email'] = form.email.data if "utoronto" in form.email.data else ""
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('base_index.html', form=form, name=session.get('name'), email=session.get('email'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)