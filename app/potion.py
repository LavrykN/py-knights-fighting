from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @staticmethod
    def create_potion(potion: dict) -> None | Potion:
        if potion is None:
            return None
        return Potion(potion["name"], potion["effect"])