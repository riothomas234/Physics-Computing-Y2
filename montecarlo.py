import random
import math





def generate_in_square():
    x = random.uniform(1, 2)
    y = random.uniform(0, 1)

    return x, y


def check_in_func(my_x,my_y):
    radius = 1/my_x

    if my_y <= radius :
        return 'y'
    else:
        return 'n'



N=10000

no_in_func = 0

for i in range(N):

    x, y = generate_in_square()
    check = check_in_func(x,y)

    if check =='y':
        no_in_func = no_in_func+1

ratio = no_in_func/N


print('predicted ln(2) = ', ratio)
print('actual ln(2) = ', math.log(2))
accuracy = (math.fabs(ratio-math.log(2))/math.log(2))*100
print(accuracy,'%')
