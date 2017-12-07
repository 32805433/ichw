# currency.py
# Qiuyu Ren
# December 6th, 2017
"""Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange."""


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    s = get_str(currency_from, currency_to, amount_from)
    return get_value(s)


def get_str(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name
    for the original and new currencies. If the query is invalid, both
    old-amount and new-amount will be empty, while "success" will be followed
    by the value false.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen
    d = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' +
                currency_from + '&to=' + currency_to + '&amt=' +
                str(amount_from))
    dstr = d.read()
    d.close()
    return(dstr.decode('ascii'))


def test_getstr():
    """test the function get_str"""
    assert(get_str('USD', 'EUR', 2.5)[-41:] ==
           ' Euros", "success" : true, "error" : "" }')


def get_value(s):
    """Returns: amount of currency after exchanging.

    In this get_value, the user is extracting the value of the amount
    of currency after exchanging from the JSON string which is a
    response to a currency query.

    The value returned has the type float.

    Parameter s: the JSON string
    Precondition: s is a JSON string which is a response to a
    valid currency query."""
    c = s.find(':')
    c = s.find(':', c+1)
    ss = s[c+3:]
    c = ss.find(' ')
    return float(ss[:c])


def test_getvalue():
    """test the function get_value"""
    assert(get_value(':  +-: "2.12345 abc') == 2.12345)


def testAll():
    """test all cases"""
    test_getstr()
    test_getvalue()
    print("All tests passed")
