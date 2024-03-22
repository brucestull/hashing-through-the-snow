import hashlib
from utils import append_the_stuff
import base64

# pbkdf2_sha256$390000$GlmgttErVULSljdg54dSZi$bUhF0wWixPqp/TCJ+60kVtJw9Ve/6a9M28Di6HkQ7jo=

# Run from `core` directory:
filename = "output/flynntknapp_output.txt"

# Run from `root` directory:
# filename = "core/output/flynntknapp_output.txt"

append_the_stuff(filename, "\n")

test_password = "01"
append_the_stuff(filename, test_password)

iterations = 390000
append_the_stuff(filename, f"Iterations: {iterations}")

salt = "2024-03-22T12:16:44.878162+00:00"
append_the_stuff(filename, salt)

stored_hash = "P6Ia+JnfLYDvCB/UgBvjkw5ql3qzmDVUyStHl3W75x8="
append_the_stuff(filename, f"stored_hash: {stored_hash}")

hash = hashlib.pbkdf2_hmac(
    "sha256", test_password.encode("utf-8"), salt.encode("utf-8"), iterations
)

hash64 = base64.b64encode(hash)

append_the_stuff(filename, f"Comparison: {hash64.decode() == stored_hash}")
