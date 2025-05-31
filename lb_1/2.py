total_cost = 0.0

try:
    with open('prices.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                try:
                    quantity = int(parts[1])
                    price = float(parts[2])
                    total_cost += quantity * price
                except ValueError:
                    continue
except FileNotFoundError:
    pass

print(f"{total_cost:.2f}")