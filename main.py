from utils import *


def lazy_heuristic(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def line_of_sight(map, node1, node2):
    x0, y0 = node1.x, node1.y
    x1, y1 = node2.x, node2.y
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if map[y0][x0] == 0:
            return False
        if x0 == x1 and y0 == y1:
            return True
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


def lazy_theta_star(map, start, goal):
    class Node:
        def __init__(self, x, y, cost=math.inf, parent=None):
            self.x = x
            self.y = y
            self.cost = cost
            self.parent = parent

        def __lt__(self, other):
            return self.cost < other.cost
    open_list = []
    closed_list = set()
    start_node = Node(start[0], start[1], 0)
    goal_node = Node(goal[0], goal[1])
    heapq.heappush(open_list, (start_node.cost +
                   lazy_heuristic(start_node, goal_node), start_node))

    while open_list:
        _, current = heapq.heappop(open_list)
        if (current.x, current.y) in closed_list:
            continue
        closed_list.add((current.x, current.y))

        if current.x == goal_node.x and current.y == goal_node.y:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        neighbors = [(current.x + dx, current.y + dy) for dx, dy in [(-1, 0),
                                                                     (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]]
        for nx, ny in neighbors:
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] == 255:
                neighbor = Node(nx, ny)
                if (nx, ny) not in closed_list:
                    if current.parent and line_of_sight(map, current.parent, neighbor):
                        new_cost = current.parent.cost + \
                            lazy_heuristic(current.parent, neighbor)
                        if new_cost < neighbor.cost:
                            neighbor.cost = new_cost
                            neighbor.parent = current.parent
                    else:
                        new_cost = current.cost + \
                            lazy_heuristic(current, neighbor)
                        if new_cost < neighbor.cost:
                            neighbor.cost = new_cost
                            neighbor.parent = current
                    heapq.heappush(open_list, (neighbor.cost +
                                   lazy_heuristic(neighbor, goal_node), neighbor))

    return None


def go_neighbor(type, count):
    global pathing_log
    assert type in ["x", "y", "xy"]
    if count == 0:
        return True
    pathing_log["steps"]["step_status"] = f"Moving {count} steps {type}..."
    # print(f"Moving {count} steps {type}...")
    try:
        if type == "x":
            if count > 0:
                now_position = get_player_position()
                target = (now_position[0] + count, now_position[1])
                keydown("d")
                distance = target[0] - now_position[0]
                last_distance = distance
                trys = 0
                while now_position[0] != target[0]:
                    stage = check_stage()
                    if stage != "in_game":
                        keyup("d")
                        return stage
                    now_position = get_player_position()
                    if now_position == None:
                        return "stuck"
                    distance = target[0] - now_position[0]
                    keydown("d", delta=min(distance*45, 500))
                    if distance >= last_distance or distance < 0:
                        trys += 1
                    if trys > 15:
                        keyup("d")
                        return "stuck"
                    last_distance = distance
                    time.sleep(0.05)
                keyup("d")
            else:
                now_position = get_player_position()
                target = (now_position[0] + count, now_position[1])
                keydown("a")
                distance = now_position[0] - target[0]
                last_distance = distance
                trys = 0
                while now_position[0] != target[0]:
                    stage = check_stage()
                    if stage != "in_game":
                        keyup("a")
                        return stage
                    now_position = get_player_position()
                    if now_position == None:
                        return "stuck"
                    distance = now_position[0] - target[0]
                    keydown("a", delta=min(distance*45, 500))
                    if distance >= last_distance or distance < 0:
                        trys += 1
                    if trys > 15:
                        keyup("a")
                        return "stuck"
                    last_distance = distance
                    time.sleep(0.05)
                keyup("a")
        elif type == "y":
            if count > 0:
                now_position = get_player_position()
                target = (now_position[0], now_position[1] + count)
                keydown("s")
                distance = target[1] - now_position[1]
                last_distance = distance
                trys = 0
                while now_position[1] != target[1]:
                    stage = check_stage()
                    if stage != "in_game":
                        keyup("s")
                        return stage
                    now_position = get_player_position()
                    if now_position == None:
                        return "stuck"
                    distance = target[1] - now_position[1]
                    keydown("s", delta=min(distance*45, 500))
                    if distance >= last_distance or distance < 0:
                        trys += 1
                    if trys > 15:
                        keyup("s")
                        return "stuck"
                    last_distance = distance
                    time.sleep(0.05)
                keyup("s")
            else:
                now_position = get_player_position()
                target = (now_position[0], now_position[1] + count)
                keydown("w")
                distance = now_position[1] - target[1]
                last_distance = distance
                trys = 0
                while now_position[1] != target[1]:
                    stage = check_stage()
                    if stage != "in_game":
                        keyup("w")
                        return stage
                    now_position = get_player_position()
                    if now_position == None:
                        return "stuck"
                    distance = now_position[1] - target[1]
                    keydown("w", delta=min(distance*45, 500))
                    if distance >= last_distance or distance < 0:
                        trys += 1
                    if trys > 15:
                        keyup("w")
                        return "stuck"
                    last_distance = distance
                    time.sleep(0.05)
                keyup("w")
        elif type == "xy":
            now_position = get_player_position()
            target = (now_position[0] + count[0], now_position[1] + count[1])
            if count[0] > 0 and count[1] > 0:
                type_ = "sd"
            elif count[0] > 0 and count[1] < 0:
                type_ = "wd"
            elif count[0] < 0 and count[1] > 0:
                type_ = "sa"
            elif count[0] < 0 and count[1] < 0:
                type_ = "wa"
            keydown(type_)
            distance = math.sqrt((target[0] - now_position[0])**2 +
                                 (target[1] - now_position[1])**2)
            last_distance = distance
            trys = 0
            while now_position != target:
                stage = check_stage()
                if stage != "in_game":
                    keyup(type_)
                    return stage
                now_position = get_player_position()
                distance = math.sqrt((target[0] - now_position[0])**2 +
                                     (target[1] - now_position[1])**2)
                keydown(type_, delta=min(distance*45, 500))
                if distance >= last_distance or distance < 0:
                    trys += 1
                if trys > 15:
                    keyup(type_)
                    return "stuck"
                last_distance = distance
                time.sleep(0.05)
            keyup(type_)
        return True
    except TypeError as e:
        print(e)
        traceback.print_exc()
        stage = check_stage()
        return stage


def reset_keyboard():
    pyautogui.keyUp("space")
    keyup("w")
    keyup("a")
    keyup("s")
    keyup("d")


def go_direction(start, end):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    player_pos = get_player_position()
    distance_ = distance(player_pos, end)
    last_distance = 1e9
    extend = max(min(distance_ * 45, 500), 50)
    try_times = 0
    while player_pos != end:
        if distance_ != 0:
            extend_x = extend * delta_x / distance_
            extend_y = extend * delta_y / distance_
        else:
            extend_x = extend_y = 0
        # print(f"Distance: {distance_}, Player: {player_pos}, End: {end}, Extend: {extend_x, extend_y}")
        mouse_pos = (1920 // 2 + extend_x, 1080 // 2 + extend_y)
        pyautogui.moveTo(mouse_pos)
        player_pos = get_player_position()
        if player_pos == None:
            return "stuck"
        distance_ = distance(player_pos, end)
        extend = max(min(distance_ * 45, 500), 50)
        delta_x = end[0] - player_pos[0]
        delta_y = end[1] - player_pos[1]
        if distance_ > last_distance:
            # print("Over walked")
            pyautogui.moveTo(1920 // 2, 1080 // 2)
            return True
        if distance_ == last_distance:
            try_times += 1
        else:
            try_times = 0
        if try_times > 13:
            # print("Stuck")
            pyautogui.moveTo(1920 // 2, 1080 // 2)
            return "stuck"
        last_distance = distance_
        if check_stage() == "in_game_dead":
            return "in_game_dead"
        elif check_stage() == "in_menu":
            return "in_menu"
        time.sleep(0.05)
    pyautogui.moveTo(1920 // 2, 1080 // 2)
    return True


def lazy_theta_execute_path(path):
    for i in range(0, len(path)-1):
        stage = check_stage()
        if stage != "in_game":
            return stage
        # print(f"Moving from {path[i]} to {path[i+1]}")
        move = go_direction(path[i], path[i+1])
        if move == "stuck":
            reset_keyboard()
            return "stuck"
        elif move == "in_game_dead":
            reset_keyboard()
            return "in_game_dead"
        elif move == "in_menu":
            reset_keyboard()
            return "in_menu"
        reset_keyboard()
    return True


def lazy_theta_pathing(location, area=[]):
    while True:
        pos = get_player_position()
        print(f"Pathing Segment: {pos} -> {location}", "INFO")
        time_now = time.time()
        path = lazy_theta_star(load_binary_map(), pos, location)
        print(f"Pathing Time: {time.time() - time_now}", "INFO")
        stat = lazy_theta_execute_path(path)
        if if_in_area(area, pos):
            return True
        elif pos == location:
            return True
        elif stat == "stuck":
            execute_anti_stuck()
        stage = check_stage()
        if stage == "in_game_dead":
            return False
        elif stage == "in_menu":
            return False


if __name__ == "__main__":
    apply_map("desert")
    # the location decided in `map_select.py`
    location = (100, 100)
    dedicated_area = [(0, 0), (200, 200)]
    # optional, if the player has moved into the area and got stuck, the code will end. Otherwise it will try to callibrate until reaching the final location
    while True:
        if lazy_theta_pathing(location, dedicated_area):
            break
    print("Pathing Done")
