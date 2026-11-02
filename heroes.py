"""Базовый герой и классы: Warrior, Mage, Rogue, Paladin. Домашнее задание «Легендарная команда»."""
import random

from items import Inventory


class Hero:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.max_hp = max(1, hp)
        self._hp = self.max_hp  # Внутреннее поле: не меняем напрямую снаружи.
        self.attack_power = max(0, attack_power)
        self.defense = max(0, defense)
        self.inventory = Inventory()  # КОМПОЗИЦИЯ: герой ИМЕЕТ инвентарь.

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(self.max_hp, value))

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        # Защита уменьшает урон; хотя бы 1 HP снимается при попадании.
        damage = max(1, amount - self.defense)
        self.hp -= damage
        print(f"💥 {self.name} получает {damage} урона; HP {self.hp}/{self.max_hp}")

    def heal(self, amount):
        before = self.hp
        self.hp += max(0, amount)
        print(f"💚 {self.name} лечится на {self.hp - before} HP")

    def attack(self, target):
        if not self.is_alive() or not target.is_alive():
            return
        weapon = self.inventory.best_weapon()
        bonus = weapon.damage_bonus if weapon else 0
        print(f"⚔️ {self.name} атакует {target.name}!")
        target.take_damage(self.attack_power + bonus)

    def special(self, target):
        # Дочерние классы переопределяют этот метод.
        print(f"{self.name} пока не знает особого приёма")

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}: HP {self.hp}/{self.max_hp}"


class Warrior(Hero):
    def __init__(self, name):
        # super() вызывает конструктор родителя Hero.
        super().__init__(name, hp=120, attack_power=18, defense=6)

    def special(self, target):
        if self.is_alive() and target.is_alive():
            print(f"🛡️ {self.name}: МОЩНЫЙ УДАР!")
            target.take_damage(self.attack_power * 2)


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, hp=75, attack_power=12, defense=2)
        self.mana = 30  # У мага есть уникальное свойство.

    def special(self, target):
        if not self.is_alive() or not target.is_alive():
            return
        if self.mana < 10:
            print(f"🔮 {self.name}: недостаточно маны!")
            return
        self.mana -= 10
        print(f"🔥 {self.name}: ОГНЕННЫЙ ШАР! Осталось маны: {self.mana}")
        target.take_damage(35)


class Rogue(Hero):
    # ДОМАШНЕЕ ЗАДАНИЕ: критический удар с вероятностью 25%.
    CRIT_CHANCE = 0.25

    def __init__(self, name):
        super().__init__(name, hp=90, attack_power=16, defense=3)

    def special(self, target):
        if self.is_alive() and target.is_alive():
            crit = random.random() < self.CRIT_CHANCE
            damage = self.attack_power * 2 if crit else self.attack_power
            crit_text = " ☠️ КРИТИЧЕСКИЙ УДАР!" if crit else ""
            print(f"🗡️ {self.name}: СКРЫТНЫЙ УДАР!{crit_text}")
            target.take_damage(damage)


class Paladin(Hero):
    """НОВЫЙ КЛАСС из домашнего задания: наследник Hero со щитом и божественной силой."""

    def __init__(self, name):
        # super() вызывает конструктор родителя Hero.
        super().__init__(name, hp=110, attack_power=15, defense=8)

    def special(self, target):
        if self.is_alive() and target.is_alive():
            print(f"✨ {self.name}: СВЕТОЕЗЛЕНИЕ!")
            target.take_damage(self.attack_power * 2)
