candies = [1,3,7,9]
number_of_kids = len(candies)
extra_candies = input("Enter the extra candies")

def greates_number_of_candies(list :candies):
    max_candies = max(candies)
    result = []
    for i in range(len(candies)):
        result.append(candies[i] + extra_candies>= max_candies)
    return result

print(greates_number_of_candies(candies))