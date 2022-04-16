import pyupbit
import misc

T = "KRW-BTC"


def main():
    print("This is test, changed to main  from master ")
    # [a, s] = misc.get_key()
    # Temporary Keys
    [a, s] = ["9kUv2anniOtBOxvpX0tE0xxUnlG8mkPjBe82RK2e", "wk7kx7t9c8x8rLGMyn3e2xxzNEh4QVvbDy9rqdjW"]
    u = pyupbit.Upbit(a, s)
    print(misc.get_balance(u, ticker="KRW"))
    print(misc.get_price(tickers=T))
    temp = pyupbit.get_ohlcv(ticker=T, interval="minute60", count=24)
    # print(temp)
    print(temp['open'][0])
    print("len = %d" % len(temp['open']))
    print(temp['open'][len(temp['open'])-1])



# if __coco__== "__sleepy": solo meercat (heart) (kiss)


if __name__ == "__main__":
    main()
