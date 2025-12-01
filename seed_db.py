import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["Spacestudysite"]


facts = [
    {
        "title": "Mars has the tallest volcano",
        "body": "Olympus Mons is the tallest volcano in the solar system, about 3 times taller than Mount Everest.",
        "tags": ["mars"],
        "created_at": datetime.utcnow()
    },
    {
        "title": "The Sun gives off solar wind",
        "body": "A stream of charged particles flows outward from the Sun, called the solar wind.",
        "tags": ["sun"],
        "created_at": datetime.utcnow()
    }
]

quizzes = [
    {
        "title": "Solar System Basics",
        "description": "Quick facts about planets",
        "difficulty": "Easy",
        "questions": [
            {
                "text": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Mercury"],
                "answer_index": 1,
                "explanation": "Mars has iron oxide on its surface, giving it a reddish appearance."
            },
            {
                "text": "Which planet is the closest to the Sun?",
                "options": ["Mercury", "Venus", "Earth", "Mars"],
                "answer_index": 0,
                "explanation": "Mercury orbits the Sun at an average distance of 57.9 million km."
            },
            {
                "text": "Which planet has rings?",
                "options": ["Mars", "Venus", "Saturn", "Earth"],
                "answer_index": 2,
                "explanation": "Saturn is famous for its visible ring system, made mostly of ice and rock."
            }
        ],
        "created_at": datetime(2025, 9, 15, 10, 23, 45)
    },
    {
        "title": "Moons of the Solar System",
        "description": "How well do you know the moons?",
        "difficulty": "Medium",
        "questions": [
            {
                "text": "What is the name of Jupiter’s largest moon?",
                "options": ["Europa", "Io", "Callisto", "Ganymede"],
                "answer_index": 3,
                "explanation": "Ganymede is the largest moon in the solar system, even bigger than Mercury."
            },
            {
                "text": "Titan is a moon of which planet?",
                "options": ["Neptune", "Jupiter", "Saturn", "Uranus"],
                "answer_index": 2,
                "explanation": "Titan is Saturn’s largest moon and has a thick atmosphere."
            },
            {
                "text": "Earth has how many natural moons?",
                "options": ["1", "2", "3", "None"],
                "answer_index": 0,
                "explanation": "Earth has only one natural moon, commonly called 'The Moon'."
            }
        ],
        "created_at": datetime(2025, 9, 15, 14, 56, 12)
    },
    {
        "title": "Stars and Galaxies",
        "description": "Exploring the universe beyond our solar system",
        "difficulty": "Medium",
        "questions": [
            {
                "text": "What is the closest star to Earth?",
                "options": ["Sirius", "Alpha Centauri", "The Sun", "Betelgeuse"],
                "answer_index": 2,
                "explanation": "The Sun is the closest star to Earth."
            },
            {
                "text": "The Milky Way is a type of what galaxy?",
                "options": ["Elliptical", "Spiral", "Irregular", "Ring"],
                "answer_index": 1,
                "explanation": "The Milky Way is a barred spiral galaxy."
            },
            {
                "text": "What is the largest known galaxy?",
                "options": ["Andromeda", "IC 1101", "Triangulum", "Messier 87"],
                "answer_index": 1,
                "explanation": "IC 1101 is the largest known galaxy, over 50 times the size of the Milky Way."
            }
        ],
        "created_at": datetime(2025, 9, 15, 18, 32, 59)
    },
    {
        "title": "Astrophysics Challenge",
        "description": "Concepts in physics and astronomy",
        "difficulty": "Hard",
        "questions": [
            {
                "text": "What is the speed of light in a vacuum?",
                "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "500,000 km/s"],
                "answer_index": 0,
                "explanation": "The speed of light in vacuum is approximately 299,792 km/s."
            },
            {
                "text": "Which law explains the relationship between a planet’s orbital period and distance from the Sun?",
                "options": ["Newton's First Law", "Kepler's Third Law", "Einstein's Theory of Relativity", "Hubble's Law"],
                "answer_index": 1,
                "explanation": "Kepler’s Third Law relates the square of a planet’s orbital period to the cube of its average distance from the Sun."
            },
            {
                "text": "What is a quasar?",
                "options": ["A type of asteroid", "A very bright galaxy nucleus", "A dying star", "A planet-sized black hole"],
                "answer_index": 1,
                "explanation": "Quasars are active galactic nuclei powered by supermassive black holes."
            }
        ],
        "created_at": datetime(2025, 9, 15, 20, 47, 8)
    },
    {
        "title": "Ultimate Space Quiz",
        "description": "Only for true space enthusiasts",
        "difficulty": "Expert",
        "questions": [
            {
                "text": "What is the estimated age of the universe?",
                "options": ["4.5 billion years", "10 billion years", "13.8 billion years", "20 billion years"],
                "answer_index": 2,
                "explanation": "Based on cosmic microwave background studies, the universe is about 13.8 billion years old."
            },
            {
                "text": "What is the event horizon of a black hole?",
                "options": ["The point of maximum radiation", "The edge beyond which nothing escapes", "The visible disk of gas", "The orbit of the nearest star"],
                "answer_index": 1,
                "explanation": "The event horizon is the boundary beyond which not even light can escape a black hole."
            },
            {
                "text": "Which element is most abundant in the universe?",
                "options": ["Helium", "Oxygen", "Hydrogen", "Carbon"],
                "answer_index": 2,
                "explanation": "Hydrogen makes up roughly 75% of the ordinary matter in the universe."
            }
        ],
        "created_at": datetime(2025, 9, 15, 22, 15, 37)
    }
]

db.facts.insert_many(facts)
db.quizzes.insert_many(quizzes)

print("✅ Seeded DB with facts and quizzes")