# w_str = "1,2,3,boom,5,6,7,8,boom,0,1,2,3,boom,5"

try:
    w_str = input("Insert game list:\n")
    temp_index = w_str.index(',')
except:
    # in case of non-logical input
    print("Incorrect input")
    exit(1)

n_str = w_str.replace('boom', 'x')

odd_steps = n_str[0::4]
even_steps = n_str[2::4]
boom_steps = n_str[7*2-2::7*2]    # 7-th places; *2 because of comas; -2 because of str start

number_of_comas = len(n_str) // 2
number_of_sevens = (len(n_str) - number_of_comas) // 7
a_booms = boom_steps[0::2]
b_booms = boom_steps[1::2]

a_faults = ( odd_steps.count('x') - a_booms.count('x')) + (len(a_booms) - a_booms.count('x'))
b_faults = (even_steps.count('x') - b_booms.count('x')) + (len(b_booms) - b_booms.count('x'))

print('Alis faults:', a_faults)
print('Bob faults:', b_faults)
