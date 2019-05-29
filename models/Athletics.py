from app import db

class Athletics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    max_athlete_count = db.Column(db.Integer)
    name_kind_of_sports = db.Column(db.String(80))
    availability_finish_line = db.Column(db.Boolean)
    average_duration = db.Column(db.Float)
    length = db.Column(db.Float)

    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length):
        self.max_athlete_count = max_athlete_count
        self.name_kind_of_sports = name_kind_of_sports
        self.availability_finish_line = availability_finish_line
        self.average_duration = average_duration
        self.length = length

    def __repr__(self):
        return  str(self.__dict__)