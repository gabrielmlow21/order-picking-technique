class Rack:
    def __init__(self, config_parser, rack_id, location):
        self.rack_id = rack_id
        self.location = location
        self.sku_limit = config_parser.getint('racks', 'MaxSKUPerRack')
        self.sku_count = 0

    def add_sku(self):
        self.sku_count += 1

    def is_rack_full(self):
        return self.sku_count >= self.sku_limit

    def __str__(self):
        return self.rack_id

    def __repr__(self):
        return self.rack_id
