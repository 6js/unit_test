from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# Define the models for Pillar, ValueStream, and Teams
class Pillar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class ValueStream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


# Create the database tables
with app.app_context():
    # db.init_app(app)
    db.create_all()
    print('Created Database!')


# Add dummy data to the tables
def add_dummy_data():
    with app.app_context():
        pillars = ['Pillar 1', 'Pillar 2', 'Pillar 3']
        value_streams = ['Value Stream A', 'Value Stream B', 'Value Stream C']
        teams = ['Team X', 'Team Y', 'Team Z']

        for pillar_name in pillars:
            pillar = Pillar(name=pillar_name)
            db.session.add(pillar)

        for value_stream_name in value_streams:
            value_stream = ValueStream(name=value_stream_name)
            db.session.add(value_stream)

        for team_name in teams:
            team = Team(name=team_name)
            db.session.add(team)

        db.session.commit()



# Define the routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_records', methods=['POST'])
def get_records():
    selection = request.form['selection']

    if selection == 'pillar':
        records = Pillar.query.all()
    elif selection == 'valuestream':
        records = ValueStream.query.all()
    elif selection == 'teams':
        records = Team.query.all()
    else:
        records = []

    print(records)

    record_list = [{'id': record.id, 'name': record.name} for record in records]
    print(record_list)
    return jsonify(record_list)




if __name__ == '__main__':
    add_dummy_data()
    app.run(debug=True)
