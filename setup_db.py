from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from models import Document, Base

# Create SQLAlchemy engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample documents to populate the database
sample_documents = [
    {"title": "Email from John Doe", "content": "Hello, we need to discuss the quarterly report..."},
    {"title": "Report: Q1 2023", "content": "The sales figures show an increase..."},
    {"title": "Article: The impact of AI on modern technology", "content": "AI is transforming various industries..."},
    {"title": "Meeting Minutes", "content": "Summary of decisions made in the meeting..."},
    {"title": "Product Launch Presentation", "content": "Details about the upcoming product launch..."},
    {"title": "Research Paper Abstract", "content": "Overview of findings from the research study..."},
    {"title": "Customer Feedback Survey Results", "content": "Analysis of customer feedback received..."},
    {"title": "Financial Statement Analysis", "content": "Review of financial performance for the quarter..."},
    {"title": "Marketing Campaign Strategy", "content": "Proposed strategy for the next marketing campaign..."}
]

for doc_data in sample_documents:
    existing_doc = session.query(Document).filter_by(title=doc_data['title']).first()
    if not existing_doc:
        new_doc = Document(title=doc_data['title'], content=doc_data['content'])
        session.add(new_doc)

session.commit()
session.close()