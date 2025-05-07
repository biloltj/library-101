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
         
    },
     "13 Things Mentally Strong People Don't Do": {
        "author": "Amy Morin",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "A Dance with Dragons": {
        "author": "George R.R. Martin",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "A Feast for Crows": {
        "author": "George R.R. Martin",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "A Random Walk Down Wall Street": {
        "author": "Burton G. Malkiel",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "A Strom of Swords": {
        "author": "George R.R. Martin",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "A Thousand Splendid Suns": {
        "author": "Khalid Hosseini",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
    "Act Like a Success, Think Like a Success": {
        "author": "Act Like a Success, Think Like a Success",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Alibaba": {
        "author": "Duncan Clarck",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
      "Arms and The Man ": {
        "author": "Bernard Shaw",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
      "Being Ehtical": {
        "author": "S. Manikutty",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
      "Beyond Order": {
        "author": "Jordan B. Peterson",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
      "Big Magic": {
        "author": "Elizabeth Gilbert",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
      "Eat That Frog!": {
        "author": "Brian Tracy!",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Elon Musk": {
        "author": "Ashlee Vange ",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Factfulness": {
        "author": "Hans Rosling",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Good to Great": {
        "author": "Jim Collins",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Heartbreak Hotel": {
        "author": "Jonathan Kellerman",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "High Performance Habits": {
        "author": "Brendon Burchard",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "How Full is Your Bucket?": {
        "author": "Tom Rath & Donald O. Clifton",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    },
     "Tom Rath & Donald O. Clifton": {
        "author": "Nir Eyal",
        "available": True,
        "borrower": None,
        "due_date": None,
        "history": []
    }
}
#
def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return get_default_books()

def save_library(library_data):
    with open(DATA_FILE, "w") as file:
        json.dump(library_data, file, indent=4)