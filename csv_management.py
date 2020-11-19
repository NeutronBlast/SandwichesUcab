BOLD = '\033[1m'
END = '\033[0m'

from datetime import datetime

def print_all_orders():
    with open("./files/orders.csv") as ref:
        i = 0
        for line in ref:
            if i == 0:
                print("\t\t\t\t"+BOLD + line.strip() + END)
            else:
                print(line.strip())
            i += 1


# Writing in a CSV file
def append_order(order, price):
    date = datetime.today().strftime('%Y-%m-%d')
    with open("./files/orders.csv", "a") as ref:
        ref.write("{}, {}, {}\n".format(order, price, date))
