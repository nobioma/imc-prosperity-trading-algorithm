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

                if product not in state.position:
                    state.position[product] = 0
                
                if len(order_depth.sell_orders) > 0 and state.position[product] < 20:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    tradingAmount = -best_ask_volume
                    if -best_ask_volume + state.position[product] >= 20:
                        tradingAmount = 20 - state.position[product]
                    if best_ask < acceptable_price:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))

                if len(order_depth.buy_orders) != 0 and state.position[product] > -20:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    tradingAmount = -best_bid_volume
                    if tradingAmount + state.position[product] <= -20:
                        tradingAmount = -20 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))

                result[product] = orders
            
            
            if product == 'BANANAS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                acceptable_price = statistics.mean(order_depth.buy_orders.keys())
                acceptable_price += statistics.mean(order_depth.sell_orders.keys())
                acceptable_price /= 2

                if product not in state.position:
                    state.position[product] = 0

                if len(order_depth.sell_orders) > 0 and state.position[product] < 20:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    tradingAmount = -best_ask_volume
                    if -best_ask_volume + state.position[product] >= 20:
                        tradingAmount = 20 - state.position[product]
                    if best_ask < acceptable_price:
                        print("BUY", str(tradingAmount) + "x", best_ask)
                        orders.append(Order(product, best_ask, tradingAmount))

                if len(order_depth.buy_orders) != 0 and state.position[product] > -20:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    tradingAmount = -best_bid_volume
                    if tradingAmount + state.position[product] <= -20:
                        tradingAmount = -20 - state.position[product]
                    if best_bid > acceptable_price:
                        print("SELL", str(-tradingAmount) + "x", best_bid)
                        orders.append(Order(product, best_bid, tradingAmount))

                result[product] = orders

        return result