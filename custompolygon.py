import random
from collections import namedtuple 
#from PyClassicRound import classic_round
from decimal import *
import cmath
import math
from session10 import Polygon

class CustomPolygon:
    def __init__(self, numedges,circumrad):
      #try:
      if isinstance(numedges, int) and circumrad >0 and numedges > 2:
          self.numedges = numedges
          self.circumrad = circumrad
      else:
          raise ValueError('num edges needs to an positive integer and circum radius needs to be positive number')
      #except ValueError as ve:
      #  print('Work with number between -1 and 1 only')
    def __len__(self):
        return self.numedges - 2

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s >=self.numedges:
                raise IndexError
            else:
                edges = self.__numedges__(s)
                edgelength = self.__edgelength__(s)
                interiorangle = self.__interiorangle__(s)
                apoth = self.__apothem__(s)
                area = self.__area__(s)
                perimeter = self.__perimeter__(s)
                CustomPolygon = namedtuple('CustomPolygon',['numofedges','edgelength','interiorangle','apothem','area','perimeter'])
                itemval = CustomPolygon(edges,edgelength,interiorangle,apoth,area,perimeter)
                return itemval
                #return "number of vertices = %s Edge Length = %s interior angle = %s apothem = %s area = %s perimeter = %s",edges, edgelength,interiorangle, apoth, area, peri
    # defining object representation
    def __repr__(self):
      return 'Returns a sequence of polygons with max vertices of ' + str(self.numedges) + ' and circum radius of ' + str(self.circumrad) + '  and alsoreturns a polygon with highest area perimeter ratio'

    def maxefficiencypolygon(self):
        l =  {n:(self.__area__(n)/self.__perimeter__(n))  for n in range(3,self.numedges)}
        print(l)
        keymax = max(l,key=l.get)
        valmax = l[keymax]
        return "max efficiency Polygon is for polygon with " + str(keymax) + " vertices and max ratio is " + str(valmax)

    def __numedges__(self,numedges=None):
        return numedges if numedges else self.numedges

    def __interiorangle__(self,numedges=None):
        if numedges:
            return (2*self.circumrad)*math.sin(math.pi/numedges)
        else:
            return (2*self.circumrad)*math.sin(math.pi/self.numedges)

    def __apothem__(self,numedges=None):
        if numedges:
            edges= numedges
        else:
            edges= self.numedges
        rad = self.circumrad
        return (rad)*math.cos(math.pi/edges)

    def __edgelength__(self,numedges=None):
        return ((numedges-2)*180)/math.pi if numedges else ((self.numedges-2)*180)/math.pi

    def __area__(self, numedges=None):
        apothemval = self.__apothem__(numedges)
        edgelengthval = self.__edgelength__(numedges)
        return ((numedges*apothemval*edgelengthval)/2) if numedges else ((self.numedges*apothemval*edgelengthval)/2)
    
    def __perimeter__(self,numedges=None):
        edgelengthval = self.__edgelength__(numedges)
        return (numedges*edgelengthval) if numedges else (self.numedges*edgelengthval)


if __name__ == '__main__':
    p = CustomPolygon(25,6)
    print(p.__repr__())
    print(p.__len__())
    print(p[3])
    print(p.maxefficiencypolygon())
    #print(f'number of vertices = {p.__numedges__()}\nnumber of edges = {p.__numedges__()}\nEdge Length = {p.__edgelength__()}\ninterior angle = {p.__interiorangle__()}\napothem = {p.__apothem__()}\narea = {p.__area__()}\nperimeter = {p.__perimeter__()}\n')