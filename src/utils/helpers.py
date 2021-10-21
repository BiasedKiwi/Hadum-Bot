import difflib

def get_similar(arr: list, *, input_: str):
    """Compares input with a list to find a closest match given a string

    Args:
        arr (list): List of Possible results
        input (str): Piece of string to compare with given list.

    Returns:
        list: Matches
    """
    try:
        return difflib.get_close_matches(input_, arr, n=1)[0]
    except IndexError:
        return None
        

def main():
    print("###")
    

if __name__ == "__main__":
    main()
    
