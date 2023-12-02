

input_file = open('input.txt', 'r')
inputs = input_file.read().splitlines()
numbers = ['1','2','3','4','5','6','7','8','9','0']
calibration_numbers = []

for line in inputs:
    values = [x for x in list(line) if x in numbers]
    line_num = int(values[0] + values[-1])
    calibration_numbers.append(line_num)

calibration_sum = sum(calibration_numbers)

print(calibration_sum)




    