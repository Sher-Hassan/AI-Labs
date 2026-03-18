import heapq

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_heuristic(state):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(state[i]-1, 3)
            dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def get_successors(state):
    successors = []
    idx = state.index(0)
    r, c = divmod(idx, 3)
    
    # Define directions for clarity
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    for dr, dc, direction in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            successors.append((tuple(new_state), direction))
    return successors

def solve_8_puzzle(start):
    # Queue stores: (f, g, current_state, path_with_directions)
    open_list = [(get_heuristic(start), 0, start, [])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal_state:
            return path + [("Goal", current)]

        if current in visited: continue
        visited.add(current)

        for succ, move_dir in get_successors(current):
            if succ not in visited:
                new_g = g + 1
                new_f = new_g + get_heuristic(succ)
                # Store the move direction alongside the state
                heapq.heappush(open_list, (new_f, new_g, succ, path + [(move_dir, current)]))

# --- Execution ---
initial = (1, 2, 3, 0, 4, 6, 7, 5, 8)
solution = solve_8_puzzle(initial)

print("--- Solution Path ---")
for step, (move, state) in enumerate(solution):
    print(f"Step {step} | Move Blank: {move}")
    print(f"{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")

print(f"Total Moves: {len(solution) - 1}")