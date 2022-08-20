

def worker_get_product(product):
    product_name = str(product).split()
    for i in product_name:
        if i.find('_') == 0:
            return i[1:]


def worker_append_product_to_order(product):
    pass


def worker_complete_order():
    pass


def worker_remove_order():
    pass


def worker_check_completed_orders():
    pass


def worker_check_actual_orders():
    pass
