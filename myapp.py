from flask import Flask, render_template,flash
from forms_file import ReForm
from  models_file import User
from  peewee import  OperationalError

app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route('/', methods=("GET", "POST"))
def index():
    form = ReForm()
    if form.validate_on_submit():
        names = form.names.data
        email = form.email.data
        dob = form.dob.data
        # items =[names,email,dob]
        User.create(names=names,email=email,dob=dob)
        flash("Succesfully Registred","success")
        items = []
        users = User.select()
        for vals in users.iterator():
            print(vals.names)
            items.append([vals.names, vals.email, vals.dob])
        return  render_template("details.html",items=items)
    return render_template("index.html", form=form)

@app.route('/details')
def details():
    items = []
    users = User.select()
    for vals in users.iterator():
        print(vals.names)
        items.append([vals.names, vals.email, vals.dob])
    return render_template("details.html", items=items)

if __name__ == '__main__':
    try:
        print("Creating Users Table")
        #create tables here
        User.create_table()
    except OperationalError:
        print("Table has already been created")
    app.run()
