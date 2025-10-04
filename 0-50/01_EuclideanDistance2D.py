"""EuclideanDistance2D"""
import math
q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())
d = math.sqrt(math.pow((q1 - p1),2) + math.pow((q2 - p2),2))
print(d)
