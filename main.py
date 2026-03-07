from flask import Flask, request, jsonify
import random

app = Flask(__name__)
PORT = 5004

# Basic class for holding quote information
class Quote():
    def __init__(self, quote: str, source: str | None = None):
        self.quote = quote
        self.source = source # Not required

# Each element is an object with a quote and source attribute
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

categories = {
    'motivational': MOTIVATIONAL_QUOTES,
    'health': HEALTH_FACTS,
    'video_game': VIDEO_GAME_QUOTES
}

# POST request to domain:PORT/quote with JSON object
# REQ has 'category' which has a domain of
# 'motivational', 'health', and 'video_game'
# RES json object with 'quote' and 'source'
@app.route('/quote', methods=['POST'])
def quote():
    # Get the category from the request
    data = request.json
    category = data['category']

    quote_list = categories.get(category)
    if not quote_list:
        return jsonify({'error': 'Category not supported'}), 400
    return jsonify_quote(random.choice(quote_list)), 200
            
# -----------------------------------------
# Helper Functions
# -----------------------------------------

# Converts quote object into JSON
def jsonify_quote(quote: Quote):
    return jsonify({
        'quote': quote.quote,
        'source': quote.source
    })


if __name__ == '__main__':
    print(f"Microservice running on http://localhost:{PORT}")
    app.run(port=PORT, debug=True)