class Item:
    def __init__(self, item_id, item_name, item_price, quantity_available):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.quantity_available = quantity_available

    def calculate_price(self, qoic):
        if(self.quantity_available >= qoic):
            self.quantity_available -= qoic
            return(self.item_price*qoic)
        else:
            return(0)


class Store:
    def __init__(self, item_list):
        self.item_list = item_list

    def generate_bill(self, items):
        bill = 0
        for item in items:
            for itemobj in self.item_list:
                if(itemobj.item_name == item):
                    bill += itemobj.calculate_price(items[item])
        return(bill)


if __name__ == "__main__":
    ilist = []
    count = int(input())
    for _ in range(count):
        item_id = int(input())
        item_name = input()
        item_price = int(input())
        quantity_available = int(input())
        i = Item(item_id, item_name, item_price, quantity_available)
        ilist.append(i)
    s = Store(ilist)
    items = {}
    item_count = int(input())
    for _ in range(item_count):
        name = input()
        quantity = int(input())
        items[name] = quantity
    print(ilist[0].calculate_price(2))
    print(s.generate_bill(items))
