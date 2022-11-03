#Codility Puzzle
#Return largest product from 3 numbers in an array

my_array = [-4, -4, 2, 8]

#multiplies all the numbers together and finds that multiplying the largest number, 8
#by itself 3 times achieves the largest product 512
def maximum_product_of_three(my_array):
    max_product = 0
    for x in range(len(my_array)):
        for y in range(len(my_array)):
            for z in range(len(my_array)):
                number = my_array[x] * my_array[y] * my_array[z]
                if number > max_product:
                    max_product = number
    return max_product

print(maximum_product_of_three(my_array))

#sorts the array to define the 3 largest numbers then multiplies them to achieve 128
def max_product_of_three(my_array):
    #print(my_array)
    new_array = []
    for num in my_array:
        new_array.append(abs(num))
    new_array.sort(reverse=True)
    #print(my_array)
    max_prod=new_array[0] * new_array[1] * new_array[2]
    return max_prod

print(max_product_of_three(my_array)) 
