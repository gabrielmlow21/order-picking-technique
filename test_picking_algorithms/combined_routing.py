def calculate_distance(location1, location2):
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])


def combined_routing(sku_objects, start_at_front=True):
    '''
    Every time all items of one aisle are picked, the question is posed whether to go to the rear end of an aisle or to return to the front end. 
    These two alternatives have to be compared with each other after which the one, resulting in the shortest route, is chosen. 
    After leaving an aisle (at the front or at the rear end), a choice between the two alternatives ending at the back and a choice between the two alternatives ending at the front has to be made. 
    There are always two possible routes to follow. 
    If the last item is picked (now, the route ends at the front end) a final choice between the two alternatives is made.
    '''
    route = []
    remaining_sku_objects = list(sku_objects)
    current_location = (0, 0)  # Starting from the central depot
    while remaining_sku_objects:
        if start_at_front:
            nearest_sku = min(remaining_sku_objects, key=lambda sku: calculate_distance(
                current_location, sku))
        else:
            nearest_sku = max(remaining_sku_objects, key=lambda sku: calculate_distance(
                current_location, sku))
        route.append(nearest_sku)
        current_location = nearest_sku
        remaining_sku_objects.remove(nearest_sku)
        start_at_front = not start_at_front  # Alternate between front and rear
    return route
