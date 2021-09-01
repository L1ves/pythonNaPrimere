school_list = ["Matematica", "Geometry", "Russian lang", "Biology", "Geograpy", "Informatic"]

index_from_client =  school_list.index(input("Make youre choice: "))
#school_list.pop(index_from_client)
del school_list[index_from_client]
print("I delete youre choice", school_list)


