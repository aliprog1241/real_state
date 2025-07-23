#import ABC for easy OOP

from abc import ABC 


import uuid

#creat BasseClass

class BaseClass:
    def __init__(self):
        self.id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4()) 

@classmethod

def generate_id(cls):
    cls._id += 1
    return cls._id


@classmethod
def store (cls, obj):
    cls.object_list.append(obj)
    
