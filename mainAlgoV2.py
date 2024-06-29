from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import math, statistics


class Trader:


    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        result = {}

        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():

            if product == 'PEARLS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                acceptable_price = statistics.mean(order_depth.buy_orders.keys())
                acceptable_price += statistics.mean(order_depth.sell_orders.keys())
                acceptable_price /= 2

                # using this constant instead of above logic for price of pearls
                # you can always change to above again
                acceptable_price = 10000
                
                if product not in state.position:
                    state.position[product] = 0
                
                numTradables = 0
                for price in order_depth.sell_orders.keys():
                    if price < acceptable_price:
                        numTradables += 1
                
                cpy = order_depth.sell_orders.copy()
                while len(order_depth.sell_orders) > 0 and state.position[product] < 20 and numTradables > 0:
                    best_ask = min(cpy.keys())
                    # best_ask_volume = order_depth.sell_orders[best_ask]
                    # tradingAmount = -best_ask_volume
                    tradingAmount = 20 - state.position[product]
                    if best_ask < acceptable_price:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))
                    cpy.pop(best_ask)
                    numTradables -= 1

                numTradables = 0
                for price in order_depth.buy_orders.keys():
                    if price > acceptable_price:
                        numTradables += 1

                cpy = order_depth.buy_orders.copy()
                while len(order_depth.buy_orders) != 0 and state.position[product] > -20 and numTradables > 0:
                    best_bid = max(cpy.keys())
                    # best_bid_volume = order_depth.buy_orders[best_bid]
                    # tradingAmount = -best_bid_volume
                    tradingAmount = -20 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))
                    cpy.pop(best_bid)
                    numTradables -= 1

                result[product] = orders
        
            if product == 'BANANAS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                acceptable_price = statistics.mean(order_depth.buy_orders.keys())
                acceptable_price += statistics.mean(order_depth.sell_orders.keys())
                acceptable_price /= 2

                acceptable_price = min(order_depth.sell_orders.keys())
                acceptable_price += max(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price /= 7

                if product not in state.position:
                    state.position[product] = 0

                numTradables = 0
                for price in order_depth.sell_orders.keys():
                    if price < acceptable_price:
                        numTradables += 1

                cpy = order_depth.sell_orders.copy()
                while len(order_depth.sell_orders) > 0 and state.position[product] < 20 and numTradables > 0:
                    best_ask = min(cpy.keys())
                    # best_ask_volume = order_depth.sell_orders[best_ask]
                    # tradingAmount = -best_ask_volume
                    tradingAmount = 20 - state.position[product]
                    if best_ask < acceptable_price:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))
                    cpy.pop(best_ask)
                    numTradables -= 1

                numTradables = 0
                for price in order_depth.buy_orders.keys():
                    if price > acceptable_price:
                        numTradables += 1

                cpy = order_depth.buy_orders.copy()
                while len(order_depth.buy_orders) != 0 and state.position[product] > -20 and numTradables > 0:
                    best_bid = max(cpy.keys())
                    # best_bid_volume = order_depth.buy_orders[best_bid]
                    # tradingAmount = -best_bid_volume
                    tradingAmount = -20 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))
                    cpy.pop(best_bid)
                    numTradables -= 1

                result[product] = orders

                
            if product == 'COCONUTS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                acceptable_price = statistics.mean(
                    order_depth.buy_orders.keys())
                acceptable_price += statistics.mean(
                    order_depth.sell_orders.keys())
                acceptable_price /= 2

                # using this constant instead of above logic for price of pearls
                # you can always change to above again
                acceptable_price = 8000

                acceptable_price = min(order_depth.sell_orders.keys())
                acceptable_price += max(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price /= 7

                if product not in state.position:
                    state.position[product] = 0

                numTradables = 0
                for price in order_depth.sell_orders.keys():
                    if price < acceptable_price:
                        numTradables += 1

                cpy = order_depth.sell_orders.copy()
                while len(order_depth.sell_orders) > 0 and state.position[product] < 600 and numTradables > 0:
                    best_ask = min(cpy.keys())
                    # best_ask_volume = order_depth.sell_orders[best_ask]
                    # tradingAmount = -best_ask_volume
                    tradingAmount = 600 - state.position[product]
                    if best_ask < acceptable_price:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))
                    cpy.pop(best_ask)
                    numTradables -= 1

                numTradables = 0
                for price in order_depth.buy_orders.keys():
                    if price > acceptable_price:
                        numTradables += 1

                cpy = order_depth.buy_orders.copy()
                while len(order_depth.buy_orders) != 0 and state.position[product] > -600 and numTradables > 0:
                    best_bid = max(cpy.keys())
                    # best_bid_volume = order_depth.buy_orders[best_bid]
                    # tradingAmount = -best_bid_volume
                    tradingAmount = -600 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))
                    cpy.pop(best_bid)
                    numTradables -= 1

                result[product] = orders

            if product == 'PINA_COLADAS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                acceptable_price = statistics.mean(
                    order_depth.buy_orders.keys())
                acceptable_price += statistics.mean(
                    order_depth.sell_orders.keys())
                acceptable_price /= 2

                # using this constant instead of above logic for price of pearls
                # you can always change to above again
                acceptable_price = 15000

                acceptable_price = min(order_depth.sell_orders.keys())
                acceptable_price += max(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price += max(order_depth.sell_orders.keys())
                acceptable_price += min(order_depth.buy_orders.keys())
                acceptable_price /= 7

                if product not in state.position:
                    state.position[product] = 0

                numTradables = 0
                for price in order_depth.sell_orders.keys():
                    if price < acceptable_price:
                        numTradables += 1

                cpy = order_depth.sell_orders.copy()
                while len(order_depth.sell_orders) > 0 and state.position[product] < 300 and numTradables > 0:
                    best_ask = min(cpy.keys())
                    # best_ask_volume = order_depth.sell_orders[best_ask]
                    # tradingAmount = -best_ask_volume
                    tradingAmount = 300 - state.position[product]
                    if best_ask < acceptable_price and state.position['COCONUTS'] > 0:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))
                    cpy.pop(best_ask)
                    numTradables -= 1

                numTradables = 0
                for price in order_depth.buy_orders.keys():
                    if price > acceptable_price:
                        numTradables += 1

                cpy = order_depth.buy_orders.copy()
                while len(order_depth.buy_orders) != 0 and state.position[product] > -300 and numTradables > 0:
                    best_bid = max(cpy.keys())
                    # best_bid_volume = order_depth.buy_orders[best_bid]
                    # tradingAmount = -best_bid_volume
                    tradingAmount = -300 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))
                    cpy.pop(best_bid)
                    numTradables -= 1

                result[product] = orders



        return result