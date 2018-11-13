# -*- coding: utf-8 -*-
# =============================================================================
# #  File: Geom.py
# 
# #  Description: This is a basic program creating fundamental shapes in geometry as objects and performing operations on them
# 
# #  Student Name: Stephen Nachazel
# 
# #  Student UT EID: sdn443
# 
# #  Course Name: CS 313E
# 
# #  Unique Number: 51345
# 
# #  Date Created:9 / 14/ 2018
# 
# #  Date Last Modified: 9 / 17 / 2018 
# =============================================================================
import math

#this function tests equality for two given values
def is_equal (a, b):
  tol = 1.0e-16
  return (abs (a - b) < tol)

#this is defining the point class and its methods
class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    return (is_equal(self.x , other.x ) and is_equal(self.y , other.y))

#this is defining the circle class and its methods
class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  # the only argument c is a Circle object
  # returns a boolean
  def does_intersect (self, c):
      distance = self.center.dist(c.center)
      return (distance + c.radius) >= self.radius
  
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribes (self, r):
      centx = (1/2) * (r.ul.x + r.lr.x)
      centy = (1/2) * (r.ul.y + r.lr.y)
      rad = (1/2) * math.hypot( (r.ul.x - r.lr.x), (r.ul.y - r.lr.y) )
      smallestCircle = Circle( radius = rad , x = centx , y = centy)
      return smallestCircle
  
  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "center  = (" + str(self.center.x) + "," + str(self.center.y) + ")" +" , radius = " + str(self.radius)

  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    return is_equal(self.radius , other.radius) 

