# Let's check our computations through code!
from scipy import stats
import numpy as np
# let's check our work with scipy
num_of_genre = np.array([4, 3, 1, 1, 5, 1])        # PUT THE DATA HERE
len_num_of_genre = len(num_of_genre)
std = np.std(num_of_genre, ddof=1)
mean = np.mean(num_of_genre)
# print(len_num_of_genre, mean, std)
t, pval = stats.ttest_1samp(num_of_genre, 4)
pval /= 2      # p-value = the probablity that this sample comes from this distribution
print("t:", t, "pval", pval)
alpha = 0.01
if alpha < pval:
    print("reject H0")
else: 
    print("do not reject H0")