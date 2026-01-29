class AmazonFreshAgent:
    def calculate_cost(self, ingredients):
        # Simula la ricerca dei prezzi su Amazon Fresh
        print(f"[Amazon Agent] Ricerca prezzi per: {ingredients}...")
        price_map = {"uova": 3.50, "latte": 1.50, "burro": 2.00}
        total = sum(price_map.get(item, 1.00) for item in ingredients)
        return f"{total:.2f}€"
