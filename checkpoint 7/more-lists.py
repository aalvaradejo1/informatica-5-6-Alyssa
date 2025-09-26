#lists with strings
# names = ["Bob", "Alex", "Kevin"]
# names.append("Joseph")

# for name in sorted(names):
#     print(name)

#Lists with floats
# measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
# mean = sum(measurements) / len(measurements)
# print("The mean is: ", mean)

#List within list
# super_list = [[5,2,3], [4,1], [2,2,5,1]]
# print(super_list[1][0])

# grades = [["Shakira", 8, "D"],["Melissa", 0, "C"], ["Shensi", 10, "A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} from {group} got a {grade}.")

#Matrices
matrix = [[1,2,3], [4,5,6], [7,8,9]]
length_row = len(matrix)
length_column = len(matrix[0])

for column_index in range(length_column):
    new_matrix = []
    for row_index in range(length_row):
        new_matrix.append(matrix[row_index][column_index])

    print(new_matrix)
