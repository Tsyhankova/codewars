def squares_needed(grains):
    if grains == 0:
        return 0
    else:
        squares = 1
        while grains > 1:
            grains = grains//2 
            squares += 1
        return squares
