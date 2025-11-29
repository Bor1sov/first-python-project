class BacteriaProducer:
    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.now_individual = 0

    def create_new(self):
        if (self.now_individual < self.max_bacteria):
            self.now_individual = self.now_individual + 1
            print(f'Добавлена одна бактерия. Количество \
бактерий в популяции: {self.now_individual}')
        else:
            print('Нет места под новую бактерию')

    def remove_one(self):
        if (self.now_individual > 0):
            self.now_individual = self.now_individual - 1
            print(f'Одна бактерия удалена. \
Количество бактерий в популяции: {self.now_individual}')
        else:
            print('В популяции нет бактерий, удалять нечего')


bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
