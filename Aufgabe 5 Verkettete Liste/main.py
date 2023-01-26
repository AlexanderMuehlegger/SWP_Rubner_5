from MyList import VerketteteListe
def main():
    myList = VerketteteListe()
    print(myList.add("Hallo1"))
    print(myList.add("Hallo2"))
    print(myList.add("Hallo3"))
    print(myList.add("Hallo4"))
    print(myList.add("Hallo5"))

    print()

    # myList.clear()
    print(myList.getObjByIndex(1))
    print(myList.insert("Hallo3", "Hallo3-"))

    print()

    print("Length: " + str(myList.length))

    myList.printList()
    print("----------------------")

    print(myList.delete("Hallo3-"))

    print("-----------------------")

    myList.printList()

    print(myList.contains("Hallo3"))
    print(myList.indexOf("Hallo2"))

    print("Length: " + str(myList.length))

    print(myList.getLastNode().getObj())

if __name__ == '__main__':
    main()