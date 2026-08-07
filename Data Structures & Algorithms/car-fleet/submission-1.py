class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()
        stack = pairs

        fleets = 0
        max_steps = -1
        while stack:
            p, s = stack.pop()
            steps = (target - p) / s
            if steps > max_steps:
                fleets += 1
                max_steps = steps
        
        return fleets

        