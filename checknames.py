'''Check if a name appears in a list or its reverse form'''

def check_name(names, search_name):
    # check if the search name is in the list
    if search_name in names:
        print(f"{search_name} appears in the list: True")
    # check if the search name appears in reverse in the list
    elif search_name[::-1] in names:
        # get the original name from the list using its reversed form
        original_name = names[names.index(search_name[::-1])]
        print(f"{search_name} appears in reverse in the list as {original_name}: True")
    # if the search name is not found or its reversed form is not found, print False
    else:
        print(f"{search_name} doesn't appear in the list or in reverse: False")

def main():
    # define the list of names
    names = ["shani", "ro", "nurielyosef"]
    # search for "inahs" in the list
    check_name(names, "inahs")

if __name__ == '__main__':
    # call the main function
    main()
