from queue import PriorityQueue
import numpy as np

# the priority will be f(n) / f(n) = g(n) + h(n)
unv_nodes = PriorityQueue()

v_nodes = []
# read maze
maze = np.loadtxt("maze.txt")


def g_cost(node):
    return node[0] - node[1]


def h_cost(node_1, node_2):
    x1, y1 = node_1
    x2, y2 = node_2
    return abs(x2 - x1) + abs(y2 - y1)


def a_star(start_point, end_point):

    new_sp = (start_point[0], start_point[1])
    new_ep = (end_point[0], end_point[1])

    rows, collumns = np.shape(maze)

    found_flag = False

    # priority is first index which is f(n), second indx is h(n)
    unv_nodes.put((0, 0, new_sp))

    v_nodes = []

    while not unv_nodes.empty():
        curr = unv_nodes.get()

        v_nodes.append(curr[2])
        # print(curr[2])

        if curr[2] == new_ep:
            print(curr[2])
            print(new_ep)
            print("YES")
            found_flag = True
            break

        # right neighbour
        if curr[2][1] + 1 < collumns:
            if maze[curr[2][0]][curr[2][1] + 1] == 1:
                if (curr[2][0], curr[2][1] + 1) not in v_nodes:
                    # print("right")
                    r_gcost = g_cost(curr) + 1
                    r_fcost = h_cost(new_ep, (curr[2][0], curr[2][1] + 1)) + r_gcost
                    unv_nodes.put(
                        (r_fcost, r_fcost - r_gcost, (curr[2][0], curr[2][1] + 1))
                    )

        # left neighbour
        if curr[2][1] - 1 >= 0:
            if maze[curr[2][0]][curr[2][1] - 1] == 1:
                if (curr[2][0], curr[2][1] - 1) not in v_nodes:
                    # print(maze[curr[2][0]][curr[2][1] - 1])
                    # print("left")
                    l_gcost = g_cost(curr) + 1
                    l_fcost = h_cost(new_ep, (curr[2][0], curr[2][1] - 1)) + l_gcost
                    unv_nodes.put(
                        (l_fcost, l_fcost - l_gcost, (curr[2][0], curr[2][1] - 1))
                    )

        # up neighbour
        if curr[2][0] - 1 >= 0:
            if maze[curr[2][0] - 1][curr[2][1]] == 1:
                if (curr[2][0] - 1, curr[2][1]) not in v_nodes:
                    u_gcost = g_cost(curr) + 1
                    u_fcost = h_cost(new_ep, (curr[2][0] - 1, curr[2][1])) + u_gcost
                    unv_nodes.put(
                        (u_fcost, u_fcost - u_gcost, (curr[2][0] - 1, curr[2][1]))
                    )

        # down neighbour
        if curr[2][0] + 1 < rows:
            if maze[curr[2][0] + 1][curr[2][1]] == 1:
                if (curr[2][0] + 1, curr[2][1]) not in v_nodes:
                    d_gcost = g_cost(curr) + 1
                    d_fcost = h_cost(new_ep, (curr[2][0] + 1, curr[2][1])) + d_gcost
                    unv_nodes.put(
                        (d_fcost, d_fcost - d_gcost, (curr[2][0] + 1, curr[2][1]))
                    )

    if not found_flag:
        print("NO")


a_star((0, 0), (78, 60))
