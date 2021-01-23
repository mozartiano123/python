import requests

class Questionnaire:

    def __init__(self, q_number, q_type):
        self.question_data = []
        self.qnumber = q_number
        self.qtype = q_type
        self.load_questions(self.qnumber, self.qtype)

    def load_questions(self,qnumber,qtype):
        parameters = {
            "amount": 10,
            "type": "boolean"
        }
        response = requests.get("https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()
        data = response.json()
        self.question_data = data["results"]

# question_data = [
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#      "question": "Undertale is an RPG created by Toby Fox and released in 2015.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Geography", "type": "boolean", "difficulty": "medium",
#      "question": "Gothenburg is the capital of Sweden.", "correct_answer": "False",
#      "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean",
#      "difficulty": "easy",
#      "question": "The name of the attack Kamehameha in Dragon Ball Z was named after a famous king of "
#                  "Hawaii.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Music", "type": "boolean", "difficulty": "medium",
#      "question": "For his performance at ComplexCon 2016 in Long Beach, California, Skrillex revived his "
#                  "Mothership set piece for one night only.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
#      "question": "Mortal Kombat was almost based on Jean-Claude Van Damme movie.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside "
#                  "swimming pools and drinking water.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
#      "question": "In career mode of Need for Speed: Underground 2, the first car the player can drive is "
#                  "the BMW M3 GTR.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Cartoon & Animations", "type": "boolean",
#      "difficulty": "medium",
#      "question": "Donald Duck played the role of Bob Cratchit in Disney&#039;s 1983 adaptation of A Christmas Carol.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
#      "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
#      "correct_answer": "True", "incorrect_answers": ["False"]}
# ]