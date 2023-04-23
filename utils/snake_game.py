class SnakeGame:

    ''' JOGO DA COBRINHA'''

    game = {
        "high_score": 0,
        "current_score": 0,
        "games_played": 0,
        "game": False,
        "head": [1, 1],
        "length": 0,
        "direction": 6,
        "body": [],
        "grid": [
            [4, 4, 4, 4, 4, 4, 4, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 3, 3, 3, 3, 3, 3, 4],
            [4, 4, 4, 4, 4, 4, 4, 4]
        ],# Just for reference
        "elements": {
            0: ":green_circle:", # Snake Head
            1: ":green_square: ", # Snake Body
            2: ":white_large_square:", # Background
            3: ":brown_square:", # Walls
            4: ":red_square:" # Food
        },
        "spawn_food": True,
        "food": []
    }