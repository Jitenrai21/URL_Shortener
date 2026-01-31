import random
import string
from .models import ShortURL


def generate_short_key(length=6):
    """
    Generate a unique short key using base62 encoding (alphanumeric characters).
    
    Args:
        length (int): Length of the short key (default: 6)
    
    Returns:
        str: A unique short key
    """
    # Base62 characters: 0-9, a-z, A-Z
    base62_chars = string.ascii_letters + string.digits
    
    max_attempts = 100
    for _ in range(max_attempts):
        # Generate a random short key
        short_key = ''.join(random.choices(base62_chars, k=length))
        
        # Check if this key already exists
        if not ShortURL.objects.filter(short_key=short_key).exists():
            return short_key
    
    # If we couldn't generate a unique key after max_attempts, increase length
    return generate_short_key(length + 1)


def encode_base62(num):
    """
    Encode a number to base62 string.
    
    Args:
        num (int): Number to encode
    
    Returns:
        str: Base62 encoded string
    """
    base62_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    if num == 0:
        return base62_chars[0]
    
    encoded = []
    while num > 0:
        num, remainder = divmod(num, 62)
        encoded.append(base62_chars[remainder])
    
    return ''.join(reversed(encoded))


def decode_base62(encoded):
    """
    Decode a base62 string to number.
    
    Args:
        encoded (str): Base62 encoded string
    
    Returns:
        int: Decoded number
    """
    base62_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    num = 0
    for char in encoded:
        num = num * 62 + base62_chars.index(char)
    
    return num
