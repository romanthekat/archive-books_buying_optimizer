class PurchaseSequence:
    purchases = []

    def add_purchase(self, purchase):
        if not purchase.is_empty_purchase():
            self.purchases.append(purchase)

    def get_total_cost(self):  # TODO calculation caching
        costs = map(lambda purchase: purchase.get_cost(), self.purchases)
        return sum(costs)
