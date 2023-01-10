class TrackOrders:
    def __init__(self):
        self.orders = list()
        self.days = dict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        if day not in self.days:
            self.days[day] = 1
        else:
            self.days[day] += 1

#    def get_most_ordered_dish_per_customer(self, customer):
#        frequency = {}
#
#        for i in self.orders:
#            if i[0] == customer:
#                if i[1] not in frequency:
#                    frequency[i[1]] = 1
#                else:
#                    frequency[i[1]] += 1
#
#        return max(frequency, key=frequency.get)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

# if __name__ == '__main__':
#     csv_parsed = [
#     ["maria", "pizza", "terça-feira"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["joao", "hamburguer", "terça-feira"],
#     ["maria", "coxinha", "segunda-feira"],
#     ["arnaldo", "misto-quente", "terça-feira"],
#     ["jose", "hamburguer", "sabado"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["joao", "hamburguer", "terça-feira"],
# ]
#     track_orders = TrackOrders()
#     for name, food, day in csv_parsed:
#         track_orders.add_new_order(name, food, day)
#     print(track_orders.get_most_ordered_dish_per_customer('maria'))
