def dijkstra():
    graph = {}
    graph["start"] = {'a':6, 'b':2}
    graph["a"] = {'finish':1}
    graph["b"] = {'a':3,'finish':5}
    graph["finish"] = {}

    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["finish"] = float("inf")

    parents = {}
    parents["a"] = 'start'
    parents["b"] = 'start'
    parents["finish"] = None

    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    
    path = ["finish"]
    last_node = parents["finish"]
    while last_node != "start":
        path.append(last_node)
        last_node = parents[last_node]
    print("Path: ")
    print("Start ---> " + "  --->  ".join(path[::-1]))
    print(f"Cost: {costs['finish']}")

