from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_db import Document, Base

engine = create_engine('sqlite:///documents.db')

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

documents = session.query(Document).all()

for doc in documents:
    print(f"ID: {doc.id}, Title: {doc.title}, Content: {doc.content}")

session.close()