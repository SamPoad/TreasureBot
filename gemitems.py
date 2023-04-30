# this page documents gems and their properties, to be imported into main.py 

gem_properties = { # 'name' : ('color', 'shape', value), 
    'Ruby' : ('Red', 'Oval', 3000), 
    'Sapphire' : ('Blue', 'Oval', 4000), 
    'Yellow Diamond' : ('Yellow', 'Oval', 7000), # check these value amounts 
    'Emerald' : ('Green', 'Rectangle', 5000), 
    'Red Beryl' : ('Red', 'Rectangle', 9000), 
    'Alexandrite' : ('Violet', 'Rectangle', 6000),
}

gem_combinations = { # 'name' : (number of gems, number of different colors, multiplier)
    'Two Colors' : (2, 2, 1.1), 
    'Duo' : (2, 1, 1.2), 
    'Three Colors' : (3, 3, 1.3), 
    'Trio' : (3, 1, 1.4), 
    'Two Duos' : (4, 2, 1.5), 
    'Four Colors' : (4, 4, 1.6), 
    'Quartet' : (4, 1, 1.7), 
    'Duo + Trio' : (5, 2, 1.8), 
    'Quintet' : (5, 1, 1.9), 
    'Five Colors' : (5, 5, 2.0), 
}