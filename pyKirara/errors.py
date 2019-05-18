class BaseError(Exception):
    """Just a bare error"""

class CategoryNotFound(BaseError):
    """Defined Category not found"""
    pass
