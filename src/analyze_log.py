import csv


def importer_csv(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file) as file:
            return format_file(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def format_file(file):
    requests = dict()

    for i in csv.reader(file):
        name, food, day = i[0], i[1], i[2]
        if name not in requests.keys():
            requests[name] = {food: {day: 1}}
        elif food not in requests[name].keys():
            requests[name][food] = {day: 1}
        elif day not in requests[name][food].keys():
            requests[name][food][day] = 1
        else:
            requests[name][food][day] += 1

    return requests


def most_requested_dish_by_maria(path_to_file):
    requests = importer_csv(path_to_file)

    frequency = {}

    for i in requests['maria'].keys():
        for j in requests['maria'][i]:
            frequency[i] = requests['maria'][i][j]

    return max(frequency, key=frequency.get)


def how_many_hamburgers_did_arnaldo_order(path_to_file):
    requests = importer_csv(path_to_file)

    hamburgers = 0

    for i in requests['arnaldo']['hamburguer']:
        hamburgers += requests['arnaldo']['hamburguer'][i]

    return hamburgers


def how_many_dishes_did_joao_ever_order(path_to_file):
    requests = importer_csv(path_to_file)

    all_foods = set()
    foods_joao = set()

    for i in requests:
        for j in requests[i]:
            all_foods.add(j)

    for foods in requests['joao']:
        foods_joao.add(foods)

    return all_foods - foods_joao


def all_days(requests):
    all_days = set()

    for name in requests:
        for food in requests[name]:
            for days in requests[name][food]:
                all_days.add(days)

    return all_days


def days_off_joao(path_to_file):
    requests = importer_csv(path_to_file)

    days_joao = set()

    for food in requests['joao']:
        for days in requests['joao'][food]:
            days_joao.add(days)

    return all_days(requests) - days_joao


def analyze_log(path_to_file):
    a = most_requested_dish_by_maria(path_to_file)
    b = how_many_hamburgers_did_arnaldo_order(path_to_file)
    c = how_many_dishes_did_joao_ever_order(path_to_file)
    d = days_off_joao(path_to_file)

    resposta = f'{a}\n{b}\n{c}\n{d}'
    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(resposta)


if __name__ == '__main__':
    print(analyze_log('data/orders_1.csv'))
