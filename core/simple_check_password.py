from utils import append_the_stuff

from simple_hash import hash_with_salt, hash_with_salt_and_iterations

# Run from `core` directory:
# filename = "output/password_output.txt"

# Run from `root` directory:
filename = "core/output/password_output.txt"

append_the_stuff(filename, "\n")

password = "1234test"
append_the_stuff(filename, password)

salt = "2024-03-22T12:45:22.892278+00:00"
append_the_stuff(filename, salt)

num_iterations = 1000
append_the_stuff(filename, f"Iterations: {num_iterations}")

stored_hash = "6b90f91b55a72dc175821cb3b8245f6b527eff44d048f8c132b46e0db351d78e"
append_the_stuff(filename, f"Checking against: {stored_hash}")

hashed_value = hash_with_salt_and_iterations(password, salt, num_iterations)
append_the_stuff(filename, hashed_value)

append_the_stuff(filename, f"Comparison: {hashed_value == stored_hash}")
