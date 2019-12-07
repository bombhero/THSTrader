# -*- coding: utf-8 -*-


from THS.THSTrader import THSTrader


if __name__ == "__main__":
    # trader = THSTrader(r"D:/THSTrader/xiadan.exe")    # 连接客户端
    trader = THSTrader(r"D:/THSTrader/xiadan.exe")    # 连接客户端
    # trader.main_wnd.print_control_identifiers()

    print(trader.get_balance())                            # 获取当前可用资金

    print(trader.get_position())                           # 获取当前持有的股票

    print(trader.sell(stock_no="002100", amount=100, price=12.5))  # 卖出股票

    result = trader.buy(stock_no="002100", amount=100, price=11.8)  # 买入股票
    print(result)

    if result["success"] == True:						   # 如果买入下单成功，尝试撤单
        print("撤单测试--->", end="")
        print(trader.cancel_entrust(entrust_no=result["entrust_no"]))

