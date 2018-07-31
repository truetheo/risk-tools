#!python3
# option pricing with Balck-Scholes
import numpy as np
import scipy.stats as ss
import time
mu, sigma = 0, 1

# Black and Scholes


def d1(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))


def BlackScholes(type, S0, K, r, sigma, T):
    """Calculate option price

    This calculates 

    :param S0: spot price at time 0
    :param K: strike price
    :param r: conitnously compound risk free rate
    :param sigma: stock volatility per year
    :param T: time to maturity in trading years
    :return: option price
    """
    if type == "C":
        return S0 * ss.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * ss.norm.cdf(d2(S0, K, r, sigma, T))
    else:
        return K * np.exp(-r * T) * ss.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * ss.norm.cdf(-d1(S0, K, r, sigma, T))


"""
test unit
"""


def main(s, x, r, sigma, T):
    res = BlackScholes(s, x, r, sigma, T)
    print(res)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
