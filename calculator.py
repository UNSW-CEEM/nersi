

def average(val_1, val_2):
    return ( float(val_1) + float(val_2) ) / 2

def calculate_max_generator_capacity(self, region, region_demand, region_available_capacity):
    """
        Calculates the maximum generator capacity in a region, for all generators in that region to have a NERSI greater than 1. 
    """
    STEP_SIZE = 20
    NERSI_THRESHOLD = 1
    if region_demand <= STEP_SIZE:
        return region_available_capacity
    
    

    low_bound = 0
    high_bound = region_demand * 3
    generator_capacity = average(high_bound, low_bound)

    while(high_bound - low_bound > STEP_SIZE):
        nersi = self.calculate_nersi( region, region_demand,region_available_capacity, generator_capacity)
        # If greater than the NERSI threshold, generator_cap is too small (ie there is sufficient competition.)
        # So set lower bound to the gen_cap
        if nersi > NERSI_THRESHOLD:
            low_bound = generator_capacity
        else:
            high_bound = generator_capacity

        generator_capacity = average(high_bound, low_bound)

    return generator_capacity





