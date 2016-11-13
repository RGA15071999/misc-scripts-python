__author__ = 'Robert Gevorgyan'


def scale(input_list):
    mean = float(sum(input_list))/len(input_list)
    difference = max(input_list) - min(input_list)
    for i in range(0, len(input_list)):
        input_list[i] = (input_list[i] - mean)/difference

x = [6, 10, 5, 4]
scale(x)
print x

