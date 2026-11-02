"""Предметы и инвентарь: пример композиции (HAS-A)."""


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Weapon(Item):
    def __init__(self, name, damage_bonus):
        super().__init__(name)  # Берём имя из родительского класса.
        self.damage_bonus = max(0, damage_bonus)

    def __str__(self):
        return f"{self.name} (+{self.damage_bonus} к атаке)"


class Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = max(0, heal_amount)

    def __str__(self):
        return f"{self.name} (лечение +{self.heal_amount} HP)"


class Inventory:
    def __init__(self):
        self.items = []  # В инвентаре хранится список объектов Item.

    def add_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Можно добавить только предмет Item")
        self.items.append(item)
        print(f"🎒 Получен предмет: {item}")

    def show(self):
        if not self.items:
            print("🎒 Инвентарь пуст")
            return
        for number, item in enumerate(self.items, start=1):
            print(f"{number}. {item}")

    def best_weapon(self):
        # Выбираем самое сильное оружие (если оно есть).
        weapons = [item for item in self.items if isinstance(item, Weapon)]
        return max(weapons, key=lambda item: item.damage_bonus, default=None)

    def use_potion(self, hero):
        # Находим первое зелье, лечим героя и удаляем использованный предмет.
        if not hero.is_alive():
            print("Нельзя лечить побеждённого героя")
            return False
        if hero.hp == hero.max_hp:
            print("Здоровье уже полное — зелье сохраним")
            return False
        for item in self.items:
            if isinstance(item, Potion):
                hero.heal(item.heal_amount)
                self.items.remove(item)
                return True
        print("В инвентаре нет зелий")
        return False
