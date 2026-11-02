import random
import time
from functools import wraps

items = [
    {"name": "Деревянный меч", "rarity": "common", "power": 10},
    {"name": "Ржавый кинжал", "rarity": "common", "power": 15},
    {"name": "Железный топор", "rarity": "uncommon", "power": 35},
    {"name": "Щит стражника", "rarity": "uncommon", "power": 40},
    {"name": "Клинок Тьмы", "rarity": "rare", "power": 85},
    {"name": "Кольцо Огня", "rarity": "rare", "power": 70},
    {"name": "Молот Повелителя Бурь", "rarity": "legendary", "power": 150},
    {"name": "Посох Бездны", "rarity": "legendary", "power": 130},
    {"name": "Зелье лечения", "rarity": "common", "power": 5},
]

rare_and_legendary = list(filter(lambda x: x["rarity"] in ["rare", "legendary"], items))
top_5_items = sorted(items, key=lambda x: x["power"], reverse=True)[:5]
top_5_names = [item["name"] for item in top_5_items]

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Выполняется действие: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[TIMER] Функция {func.__name__} выполнена за {end_time - start_time:.6f} сек.")
        return result
    return wrapper

@log_action
@timer
def attack(hero, target, damage):
    print(f"⚔️ {hero} атакует {target} и наносит {damage} урона!")
    return damage

def loot_generator(items_list):
    while True:
        yield random.choice(items_list)

if __name__ == "__main__":
    print("=== 1. РЕДКИЕ И ЛЕГЕНДАРНЫЕ ПРЕДМЕТЫ ===")
    for item in rare_and_legendary:
        print(f"- {item['name']} ({item['rarity']}): {item['power']} силы")

    print("\n=== 2. ТОП-5 САМЫХ СИЛЬНЫХ ПРЕДМЕТОВ ===")
    print("Названия:", top_5_names)

    print("\n=== 3. ВЫПАДЕНИЕ ЛУТА (ПЕРВЫЕ 10 РЕЗУЛЬТАТОВ) ===")
    loot_gen = loot_generator(items)
    for i in range(1, 11):
        dropped = next(loot_gen)
        print(f"Лут #{i}: {dropped['name']} [{dropped['rarity']}]")

    print("\n=== 4. ЛОГИРОВАНИЕ И ТАЙМЕР БОЯ ===")
    attack("Воин", "Дракон", 120)
