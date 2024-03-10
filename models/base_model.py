#!/usr/bin/python3
"""
Defines BaseModel class
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents BaseModel of the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args(any): Unused
            **kwargs(dict): attrubute key/value
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns string representation of the BaseModel
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates 'updated_at' - with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns the dictionary of the BaseModel instance.

        Includes keys/value of __dict__ instance
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
