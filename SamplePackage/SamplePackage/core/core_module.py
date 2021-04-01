# SamplePackage.core_module
# Explanation of this file goes here

# 'CoreClass' explanation goes here
class CoreClass:
    """
    CoreClass Docstring
    """
    # Class Variables #
    class_name = 'CoreClass'

    # Special Methods #
    def __init__(self):
        self.name = None
        self.ready = False
    
    def __repr__(self):
        return f'< CoreClass | Name: {self.name} >'

    # Getters and Setters #
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_ready(self, ready_bool):
        self.ready = ready_bool

    def get_ready(self):
        return self.ready

    # Attribute Methods #
    # 'set_attribute' and 'set_attributes' methods are redundant
    # with the getters and setters above, but are included as an
    # alternative.
    def to_dict(self):
        """
        Returns a dictionary of the object's attributes
        { 'attribute_name':attribute_value }
        """
        attribute_dict = {
            "name": self.name,
        }

        return attribute_dict

    # Set the value of a single attribute of this object
    def set_attribute(self, attribute_name, attribute_value):
        """
        Set the value of a single attribute of this object
        given the attribute's name and the new value
        """
        for attribute in ["name"]:
            if attribute == attribute_name:
                setattr(self, attribute, attribute_value)
                break

    # Set the value of one or more attributes of this object
    def set_attributes(self, attribute_dict):
        """
        Set the value of every attribute of this object
        matching a key in the given dictionary
        to the corresponding value
        """
        for attribute in ["name"]:
            if attribute in attribute_dict:
                setattr(self, attribute, attribute_dict[attribute])

    # Utility Methods #
    
    # Primary Methods #


