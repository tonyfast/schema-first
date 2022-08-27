from .models import my_schema_model

class Item(my_schema_model.Model):
    def __str__(self):
        return F"## {self.name}\n\n> {self.description}\n\n"

def get_item(name, description=None):
    return Item(name=name, description=description)