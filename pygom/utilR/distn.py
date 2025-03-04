"""
    .. moduleauthor:: Edwin Tye <Edwin.Tye@phe.gov.uk>

    Functions of distributions that replicate those in R.
    See the R online documentation for each of the functions
    with matching names, i.e. dgamma, pgamma and rgamma
    can be found at
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html

"""

import scipy.stats as st
import numpy as np
from scipy.special import gammaln

###############################################################
#
# Continuous distribution
#
###############################################################

##### exponential distribution

def dexp(x, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    if log:
        return st.expon.logpdf(x, scale=1.0/rate)
    else:
        return st.expon.pdf(x, scale=1.0/rate)

def pexp(q, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    if log:
        return st.expon.logcdf(q, scale=1.0/rate)
    else:
        return st.expon.cdf(q, scale=1.0/rate)

def qexp(p, rate=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html
    '''
    return st.expon.ppf(p, scale=1.0/rate)

def rexp(n, rate=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Exponential.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.exponential
    else:
        rvs = test_seed(seed).exponential

    if n > 1:
        return rvs(scale=1.0/rate, size=n)
    else:
        return rvs(scale=1.0/rate, size=n)[0]


##### gamma distribution

def dgamma(x, shape, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    if log:
        return st.gamma.logpdf(x, a=shape, scale=1.0/rate)
    else:
        return st.gamma.pdf(x, a=shape, scale=1.0/rate)

def gamma_mu_shape(x, mu, shape, log=False):
    '''
    The probability density function (pdf) of gamma distrbution in terms of mean and shape.

    Parameters
    ----------
    x: array like observation.
    mu: mean or prediction.
    shape: shape (a in latex equation below).
    log: if True the natural log of the pmf is given.
    See: Bolker, B. M. (2008). Gamma. In Ecological Models in R (pp. 131–133).
         Princeton University Press.
         Jupyter notebook titled "Loss function Calculations.ipnyb"


    Returns
    -------
    pdf, :math:
        `\\mathcal\\{p}(x; \\mu,a) = \\exp(- a \\ln{\\left(\\frac{\\mu}{a} \\right)} - \\frac{a x}{\\mu} + \\left(a - 1\\right) \\ln{\\left(x \\right)} - \\ln{\\left(\\Gamma\\left(a\\right) \\right)})`

    '''
    logpdf_p1 = -gammaln(shape)
    logpdf_p2 = (shape - 1)*np.log(x)
    logpdf_p3 = -shape*np.log(mu/shape)
    logpdf_p4 = -shape*x/mu
    logpdf = logpdf_p1+logpdf_p2+logpdf_p3+logpdf_p4
    if log:
        ans = logpdf
    else:
        ans = np.exp(logpdf)
    return ans

def pgamma(q, shape, rate=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    if log:
        return st.gamma.logcdf(q, a=shape, scale=1.0/rate)
    else:
        return st.gamma.cdf(q, a=shape, scale=1.0/rate)

def qgamma(q, shape, rate=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html
    '''
    return st.gamma.ppf(q, a=shape, scale=1.0/rate)

def rgamma(n, shape, rate=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/GammaDist.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.gamma
    else:
        rvs = test_seed(seed).gamma

    if n > 1:
        return rvs(shape, scale=1.0/rate, size=n)
    else:
        return rvs(shape, scale=1.0/rate, size=n)[0]

##### normal distribution

def dnorm(x, mean=0, sd=1, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    if log:
        return st.norm.logpdf(x, loc=mean, scale=sd)
    else:
        return st.norm.pdf(x, loc=mean, scale=sd)

def pnorm(q, mean=0, sd=1, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    if log:
        return st.norm.logcdf(q, loc=mean, scale=sd)
    else:
        return st.norm.cdf(q, loc=mean, scale=sd)

def qnorm(p, mean=0, sd=1):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html
    '''
    return st.norm.ppf(p, loc=mean, scale=sd)
    
def rnorm(n, mean=0, sd=1, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Normal.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used.  If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.normal
    else:
        rvs = test_seed(seed).normal

    if n > 1:
        return rvs(loc=mean, scale=sd, size=n)
    else:
        return rvs(loc=mean, scale=sd, size=n)[0]

##### Chi-squared distribution

def dchisq(x, df, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    if log:
        return st.chi2.logpdf(x, df=df)
    else:
        return st.norm.pdf(x, df=df)

def pchisq(x, df, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    if log:
        return st.chi2.logpdf(x, df=df)
    else:
        return st.chi2.pdf(x, df=df)

def qchisq(p, df):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    '''
    return st.chi2.ppf(p, df=df)

def rchisq(n, df, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.chisquare
    else:
        rvs = test_seed(seed).chisquare

    if n > 1:
        return rvs(df=df, size=n)
    else:
        return rvs(df=df, size=n)[0]

##### Uniform distribution

def dunif(x, min=0.0, max=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    if log:
        return st.uniform.logpdf(x, loc=min, scale=max-min)
    else:
        return st.uniform.pdf(x, loc=min, scale=max-min)

def punif(q, min=0.0, max=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    if log:
        return st.uniform.logcdf(q, loc=min, scale=max-min)
    else:
        return st.uniform.cdf(q, loc=min, scale=max-min)

def qunif(p, min=0.0, max=1.0):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html
    '''
    return st.uniform.ppf(p, loc=min, scale=max-min)

def runif(n, min=0.0, max=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Uniform.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.uniform
    else:
        rvs = test_seed(seed).uniform

    if seed:
        if n > 1:
            return st.uniform.rvs(loc=min, scale=max-min, size=n)
        else:
            return st.uniform.rvs(loc=min, scale=max-min, size=n)[0]
    else:
        if n > 1:
            return rvs(low=min, high=max, size=n)
        else:
            return rvs(low=min, high=max, size=n)[0]
        
##### beta distribution
# To do: write these in the same format as above with seeds
def dbeta(x, shape1, shape2, log=False):
    """
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Beta.html
    """
    return st.beta.pdf(x, shape1, shape2)

def rbeta(n, shape1, shape2, seed=None):
    """
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Beta.html
    """
    return st.beta.rvs(shape1, shape2, size=n)

def qbeta(p, shape1, shape2):
    """
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Beta.html
    """
    return st.beta.ppf(p, shape1, shape2)

##### multivariate normal distribution
def dmvnorm(x, mean=None, sigma=None):
    """
    See
    https://www.rdocumentation.org/packages/mvtnorm/versions/1.0-12/topics/mvnorm
    """
    if mean is None:
        mean = np.repeat(0, len(x))
    if sigma is None:
        sigma = np.identity(len(x))
    return st.multivariate_normal.pdf(x, mean=mean, cov=sigma)

def rmvnorm(n, mean, sigma, seed=None):
    '''
    See
    https://www.rdocumentation.org/packages/mvtnorm/versions/1.0-12/topics/mvnorm
    '''
    return st.multivariate_normal.rvs(mean=mean, cov=sigma, size=n)

###############################################################
#
# Discrete distribution
#
###############################################################

##### Poisson distribution

def dpois(x, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    if log:
        return st.poisson.logpmf(x, mu=mu)
    else:
        return st.poisson.pmf(x, mu=mu)

def ppois(q, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    if log:
        return st.poisson.logcdf(q, mu=mu)
    else:
        return st.poisson.cdf(q, mu=mu)

def qpois(q, mu=1.0, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html
    '''
    return st.poisson.ppf(q, mu=mu)

def rpois(n, mu=1.0, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Poisson.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.poisson
    else:
        rvs = test_seed(seed).poisson

    if n > 1:
        return rvs(mu, size=n)
    else:
        return rvs(mu, size=n)[0]

##### Binomial distribution

def dbinom(x, size, prob, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    if log:
        return st.binom.logpmf(x, n=size, p=prob)
    else:
        return st.binom.pmf(x, n=size, p=prob)

def pbinom(q, size, prob, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    if log:
        return st.binom.logcdf(q, n=size, p=prob)
    else:
        return st.binom.cdf(q, n=size, p=prob)

def qbinom(q, size, prob):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html
    '''
    return st.binom.ppf(q, n=size, p=prob)

def rbinom(n, size, prob, seed=None):
    '''
    See
    https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Binomial.html

    @param seed represent which type of seed to use.  None or False uses the
    default seed.  When seed is an integer number, it will reset the seed
    via numpy.random.seed.  When seed=True, then a
    :class:`numpy.random.RandomState` object will be used. If seed is an
    object of :class:`numpy.random.RandomState` then it will be used directly
    '''
    if seed is None:
        rvs = np.random.binomial
    else:
        rvs = test_seed(seed).binomial

    if n > 1:
        return rvs(n=size, p=prob, size=n)
    else:
        return rvs(n=size, p=prob, size=n)[0]
    
##### Negitive binomial
def pnbinom(q, size, prob, mu, lower_tail=True, log=True):
    '''
    See
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/NegBinomial.html
    '''

def qnbinom(p, size, prob, mu, lower_tail=True, log=True):
    '''
    See
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/NegBinomial.html
    '''

##### Negative Binomial distribution
def nb2pmf(x, mu, k, log=False):
    '''
    The probability mass function (pmf) of Negative Binomial 2 distribution.
    This definition of the negative binomial distribution is often refered to as
    negative binomial 2, or the ecological parameterisation. This parameterisation
    takes the mean and k (an overdispersion parameter). The variance = mean(1+mean/k),
    some notation uses alpha (k=1/alpha).
    See: Bolker, B. M. (2008). Negative Binomial. In Ecological Models in R (pp. 124–126).
         Princeton University Press.
         Jupyter notebook titled "Loss function Calculations.ipnyb"

    Parameters
    ----------
    x: array like observation.
    mu: mean or prediction.
    k: overdispersion parameter (variance = mean(1+mean/k)). Note some notation
       uses $\alpha$, ($k=\alpha^{-1}$).
    log: if True the natural log of the pmf is given.
    See:
        Bolker, B. M. (2008). Negative Binomial. In Ecological Models in R (pp. 124–126).
        Princeton University Press.
        File "Loss function Calculations.ipnyb"

    Returns
    -------
    log pmf:
    math:`\\mathcal\\p(x; \\mu,k)) = \\exp(\\ln(\\frac{\\Gamma \\left(k+x\\right)}{\\Gamma \\left(k\\right)x!}(\\frac{k}{k+\\mu})^{k}(\\frac{\\mu}{k+\\mu})^{x}))`

    '''
    logpmf_p1 = -gammaln(x+1)
    logpmf_p2 = -gammaln(k)
    logpmf_p3 = k*(np.log(k) - np.log(k + mu))
    logpmf_p4 = x*(np.log(mu) - np.log(k + mu))
    logpmf_p5 = gammaln(k+x)
    logpmf = logpmf_p1+logpmf_p2+logpmf_p3+logpmf_p4+logpmf_p5
    if log:
        ans = logpmf
    else:
        ans = np.exp(logpmf)
    return ans

def dnbinom(x, size, prob=None, mu=None, log=False):
    '''
    See
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/NegBinomial.html
    '''
    if mu is None and prob is None:
        raise Exception("Neither 'prob' or 'mu' were specified")

    if mu is not None:
        if prob is not None:
            raise Exception("'prob' and 'mu' both specified")
        if log:
            ans = nb2pmf(x=x, mu=mu, k=size, log=True)
        else:
            ans = nb2pmf(x=x, mu=mu, k=size, log=False)

    else:
        if log:
            ans = st.nbinom.logpmf(x, n=size, p=prob)
        else:
            ans = st.nbinom.pmf(x, n=size, p=prob)

    return ans

def test_seed(seed):
    '''
    Test the input type of `seed` and return a new random generator if
    appropriate.

    Parameters
    ----------
    seed:
        If True, then a new :class:`numpy.random.RandomState` will be created.
        If False, then a :class:`numpy.random.RandomState` with the current
        global state of the random number generator is returned.
        If it is an int, then the input seed is used to create a new
        random state.
        If it is already a :class:`numpy.random.RandomState` object then
        the same object is returned.

    Returns
    -------
    :class:`numpy.random.RandomState`
    '''
    if seed is True:
        return np.random.RandomState()
    elif isinstance(seed, np.random.RandomState):
        return seed
    elif isinstance(seed, int):
        return np.random.RandomState(seed)
    elif seed is False:
        state = np.random.get_state()
        rvs = np.random.RandomState()
        rvs.set_state(state)
        return rvs
    else:
        raise RuntimeError("seed must be (bool, int or np.random.RandomState")
