from flask import Flask, request, render_template, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI (replace 'sqlite:///your_database.db' with the desired database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    with app.app_context():
        files = UploadedFile.query.all()
        files_list = [{'id': file.id, 'filename': file.filename, 'file_path': file.file_path} for file in files]
    return render_template('index.html', files=files_list)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        with app.app_context():
            db.session.add(UploadedFile(filename=file.filename, file_path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)))
            db.session.commit()
    return 'File uploaded successfully'

if __name__ == '__main__':
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
