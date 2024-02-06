from collections import Counter

def greedy_algorithm_unlim(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    index = 0
    while(budget > 0 and index < len(sorted_items)):
        key, val = sorted_items[index]
        if val["cost"] <= budget:
            budget -= val["cost"]
            selected_items.append(key)
        else:
            index += 1

    return dict(Counter(selected_items))


def greedy_algorithm(items, budget):
    total_cost = 0
    total_calories = 0
    selected_items = []
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    for key, val in sorted_items:
        if total_cost + val["cost"] <= budget:
            selected_items.append(key)
            total_cost += val["cost"]
            total_calories += val["calories"]
    
    return selected_items


def dynamic_algorithm_unlim(items, budget):
    max_values = [0] * (budget + 1)
    selected_items = [None] * (budget + 1)
    for b in range(1, budget + 1):
        for item_name, item_attributes in items.items():
            if item_attributes['cost'] <= b:
                value_with_item = max_values[b - item_attributes['cost']] + item_attributes["calories"]
                if value_with_item > max_values[b]:
                    max_values[b] = value_with_item
                    selected_items[b] = item_name
    
    result = []
    remaining_budget = budget
    while remaining_budget > 0 and selected_items[remaining_budget] is not None:
        last_item = selected_items[remaining_budget]
        item_attributes = items[last_item]
        result.append(last_item)
        remaining_budget -= item_attributes['cost']
    
    return dict(Counter(result))


def dynamic_algorithm(items, budget):
    max_values = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    selected_items = [[None] * (budget + 1) for _ in range(len(items) + 1)]
    for i, (item_name, item_attributes) in enumerate(items.items(), start=1):
        for b in range(1, budget + 1):
            if item_attributes['cost'] <= b:
                value_with_item = max_values[i - 1][b - item_attributes['cost']] + item_attributes["calories"]                
                if value_with_item > max_values[i - 1][b]:
                    max_values[i][b] = value_with_item
                    selected_items[i][b] = item_name
                else:
                    max_values[i][b] = max_values[i - 1][b]
                    selected_items[i][b] = selected_items[i - 1][b]
            else:
                max_values[i][b] = max_values[i - 1][b]
                selected_items[i][b] = selected_items[i - 1][b]
    result = []
    remaining_budget = budget
    for i in range(len(items), 0, -1):
        if selected_items[i][remaining_budget] is not None:
            item_name = selected_items[i][remaining_budget]
            item_attributes = items[item_name]
            result.append(item_name)
            remaining_budget -= item_attributes['cost']
    
    return result

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    print("Жадібний алг., який може вибирати страви безліч кількість разів: ", greedy_algorithm_unlim(items, 100))
    print("Жадібний алг., який може вибирати страви лише 1 раз: ", greedy_algorithm(items, 100))

    print("Динамічний алг., який може вибирати страви безліч кількість разів: ", dynamic_algorithm_unlim(items, 100))
    print("Динамічний алг., який може вибирати страви лише 1 раз: ", dynamic_algorithm(items, 100))

