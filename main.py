# Kajetan Knopp (khknopp) - 2022

# Main flask imports
from flask import Flask, render_template, redirect, request, url_for, session, flash
# Database import
# Form import
from wtforms import Form, StringField, IntegerField, validators

# Main flask definitions
app = Flask(__name__)
app.secret_key = "Code4Ukraine"

# Form definition

class PersonForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    age = IntegerField('Age', [validators.NumberRange(min=0, max=140)])

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if 'add' in request.form:
            return redirect(url_for("add"))
        elif 'all' in request.form:
            return redirect(url_for("all"))
        elif 'last' in request.form:
            return redirect(url_for("last"))
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PersonForm(request.form) 
    if request.method == "POST" and form.validate():
        # Adding this person as last one added
        flash("Thanks for adding a new person to the database!")
        return redirect(url_for('main'))
    else:
        return render_template("add.html", form=form)

@app.route('/all')
def all():
    people = ['a', 'b', 'c']
    return render_template('all.html', people = people)

@app.route('/one/<int:id>')
def one(id):
    return render_template('one.html', person = "a")

@app.route('/last')
def last():
    if('last' not in session):
        flash("No people added in this session!")
        return redirect(url_for("main"))
    else:
        return redirect(url_for("one", id=5))

if __name__ == '__main__':
    app.run(debug=True)
