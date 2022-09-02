from math import sqrt


def calculate_correlation(set_x, set_y):
    # The sum of all the values in each dataset
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    # The sum of all squared values in each dataset
    sum_x2 = sum([x ** 2 for x in set_x])

    sum_y2 = 0
    for y in set_y:
        sum_y2 += y ** 2

    # The sum of the product of each respective element
    # in each dataset.
    sum_xy = 0

    for i in range(len(set_x)):
        sum_xy += set_x[i] * set_y[i]

    # The length of the dataset
    n = len(set_x)

    # Calculate the correlation of the coefficient
    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) *
                       (n * sum_y2 - sum_y ** 2))

    return numerator / denominator
