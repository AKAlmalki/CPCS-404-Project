from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# 1NF - Single Valued Cells, Entries in column are same type, Rows are Unique
# 2NF - All attributes dependent on the key
# 3NF - All fields can be determined Only by the Key in the table and no other column

# Implement Show and Artist models, and complete all model relationships and properties, as a database migration. [done]

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    is_seeking_talent = db.Column(db.Boolean(), default=False)
    seeking_talent_desc = db.Column(db.String(200))
    shows = db.relationship('Show', backref='venue_show', lazy=True)
    

    def __repr__(self):
      return f'<Venue_id: {self.id}, name: {self.name}, address: {self.address}>'
    

    # implement any missing fields, as a database migration using Flask-Migrate [done]

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    is_seeking_venues = db.Column(db.Boolean(), default=False)
    seeking_venues_desc = db.Column(db.String(200))
    shows = db.relationship('Show', backref='artist_show', lazy=True)

    def __repr__(self):
      return f'<Artist_id: {self.id}, name: {self.name}, genres: {self.genres}>'

    # implement any missing fields, as a database migration using Flask-Migrate [done]

class Show(db.Model):
  __tablename__='Show'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
  start_time = db.Column(db.DateTime, nullable = False)

  def __repr__(self):
      return f'<Show {self.id} {self.start_time}>'
    
  def format(self):
    return {
      'id': self.id,
      'artist_id': self.artist_id,
      'venue_id': self.venue_id,
      'start_time': self.start_time
    }
