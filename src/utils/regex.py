"""
Utility functions related to regex. Note: this isn't used yet but will when music will be implemented or when it will need to be used
"""
import re
import sys


def is_youtube_link(txt: str) -> bool:
    """Return true or false if txt is a youtube link

    Args:
        txt (str): String to check

    Returns:
        bool: True if txt is a youtube link, False otherwise
    """
    pattern = r"https?:\/\/(www\.)?(youtube|youtu)\.(com|be)\/?(\w+)?"
    return bool(re.match(pattern, txt))


if __name__ == "__main__":
    foo = is_youtube_link(sys.argv[1])
    print(foo)
