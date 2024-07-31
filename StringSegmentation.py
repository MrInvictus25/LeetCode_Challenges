"""You are provided with a large string and a dictionary of the words. You have to find if the input string can be
segmented into words using the dictionary or not. """
def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        print(i)
        first_str = s[0:i] # The first substring will check each point in the large string from s[0:i]
        print(first_str)
        if first_str in dictionary:
            second_str = s[i:]
            print("This is the second str", second_str)
            if (
                not second_str # if second substring is of zero length
                or second_str in dictionary
                #or can_segment_str(second_str, dictionary)
            ):
                print("True")
                return True
    print("False")
    return False


s = "datacamp"
dictionary = ["data", "camp", "cam", "lack"]
can_segment_str(s, dictionary)
# True


