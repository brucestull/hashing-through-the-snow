from utils import append_the_stuff

from simple_hash import (
    hash_with_salt,
)

append_the_stuff("simple_hash_output.txt", "\n")

password = "1234test"
append_the_stuff("simple_hash_output.txt", password)

salt = "2024-03-21T22:42:46.400061+00:00"
append_the_stuff("simple_hash_output.txt", salt)

stored_hash = "28a6fba6ebb3198a63517d437cc445b1c4a2b378210e1c87cd59e70f154121ec"

hashed_value = hash_with_salt(password, salt)
append_the_stuff("simple_hash_output.txt", hashed_value)

append_the_stuff("simple_hash_output.txt", f"Comparison: {hashed_value == stored_hash}")
