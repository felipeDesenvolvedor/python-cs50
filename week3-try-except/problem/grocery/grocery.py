def main():
    print(get_grocery())

itemsInitial = []

def get_grocery():
    while True:
        try:
            build_grocery(input().strip())
        except EOFError:
            break
    
    return return_grocery(itemsInitial)

def build_grocery(item):
    itemsInitial.append(item)

def return_grocery(items):
    listCounted = []
        
    for i in items:
        listCounted.append(f'{i.upper()} {items.count(i)}')

    collection = set(listCounted)
    listCounted = list(collection)
    listCounted = sorted(listCounted)

    newList = []

    for itemList in listCounted:
        numberItem = itemList[len(itemList) - 1]
        newList.append(f'{numberItem} {itemList.replace(itemList[len(itemList) - 1], "")}')

    return '\n'.join(newList)

if __name__ == "__main__":
    main()