def main():
    from MyList import VerketteteListe
    myList = VerketteteListe()
    print(myList.add("Hallo1"))
    print(myList.add("Hallo2"))
    print(myList.add("Hallo3"))
    print(myList.add("Hallo4"))
    print(myList.add("Hallo4"))
    print(myList.add("Hallo4"))
    print(myList.add("Hallo4"))
    print(myList.add("Hallo5"))
    
    print(myList)

    print(myList[1])

    myList = myList.shuffle()
    
    print("===============================")
    # myList.clear()
    print(myList.insert("Hallo3", "Hallo3-"))

    print()

    print("Length: " + str(len(myList)))

    print(myList)
    print("----------------------")

    print(myList.delete("Hallo3-"))
    print(myList.remove("Hallo4"))

    print("-----------------------")

    print(myList)

    print(myList.contains("Hallo3"))
    print(myList.indexOf("Hallo2"))

    print("Length: " + str(len(myList)))

    print(myList.getLastNode().getObj())

if __name__ == '__main__':
    main()