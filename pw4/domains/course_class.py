
class course :
    def __init__(self,i,n,c):     
        self._course_id=i
        self._course_name=n 
        self._course_credit=c 
    '''
    validation method section
    '''     
    def __validate_id(self,i):
        if( i != None and i.isnumeric() ):
            return i
        else:
            raise Exception(f"invalid course id :{i}")
    def __validate_name(self,n):
        if(n !=None ):
            return n
        else:
            raise Exception("invalid course name")
    def __validate_credit(self,c):
        if( c != None and c.isnumeric() ):
            return c
        else:
            raise Exception(f"invalid course credit :{c}")        
    '''
    getter setted method section using property funtion and decorator function
    funtion
    '''      
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def course_name(self):
        return self._course_name 
    
    @property
    def course_credit(self):
        return self._course_credit
    @course_id.setter
    def course_id(self, i):
        self.__validate_id(i)
        self._course_id=i   
    
    @course_name.setter
    def course_name(self,n):
        self.__validate_name(n)
        self._course_name=n 
    
    @course_credit.setter
    def course_credit(self,c):
        self.__validate_credit(c)
        self._course_credit=c      