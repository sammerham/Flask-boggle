from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id

games = {}


@app.route("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.route("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique id for the board we're creating
    game_id = str(uuid4())  
    game = BoggleGame()   
    games[game_id] = game   

    print("making new game", games)

    return jsonify(game_id=game_id, board=game.board)



 


# games dict holds the game instance we want to check
    # current_game = games[id] to find right instance
    #is_word_in_word_list(self, word) checks if word is in dictionary (wordlist)
        # current_game.word_list.check_word(user_word) ==
        #   true means its in list!
        #   false means its not in word list
    # check_word_on_board(self, word)
        #Can word be found in board? Returns True/False.


@app.route('/api/score-word', methods=['POST'])
def score_word():
    """check if word is legal and calculate score"""
    data = request.json
    user_word = data['word'].upper()
    game_id = data['game_id']
    current_game = games[game_id]

    print("checking word", games)
    
    if not current_game.is_word_in_word_list(user_word):  # true/false
        result = "not-word"
    elif not current_game.check_word_on_board(user_word):  # true/false
        result = "not-on-board"
    else:
        result = "ok"
    

    return jsonify(result=result)