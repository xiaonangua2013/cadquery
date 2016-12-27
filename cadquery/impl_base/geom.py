import math
from cadquery import Configuration

"""
    Base objects. Designed to be immutable, and implemented as a part of a backend

"""
class BaseVector(object):
    
    def __init__(self,x, y, z):
        pass
      
    def X(self):
        raise NotImplementedError("Please Implement this Vector Method")

    def Y(self):
        raise NotImplementedError("Please Implement this Vector Method")

    def Z(self):
        raise NotImplementedError("Please Implement this Vector Method")

    def angle(self,another_vector):
        raise NotImplementedError("Please Implement this Vector Method")        
        
    def length(self):
        raise NotImplementedError("Please Implement this Vector Method")
        
    def add(self,other_vector):
        raise NotImplementedError("Please Implement this Vector Method")
    
    def sub(self,other_vector):
        raise NotImplementedError("Please Implement this Vector Method")

    def dot(self,other_vector):
        raise NotImplementedError("Please Implement this Vector Method")    
        
    def cross(self,other_vector):
        raise NotImplementedError("Please Implement this Vector Method")

    def reverse(self):
        raise NotImplementedError("Please Implement this Vector Method")        
        
    def normalize(self):
        raise NotImplementedError("Please Implement this Vector Method")    
   
    def scale(self,scale):
        raise NotImplementedError("Please Implement this Vector Method") 
    
    def distance(self,other):
        raise NotImplementedError("Please implement this Vector Method")
        
    def tolerant_equals(self,other):
        return self.distance(other) < Configuration.TOLERANCE

    def __eq__(self,other):
        return self.tolerant_equals(other) 
        
    def __str__(self):
        return "Vector: x=%0.3f,y=%0.3f,z=%0.3f, class=%s" % ( self.X(),self.Y(),self.Z(), str(self.__class__))
        
    #TODO: might be nice to implement __rmul__, __lmul, etc

    

class BaseAxis(object):
    """
        An axis contains two vectors-- a point and a direction
    """
    def __init__(self,origin,direction):
        pass
    
    
    def direction(self):
        raise NotImplementedError("Please return a Vector that represents the direction of this axis")
        
    def origin(self):
        raise NotImplementedError("please return a vector that represents the origin of this axis")
        
    
class BaseTransformation(object):
    
    # base constructor should create an identity transformation
    # ( no scale, no rotation, no translation)
    def __init__(self):
        pass
    
    def with_values(tuple_of_tuple_4x4):
         raise NotImplementedError("Please implment this Transformation Method")

    def transform(self, vector):
        raise NotImplementedError("Please implment this Transformation Method")
        
    def multiplied(self, another_transformation):
        raise NotImplementedError("Please implment this Transformation Method")
        
    def inverted(self):
        raise NotImplementedError("Please implment this Transformation Method")

    def scaled(self, scalar):
        raise NotImplementedError("Please implment this Transformation Method")

    def translated(self,vector):
        raise NotImplementedError("Please implment this Transformation Method")
        
    def rotated_x(self, angle):
        raise NotImplementedError("Please implment this Transformation Method")
        
    def rotated_y(self, angle):
        raise NotImplementedError("Please implment this Transformation Method")

    def rotated_z(self, angle):
        raise NotImplementedError("Please implment this Transformation Method") 


class BaseBoundingBox(object):
    
    """ A bounding Box. Initial constructor should create an empty one"""
    def __init__(self):
        pass
    
    def get_min(self):
        raise NotImplementedError("Please return a vector holding the minimum corner")   

    def get_max(self):
        raise NotImplementedError("Please return a vector holding the maximum corner")        
    
    def add_shape(self, shape):
        raise NotImplementedError("Please return a new bounding box with the shape added")   
            
    def add_bbox(self, bb_to_add):
        raise NotImplementedError("Please return a new bounding box with bbox added")
            
    def is_shape_inside(self, object_to_test):
        raise NotImplementedError("Please return boolean, indicating if the provided shape is in this one")        

    def is_shape_outside(self,object_to_test):
        raise NotImplementedError("Please return boolean, indicating if the provided shape is outside this one")  
        
    def is_bbox_inside(self, object_to_test):
        raise NotImplementedError("Please return boolean, indicating if the provided bbox is in this one")        

    def is_bbox_outside(self,object_to_test):
        raise NotImplementedError("Please return boolean, indicating if the provided bbox is outside this one")          