from __future__ import annotations

from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list[Armour],
            weapon: Weapon,
            potion: None | Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def create_knight(knight_source: dict) -> Knight:
        armours = []
        for armour in knight_source["armour"]:
            armours.append(Armour(armour["part"], armour["protection"]))

        weapon = Weapon.create_weapon(knight_source["weapon"])
        potion = Potion.create_potion(knight_source["potion"])
        knight = Knight(
            knight_source["name"],
            knight_source["power"],
            knight_source["hp"],
            armours,
            weapon,
            potion
        )
        return knight

    def prepare_to_battle(self) -> Knight:
        self.power += self.weapon.power
        for armour in self.armours:
            self.protection += armour.protection

        if self.potion is not None:
            for name, score in self.potion.effect.items():
                if name == "power":
                    self.power += score
                elif name == "hp":
                    self.hp += score
                elif name == "protection":
                    self.protection += score
        return self

    def __add__(self, other: Knight) -> None:
        self.hp = max(self.hp - other.power + self.protection, 0)
        other.hp = max(other.hp - self.power + other.protection, 0)