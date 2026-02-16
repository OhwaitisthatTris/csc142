import random


class Review:
    def __init__(self, rating, text):
        if not isinstance(rating, (int, float)):
            raise TypeError("The rating must be a number between 0-15.")
        if rating < 0 or rating > 15:
            raise ValueError("Rating must be between 0 and 15.")

        self.rating = rating
        self.text = text

    def __str__(self):
        return f"Rating: {self.rating}/15\nReview: {self.text}"


class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def add_review(self, review):
        if not isinstance(review, Review):
            raise TypeError("You can only add Review objects.")
        self.reviews.append(review)

    def average_rating(self):
        if not self.reviews:
            return 0
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews)

    def best_review(self):
        if not self.reviews:
            return None
        highest_rating = max(review.rating for review in self.reviews)
        best_reviews = [
            review for review in self.reviews
            if review.rating == highest_rating
        ]
        return random.choice(best_reviews)

    def worst_review(self):
        if not self.reviews:
            return None
        lowest_rating = min(review.rating for review in self.reviews)
        worst_reviews = [
            review for review in self.reviews
            if review.rating == lowest_rating
        ]
        return random.choice(worst_reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews yet.")
            return

        for review in self.reviews:
            print(review)
            print("-" * 40)


# Test the code
m = Movie("Interception")

r1 = Review(14, "Mid movie!")
r2 = Review(7, "Okay this is a good one!")

m.add_review(r1)
m.add_review(r2)

m.display_reviews()

print("Average rating:", m.average_rating())

print("Best review:")
print(m.best_review())

print("Worst review:")
print(m.worst_review())
