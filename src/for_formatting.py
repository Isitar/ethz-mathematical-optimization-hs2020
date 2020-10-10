def pivot(T, i, j):
	rhsIndex = T.shape[1] - 1

	if (0 == i  # objective function row
			or j == rhsIndex  # rhs
	):
		print("[Error] Given indices are not pointing at a potential pivot.")
		return T

	if (0 == T[i, j]):  # Check if the indicated pivot is zero
		print("[Error] Given pivot is zero, step cannot be performed.")
		return T

	def quotient(row):
		return T[row, rhsIndex] / T[row, j]

	# check quotient rule
	isMinQuotient = True
	chosenQutient = quotient(i)
	for row in range(T.shape[0]):
		if (T[row, j] <= 0):
			continue
		if (quotient(row) < chosenQutient):
			isMinQuotient = False
			break

	if (T[0, j] < 0 and isMinQuotient):  # Check if indicated pivot is legal for phase II of Simplex Method
		print("[Info] Given pivot is legal.")
	else:
		print("[Warning] Given pivot is illegal.")

	# Implement pivoting step here
	T_pivoted = np.copy(T)

	for row in range(T_pivoted.shape[0]):
		for col in range(T_pivoted.shape[1]):
			# pivot element
			if (i == row and j == col):
				T_pivoted[row, col] = 1 / T[i, j]
			# pivot col
			elif (j == col):
				T_pivoted[row, col] = -T[row, col] / T[i, j]
			# pivot row
			elif (i == row):
				T_pivoted[row, col] = T[row, col] / T[i, j]
			# other elements
			else:
				T_pivoted[row, col] = T[row, col] - (T[row, j] * T[i, col]) / T[i, j]

	return T_pivoted
