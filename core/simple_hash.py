import hashlib
from datetime import datetime, timezone


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


def hash_with_salt_and_iterations(input_value, salt, num_iterations=1):
    # Combine the input value and the salt
    combined = f"{input_value}{salt}".encode()

    # Create a SHA-256 hash of the combined input and salt
    hash_object = hashlib.sha256(combined)

    # Perform the hashing process a number of times
    for _ in range(num_iterations - 1):
        hash_object = hashlib.sha256(hash_object.digest())

    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()


def compare_hashes(input_value, salt, hashed_value):
    # Hash the input value with the salt
    new_hashed_value = hash_with_salt(input_value, salt)

    # Compare the new hashed value with the original hashed value
    return f"Comparison Passes: {new_hashed_value == hashed_value}"


def main():
    # Example input to hash
    input_value = "example_password"

    # Generate a salt that includes the current UTC time
    salt = generate_salt()

    # Hash the input with the generated salt
    hashed_value = hash_with_salt(input_value, salt)

    print(f"Salt: {salt}")
    print(f"Hashed Value: {hashed_value}")

    # Compare the hashed value with a new hashed value
    print("Comparing hashed value with new hashed value...")
    print(compare_hashes(input_value, salt, hashed_value))


if __name__ == "__main__":
    main()
