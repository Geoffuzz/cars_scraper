from scrapy.item import Item, Field

class NewCarsItem(Item):
    """Cars container (dictionary-like object) for scraped data"""
    make = Field()
    model = Field()
    version = Field()
    price = Field()
    curr_date = Field()
    '''intro_date = Field()
    model_intro_date = Field()
    sa_intro_date = Field()
    fuel_consumption = Field()
    engine_capacity = Field()
    engine_size = Field()
    engine_location = Field()
    cylinders = Field()
    power_max = Field()
    torque_max = Field()
    transmission = Field()
    abs_brakes = Field()
    acceleration_0to100 = Field()
    top_speed = Field()
    airbags = Field()
    fuel = Field()
    doors = Field()
    seats = Field()
    body_shape = Field()
    driven_wheels = Field()
    gears = Field()
    length = Field()
    width = Field()
    weight = Field()
    load_volume_capacity = Field()
    load_carrying_capacity = Field()
    fuel_capacity = Field()
    warranty_distance = Field()
    service_plan_distance = Field()
    service_interval_distance = Field()'''

