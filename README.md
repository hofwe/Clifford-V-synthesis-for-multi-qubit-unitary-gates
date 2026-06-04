# Clifford-V-synthesis-for-multi-qubit-unitary-gates


# Figure 1

fig1/dist_mat2.txt ... √2*(CME distance) between Haar randomly generated 1000 SU(2)s.

fig1/dist_mat4.txt ... √2*(CME distance) between Haar randomly generated 1000 SU(4)s.

fig1/dist_mat2.txt ... √2*(ACME distance) between Haar randomly generated 1000 SU(2)s.

fig1/dist_mat4.txt ... √2*(ACME distance) between Haar randomly generated 1000 SU(4)s.

# Figure 3
Each file has the result of a test calculation in each row. Each column is constructed as follows.
```
error(epsilon) V-count
```

fig3/rev_result_CC_V.txt ... CC_V

fig3/rev_result_V.txt ... V

# Figure 4
Each file has the result of a test calculation in each row. Each column is constructed as follows.
```
error(epsilon) V-count
```

fig4/SU4_100_res.txt ... SU(4) by Meet-in-the-Middle Exhaustive Search

fig4/SU4_C100_res.txt ... Generalized controlled gate by Meet-in-the-Middle Exhaustive Search

fig4/SU4_C100_sgg_res.txt ... Generalized controlled gate by Subgroup Guided Search + SU(2)

fig4/SU4_IDC100_res.txt ... Controlled gate by Meet-in-the-Middle Exhaustive Search

fig4/SU2_100_sgg_res.txt ... Controlled gate by Subgroup Guided Search + SU(2)
