# Let's check our computations through code!
from scipy import stats
import numpy as np
# let's check our work with scipy

# Jaylene stats: 
# [4, 3, 1, 3, 1, 1, 2]
# ["pop", "alternative", "electro pop", "dance pop", "country", "indie", "rap pop"]

# Carson stats:
# [4, 3, 1, 1, 5, 1]
# ["4rap", "3hiphop", "1alternative", "1rock", "5pop", "1alternative pop rock"]

# Merged Data Stats:
# ["pop", "alternative", "electro pop", "dance pop", "country" "indie", "rap pop", "rap", "hip hop", "rock" "alternative pop rock"]
# [9, 4, 1, 3, 1, 1, 2, 4, 3, 1, 1]

num_of_genre = np.array([9, 4, 1, 3, 1, 1, 2, 4, 3, 1, 1])
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