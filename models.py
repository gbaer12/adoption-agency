from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


class Pet(db.Model):
    """Pet potentially available for adoption."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    def image_url(self):
        """Return image of pet or default image."""

        return self.photo_url or DEFAULT_IMAGE_URL
    
def connect_db(app):
    """Connect to database."""
    
    db.app = app
    db.init_app(app)