from matplotlib import pyplot as plt
import numpy as np

# 正解との比較
for n in range(1, 3):
    D = 1 << n
    file = "dist_mat" + str(D) + ".txt"
    my_file = "my_dist_mat" + str(D) + ".txt"
    data = np.loadtxt(file)
    my_data = np.loadtxt(my_file)
    my_data = np.minimum(my_data, my_data.T)
    mask = data>0.25
    x = (my_data[mask]/data[mask]).reshape(-1)
    weights = np.ones_like(data[mask]) / len(data[mask])
    print("n:", n)
    print("num:", len(x))
    print("std:", np.std(x))
    print("log std:", np.std(np.log(x)))
    print("max:", np.max(x))
    print("reverse:", np.sum(np.abs(np.argsort(data, axis=0) - np.argsort(my_data, axis=0)))/(1000*999*998))
    plt.hist(x, bins=50, weights=weights)
    plt.xlabel(r'$\left.{\|U-V\|_\mathrm{ACME}}\right/{\|U-V\|_\mathrm{CME}}$')
    plt.ylabel('proportion')
    plt.show()