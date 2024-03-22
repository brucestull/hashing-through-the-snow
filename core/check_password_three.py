from utils import append_the_stuff

from simple_hash import (
    generate_salt,
    hash_with_salt_and_iterations,
)

hashing_algorithm = "Seth_simple_algorithm"


filename = "check_password_three_output.txt"

append_the_stuff(filename, "\n")

password = "1234test"
append_the_stuff(filename, password)

salt = generate_salt()
append_the_stuff(filename, salt)
# salt = "2024-03-21T23:08:07.296550+00:00"

num_iterations = 10000000
append_the_stuff(filename, f"Iterations: {num_iterations}")

hashed_value = hash_with_salt_and_iterations(password, salt, num_iterations)
append_the_stuff(filename, hashed_value)

append_the_stuff(
    filename, f"{hashing_algorithm}${salt}${num_iterations}${hashed_value}"
)

# stored_hash = "43140717d08b2506dfca67e527567dd6f5f97d3b972a76d60636f331ca65900e"

# append_the_stuff(filename, f"Comparison: {hashed_value == stored_hash}")
