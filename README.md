The project involves:  

API Development: Flask-based API (api.py) for accessing and serving document data stored in an SQLite database (documents.db).  
Database Setup: Initialization and population script (setup_db.py) for creating the database schema and seeding initial data using SQLAlchemy.  
Text Analysis: Utilizes spaCy for natural language processing tasks such as entity extraction and clustering.  
Visualization: Matplotlib and Seaborn are used for visualizing data extracted from documents.  


Key Files:  

api.py: Flask API endpoints for document retrieval and serving.  
setup_db.py: Script to initialize and populate the SQLite database.  
text_analysis.py: Handles text preprocessing, entity extraction, and clustering.  
visualizations.py: Generates visualizations using Matplotlib and Seaborn.  


Git Ignore:  

Ignores documents.db to avoid tracking SQLite database files.  
Ignores __pycache__ directory to exclude Python bytecode caches.  


Dependencies:  

Flask  
SQLAlchemy  
spaCy  
Matplotlib  
Seaborn  
