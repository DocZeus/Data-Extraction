from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # Initialize Flask-SQLAlchemy with your app instance

# Define your Document model
class Document(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)

@app.route('/api/documents', methods=['GET'])
def get_documents():
    documents = Document.query.all()
    docs = [{"id": doc.id, "title": doc.title, "content": doc.content} for doc in documents]
    return jsonify(docs)

if __name__ == '__main__':
    app.run(debug=True)