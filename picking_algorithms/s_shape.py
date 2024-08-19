def s_shape_picking_technique(sku_objects):
    """
    Implementation of the S-Shape order picking algorithm.

    Parameters:
        sku_objects (list of SKU): Each SKU object has a pickup_location attribute that represents the 2D coordinates (x, y) of a picking location.

    Returns:
        list of SKU: The sorted SKU objects based on the S-Shape algorithm.
    """
    if len(sku_objects) <= 1:
        return sku_objects

    # Function to calculate the distance between two points (Euclidean distance)
    def distance(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    # Sort the SKU objects based on the x-coordinate of the pickup_location
    sku_objects.sort(key=lambda sku: sku.pickup_location[0])

    # Split the SKU objects into two groups (top and bottom)
    mid_index = len(sku_objects) // 2
    top_group = sku_objects[:mid_index]
    bottom_group = sku_objects[mid_index:]

    # Sort the bottom group based on the y-coordinate of the pickup_location in reverse order
    bottom_group.sort(key=lambda sku: sku.pickup_location[1], reverse=True)

    # Combine the two groups in an S-shape order
    sorted_sku_objects = []
    for top, bottom in zip(top_group, bottom_group):
        sorted_sku_objects.append(top)
        sorted_sku_objects.append(bottom)

    # Add any remaining SKUs from the longer group (if the number of SKUs is odd)
    if len(top_group) > len(bottom_group):
        sorted_sku_objects.extend(top_group[-1:])
    elif len(bottom_group) > len(top_group):
        sorted_sku_objects.extend(bottom_group[-1:])

    return sorted_sku_objects
