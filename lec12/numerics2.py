def newton_division(R, b, initial, delta=1):
    result = 2 * initial - b * initial**2 / R
    while True:
        previous = result
        result = 2 * result - b * result**2 / R
        if abs(previous - result) < delta:
            break
    return result


print(newton_division(65536, 5, 16384))
