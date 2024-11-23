for space in adjacentSpaces:
            newDist = space.value + pos.dist
            if newDist < space.dist:
                if pos.last and is_straight_move(pos.last, space):
                    space.consecutive_straight_moves = pos.consecutive_straight_moves + 1
                else:
                    space.consecutive_straight_moves = 0

                if space.consecutive_straight_moves <= max_consecutive_straight_moves:
                    space.dist = newDist
                    space.last = pos
                    searchSpaces.append(space)
def Dijkstra(grid: list[list[Position]], pos: Position, target: Position):
    loopNum = 0
    searchSpaces = [pos]
    while not target.visited:
        pos = min([space for space in searchSpaces if not space.visited])
        searchSpaces.remove(pos)
        printGrid(grid, pos=pos, wait=1)
        # print(loopNum)
        loopNum += 1
        row = pos.row
        col = pos.col
        searchList = [[row-1, col, 0], [row, col-1, 0], [row, col+1, 0], [row+1, col, 0]]

        last_straight_line = 0
        temp_last = pos.last
        while temp_last and temp_last.row == pos.row:
            last_straight_line += 1
            temp_last = temp_last.last
        while temp_last and temp_last.col == pos.col:
            last_straight_line += 1
            temp_last = temp_last.last

        if last_straight_line == 3:
            if pos.last.row == pos.row:
                searchList.pop(2)
                searchList.pop(1)
                # searchList[1][2] = math.inf
                # searchList[2][2] = math.inf
            elif pos.last.col == pos.col:
                searchList.pop(3)
                searchList.pop(0)
                # searchList[0][2] = math.inf
                # searchList[3][2] = math.inf

        for searchRow, searchCol, penalty in searchList:
            grid[searchRow][searchCol].penalty = penalty

        adjacentSpaces = sorted([grid[searchRow][searchCol] for searchRow, searchCol, penalty in searchList])# if not grid[searchRow][searchCol].visited])
        for space in adjacentSpaces:
            newDist = space.value + pos.dist + space.penalty
            if newDist < space.dist:
                space.dist = newDist# + space.penalty
                space.last = pos
                searchSpaces.append(space)

        pos.visited = True

