from src.stack import Stack


def calculate_span(stock_price: list):
    if len(stock_price) == 0:
        raise ValueError("The list cannot be an empty list")

    if not isinstance(stock_price, list):
        raise ValueError("The `stocks_prices` must be a list")

    if not all([isinstance(i, int) for i in stock_price]):
        raise ValueError("All values must be integers")

    s = Stack(len(stock_price) + 1)
    s.push(0)
    span = [0] * len(stock_price)
    for idx, i in enumerate(stock_price):
        while not s.empty() and stock_price[s.top.value] <= i:
            v = s.pop()
        if (s.empty()):
            span[idx] = idx + 1
        else:
            span[idx] = idx - s.top.value
        s.push(idx)
    return span


if __name__ == "__main__":
    span = calculate_span([100, 80, 60, 70, 60, 75, 85])
    print(span)
