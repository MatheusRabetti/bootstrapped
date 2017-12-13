from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import numpy as np
import bootstrapped.bootstrap as bs
import bootstrapped.compare_functions as bs_compare
import bootstrapped.stats_functions as bs_stats
import scipy.sparse as sparse
import scipy.stats as st


mean = 100
stdev = 10

samples = np.random.normal(loc=mean, scale=stdev, size=5000)
samples_t = np.random.normal(loc=mean, scale=stdev, size=5000)

bsr = bs.bootstrap(samples, bs_stats.mean)
print(bsr)

bsr2 = bs.bootstrap(samples, bs_stats.mean, method = "pi")
print("pi:")
print(bsr2)

bsr3 = bs.bootstrap(samples, bs_stats.trimmed_mean)
print("trimmed mean:")
print(bsr3)

bsr4 = bs.bootstrap_ab(samples, samples_t, bs_stats.trimmed_mean, bs_compare.percent_change)
print("ab:")
print(bsr4)

bsr5 = bs.bootstrap_ab(samples, samples_t, bs_stats.trimmed_mean, bs_compare.percent_change, method ="pi")
print("ab pi:")
print(bsr5)

