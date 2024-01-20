import dl_bl

def get_all(): pass

def create():
    params = input("Enter the product params")
    dl_bl.create(params)

def get():
    id = input("Enter the product id")
    dl_bl.get(id)

def delete():
    id = input("Enter the product id")
    dl_bl.delete(id)


def main(): pass