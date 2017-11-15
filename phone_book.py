#here we use dictionaries to build a phone_book

phone_book={
    'ashwin':'9998887766',
    'ashish':'8899776655',
    'joy':'7778889990',
    'sherly':'7898767890',
    'adam':'123-456-7890'
    }
def contacts(key):
    print(phone_book[key])

print("Enter the name here :")
k=input()
contacts(k)
