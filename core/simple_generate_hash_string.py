from utils import append_the_stuff

from simple_hash import (
    generate_salt,
    hash_with_salt_and_iterations,
)

# Run from `core` directory:
# filename = "output/password_output.txt"

# Run from `root` directory:
filename = "core/output/password_output.txt"

hashing_algorithm = "SimpleHashAlgorithm"

append_the_stuff(filename, "\n")

password = "1234test"
append_the_stuff(filename, password)

salt = generate_salt()
append_the_stuff(filename, salt)

num_iterations = 1000
append_the_stuff(filename, f"Iterations: {num_iterations}")

hashed_value = hash_with_salt_and_iterations(password, salt, num_iterations)
append_the_stuff(filename, hashed_value)

append_the_stuff(
    filename, f"{hashing_algorithm}${salt}${num_iterations}${hashed_value}"
)
