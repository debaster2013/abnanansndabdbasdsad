"""Запуск Dungeon Code — домашнее задание «Легендарная команда»."""
from heroes import Warrior, Mage, Rogue, Paladin
from items import Weapon, Potion
from boss import Boss
from battle import team_battle


def main():
    # Каждый класс создаёт объект со своими характеристиками.
    warrior = Warrior("Артур")
    mage = Mage("Луна")
    rogue = Rogue("Тень")
    paladin = Paladin("Александр")  # Новый герой из домашнего задания.
    team = [warrior, mage, rogue, paladin]  # Новый герой добавлен в команду.

    # Выдаём предметы: у каждого героя СВОЙ инвентарь.
    warrior.inventory.add_item(Weapon("Стальной меч", 7))
    warrior.inventory.add_item(Potion("Малое зелье", 25))
    mage.inventory.add_item(Potion("Зелье здоровья", 30))
    rogue.inventory.add_item(Weapon("Кинжал", 5))
    paladin.inventory.add_item(Weapon("Молот Огра", 9))  # Новый предмет из домашнего задания.

    print("\n🧙 НАША КОМАНДА")
    for hero in team:
        print(hero)
        hero.inventory.show()

    # Демонстрация лечения: сначала герой получает урон.
    warrior.take_damage(20)
    warrior.inventory.use_potion(warrior)

    # Демонстрация обычной атаки и оружия.
    training_dummy = Boss("Тренировочный голем")
    warrior.attack(training_dummy)

    # Главный бой с боссом: команда (уже с новым героем) против босса.
    boss = Boss("Огненный дракон")
    team_battle(team, boss)


if __name__ == "__main__":
    main()
