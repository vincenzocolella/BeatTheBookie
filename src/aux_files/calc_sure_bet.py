rate1 = 1.6
rate2 = 3.5
bet = 1000

margin = 1 / rate1 + 1 / rate2

if margin < 1:
    x1 = 1 * bet
    x2 = rate1 / rate2 * bet
    
    # 1000 * 1.55
    
    msg = f"Earning margin: {margin:.2f}."
    print(msg)
    msg = f"Sure bet at rate1: {x1:.2f}, rate 2: {x2:.2f}."
    print(msg)
else:
    msg = f"Still not profitable for arbitrage: {margin:.2f}"
    print(msg)

# rate2 / rate1

# bet1 = x1 * bet
# bet2 = x2 * bet

# Note that the sprintf function in MATLAB is equivalent to string formatting in Python, which is achieved using the % operator (older syntax) or the f-string (newer syntax) in Python 3.6+. The disp function in MATLAB is equivalent to the print function in Python.