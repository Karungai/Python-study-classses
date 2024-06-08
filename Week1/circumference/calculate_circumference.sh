#!/bin/bash

# Set the radius to a fixed value of 5
radius=5
echo "Using a fixed radius of $radius."

# Calculate the circumference using the formula: circumference = 2 * pi * radius
pi=3.14159
circumference=$(awk "BEGIN {print 2 * $pi * $radius}")

# Display the result
echo "The circumference of the circle with radius $radius is: $circumference"

