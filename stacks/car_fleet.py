'''
Car Fleet
'''


# Attempt 1: Stack
# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) == 1:
            return 1

        # Keep a stack of fleets
        fleets = []
        # Get the number of cars. This will be used to determine when the last 
        # car has passed the destination.
        n = len(position)

        # Work out how many iterations each car needs to reach the destination.
        def calculate_iterations(speed, position):
            # Distance to cover is the target - starting position
            return (target - position) / speed
            
        leading_iterations = 0

        # Find the order to process the cars
        order = {}
        for i in range(len(position)):
            order[position[i]] = speed[i]
        
        # Get the correct order of positions by sorting in reverse.
        position.sort(reverse = True)

        number_of_cars = 0

        for car_pos in position:
            # Get current car attributes
            car_spd = order[car_pos]
            # Calculate iterations from end.
            iterations = calculate_iterations(car_spd, car_pos)
            
            if car_pos == position[0]:
                fleet = [car_pos]
                leading_iterations = iterations
                number_of_cars += 1
            else:
                # Work out if the car meets the leading car before the destination.
                if iterations <= leading_iterations:
                    # Add to current fleet.
                    fleet.append(i)
                    number_of_cars += 1
                else:
                    # If it does not meet, it becomes the leader of a new fleet
                    # Store previous fleet on stack
                    fleets.append(fleet)
                    # Start a new fleet
                    fleet = [car_pos]
                    leading_iterations = iterations
                    number_of_cars += 1
            
            # Once all cars are in a fleet, add the final fleet to stack.
            if number_of_cars == n:
                fleets.append(fleet)
            
        # Return length of the final stack.
        return len(fleets)

            

        

        

        