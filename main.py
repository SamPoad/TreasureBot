# This will serve as the main script 

# IMPORT DEPENDENCIES 
import numpy as np 
import pandas as pd 
from treasureitems import treasure_properties
from gemitems import gem_properties, gem_combinations 


# DEFINE THE FUNCTION 
# how best to go about this? treasure, gems, and combo as different dataframes? then compare the user's inventory, and numpy/pandas to run over it? 
# dataframe with all of the possible combinations, and then filter with the user's inventory and pick the max value one? 
treasure_df = pd.DataFrame.from_dict(treasure_properties, orient = 'index', columns= ['oval_slots', 'rectangle_slots', 'base_value'])
print(treasure_df.head())

gem_df = pd.DataFrame.from_dict(gem_properties, orient = 'index', columns= ['color', 'shape', 'value'])
print(gem_df.head())

combo_df = pd.DataFrame.from_dict(gem_combinations, orient = 'index', columns= ['number_of_gems', 'number_of_colors', 'multiplier'])
print(combo_df.head())




# GET INPUT FROM THE USER ON THEIR TREASURE AND GEM ITEMS 

# calculate the possible combinations of gems and treasure



# look at the treasure, gem, and combo dataframes and find the max value combination
def find_max_value():
    # find the max value combination 
    # return the combination and the value 
    return treasure_df['base_value'] * combo_df['multiplier']

# CALCULATE AND RETURN 

# CALL THE FUNCTION 

print("Ran sucessfully!")