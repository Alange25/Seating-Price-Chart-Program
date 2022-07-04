"""-seating chart program-
   -created by Alexander-
   -04-07-2022-"""

import random

ROW_NUMBER = 6
COLUMN_NUMBER = 4


def display_title():
    """the display title"""
    print("--------------------------------------------")
    print("Seating-Price Chart Program in Python")
    print()
    print("Created by: Alexander")
    print("Created at: 04-16-2022")
    print("Description: The program is designed to")
    print("1 - Create an airplane seating-price chart")
    print("2 - Display the seating-price chart")
    print("3 - Find and display the highest seat price")
    print("4 - Find and display the lowest seat price")
    print("5 - Calculate the average price")
    print("6 - Find ALL seats (row and column) that have the lowest price ")
    print("7 - Find ALL seats (row and column) that have the highest price ")
    print("8 - Find a seat (row and column) based on the price entered by users")
    print("--------------------------------------------")
    print()


def create_seating_price_chart(rows, cols):
    """creating a seating price chart"""
    seats = []
    for row in range(rows):
        row_seats = []
        for col in range(cols):
            row_seats.append(random.randint(500, 1000))
        seats.append(row_seats)
    return seats


def display_seating_price_chart(chart_2d):
    """displaying a seating price chart"""
    print('-------Display Seating Price Chart-------')
    print(f'There are {len(chart_2d)} row and {len(chart_2d[0])} column in the plane\n')
    print()
    for row in chart_2d:
        print(row)
    print('-----------------------------------------\n')


def find_max_value(chart_2d):
    """find the max value"""
    max_price = chart_2d[0][0]
    for row in chart_2d:
        for price in row:
            if price > max_price: max_price = price
    return max_price


def find_min_value(chart_2d):
    """find the min value"""
    min_price = chart_2d[0][0]
    for row in chart_2d:
        for price in row:
            if price < min_price: min_price = price
    return min_price


def calculate_average_price(chart_2d):
    """calculating the average price"""
    rows, cols = len(chart_2d), len(chart_2d[0])
    total = 0
    for row in chart_2d:
        total += sum(row)
    return total / (rows * cols)


def find_seats_with_price(chart_2d, price):
    """find seats with the price you are looking for"""
    seats = []
    for i in range(len(chart_2d)):
        for j in range(len(chart_2d[i])):
            if chart_2d[i][j] == price:
                seats.append([i, j])
    return seats


def display_seat_list(chart_2d):
    """displaying seats with the lowest and highest price"""
    highest_price = find_max_value(chart_2d)
    lowest_price = find_min_value(chart_2d)
    seats = find_seats_with_price(chart_2d, lowest_price)
    print('--Display seat list with lowest price--')
    for seat in seats:
        print(seat)
    print('-----------------------------------------\n')

    seats = find_seats_with_price(chart_2d, highest_price)
    print('--Display seat list with highest price--')
    for seat in seats:
        print(seat)
    print('-----------------------------------------\n')


if __name__ == '__main__':
    # the display title function
    display_title()

    # create and display the seating price chart
    chart_2d = create_seating_price_chart(ROW_NUMBER, COLUMN_NUMBER)
    display_seating_price_chart(chart_2d)

    highest_price = find_max_value(chart_2d)
    print(f'The highest price is ${highest_price}')

    lowest_price = find_min_value(chart_2d)
    print(f'The lowest price is ${lowest_price}')

    average_price = calculate_average_price(chart_2d)
    print(f'The average price is ${average_price:.2f}')

    display_seat_list(chart_2d)

    # getting user input for the program
    while True:
        try:
           try:
               price = int(input('Please enter a price between 500 and 1000: '))
               seats = find_seats_with_price(chart_2d, price)
               for seat in seats:
                   print("--------Display seat list with entered price--------")
                   print(seat)
                   print("---------------------------------------")
                   exit()
               if price < 500 or price > 1000:
                   print("please enter a valid number (between 500 and 1000)")
               if seat not in seats:
                   print()
           except NameError:
               print("--------Display seat list with entered price--------")
               print(f"Cannot find a seat with the price {price}. Please enter price again")
               print("-----------------------------------------")
               continue
        except ValueError:
            print("please enter a valid number (between 500 and 1000)")
            continue

