from . import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=False)

    def repr(self):
        return f'<Photo {self.title}>'