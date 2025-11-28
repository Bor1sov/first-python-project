class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


employee1 = Employee(first_name='Robert', second_name='Kruzo', gender='M')
employee2 = Employee(first_name='Darya', second_name='Melihan', gender='F')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name},\
 Пол: {employee1.gender}, Отпускных дней в году:\
 {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name},\
 Пол: {employee2.gender}, Отпускных дней в году:\
 {employee2.vacation_days}.')
