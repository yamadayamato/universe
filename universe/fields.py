from . import exceptions


class Field:
    def __init__(self, required=True):
        self.required = required

    @property
    def data_name(self):
        return self.name

    def from_data(self, data):
        return data.get(self.data_name)

    def to_data(self, value):
        return value

    def serialize(self, data):
        if self.data_name in data:
            return {self.data_name: data[self.data_name]}
        return {}

    def validate(self, data):
        if self.required and self.data_name not in data:
            raise exceptions.ValidationError(f"{self.data_name!r} is required.")


class BooleanField(Field):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        super().validate(data)
        value = data[self.data_name]
        if not isinstance(value, bool):
            raise exceptions.ValidationError(f"{self.data_name!r} must be a boolean.")


class IntField(Field):
    def __init__(self, min=None, max=None, **kwargs):
        super().__init__(**kwargs)
        self.min = min
        self.max = max

    def validate(self, data):
        super().validate(data)
        if self.data_name not in data:
            return
        value = data[self.data_name]
        if not isinstance(value, int):
            raise exceptions.ValidationError(f"{self.data_name!r} must be an integer.")
        if self.min is not None and value < self.min:
            raise exceptions.ValidationError(f"{self.data_name!r} must be greater than or equal to {self.min}.")
        if self.max is not None and value > self.max:
            raise exceptions.ValidationError(f"{self.data_name!r} must be less than or equal to {self.max}.")


class CharField(Field):
    def validate(self, data):
        super().validate(data)
        if self.data_name not in data:
            return
        value = data[self.data_name]
        if not isinstance(value, str):
            raise exceptions.ValidationError(f"{self.data_name!r} must be a string.")


class PrimaryKey(Field):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        super().validate(data)
        value = data[self.name]
        if not isinstance(value, int):
            raise exceptions.ValidationError(f"{self.name!r} must be an integer.")


class Reference(Field):
    def __init__(self, types=None, **kwargs):
        super().__init__(**kwargs)
        self.types = types

    @property
    def data_name(self):
        return f'{self.name}_id'

    def from_data(self, data):
        value = data.get(self.data_name)
        if value is None:
            return None

        from .engine import Entity
        return Entity.manager.get_entity('metadata', value)

    def to_data(self, value):
        from .engine import Entity
        if isinstance(value, Entity):
            return value.pk
        if value is None:
            raise exceptions.empty
        return value

    def validate(self, data):
        super().validate(data)
        if self.data_name not in data:
            return
        value = data[self.data_name]
        if not isinstance(value, int):
            raise exceptions.ValidationError(f"{self.data_name!r} must be an integer.")

        from .engine import Entity
        entity = Entity.manager.get_entity('metadata', value)
        if entity is None:
            raise exceptions.ValidationError(f"{self.data_name!r} is not an existing entity.")
        if self.types is not None and entity.type not in self.types:
            raise exceptions.ValidationError(f"{self.data_name!r} cannot point to an entity of this type.")
