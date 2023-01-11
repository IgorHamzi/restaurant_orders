class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        frequency = {}

        for i in self.orders:
            if i[0] == customer:
                if i[1] not in frequency:
                    frequency[i[1]] = 1
                else:
                    frequency[i[1]] += 1

        return max(frequency, key=frequency.get)

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set()
        dishes_customer = set()

        for i in self.orders:
            all_dishes.add(i[1])
            if i[0] == customer:
                dishes_customer.add(i[1])

        return all_dishes - dishes_customer

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        days_customer = set()

        for i in self.orders:
            all_days.add(i[2])
            if i[0] == customer:
                days_customer.add(i[2])

        return all_days - days_customer

    def get_busiest_day(self):
        frequency = {}

        for i in self.orders:
            if i[2] not in frequency:
                frequency[i[2]] = 1
            else:
                frequency[i[2]] += 1

        return max(frequency, key=frequency.get)

    def get_least_busy_day(self):
        frequency = {}

        for i in self.orders:
            if i[2] not in frequency:
                frequency[i[2]] = 1
            else:
                frequency[i[2]] += 1

        return min(frequency, key=frequency.get)
