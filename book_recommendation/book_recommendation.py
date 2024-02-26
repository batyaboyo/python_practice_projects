books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "genre": "Non-Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "The Lean Startup", "author": "Eric Ries", "genre": "Business"},
    {"title": "1984", "author": "George Orwell", "genre": "Science Fiction"},
]

def recommend_book(genre):
    for book in books:
        if book["genre"] == genre:
            return f"I recommend '{book['title']}' by {book['author']}."
    
    return "Sorry, I couldn't find any book in that genre. Try another one!"

user_genre = input("Please enter a genre: ")
recommendation = recommend_book(user_genre)
print(recommendation)