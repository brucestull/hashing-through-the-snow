import hashlib
from datetime import datetime, timezone
from utils import append_the_stuff


def generate_salt():
    utc_time = datetime.now(timezone.utc).isoformat()
    # You can add any other unique identifier to the salt, if necessary
    return utc_time


def hash_with_salt(input_value, salt):
    # Combine the input value and the salt
    combined = f"{input_value}{salt}".encode()

    # Create a SHA-256 hash of the combined input and salt
    hash_object = hashlib.sha256(combined)

    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()


def hash_with_salt_and_iterations(password, salt, num_iterations=1):
    # Combine the input value and the salt
    combined = f"{password}{salt}".encode()

    # Create a SHA-256 hash of the combined input and salt
    hash_object = hashlib.sha256(combined)

    # Perform the hashing process a number of times
    for _ in range(num_iterations - 1):
        hash_object = hashlib.sha256(hash_object.digest())

    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()


def compare_hashes(password, salt, hashed_value):
    # Hash the input value with the salt
    new_hashed_value = hash_with_salt(password, salt)

    # Compare the new hashed value with the original hashed value
    # return f"Comparison Passes: {new_hashed_value == hashed_value}"
    return (
        "Comparison Passes!"
        if new_hashed_value == hashed_value
        else "Comparison Fails!"
    )


# Run from `core` directory:
# filename = "output/simple_hash_output.txt"

# Run from `root` directory:
filename = "core/output/simple_hash_output.txt"


def main():
    append_the_stuff(filename, "\n")
    # Example input to hash
    password = "letmein"
    append_the_stuff(filename, password)
    print(f"Password: {password}")

    # Generate a salt that includes the current UTC time
    salt = generate_salt()
    append_the_stuff(filename, salt)
    print(f"Salt: {salt}")

    # Hash the input with the generated salt
    hashed_value = hash_with_salt(password, salt)
    append_the_stuff(filename, hashed_value)
    print(f"Hashed Value: {hashed_value}")

    # Compare the hashed value with a new hashed value
    print("Comparing hashed value with new hashed value...")
    result = compare_hashes(password, salt, hashed_value)
    append_the_stuff(filename, result)
    print(compare_hashes(password, salt, hashed_value))


if __name__ == "__main__":
    main()