#this is defining the rectangle class and its methods
class Rectangle (object):
    
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
      return math.hypot(self.lr.x - self.ul.x , self.ul.y - self.ul.y)
  
  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
      return math.hypot(self.lr.x - self.lr.x , self.ul.y - self.lr.y)

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    width = self.width()
    length = self.length()
    return 2 * width + 2 * length 

  # determine the area
  # takes no arguments, returns a float
  def area (self):
      return self.width() * self.length()
  
  def point_overlap (self, p):
      left_bound  = self.ul.x <= p.x
      right_bound = p.x <= self.lr.x
      upper_bound = p.y <= self.ul.y
      lower_bound = self.lr.y <= p.y
      return (left_bound and right_bound) or (lower_bound and upper_bound)
 
    # determine if a point is  inside the Rectangle or on an edge
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
      left_bound  = self.ul.x < p.x
      right_bound = p.x < self.lr.x
      upper_bound = p.y < self.ul.y
      lower_bound = self.lr.y < p.y
      return left_bound and right_bound and lower_bound and upper_bound
  
  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
      left_bound  = self.ul.x < r.ul.x
      right_bound = r.lr.x < self.lr.x
      upper_bound = r.ul.y < self.ul.y
      lower_bound = self.lr.y < r.lr.y
      return left_bound and right_bound and lower_bound and upper_bound  
  
  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def does_intersect (self, other):
     ll = Point(other.ul.x , other.lr.y)
     ur = Point(other.lr.x , other.ul.y)
     return self.point_overlap(other.lr) or self.point_overlap(other.ul) or self.point_overlap(ll) or self.point_overlap(ur)
 
    # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rect_circumscribe (self, c):
      ulx = c.center.x - c.radius
      uly = c.center.y + c.radius
      lrx = c.center.x + c.radius
      lry =  c.center.y - c.radius 
      smallestRect = Rectangle(ul_x = ulx , ul_y = uly , lr_x = lrx , lr_y = lry)
      return smallestRect
 
    # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
      return "UL: (" + str(self.ul.x) + "," + str(self.ul.y) + "), LR: (" + str(self.lr.x) + "," + str(self.lr.y) + ")"
  
  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
      return self.length() == other.length() and self.width() == other.width()
  
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  def main():
      # open the file geom.txt
      in_file = open("./geom.txt" , "r")
      
      # create Point objects P and Q
      pline = in_file.readline()
      pline.strip()
      container = pline.split(" ")
      px = float(container[0])
      py = float(container[1])
      p = Point( px , py)
      
      qline = in_file.readline()
      qline.strip()
      container = qline.split(" ")
      qx = float(container[0])
      qy = float(container[1])
      q = Point( qx , qy)
      
      # print the coordinates of the points P and Q
      print("Cooridnates of P: " + p.__str__())
      print("Coordinates of Q: " + q.__str__())
      
      # find the distance between the points P and Q
      print("Distance between P and Q: " , p.dist(q))
      
      # create two Circle objects C and D
      cline = in_file.readline()
      cline.strip()
      container = cline.split(" ")
      cx = float(container[0])
      cy = float(container[1])
      cradius = float(container[2])
      c = Circle( cradius , cx , cy)
      
      dline = in_file.readline()
      dline.strip()
      container = dline.split(" ")
      dx = float(container[0])
      dy = float(container[1])
      dradius = float(container[2])
      d = Circle(dradius , dx , dy)
      
      # print C and D
      print("Cirlce C: " + c.__str__())
      print("Circle D: " + d.__str__())
      
      # compute the circumference of C
      print("Circumference of C: " + str(c.circumference()))
      
      # compute the area of D
      print("Area of D: "  + str(d.area()))
      
      # determine if P is strictly inside C
      if c.point_inside(p):
           print("Point P is inside C.")
      else:
          print("Point P is not inside C.")
          
      # determine if C is strictly inside D
      if d.circle_inside(c):
          print("C is inside D")
      else:
         print("C is not inside D")
         
      # determine if C and D intersect (non zero area of intersection)
      if c.does_intersect(d):
          print("C does intersect D")
          
      else:
          print(" C does not intersect D")
          
      # determine if C and D are equal (have the same radius)
      if c.__eq__(d):
          print("C is equal to D")
          
      else:
          print("C is not equal to D")
          
      # create two rectangle objects G and H
      gline = in_file.readline()
      gline.strip()
      container = gline.split(" ")
      gx1 = float(container[0])
      gy1 = float(container[1])
      gx2 = float(container[2])
      gy2 = float(container[3])
      g = Rectangle( gx1 , gy1 , gx2 , gy2)
      
      hline = in_file.readline()
      hline.strip()
      container = hline.split(" ")
      hx1 = float(container[0])
      hy1 = float(container[1])
      hx2 = float(container[2])
      hy2 = float(container[3])
      h = Rectangle( hx1 , hy1 , hx2 , hy2)
      
      # print the two rectangles G and H
      print( "G: " + g.__str__())
      print("H: "  + h.__str__())
      
      # determine the length of G (distance along x axis)
      print("Length of G: " + str(g.length()))
      
      # determine the width of H (distance along y axis)
      print("Width of H: " + str(h.width()))
      
      # determine the perimeter of G
      print("Perimeter of G: " + str(g.perimeter()))
      
      # determine the area of H
      print("Area of H: " + str(h.area()))
      
      # determine if point P is strictly inside rectangle G
      if g.point_inside(p):
          print("P is inside G")
          
      else:
          print("P is not inside G")
          
      # determine if rectangle G is strictly inside rectangle H
      if h.rectangle_inside(g):
          print("G is inside H")
          
      else:
          print("G is not inside H")
          
      # determine if rectangles G and H overlap (non-zero area of overlap)
      if g.does_intersect(h):
          print("G does overlap H")
          
      else: 
          print("G does not overlap H")
          
      # find the smallest circle that circumscribes rectangle G
      # goes through the four vertices of the rectangle
      print("Circle that circumscribes G: " , d.circle_circumscribes(g).__str__())
      
      # find the smallest rectangle that circumscribes circle D
      # all four sides of the rectangle are tangents to the circle
      print("Rectangle that circumscribes D: " , g.rect_circumscribe(d).__str__())
      
      # determine if the two rectangles have the same length and width
      if g.__eq__(h):
          print( "Rectangle G is equal to H")
          
      else: 
          print("Rectangle G is not equal to H")
          
      # close the file geom.txt
      in_file.close()
      
      
  main()