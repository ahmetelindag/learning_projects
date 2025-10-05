# Square Number Finder
A program written in C that generates a random array and finds which elements are perfect squares.


### Description
- Generates 20 random numbers between 0 and 99.
- Checks each number to see if it is a perfect square.
- Prints the index, value, and square root of matching numbers.

## Notes
- Uses rand() for random numbers, seeded with time.
- Optimized to check up to the square root of each number without using math library.
- Note: The math library (math.h) could be used for sqrt optimization if desired.
