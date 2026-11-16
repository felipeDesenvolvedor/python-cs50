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
        listCounted.append(f'{items.count(i)} {i.upper()}')

    collection = set(listCounted)
    listCounted = list(collection)
    listCounted.sort()

    return '\n'.join(listCounted)

if __name__ == "__main__":
    main()