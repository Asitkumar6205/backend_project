from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import SupermarketModelSerializer
import logging as log

class CheckoutView(CreateAPIView):

    def __init__(self):
        # Pricing rules
        self.prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        # Special offers
        self.special_prices = {
            'A': (3, 130),  # 3 for 130
            'B': (2, 45)    # 2 for 45
        }

    def calculate_total(self, items):

        # Count occurrences of each item
        item_counts = {}
        for item in items:
            if item not in self.prices:
                log.warning(f" Item '{item}' is not recognized and will be ignored.")
                continue
            item_counts[item] = item_counts.get(item, 0) + 1

        # Calculate total price
        total = 0
        for item, count in item_counts.items():
            if item in self.special_prices:
                group_size, group_price = self.special_prices[item]
                total += (count // group_size) * group_price
                total += (count % group_size) * self.prices[item]
            else:
                total += count * self.prices[item]

        return total

    serializer_class = SupermarketModelSerializer
    def post(self, request, *args, **kwargs):
        items = self.request.POST["item_lists"]
        result = self.calculate_total(items)

        return Response({'response': result}, status=status.HTTP_200_OK)  


