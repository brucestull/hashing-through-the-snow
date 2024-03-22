def append_the_stuff(filename, value):
    """
    Append the argument value to a file.

    Args:
    value: The value to append to the file.
    """

    # Open a file in append mode to add new data without deleting old data
    with open(filename, "a") as file:
        # Write the value to file, followed by a newline character to keep entries separate
        file.write(f"{value}\n")

        # Optional: flush the file to ensure data is written, useful in long loops
        file.flush()
