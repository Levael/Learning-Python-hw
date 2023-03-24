# exit code 0: everything ok
# exit code 1: incorrect input
# exit code 2: input number doesn't match it's base

try:
    input_base = int(input("The base of the number: "))
    input_number = float(input("The number itself: "))
except:
    print("Incorrect input")
    exit(1)

output_base = 10

is_float = bool(float(input_number) - int(input_number))
int_part_len = len(str(int(float(input_number)))) + int(is_float)   # 1 if float, 0 if int
fract_part_len = (len(str(input_number)) - int_part_len) - 2*(int(not is_float))   # - .0
interim_num = int(float(input_number) * (output_base**fract_part_len))   # no point int -> change base

try:
    output_number = int(str(interim_num), int(input_base)) / (int(input_base)**fract_part_len)
except:
    print(input_number, " is not in base ", input_base)
    exit(2)

print("output_number: ", output_number)
