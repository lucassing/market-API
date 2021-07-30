from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Category, Product, Basket, ItemBasket
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[
        UniqueValidator(queryset=Category.objects.all(),
                        message='Category already exist!')])

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)


class ItemBasketSerializer(serializers.ModelSerializer):
    basket = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = ItemBasket
        fields = ["basket", 'product', 'qty']

    def validate(self, data):
        if data['product'].stock < data['qty']:
            raise serializers.ValidationError("Not enough stock!")
        return data

    def validate_qty(self, value):
        """
        Check that qty is valid
        """
        if value == 0:
            raise serializers.ValidationError("Qty must be more than 0")
        return value

    def create(self, validated_data):
        """Creates a new basket object for the user the first time it adds an Item to it"""
        validated_data['basket'] = \
            Basket.objects.get_or_create(user=self.context["request"].user)[0]
        return super().create(validated_data)


class BasketSerializer(serializers.ModelSerializer):
    class ItemBasketSer(serializers.ModelSerializer):
        class Meta:
            model = ItemBasket
            fields = ["qty", "product", "id"]
            depth = 1

    items = ItemBasketSer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ["items", ]
        depth = 1
