import heapq

def minimize_heat_loss(grid):
    rows, cols = len(grid), len(grid[0])

    def h(i, j, dest_i, dest_j):
        return abs(dest_i-i)+abs(dest_j-j)

    # Priority queue to store the state: (total_heat_loss + heuristic, total_heat_loss, i, j, direction, straight_line_count)
    pq = [(0+h(0, 0, rows-1, cols-1), 0, 0, 0, 0, 0)]

    # Set to keep track of visited states
    visited = set()

    while pq:
        _, total_heat_loss, i, j, direction, straight_line_count = heapq.heappop(pq)

        # Check if we've reached the destination
        if i == rows-1 and j == cols-1:
            return total_heat_loss

        # Skip if the state has been visited
        if (i, j, direction, straight_line_count) in visited:
            continue

        # Mark the state as visited
        visited.add((i, j, direction, straight_line_count))

        # Define the possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Try each possible direction
        for d in range(4):
            ni, nj = i+directions[d][0], j+directions[d][1]

            # Check if the new position is within bounds
            if 0 <= ni < rows and 0 <= nj < cols and (d+2)%4 != direction:
                # Calculate the total heat loss for the next position
                next_total_heat_loss = total_heat_loss+grid[ni][nj]

                # Update straight_line_count
                next_straight_line_count = straight_line_count+1 if d == direction else 0

                # Calculate the heuristic for the next position
                heuristic = h(ni, nj, rows-1, cols-1)

                # Push the new state to the priority queue
                heapq.heappush(pq, (next_total_heat_loss+heuristic, next_total_heat_loss, ni, nj, d, next_straight_line_count))

    return float('inf')  # No valid path found

# Example usage with the provided grid
grid = [
    [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
    [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
    [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
    [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
    [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6],
    [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
    [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
    [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
    [4, 6, 5, 4, 9, 6, 7, 9, 7, 9, 7, 5, 3],
    [4, 5, 6, 4, 6, 7, 9, 8, 8, 7, 7, 6, 6],
    [1, 2, 2, 4, 6, 8, 6, 6, 5, 5, 6, 3, 6],
    [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 5, 3],
    [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 3, 3, 3],
]

result = minimize_heat_loss(grid)
print(result)
