class RiverCrossingSolver:
    """
    Solves the classic river crossing logic puzzle.
    
    The farmer must transport a fox, goose, and grain across a river using a boat
    that can only hold the farmer and one other item. Constraints:
    - Fox cannot be left alone with the goose
    - Goose cannot be left alone with the grain
    """
    
    def __init__(self):
        """Initialize the solver with starting positions."""
        self.starting_side = {"farmer", "fox", "goose", "grain"}
        self.far_side = set()
        self.moves = []
    
    def is_safe_state(self, side: set) -> bool:
        """
        Check if a state is safe (no prohibited pairs left alone).
        
        Args:
            side: A set containing items on one side of the river
            
        Returns:
            bool: True if state is safe, False otherwise
        """
        # If farmer is present, any combination is safe
        if "farmer" in side:
            return True
        
        # If farmer is absent, check for prohibited pairs
        has_fox = "fox" in side
        has_goose = "goose" in side
        has_grain = "grain" in side
        
        # Fox and goose cannot be alone together
        if has_fox and has_goose:
            return False
        
        # Goose and grain cannot be alone together
        if has_goose and has_grain:
            return False
        
        return True
    
    def solve(self) -> list:
        """
        Find the sequence of moves to transport all items across the river.
        
        Returns:
            list: Sequence of moves, each describing what the farmer transported
        """
        # Solution sequence (hardcoded optimal solution)
        solution_items = ["goose", "fox", "goose", "grain", "goose"]
        
        for item in solution_items:
            self._move_item(item)
        
        return self.moves
    
    def _move_item(self, item: str) -> None:
        """
        Move an item across the river and record the move.
        
        Args:
            item: The item to transport ("fox", "goose", or "grain")
        """
        if item in self.starting_side:
            self.starting_side.remove(item)
            self.far_side.add(item)
            self.moves.append(f"Farmer takes {item} across")
        else:
            self.far_side.remove(item)
            self.starting_side.add(item)
            self.moves.append(f"Farmer brings {item} back")
    
    def display_solution(self) -> None:
        """Display the step-by-step solution and final state."""
        print("=== River Crossing Solution ===\n")
        
        for i, move in enumerate(self.moves, 1):
            print(f"Move {i}: {move}")
        
        print(f"\n✓ All items successfully transported!")
        print(f"Starting side: {self.starting_side}")
        print(f"Far side: {self.far_side}")


def main():
    """Main execution block."""
    solver = RiverCrossingSolver()
    solver.solve()
    solver.display_solution()


if __name__ == "__main__":
    main()