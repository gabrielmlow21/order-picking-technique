def calculate_distance(location1, location2):
    '''
    Calculates the distance between two locations in a warehouse. 
    In this case, the distance is often measured in terms of the number of aisles and positions moved to travel from one location to another.
    '''
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])


def optimal_routing(sku_objects):
    '''
    The optimal routing strategy can calculate a shortest route, regardless of layout or location of the items. Optimal routes will typically look like a mixture of S-Shape and Largest Gap.
    '''
    route = []
    remaining_sku_objects = list(sku_objects)
    current_location = (0, 0)  # Starting from the central depot
    while remaining_sku_objects:
        nearest_sku = min(remaining_sku_objects, key=lambda sku: calculate_distance(
            current_location, sku))
        route.append(nearest_sku)
        current_location = nearest_sku
        remaining_sku_objects.remove(nearest_sku)
    return route
