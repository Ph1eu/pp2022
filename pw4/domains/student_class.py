

import re


from datetime import datetime


class student :  
     
    def __init__(self,i,n,D):
          
        self._id=self.__validate_id(i)
        self._name=self.__validate_name(n)
        self._DoB=self.__validate_Dob(D)
    
    def set_id(self, i):
         self._id=self.__validate_id(i)
    def set_name(self,n):
        self._name=self.__validate_name(n)
    def set_Dob(self,D):
        self._D=self.__validate_Dob(D)             
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._DoB
    
    '''
    validation method section
    '''    
    def __validate_id(self,i):
        if( i != None): 
            return i
        else:
            raise Exception(f"invalid id :{i}")
    def __validate_name(self,n):
        if(n !=None ):
            return n
        else:
            raise Exception("invalid name")
    def __validate_Dob(self,d):
        format = "%d-%m-%Y"
        res = True
        try:
            res = bool(datetime.strptime(d, format))
        except Exception:
             res = False
             raise Exception("invalid date")  
        if(res==True):
            return d   
            
    def __lt__(self, other):
         return self._id < other._id