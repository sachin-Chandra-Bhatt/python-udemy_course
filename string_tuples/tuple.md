# Tuples in Python

Tuples are immutable sequences in Python, useful for grouping related data. Here are some common tuple operations and examples:

## Tuple Creation and Unpacking

```python
masala_spice = ("cumin", "coriander", "turmeric", "chili powder")
(spices1, spices2, spices3, spices4) = masala_spice
print(f"Spices: {spices1}, {spices2}, {spices3}, {spices4}\n")
```

## Tuple Unpacking and Swapping

```python
ginger_ratio, garlic_ratio, turmeric_ratio = 1, 2, 3
print(f"Ginger Ratio: {ginger_ratio}, Garlic Ratio: {garlic_ratio}, Turmeric Ratio: {turmeric_ratio}\n")

# Swapping values using tuple unpacking
ginger_ratio, garlic_ratio, turmeric_ratio = turmeric_ratio, ginger_ratio, garlic_ratio
print(f"After swapping: Ginger Ratio: {ginger_ratio}, Garlic Ratio: {garlic_ratio}, Turmeric Ratio: {turmeric_ratio}\n")
```

## Single and Multi-element Tuples

```python
single_element_tuple = (42,)  # Note the comma
print(f"Single Element Tuple: {single_element_tuple}\n")

multi_element_tuple = (1, 2, 3, 4, 5)
print(f"Multi Element Tuple: {multi_element_tuple}\n")
```

## Membership Test

```python
if "cumin" in masala_spice:
    print("Cumin is in the masala spice tuple.\n")
```

## Tuple Concatenation

```python
new_masala_spice = masala_spice + ("black pepper", "cardamom")
print(f"New Masala Spice Tuple: {new_masala_spice}\n")
```

## Tuple Slicing

```python
sliced_spices = new_masala_spice[1:4]
print(f"Sliced Spices: {sliced_spices}\n")
```

## Tuple Length

```python
print(f"Length of New Masala Spice Tuple: {len(new_masala_spice)}\n")
```

## Iterating Over a Tuple

```python
print("Iterating over New Masala Spice Tuple:")
for spice in new_masala_spice:
    print(spice)
print("\n")
```

## Tuple Methods

- **count()**: Returns the number of times a value appears.
- **index()**: Returns the index of the first occurrence of a value.

```python
print(f"Count of 'cumin' in New Masala Spice Tuple: {new_masala_spice.count('cumin')}\n")
print(f"Index of 'turmeric' in New Masala Spice Tuple: {new_masala_spice.index('turmeric')}\n")
```

## Tuple Immutability

Tuples cannot be changed after creation. Attempting to modify an element raises a `TypeError`:

```python
try:
    new_masala_spice[0] = "black cumin"  # Raises an error
except TypeError as e:
    print(f"Error: {e}\n")
```

---

**Summary:**  
Tuples are immutable, support unpacking, concatenation, slicing, and basic methods like `count` and `index`. They are ideal for fixed collections of items.