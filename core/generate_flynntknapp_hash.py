import hashlib
from utils import append_the_stuff
from simple_hash import generate_salt, hash_with_salt_and_iterations
import base64

filename = "check_flynntknapp_password_output.txt"

append_the_stuff(filename, "\n")

password = "01"
append_the_stuff(filename, password)

iterations = 390000
append_the_stuff(filename, f"Iterations: {iterations}")

salt = generate_salt()
append_the_stuff(filename, salt)

generated_hash = hashlib.pbkdf2_hmac(
    "sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations
)
generated_hash64 = base64.b64encode(generated_hash)
append_the_stuff(
    filename,
    f"Generated Hash: {generated_hash64.decode()}",
)
