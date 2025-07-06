# tuple

masala_spice = ("cumin", "coriander", "turmeric", "chili powder")
(spices1 , spices2, spices3, spices4) = masala_spice
print(f"Spices: {spices1}, {spices2}, {spices3}, {spices4}\n")

# tuple 
ginger_ratio , garlic_ratio, turmeric_ratio = 1, 2, 3
print(f"Ginger Ratio: {ginger_ratio}, Garlic Ratio: {garlic_ratio}, Turmeric Ratio: {turmeric_ratio}\n")
# we can do this because of tuple unpacking

ginger_ratio, garlic_ratio, turmeric_ratio = turmeric_ratio, ginger_ratio, garlic_ratio
print(f"After swapping: Ginger Ratio: {ginger_ratio}, Garlic Ratio: {garlic_ratio}, Turmeric Ratio: {turmeric_ratio}\n")
# this is a tuple unpacking technique to swap values

# tuple with single element
single_element_tuple = (42,)  # note the comma
print(f"Single Element Tuple: {single_element_tuple}\n")

# tuple with multiple elements
multi_element_tuple = (1, 2, 3, 4, 5)
print(f"Multi Element Tuple: {multi_element_tuple}\n")

# membership test
if "cumin" in masala_spice:
    print("Cumin is in the masala spice tuple.\n")

# tuple concatenation
new_masala_spice = masala_spice + ("black pepper", "cardamom")
print(f"New Masala Spice Tuple: {new_masala_spice}\n")

# tuple slicing
sliced_spices = new_masala_spice[1:4]  # slicing
print(f"Sliced Spices: {sliced_spices}\n")

# tuple length
print(f"Length of New Masala Spice Tuple: {len(new_masala_spice)}\n")

# tuple iteration
print("Iterating over New Masala Spice Tuple:")
for spice in new_masala_spice:
    print(spice)
print("\n")

# tuple methods
# count method
print(f"Count of 'cumin' in New Masala Spice Tuple: {new_masala_spice.count('cumin')}\n")
# index method
print(f"Index of 'turmeric' in New Masala Spice Tuple: {new_masala_spice.index('turmeric')}\n")
# tuple immutability
# trying to change an element will raise an error
try:
    new_masala_spice[0] = "black cumin"  # this will raise an error
except TypeError as e:
    print(f"Error: {e}\n")

