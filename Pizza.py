#!/usr/bin/env python


def print_shopping_cart(shopping_cart):
    subtotal = 0.00
    tax_rate = .075
    tax = 0.00
    total = 0.00
    divider = '                 ---------'

    print("Your Shopping Cart:")
    for [item, price] in shopping_cart:
        print('  {:15s} ${:6.2f}'.format(item, price))
        subtotal += price
    tax = round(subtotal * tax_rate, 2)
    total = subtotal + tax
    print(divider)
    print('  Subtotal:       ${:6.2f}'.format(subtotal))
    print('  Tax:            ${:6.2f}'.format(tax))
    print(divider)
    print('  Total:          ${:6.2f}'.format(total))
    print(divider)


def print_menu(choices):
    print('Available pizzas:')
    for (choice, price) in choices:
        print('  {:15s} ${:6.2f}'.format(choice, price))


def get_selection(choices):
    user_input = input('Which pizza would you like to add: ')

    for choice in choices:
        if user_input.lower() in choice[0].lower():
            return choice

    return [None, 0.00]


def main():
    shopping_cart = []
    choices = [["Cheese", 15.99],
               ["Pepperoni", 19.99],
               ["Deluxe", 23.99],
               ["Done", 0.00]]

    while True:
        print_shopping_cart(shopping_cart)
        print_menu(choices)

        [selection, price] = get_selection(choices)
        if selection is None:
            print("Sorry, we're out of that one.")
            continue
        elif selection == 'Done':
            print_shopping_cart(shopping_cart)
            break
        else:
            shopping_cart.append([selection, price])
            continue


if __name__ == '__main__':
    main()
