grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def srednyi_ball(name, marks):
    name = sorted(name)
    temp_mark = []
    total_dict = {}

    for i in range(len(name)):
         temp_mark = sum(marks[i]) / len(marks[i])
         total_dict.update({name[i]: round(temp_mark, 2)})

    return total_dict 


print(srednyi_ball(students, grades))
