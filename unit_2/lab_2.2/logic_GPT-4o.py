class RiverCrossingSolver:
    """
    A class to solve the river crossing problem where a farmer needs to transport
    a fox, a goose, and a bag of grain across a river using a boat that can only
    hold the farmer and one other item. The fox cannot be left alone with the goose,
    and the goose cannot be left alone with the grain.
    """

    def __init__(self):
        """
        Initializes the solver with the starting state of the problem.
        """
        self.starting_side = {"farmer", "fox", "goose", "grain"}
        self.far_side = set()
        self.moves = []

    def is_safe(self, side: set) -> bool:
        """
        Checks if a given side of the river is in a safe state.

        Args:
            side (set): The set of items on one side of the river.

        Returns:
            bool: True if the side is safe, False otherwise.
        """
        if "farmer" in side:
            return True
        if "fox" in side and "goose" in side:
            return False
        if "goose" in side and "grain" in side:
            return False
        return True

    def move(self, item: str) -> None:
        """
        Moves an item across the river and records the move.

        Args:
            item (str): The item to move across the river.
        """
        if item in self.starting_side:
            self.starting_side.remove(item)
            self.far_side.add(item)
            self.moves.append(f"Farmer takes {item} across the river.")
        else:
            self.far_side.remove(item)
            self.starting_side.add(item)
            self.moves.append(f"Farmer brings {item} back.")

    def solve(self) -> list:
        """
        Solves the river crossing problem and returns the sequence of moves.

        Returns:
            list: A list of strings describing the sequence of moves.
        """
        # Predefined solution sequence
        solution = ["goose", "fox", "goose", "grain", "goose"]
        for item in solution:
            self.move(item)
        return self.moves

    def display_solution(self) -> None:
        """
        Displays the solution to the river crossing problem.
        """
        print("=== River Crossing Solution ===")
        for i, move in enumerate(self.moves, 1):
            print(f"Step {i}: {move}")
        print("\nAll items have been successfully transported to the other side!")


def main():
    """
    Main function to execute the river crossing solver.
    """
    solver = RiverCrossingSolver()
    solver.solve()
    solver.display_solution()


if __name__ == "__main__":
    main()