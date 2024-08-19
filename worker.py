from picking_algorithms.optimal_routing import optimal_routing
from picking_algorithms.combined_routing import combined_routing
from picking_algorithms.s_shape import s_shape_picking_technique
from picking_algorithms.largest_gap import largest_gap_picking_tecnnique
from picking_algorithms.traversal import find_total_distance
import ast


class Worker:
    def __init__(self, config_parser, warehouse):
        self.carrying_capacity = config_parser.getint(
            'worker', 'CarryingCapacity')
        self.warehouse = warehouse
        self.orders = warehouse.orders
        self.speed = config_parser.getint('worker', 'Speed')

    def get_destinations_based_on_carrying_capacity(self, sorted_orders):
        destinations = []
        current_capacity = 0
        destinations.append(ast.literal_eval(self.warehouse.starting_point))
        for i in range(len(sorted_orders)):
            if (current_capacity + sorted_orders[i].weight > self.carrying_capacity):
                destinations.append(ast.literal_eval(
                    self.warehouse.dropoff_location))
                current_capacity = 0
            destinations.append(sorted_orders[i].pickup_location)
            current_capacity += sorted_orders[i].weight
        destinations.append(ast.literal_eval(self.warehouse.dropoff_location))
        return [tuple(reversed(t)) for t in destinations]

    def get_traversal_distance(self, sorted_orders):
        return find_total_distance(self.warehouse.warehouse, self.get_destinations_based_on_carrying_capacity(sorted_orders), self.warehouse.walkable_tile)

    def get_distance_naive(self):
        return self.get_traversal_distance(self.orders)

    def get_distance_largest_gap(self):
        return self.get_traversal_distance(largest_gap_picking_tecnnique(self.orders))

    def get_distance_s_shape(self):
        return self.get_traversal_distance(s_shape_picking_technique(self.orders))

    def get_distance_combined_routing(self):
        return self.get_traversal_distance(combined_routing(self.orders))

    def get_distance_optimal_routing(self):
        return self.get_traversal_distance(optimal_routing(self.orders))

    def get_time_largest_gap(self):
        return self.get_distance_largest_gap() * self.speed

    def get_time_s_shape(self):
        return self.get_distance_s_shape() * self.speed

    def get_time_combined_routing(self):
        return self.get_distance_combined_routing() * self.speed

    def get_time_optimal_routing(self):
        return self.get_distance_optimal_routing() * self.speed

    def get_time_naive(self):
        return self.get_distance_naive() * self.speed
