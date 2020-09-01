from nersi import NodalMarket

# Create a nodal market.
market = NodalMarket()

# Add trading nodes. 
market.add_node('NSW')
market.add_node('VIC')
market.add_node('SA')
market.add_node('QLD')
market.add_node('TAS')

# Set the transmission limit from each node to any others it is linked to.
market.set_transmission('NSW', 'QLD',  107, "Terranora NSW->QLD")
market.set_transmission('QLD', 'NSW', 210, "Terranora QLD->NSW")
market.set_transmission('NSW', 'QLD',  600, "Queensland NSW Interconnector NSW->QLD")
market.set_transmission('QLD', 'NSW', 1078, "Queensland NSW Interconnector QLD->NSW")
market.set_transmission('VIC', 'NSW',  1600, "Victoria to NSW Interconnector VIC->NSW")
market.set_transmission('NSW', 'VIC',  1350, "Victoria to NSW Interconnector NSW->VIC")
market.set_transmission('TAS', 'VIC',  594, "Basslink TAS->VIC") 
market.set_transmission('VIC', 'TAS', 478, "Basslink VIC->TAS")
market.set_transmission('VIC', 'SA',  600, "Heywood Interconnector VIC->SA") 
market.set_transmission('SA', 'VIC',  500, "Heywood Interconnector SA->VIC")
market.set_transmission('VIC', 'SA', 220, "Murraylink VIC->SA") 
market.set_transmission('SA', 'VIC',  200, "Murraylink SA->VIC")


# Set the surplus generation capacity at each relevant trading node. 
market.set_surplus_capacity('VIC', 100)
market.set_surplus_capacity('NSW', 50)
market.set_surplus_capacity('QLD', 600)

# Display the market nodal network
# market.draw()
market.print()

# Calculate the maximum flow into a given node. 
flow = market.calculate_max_flow('SA')
print("Flow",flow)

# Calculate NERSI
nersi = market.calculate_nersi(region='SA', region_demand=100, region_available_capacity=110, generator_capacity=30)
print("Nersi of a generator with a capacity of 30 MW", nersi)

# Calculate the maximum allowable generator size for all participants to have NERSI > 1
max_size_MW = market.calculate_max_generator_capacity('SA', region_demand=100, region_available_capacity=110)
print('Maximum allowable generator size for all participants to have NERSI > 1', max_size_MW)
