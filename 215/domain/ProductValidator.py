from domain.Product import Product

__author__ = 'Roland'
class ValidationException(Exception):
    pass

class ProductValidator:

    def validate(self,product):
        if not isinstance(product,Product):
            raise ValidationException("Wrong type for this repository")
        errors = []
        if type(product.id) != int:
            errors.append("Id is not integer")
        if type(product.name) != str:
            errors.append("Name is not a string")
        if product.name == '':
            errors.append("Name must not be empty")
        if type(product.quantity) != int:
            errors.append("Quantity must be an integer")
        if product.quantity <= 0:
            errors.append("Quantity must be pozitive")
        if len(errors):
            raise ValidationException(errors)
        return True
