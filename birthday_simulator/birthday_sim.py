import csv
import os
from random import choices

import matplotlib.pyplot as plt


class BirthdaySim:
    SIMULATIONS_SAVE_PATH = "data/simulations.csv"
    PLOT_SAVE_PATH = "../plots/simulation_graph.png"

    def __init__(self, total_simulations: int = 100000, group_size: int = 23):
        """
        Initializes the birthday simulation

        :param total_simulations: Number of times to run the simulation
        :param group_size: Number of people in the group
        """
        self.total_simulations = total_simulations
        self.group_size = group_size

    def simulate(self) -> None:
        """Runs the birthday paradox simulation"""
        print("\nSimulate is starting...")

        duplicate_count = 0
        for _ in range(self.total_simulations):
            birthdays = choices(range(1, 366), k=self.group_size)
            if self._has_duplicate(birthdays):
                duplicate_count += 1

        probability = round(duplicate_count / self.total_simulations * 100, 2)

        print(f"Simulations save to {self.SIMULATIONS_SAVE_PATH}")
        self._save(duplicate_count, probability)

    @staticmethod
    def _has_duplicate(birthdays: list) -> bool:
        """Checks if there are any duplicate birthdays in the list"""
        seen = set()
        for b in birthdays:
            if b in seen:
                return True
            seen.add(b)
        return False

    def _save(self, duplicate_count: int, probability: float) -> None:
        """Saves the simulation results to a CSV file"""
        file_exists = os.path.exists(self.SIMULATIONS_SAVE_PATH)
        with open(self.SIMULATIONS_SAVE_PATH, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow([
                    "id", "group_size", "total_simulations", "duplicate_count", "probability"
                ])
                row_id = 1
            else:
                with open(self.SIMULATIONS_SAVE_PATH, "r", encoding="utf-8") as f:
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
        """Formats a number with spaces for readability"""
        return f"{num:_}".replace("_", " ")

    def draw_graph(self, save: bool = False) -> None:
        """Draws a line graph of previous simulation results"""
        group_size = []
        probability = []

        try:
            with open(self.SIMULATIONS_SAVE_PATH, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    group_size.append(int(row["group_size"]))
                    probability.append(float(row["probability"]))
        except FileNotFoundError:
            print("[ERROR] File doesn't exist")
            return

        fig, ax = plt.subplots()

        ax.plot(sorted(group_size), sorted(probability), marker="o")

        ax.set_title("Birthday Paradox")
        ax.set_xlabel("Group size")
        ax.set_ylabel("Probability of a match (%)")

        ax.grid(True)

        ax.set_xticks(group_size)
        ax.set_yticks(range(0, 101, 10))

        if save:
            print(f"Plot saved to {self.PLOT_SAVE_PATH}")
            fig.savefig(self.PLOT_SAVE_PATH)
        else:
            plt.show()


if __name__ == "__main__":
    birthday_sim = BirthdaySim()
    birthday_sim.simulate()
    birthday_sim.draw_graph()
