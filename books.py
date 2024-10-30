books = {
    "The Lord of the Rings": {"Genre": "Fantasy", "Rating": 9.5},
    "Pride and Prejudice": {"Genre": "Romance", "Rating": 8.8},
    "To Kill a Mockingbird": {"Genre": "Historical Fiction", "Rating": 9.1},
    "1984": {"Genre": "Dystopian", "Rating": 9.2}
}

user_preferences = {}

def get_recommendations():
    preferred_genres = set(user_preferences.values())
    recommendations = []
    for book, info in books.items():
        if info["Genre"] in preferred_genres:
            recommendations.append((book, info["Rating"]))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

while True:
    genre = input("Enter a genre you like (or 'q' to quit): ")
    if genre.lower() == 'q':
        break
    user_preferences[genre] = genre

    recommendations = get_recommendations()
    if recommendations:
        print("\nRecommended books:")
        for book, rating in recommendations:
            print(f"- {book} (Rating: {rating})")
    else:
        print("No recommendations yet. Add more genres you like!")
