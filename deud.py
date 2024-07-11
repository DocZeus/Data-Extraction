import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Document, db
from config import Config

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    return text

# Function to extract entities using spaCy and noun chunks
def extract_entities(doc):
    entities = []
    
    # Extract named entities
    nlp_doc = nlp(doc)
    for ent in nlp_doc.ents:
        if ent.text.strip():  # Ensure only non-empty entities are included
            entities.append(ent.text.strip())
    
    # Extract noun chunks
    for chunk in nlp_doc.noun_chunks:
        if chunk.text.strip():  # Ensure only non-empty chunks are included
            entities.append(chunk.text.strip())
    
    return entities

# Function to perform clustering
def perform_clustering(entities_flat):
    if len(entities_flat) < 3:
        raise ValueError("Insufficient samples for clustering.")
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(entities_flat)
    
    n_clusters = min(3, X.shape[0])  # Ensure n_clusters is at most the number of documents
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
    return kmeans

# Main function to orchestrate the process
def main():
    # Create SQLAlchemy engine
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Query all documents
        documents = session.query(Document).all()
        
        # Extract and collect all entities from documents
        entities_list = []
        for doc in documents:
            entities = extract_entities(doc.content)
            entities_list.extend(entities)
        
        # Preprocess entities_flat
        preprocess_docs = [preprocess_text(doc) for doc in entities_list]
        
        # Perform clustering
        try:
            kmeans = perform_clustering(preprocess_docs)
            
            # Print clustering results
            for i, label in enumerate(kmeans.labels_):
                print(f"Entity: {entities_list[i]}, Cluster: {label}")
            
            # Create DataFrame for visualization
            df = pd.DataFrame({'Entity': entities_list, 'Cluster': kmeans.labels_})
            
            # Plot clustering results
            plt.figure(figsize=(12, 6))
            sns.scatterplot(data=df, x='Entity', y='Cluster', hue='Cluster', palette='viridis', legend=False)
            plt.xticks(rotation=90)
            plt.title('Entity Clusters')
            plt.tight_layout()
            plt.show()
        
        except ValueError as e:
            print(f"Error during clustering: {e}")
    
    finally:
        # Close session
        session.close()

if __name__ == "__main__":
    main()