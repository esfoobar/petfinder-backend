from application import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name, species, description, photo):
        self.count = count

    def __repr__(self):
        return '<Count %r>' % self.count
