from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = "Populate the Questions model with default questions."

    def handle(self, *args, **kwargs):
        questions = [
            {"text": "What is the capital of France?", "option_a": "Berlin", "option_b": "Madrid", "option_c": "Paris", "option_d": "Rome", "correct_option": "C"},
            {"text": "Which planet is known as the Red Planet?", "option_a": "Venus", "option_b": "Mars", "option_c": "Jupiter", "option_d": "Saturn", "correct_option": "B"},
            {"text": "Who wrote 'To Kill a Mockingbird'?", "option_a": "Harper Lee", "option_b": "J.D. Salinger", "option_c": "George Orwell", "option_d": "Mark Twain", "correct_option": "A"},
            {"text": "What is the chemical symbol for Gold?", "option_a": "Gd", "option_b": "Go", "option_c": "Ag", "option_d": "Au", "correct_option": "D"},
            {"text": "What is the smallest prime number?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "5", "correct_option": "B"},
            {"text": "How many continents are there?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_option": "C"},
            {"text": "What is the largest ocean on Earth?", "option_a": "Atlantic", "option_b": "Indian", "option_c": "Pacific", "option_d": "Arctic", "correct_option": "C"},
            {"text": "Who painted the Mona Lisa?", "option_a": "Leonardo da Vinci", "option_b": "Vincent van Gogh", "option_c": "Claude Monet", "option_d": "Pablo Picasso", "correct_option": "A"},
            {"text": "What is the boiling point of water in Celsius?", "option_a": "90°C", "option_b": "100°C", "option_c": "120°C", "option_d": "80°C", "correct_option": "B"},
            {"text": "Who discovered gravity?", "option_a": "Albert Einstein", "option_b": "Galileo Galilei", "option_c": "Isaac Newton", "option_d": "Nikola Tesla", "correct_option": "C"},
            {"text": "What is the capital of Japan?", "option_a": "Seoul", "option_b": "Bangkok", "option_c": "Tokyo", "option_d": "Beijing", "correct_option": "C"},
            {"text": "How many legs does a spider have?", "option_a": "6", "option_b": "8", "option_c": "10", "option_d": "12", "correct_option": "B"},
            {"text": "What is the square root of 64?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_option": "C"},
            {"text": "Who invented the telephone?", "option_a": "Thomas Edison", "option_b": "Alexander Graham Bell", "option_c": "Nikola Tesla", "option_d": "Albert Einstein", "correct_option": "B"},
            {"text": "Which planet is closest to the Sun?", "option_a": "Earth", "option_b": "Mars", "option_c": "Venus", "option_d": "Mercury", "correct_option": "D"},
            {"text": "What is the longest river in the world?", "option_a": "Amazon", "option_b": "Nile", "option_c": "Yangtze", "option_d": "Mississippi", "correct_option": "B"},
            {"text": "What is the largest mammal?", "option_a": "Elephant", "option_b": "Blue Whale", "option_c": "Giraffe", "option_d": "Hippopotamus", "correct_option": "B"},
            {"text": "How many bones are in the adult human body?", "option_a": "206", "option_b": "208", "option_c": "210", "option_d": "212", "correct_option": "A"},
            {"text": "Which gas do plants absorb from the atmosphere?", "option_a": "Oxygen", "option_b": "Carbon Dioxide", "option_c": "Nitrogen", "option_d": "Hydrogen", "correct_option": "B"},
            {"text": "Who invented the light bulb?", "option_a": "Alexander Graham Bell", "option_b": "Nikola Tesla", "option_c": "Thomas Edison", "option_d": "James Watt", "correct_option": "C"},
            {"text": "Which country is known as the Land of the Rising Sun?", "option_a": "China", "option_b": "Japan", "option_c": "South Korea", "option_d": "Thailand", "correct_option": "B"},
            {"text": "How many sides does a triangle have?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_option": "A"},
            {"text": "What is the freezing point of water in Celsius?", "option_a": "0°C", "option_b": "10°C", "option_c": "32°C", "option_d": "-10°C", "correct_option": "A"},
            {"text": "Who discovered penicillin?", "option_a": "Marie Curie", "option_b": "Alexander Fleming", "option_c": "Louis Pasteur", "option_d": "Joseph Lister", "correct_option": "B"},
            {"text": "What is the hardest natural substance on Earth?", "option_a": "Gold", "option_b": "Iron", "option_c": "Diamond", "option_d": "Graphite", "correct_option": "C"},
            {"text": "Which language is the most spoken worldwide?", "option_a": "Spanish", "option_b": "English", "option_c": "Mandarin Chinese", "option_d": "Hindi", "correct_option": "C"},
            {"text": "What part of the cell contains genetic material?", "option_a": "Cytoplasm", "option_b": "Nucleus", "option_c": "Mitochondria", "option_d": "Ribosome", "correct_option": "B"},
            {"text": "What is the largest desert in the world?", "option_a": "Sahara", "option_b": "Gobi", "option_c": "Antarctica", "option_d": "Kalahari", "correct_option": "C"},
            {"text": "Who was the first President of the United States?", "option_a": "Abraham Lincoln", "option_b": "George Washington", "option_c": "John Adams", "option_d": "Thomas Jefferson", "correct_option": "B"},
            {"text": "What is the chemical formula for table salt?", "option_a": "NaCl", "option_b": "H2O", "option_c": "CO2", "option_d": "NaHCO3", "correct_option": "A"},
            {"text": "Which animal is known as the 'King of the Jungle'?", "option_a": "Tiger", "option_b": "Elephant", "option_c": "Lion", "option_d": "Leopard", "correct_option": "C"},
            {"text": "What is the main gas in Earth's atmosphere?", "option_a": "Oxygen", "option_b": "Nitrogen", "option_c": "Carbon Dioxide", "option_d": "Hydrogen", "correct_option": "B"},
            {"text": "What is the capital of Australia?", "option_a": "Sydney", "option_b": "Melbourne", "option_c": "Canberra", "option_d": "Brisbane", "correct_option": "C"},
        ]


        for q in questions:
            Question.objects.get_or_create(
                text=q["text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"],
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated the Questions model."))
