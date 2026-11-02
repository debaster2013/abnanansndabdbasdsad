"""Пошаговый бой команды с боссом."""


def team_battle(heroes, boss):
    round_number = 1
    print(f"\n🏰 Команда выходит против босса {boss.name}!")
    while boss.is_alive() and any(hero.is_alive() for hero in heroes):
        print(f"\n===== РАУНД {round_number} =====")
        # Каждый живой герой применяет особую способность.
        # ПОЛИМОРФИЗМ: одинаковый вызов special(), но разные эффекты.
        for hero in heroes:
            if hero.is_alive() and boss.is_alive():
                hero.special(boss)
        if not boss.is_alive():
            break
        # Босс выбирает первого живого героя и атакует его.
        target = next(hero for hero in heroes if hero.is_alive())
        if round_number % 2 == 0:
            boss.special(target)
        else:
            boss.attack(target)
        round_number += 1
        if round_number > 100:  # Защита от бесконечного боя при ошибках.
            print("Бой остановлен по лимиту раундов")
            return False
    victory = not boss.is_alive()
    print("\n🏆 Победа команды!" if victory else "\n☠️ Босс победил команду")
    return victory
