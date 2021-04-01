# SamplePackage.sample_module
# EXPLANATION
"""
SamplePackage.sample_module
DOCSTRING
"""

# Content #
    # F1. Import Statements
    # V1. module_variable: 
    # C1. SampleObject: 
    # M1. core_function: 

# V1 'module_variable'
# EXPLANATION
module_variable = None

# C1 'SampleObject'
# EXPLANATION
class SampleObject:
    """
    SampleObject
    DOCSTRING
    """
    # Class Variables #
    class_name = 'SampleObject'

    # Special Methods #
    def __init__(self):
        self.name = None

    def __str__(self):
        return 'SampleObject'

    def __repr__(self):
        return f'< SamplePackage.sample_module.SampleObject >'

    # Getters and Setters #
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

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

# M1 'core_method'
# EXPLANATION
def core_method(argument):
    """
    core_method
    DOCSTRING
    """
    pass