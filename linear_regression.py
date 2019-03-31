X = [[1, 1], [1, 2], [1, 3], [1, 4]]
Y = [3, 5, 7, 9]
theta = [1, 0]
alpha = 0.0001
a = 0
j = 1
while a < 1000:
    error_sum = 0
    print(theta[1])
    for i in range(len(X)):
        error_sum += (Y[i] - theta[0] - theta[1] * X[i][1]) * X[i][j]
    theta[j] = theta[j] + alpha * error_sum
    print(theta[j])
    a += 1


