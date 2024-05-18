#!/usr/bin/python3
 
import uuid
import datetime

class BaseModel():
    def __init__(self, *arg, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(selfm keym value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
        

    def __str__(self):
        return f"[{self.__class__.__name__>}] ({self.id}) {self.__dict__}"
        
    def save(self):
        self.update_at = datetime.datetime.now()
        
    def to_dict(self):
        return {
           'id' : 'self.id'
           'created_at' : 'self.created_at'
           'updated_at' : 'self.updated_at'
        }
        
    def __init__(self, *args, **kwargs):
        
            