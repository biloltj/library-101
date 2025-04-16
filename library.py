from datetime import datetime, timedelta

# Sample book database
library = {
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
    "Atomic habits": {
        "author": "James Clear",
        "available": True,
        "borrower": "Bilol",
        "due_date": "2025-05-01",
        "history": [("Ibrohim", "2025-03-15", "2025-05-01")]
         
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
        "history": [("Ibrohim", "2025-03-15", "2025-04-01")]
    }
}
