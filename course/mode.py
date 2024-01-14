def find_mode_of_intervals(X):
    # Step 1: Initialize I as the intersection of all intervals in X
    I = set.intersection(*[set(x) for x in X])

    # Step 2: Check if I is not empty
    if I:
        # Step 3: mode X <- I
        mode_X = I
        # Step 4: L mu <- n
        mu = len(X)
    else:
        # Step 6: Combine all endpoints into array Y
        Y = sorted([y for interval in X for y in interval])
        print("Y = ", Y)

        # Step 8: Create intervals z_i
        Z = [(Y[i], Y[i + 1]) for i in range(0, len(Y) - 1)]
        print("Z = ", Z)

        # Step 9: Count overlapping intervals
        mu_i = [sum(1 for interval in X if z[0] >= interval[0] and z[1] <= interval[1]) for z in Z]
        print("mu_i = ", mu_i)
        # Step 10: Update mu
        mu = max(mu_i)

        # Step 11: Identify intervals with maximum count mu
        K = {i for i, count in enumerate(mu_i) if count == mu}
        for k in K:
            print(Z[k])
        # Step 12: mode X <- union of intervals z_k for k in K
        mode_X = set.union(*[set(Z[k]) for k in K])

    return mode_X, mu


X = [(0.98774,1.012),(1.0007,0.99935),
     (0.99622, 1.0037), (0.99564, 1.0043),
     (0.99109,1.0087),(0.96723,1.0027),
     (0.96715,1.0027)]

# X = [ (1,4), (5,9), (1.5, 4.5), (6, 9)]

mode_result, mu_result = find_mode_of_intervals(X)
print("Mode of X:", mode_result)
print("Frequency (mu):", mu_result)




# X = [[-43.845, -0.7172], [1.7427, 1.1414],
#      [3.5308, 5.4007], [2.3321, 4.4861],
#      [0.14995, 2.097], [-3.3556, 1.505], [-3.3659, 1.5069]]
# X = [[1, 4], [5, 9], [1.5, 4.5], [6, 9]]
data = []
for a in X:
    for b in a:
        data.append(b)
data = sorted(list(set(data)))
z = []
for i in range(len(data) - 1):
    z.append([data[i], data[i + 1]])
print(z)
index = []
for i in range(len(z)):
    count = 0
    for j in range(len(X)):
        if z[i][0] >= X[j][0] and z[i][1] <= X[j][1]:
            count += 1
    index.append(count)
print(index)

# print(find_mode([[1,4],[5,9], [1.5, 4.5], [6, 9]]))