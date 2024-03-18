import collections

custom_power = lambda x=0, /, e=1: x ** e
print(custom_power(7, 2))

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    This function calculates the result of (x ** a + y ** b)/c

    :param x: The base value for exponentiation. Default is 0.
    :type x: int
    :param y: The base value for second exponentiation. Default is 0.
    :type y: int
    :param a: The exponent for the base value x. Default is 1
    :type a: int
    :param b: The exponent for the base value y. Default is 1.
    :type b: int
    :param c: The divisor. Default is 1.
    :type c: int
    :return: The result of the equation.
    :rtype: float
    """
    return (x ** a + y ** b) / c
#print(custom_equation.__doc__)
#print(custom_equation.__annotations__)

def fn_w_counter() -> tuple[int, dict]:
    call_counter = collections.defaultdict(int)
    fn_w_counter.total_calls += 1

    caller = getattr(fn_w_counter, '__name__', 'Unknown')

    call_counter[caller] += 1

    return fn_w_counter.total_calls, dict(call_counter)
fn_w_counter.total_calls = 0

#print(fn_w_counter())
#print(fn_w_counter.total_calls)
