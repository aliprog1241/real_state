#import ABC for easy OOP

from abc import ABC 


import uuid

#creat BaseClass

class BaseClass:
    _id = 0
    def __init__(self):
        self.id = self.generate_id()

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id


    @classmethod
    def store (cls, obj):
        cls.object_list.append(obj)
    
