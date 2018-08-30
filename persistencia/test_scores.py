# Python 3.7
import scores

values = [("Raul", 24, "11:21"),("Kelly", 25, "8:30")]
scores.save_scores("scores.txt", values)

get_scores = scores.get_scores("scores.txt")
print(get_scores)

