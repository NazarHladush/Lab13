from app import app
from flask import request, jsonify
from app import ma
from app import db
from models.Athletics import Athletics


class AthleticsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'max_athlete_count', 'name_kind_of_sports','availability_finish_line', 'average_duration', 'length')

athletic_schema = AthleticsSchema()
athletics_schema = AthleticsSchema(many=True)
db.create_all()

@app.route('/athletic', methods=["POST"])
def add_achletic():
    max_athlete_count = request.json["max_athlete_count"]
    name_kind_of_sports = request.json["name_kind_of_sports"]
    availability_finish_line = request.json["availability_finish_line"]
    average_duration = request.json["average_duration"]
    length = request.json["length"]

    new_athletic = Athletics(max_athlete_count, name_kind_of_sports, availability_finish_line,average_duration, length)

    db.session.add(new_athletic)
    db.session.commit()

    return athletic_schema.jsonify(new_athletic)

@app.route("/athletic", methods=['GET'])
def get_athletic():
    all_athletics = Athletics.query.all()
    result = athletics_schema.dump(all_athletics)
    return jsonify(result.data)

@app.route('/athletic/<id>', methods=["GET"])
def get(id):
    athletic = Athletics.query.get(id)
    return athletic_schema.jsonify(athletic)

@app.route('/athletic/<id>', methods=["PUT"])
def athletic_update(id):
    athletic = Athletics.query.get(id)
    max_athlete_count = request.json["max_athlete_count"]
    name_kind_of_sports = request.json["name_kind_of_sports"]
    availability_finish_line = request.json["availability_finish_line"]
    average_duration = request.json["average_duration"]
    length = request.json["length"]

    athletic.max_athlete_count = max_athlete_count
    athletic.name_kind_of_sports = name_kind_of_sports
    athletic.availability_finish_line = availability_finish_line
    athletic.average_duration = average_duration
    athletic.length = length

    db.session.commit()
    return athletic_schema.jsonify(athletic)

@app.route("/athletic/<id>", methods=["DELETE"])
def delete_athletic(id):
    athletic = Athletics.query.get(id)
    db.session.delete(athletic)
    db.session.commit()

    return athletic_schema.jsonify(athletic)

@app.route('/', methods=["GET"])
def index():
    return '<h1> Your server is started! </h1>'
