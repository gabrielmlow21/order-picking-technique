import random
from layouts import Layout
from rack import Rack
from sku import SKU


class Warehouse:
    '''
    creates a single-sided picking warehouse, https://www.researchgate.net/figure/Warehouse-top-view-with-single-sided-picking-left-and-two-sided-picking-right-using_fig1_237117821
    '''

    def __init__(self, rng_seed_adder, config_parser, constants_config_parser):
        self.config_parser = config_parser
        self.constants_config_parser = constants_config_parser
        self.rng_seed = self.constants_config_parser.getint(
            'RNG', 'RNGSeed') + rng_seed_adder
        self.rows = self.config_parser.getint('warehouse', 'WarehouseWidth')
        self.columns = self.config_parser.getint(
            'warehouse', 'WarehouseLength')
        self.walkable_tile = "0" * (len(str(self.rows * self.columns)) + 1)
        self.warehouse, self.racks = self.create_warehouse_x() if self.config_parser.get(
            'racks', 'RacksOrientation') == "x" else self.create_warehouse_y()
        self.skus = self.initialize_skus()
        self.orders = self.generate_skus_for_order()
        self.dropoff_location = self.config_parser.get(
            'warehouse', 'DropoffLocation')
        self.starting_point = self.config_parser.get(
            'warehouse', 'StartingPoint')

    def create_warehouse_x(self):
        split_walkways_indices = [i * self.columns // self.config_parser.getint(
            'warehouse', 'TotalCrossAisles')+1 for i in range(1, self.config_parser.getint(
                'warehouse', 'TotalCrossAisles')+1)]
        # print(split_walkways_indices)
        racks = []
        warehouse = [[self.walkable_tile] *
                     self.columns for _ in range(self.rows)]
        MAX_RACKS = self.config_parser.getint('racks', 'MaxRacks')
        WALKABLE_ISLES_BETWEEN_RACKS = self.config_parser.getint(
            'racks', 'WalkableAisleBetweenRacks')
        PUT_TWO_RACKS_TOGETHER = self.config_parser.getint(
            'racks', 'PutTwoRacksTogether')

        rack_id = 1
        for row_index in range(len(warehouse)):
            for rack_index in range(len(warehouse[0])):
                if row_index != 0 and row_index != len(warehouse) - 1 and rack_id <= MAX_RACKS and row_index not in split_walkways_indices:
                    if rack_index == 0:
                        new_rack = Rack(self.config_parser, "R" + "0"*(
                            len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                        warehouse[row_index][rack_index] = new_rack.rack_id
                        racks.append(new_rack)
                        rack_id += 1
                    else:
                        if (rack_index > WALKABLE_ISLES_BETWEEN_RACKS and warehouse[row_index][rack_index-WALKABLE_ISLES_BETWEEN_RACKS] == self.walkable_tile):
                            if (PUT_TWO_RACKS_TOGETHER == 0 and warehouse[row_index][rack_index-1] == self.walkable_tile):
                                new_rack = Rack(self.config_parser, "R" + "0"*(
                                    len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                                warehouse[row_index][rack_index] = new_rack.rack_id
                                racks.append(new_rack)
                                rack_id += 1
                            elif (PUT_TWO_RACKS_TOGETHER == 1 and warehouse[row_index][rack_index-1] != self.walkable_tile and warehouse[row_index][rack_index-2] == self.walkable_tile):
                                new_rack = Rack(self.config_parser, "R" + "0"*(
                                    len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                                warehouse[row_index][rack_index] = new_rack.rack_id
                                racks.append(new_rack)
                                rack_id += 1
            # print(warehouse)
        return warehouse, racks

    def create_warehouse_y(self):
        split_walkways_indices = [i * self.rows // self.config_parser.getint(
            'warehouse', 'TotalCrossAisles')+1 for i in range(1, self.config_parser.getint(
                'warehouse', 'TotalCrossAisles')+1)]
        racks = []
        warehouse = [[self.walkable_tile] *
                     self.columns for _ in range(self.rows)]
        MAX_RACKS = self.config_parser.getint('racks', 'MaxRacks')
        WALKABLE_ISLES_BETWEEN_RACKS = self.config_parser.getint(
            'racks', 'WalkableAisleBetweenRacks')
        PUT_TWO_RACKS_TOGETHER = self.config_parser.getint(
            'racks', 'PutTwoRacksTogether')
        rack_id = 1
        for row_index in range(len(warehouse)):
            for rack_index in range(len(warehouse[0])):
                if rack_index != 0 and rack_index != len(warehouse[0]) - 1 and rack_id <= MAX_RACKS and row_index not in split_walkways_indices:
                    if row_index == 0:
                        new_rack = Rack(self.config_parser, "R" + "0"*(
                            len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                        warehouse[row_index][rack_index] = new_rack.rack_id
                        racks.append(new_rack)
                        rack_id += 1
                    else:
                        if (row_index > WALKABLE_ISLES_BETWEEN_RACKS and warehouse[row_index-WALKABLE_ISLES_BETWEEN_RACKS][rack_index] == self.walkable_tile):
                            if (PUT_TWO_RACKS_TOGETHER == 0 and warehouse[row_index-1][rack_index] == self.walkable_tile):
                                new_rack = Rack(self.config_parser, "R" + "0"*(
                                    len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                                warehouse[row_index][rack_index] = new_rack.rack_id
                                racks.append(new_rack)
                                rack_id += 1
                            elif (PUT_TWO_RACKS_TOGETHER == 1 and warehouse[row_index-1][rack_index] != self.walkable_tile and warehouse[row_index-2][rack_index] == self.walkable_tile):
                                new_rack = Rack(self.config_parser, "R" + "0"*(
                                    len(str(self.rows * self.columns)) - len(str(rack_id))) + str(rack_id), (rack_index, row_index))
                                warehouse[row_index][rack_index] = new_rack.rack_id
                                racks.append(new_rack)
                                rack_id += 1
            # print(warehouse)
        return warehouse, racks

    def initialize_skus(self):
        random.seed(self.rng_seed)
        MAX_SKU = self.config_parser.getint('SKU', 'TotalSKUInWarehouse')
        MIN_SKU_WEIGHT = self.config_parser.getint('SKU', 'MinSKUWeight')
        MAX_SKU_WEIGHT = self.config_parser.getint('SKU', 'MaxSKUWeight')
        sku_index = 1
        skus = []
        i = 0
        while i < MAX_SKU:
            target_rack = self.racks[random.randint(0, len(self.racks)-1)]
            if not target_rack.is_rack_full():
                new_sku = SKU("SKU" + "0" * (len(str(MAX_SKU)) -
                                             len(str(sku_index))) + str(sku_index), target_rack, random.randint(MIN_SKU_WEIGHT, MAX_SKU_WEIGHT), self.get_sku_pickup_location(target_rack.location))
                skus.append(new_sku)
                target_rack.add_sku()
                i += 1
                sku_index += 1
        return skus

    def generate_skus_for_order(self):
        return [self.skus[random.randint(0, len(self.skus)-1)] for _ in range(random.randint(self.constants_config_parser.getint('orders', 'MinOrderSize'), self.constants_config_parser.getint('orders', 'MaxOrderSize')))]

    # gets the location where the picker SHOULD be standing to get an item based on the rack_id
    def get_sku_pickup_location(self, location):
        rack_x = location[0]
        rack_y = location[1]
        if rack_x == 0:
            return (1, rack_y)
        return (rack_x-1, rack_y) if self.warehouse[rack_y][rack_x-1] == self.walkable_tile else (rack_x+1, rack_y)

    def display(self):
        for row in self.warehouse:
            print(" ".join(row))
