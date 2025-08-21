from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        meta = getattr(self, "Meta", None)
        if meta:
            return getattr(meta, "model", None)

        return None

    def create(self, validated_data):
        user_info = (
            {
                "created_by": self.user.id,
                "updated_by": self.user.id,
            }
            if self.user
            else {}
        )
        new_validated_data = {**validated_data, **user_info}
        return super().create(new_validated_data)

    def update(self, instance, validated_data):
        user_info = (
            {
                "updated_by": self.user.id,
            }
            if self.user
            else {}
        )
        new_validated_data = {**validated_data, **user_info}
        return super().update(instance, new_validated_data)


class BaseSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        meta = getattr(self, "Meta", None)
        if meta:
            return getattr(meta, "model", None)

        return None

    def create(self, validated_data):
        user_info = (
            {
                "created_by": self.user.id,
                "updated_by": self.user.id,
            }
            if self.user
            else {}
        )
        new_validated_data = {**validated_data, **user_info}
        return self.model_class.objects.create(**new_validated_data)

    def update(self, instance, validated_data):
        user_info = (
            {
                "updated_by": self.user.id,
            }
            if self.user
            else {}
        )
        new_validated_data = {**validated_data, **user_info}
        return self.model_class.objects.update(**new_validated_data)
