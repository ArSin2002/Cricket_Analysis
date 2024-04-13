def count_powerful_integers(start, finish, limit, s):
    # Convert s to an integer
    suffix = int(s)

    # Calculate the length of the suffix
    suffix_length = len(s)

    # Calculate the upper limit for the powerful integers
    upper_limit = min(limit, 9)

    count = 0

    # Iterate through each possible suffix
    for current_suffix in range(suffix, upper_limit + 1):
        # Calculate the lowest number with the current suffix
        lowest_number = int(str(current_suffix) + s)

        # Calculate the maximum number with the current suffix
        max_suffix_length = finish // 10**suffix_length
        highest_number = int(str(current_suffix) + "9" * (suffix_length * max_suffix_length))

        # Count the number of powerful integers in the current range
        count += max(0, min(highest_number, finish) - max(lowest_number, start) + 1)

    return count

# Example usage:
start = 182905
finish = 1255574165
limit = 7
s = "11223"
result = count_powerful_integers(start, finish, limit, s)
print(result)
