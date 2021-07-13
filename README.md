# Session 10 Assignment

In this assignment we will go through sequence types in python such as 

Sequence Types
Mutable Sequences
Lists vs Tuples
Copying Sequences
Slicing
Custom Sequences
Sorting Sequences
List Comprehensions 

Here we will create two classes
1. Polygon class that can take num of edges and vertices as input and provide following properties:
# edges
# vertices
interior angle
edge length
apothem
area
perimeter
 and also implementing following functionalities:
__repr__ function
implements equality (==) based on # vertices and circumradius (__eq__)
implements > based on number of vertices only (__gt__)

2. Custom Polygon class
where initializer takes in:
1. number of vertices for largest polygon in the sequence
2. comon circumradius for all polygons

can provide these properties: max efficiency polygon: returns the Polygon with the highest area: perimeter ratio

The class has functionalities such as __getitem__, __len__, __repr__
