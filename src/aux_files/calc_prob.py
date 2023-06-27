nGames = 50  # number of games
bet = 100  # units: escudos

pwin = 0.8  # probability of winning
ploss = 1 - pwin  # loosing probability

rate = 0.25  # paying bet (what the house pays). This will be the average of
# bet payment with multiple bets

earnings = ((rate * pwin) - ploss) * bet * nGames



# The provided MATLAB code has a variable win, which has not been defined. I assume that this is a typo, and that the variable should instead be pwin, which is defined earlier in the code