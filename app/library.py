# library.py 
import json
import os
from datetime import datetime, timedelta

DATA_FILE = "library_data.json"

# Sample book database
def get_default_books():
    return {
    "1984": {
        "author": "George Orwell",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
   
    "Deep Work": {
        "author": "Call Newport",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    
    "The Kite Runner": {
        "author": "Khaled Hosseini",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },

    "The Alchemist": {
        "author": "Paulo Coelho",
        "available": False,
        "borrower": "Ibrohim",
        "due_date": "2025-04-20",
        "history": [["Ibrohim", "2025-03-15", "2025-04-01"]]
    },
     "Atomic habits": {
        "author": "James Clear",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
         
    }
}

def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return get_default_books()

def save_library(library_data):
    with open(DATA_FILE, "w") as file:
        json.dump(library_data, file, indent=4)