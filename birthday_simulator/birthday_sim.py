import csv
import os
from random import choices


class BirthdaySim:
    SAVE_PATH = "data/simulations.csv"

    def __init__(self, total_simulations: int = 100000, group_size: int = 23):
        self.total_simulations = total_simulations
        self.group_size = group_size

    def simulate(self) -> None:
        """Performs a simulation"""
        print("\nSimulate is starting...")

        duplicate_count = 0
        for _ in range(self.total_simulations):
            birthdays = choices(range(1, 366), k=self.group_size)
            if self._has_duplicate(birthdays):
                duplicate_count += 1

        probability = round(duplicate_count / self.total_simulations * 100, 2)

        print(f"Save to {self.SAVE_PATH}")
        self._save(duplicate_count, probability)

    @staticmethod
    def _has_duplicate(birthdays: list) -> bool:
        """Checks if birthdays are duplicated"""
        seen = set()
        for b in birthdays:
            if b in seen:
                return True
            seen.add(b)
        return False

    def _save(self, duplicate_count: int, probability: float) -> None:
        """Saves results to csv"""
        file_exists = os.path.exists(self.SAVE_PATH)
        with open(self.SAVE_PATH, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow([
                    "id", "group_size", "total_simulations", "duplicate_count", "probability"
                ])
                row_id = 1
            else:
                with open(self.SAVE_PATH, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if len(lines) > 1:
                        last_id = int(lines[-1].split(',')[0])
                        row_id = last_id + 1
                    else:
                        row_id = 1

            writer.writerow([
                row_id,
                self.group_size,
                self._format_num(self.total_simulations),
                self._format_num(duplicate_count),
                probability
            ])

    @staticmethod
    def _format_num(num: int) -> str:
        """Formats number to string"""
        return f"{num:_}".replace("_", " ")


if __name__ == "__main__":
    birthday_sim = BirthdaySim()
    birthday_sim.simulate()
