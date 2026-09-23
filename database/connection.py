import os
import psycopg2
from configparser import ConfigParser
from dotenv import load_dotenv

load_dotenv()

def config(filename=None, section="postgresql"):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "database.ini")
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} is not found in the {filename} file.")
    
    return db

def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return psycopg2.connect(database_url)
    
    data = config()
    return psycopg2.connect(**data)


