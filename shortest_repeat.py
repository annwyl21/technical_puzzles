#Shortest repeat of 'a' or 'b'
#replace the ?'s then count the repeats and return the min possible length of the longest repeat
#Given S = "aa??bbb", your function should return 3
#Given S = "a?b?aa?b?a", your function should return 2. Question marks can be replaced in the following way: "aabbaabbaa".
#Given S = "??b??", your function should return 1.
#Given S = "aa?b?aa", your function should return 3.

def shortest_repeat(string_of_letters):
    max_count = 0
    count = 1
    for letter in string_of_letters:
        index = string_of_letters.find(letter)
        if letter == letter[index+1]:
            count +=1
            if max_count < count:
                max_count = count
        else:
            count = 1
    return max_count

print(shortest_repeat("aa?b?aa"))