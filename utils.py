import numpy as np
import statsmodels.api as sm

def generate_price_stream(length, arparams, maparams, tick_size):
    arparams = np.array(arparams)
    maparams = np.array(maparams)
    ar = np.r_[1, -arparams] # add zero-lag and negate
    ma = np.r_[1, maparams] # add zero-lag
    y = sm.tsa.arma_generate_sample(ar, ma, length)
    return np.round(y + 100) // tick_size * tick_size

def add_gaussian_noise(ps, std=3.0):
    return ps + np.random.normal(0, std, len(ps))
