def exchange_money(budget, exchange_rate):
    """
    Calculate the exchanged amount of money based on the budget and the exchange rate.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate the amount left after exchanging a specified value of the budget.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of a set number of bills of a given denomination.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate how many whole bills of a certain denomination can be obtained from an amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount after taking out as many whole bills of a certain denomination as possible.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value in the foreign currency that can be obtained in whole bills.
    """
    actual_exchange_rate = exchange_rate * (1 + spread / 100)  # Adjusting for the exchange fee
    exchanged_amount = exchange_money(budget, actual_exchange_rate)  # Money after exchange
    number_of_bills = get_number_of_bills(exchanged_amount, denomination)  # Number of whole bills
    return get_value_of_bills(denomination, number_of_bills)  # Maximum value in whole bills

