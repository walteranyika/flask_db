from peewee import SqliteDatabase, Model, CharField

database = SqliteDatabase('weed.db')


class User(Model):
    names = CharField()
    email = CharField(unique=True)
    dob = CharField()

    class Meta:
        database = database
