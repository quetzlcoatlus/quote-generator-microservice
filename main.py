from flask import Flask, request, jsonify
import random

app = Flask(__name__)
PORT = 5004


# Basic class for holding the information
class Quote():
    def __init__(self, quote: str, source: str | None = None):
        self.quote = quote
        self.source = source # Not required


# Each element is an object with a quote, author and source attribute
# Accessed with .quote, .author and .source respectively
MOTIVATIONAL_QUOTES = [
    Quote(
        "Action is the foundational key to all success.",
        "Pablo Picasso"
    ),
    Quote(
        "The mind is everything. What you think you become.",
        "Buddha"
    ),
    Quote(
        "The best revenge is massive success.",
        "Frank Sinatra"
    ),
    Quote(
        "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed.",
        "Michael Jordan"
    ),
    Quote(
        "There is only one way to avoid criticism: do nothing, say nothing, and be nothing.",
        "Aristotle"
    )
]

HEALTH_FACTS = [
    Quote(
        "Laughter boosts the immune system.",
        "https://ohmyfacts.com/health-wellness/45-facts-about-health/"
    ),
    Quote(
        "Walking can reduce the risk of stroke.",
        "https://ohmyfacts.com/health-wellness/45-facts-about-health/"
    ),
    Quote(
        "Strength training boosts metabolism.",
        "https://ohmyfacts.com/health-wellness/45-facts-about-health/"
    ),
    Quote(
        "Reading can reduce stress.",
        "https://ohmyfacts.com/health-wellness/45-facts-about-health/"
    ),
    Quote(
        "Social connections improve longevity.",
        "https://ohmyfacts.com/health-wellness/45-facts-about-health/"
    )
]

VIDEO_GAME_QUOTES = [
    Quote(
        "It’s dangerous to go alone, take this!", 
        "The Legend of Zelda"
    ),
    Quote(
        "The cake is a lie", 
        "Portal"
    ),
    Quote(
        "Praise the sun!", 
        "Dark Souls"
    ),
    Quote(
        "FINISH HIM!", 
        "Mortal Kombat"
    ),
    Quote(
        "Do a barrel roll!", 
        "Star Fox 64"
    )
]

# POST request to domain:PORT/route with JSON object
# REQ has 'category' which has a domain of
# 'motivational', 'health', and 'video_game'
# RES json object with 'quote' and 'source'
@app.route('/quote', methods=['POST'])
def quote():
    # Get the category from the request
    data = request.json
    category = data['category']

    match(category):
        case 'motivational':
            quote = random_motivational_quote()
            return jsonify_quote(quote), 200
        case 'health':
            quote = random_health_fact()
            return jsonify_quote(quote), 200
        case 'video_game':
            quote = random_video_game_quote()
            return jsonify_quote(quote), 200
        case _:
            return jsonify({'error': 'Category not supported'}), 400

# -----------------------------------------
# Helper Functions
# -----------------------------------------

# Returns random quote object from MOTIVATIONAL_QUOTES
def random_motivational_quote():
    i = random.randint(0,len(MOTIVATIONAL_QUOTES)-1)
    return MOTIVATIONAL_QUOTES[i]


# Returns random quote object from HEALTH_FACTS
def random_health_fact():
    i = random.randint(0,len(HEALTH_FACTS)-1)
    return HEALTH_FACTS[i]


# Returns random quote object from VIDEO_GAME_QUOTES
def random_video_game_quote():
    i = random.randint(0,len(VIDEO_GAME_QUOTES)-1)
    return VIDEO_GAME_QUOTES[i]


# Converts quote object into JSON
def jsonify_quote(quote: Quote):
    return jsonify({
        'quote': quote.quote,
        'source': quote.source
    })


if __name__ == '__main__':
    print(f"Microservice running on http://localhost:{PORT}")
    app.run(port=PORT, debug=True)