"""Босс: отдельный класс, который можно разработать в ветке feature-boss."""
from heroes import Hero


class Boss(Hero):
    def __init__(self, name="Дракон"):
        super().__init__(name, hp=150, attack_power=17, defense=4)

    def special(self, target):
        if self.is_alive() and target.is_alive():
            print(f"🐉 {self.name}: ОГНЕННОЕ ДЫХАНИЕ!")
            target.take_damage(27)
