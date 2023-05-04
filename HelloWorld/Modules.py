# Import the whole module containing code in a different file
import converters
import utils

# Or

# Import specific function from module
from converters import kg_to_lbs

# No need to prefix the function object, converters, as it is imported directly
print(kg_to_lbs(100))

# Or

#calling the function created in the other module, passing in required argument, and printing result
print(converters.kg_to_lbs(70))

print(utils.find_max([1,2,5,9,4,7]))