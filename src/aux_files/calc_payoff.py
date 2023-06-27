avg_odd = 3.93
max_odd = 4.27

p_margin = 0.04
p_real = (1 / avg_odd) - p_margin  # our estimate of the "true" probability

p_max = 1 / max_odd

payoff = p_real * max_odd - 1

if payoff > 0:
    msg = f"Payoff = {payoff:.2f}. Place bet"
    print(msg)
else:
    msg = f"Payoff = {payoff:.2f}. Do not Place bet"
    print(msg)
    
    
    
    #Note that the syntax for the if statement in Python is slightly different than in MATLAB. In Python, you do not need to enclose the condition in parentheses, but you do need to end the statement with a colon and indent the code block that follows.