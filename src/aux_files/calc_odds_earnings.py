def calc_odds_earnings():
    home = 1.70
    draw = 3.75
    away = 4.75
    
    pHome_draw = (1 / home) + (1 / draw)
    min_odds = 1 / pHome_draw
    msg = f"probability of Home - Draw: {pHome_draw:.2f}, min odds required: {min_odds:.2f}"
    print(msg)
    

# Note that the sprintf function in MATLAB is equivalent to string formatting in Python, which is achieved using the % operator (older syntax) or the f-string (newer syntax) in Python 3.6+. The disp function in MATLAB is equivalent to the print function in Python.