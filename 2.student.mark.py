import datetime


class student :  
    
    def __init__(self,i,n,d):
          
        self.id=i
        self.name=n
        self.DoB=d 
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def DoB(self):  
        return self._DoB        
    @id.setter
    def id(self,i):
        if( i !=None):
            return i
        else:
            raise ValueError(f"invalid id :{i}")  
        self._id=i     
    @name.setter
    def name(self,n):
        if(n !=None ):
            return n
        else:
            raise ValueError("invalid name")
        self._name=n    
    @DoB.setter
    def DoB(self,d):  
        split_dob=d.split("/")
        correctDate = None
        try:
            newDate = datetime.datetime(split_dob[2],split_dob[1],split_dob[0])
            correctDate = True
        except ValueError("wrong date"):
                correctDate = False
        if(correctDate==True):
            return d             
        self._DoB=d
class course :
    def __init__(self,i,n):     
        self.course_id=i
        self.course_name=n        
if __name__=="__main__":        
    name1=student(1,"mr A","11/10/2000")        
    