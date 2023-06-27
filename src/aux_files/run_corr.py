import numpy as np
from scipy.stats import linregress, pearsonr

def run_corr(x, y):
    # p = polyfit(x, y, 1)
    # slp = p(1)
    # itrc = p(2)
    slp, itrc, _, _, _ = linregress(x, y)
    
    # yfit = polyval(p, x)
    yfit = slp * x + itrc
    
    # yresid = y - yfit
    yresid = y - yfit
    
    # SSresid = sum(yresid.^2)
    SSresid = np.sum(yresid**2)
    
    # SStotal = (length(y)-1) * var(y)
    SStotal = (len(y) - 1) * np.var(y)
    
    # rsq = 1 - SSresid/SStotal
    rsq = 1 - SSresid / SStotal
    
    # [R,P] = corrcoef(x, y)
    R, P = pearsonr(x, y)
    
    # r_corr = R(2)
    r_corr = R
    
    # p_val = P(2)
    p_val = P
    
    return slp, itrc, rsq, r_corr, p_val
    
    
    
 # Note that the polyfit function in MATLAB is equivalent to the linregress function in Python, which returns the slope and intercept of the linear regression line, as well as other statistics such as the correlation coefficient and p-value. The polyval function in MATLAB is equivalent to the equation yfit = slp * x + itrc in Python. The corrcoef function in MATLAB is equivalent to the pearsonr function in Python, which returns the correlation coefficient and p-value.