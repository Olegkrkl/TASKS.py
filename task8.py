def count_password_combinations(m, n):
    
    combinations = n ** m
    return combinations

m = 4
n = 25

total_combinations = count_password_combinations(m, n)
print("Кількість можливих комбінацій пароля: ", total_combinations)