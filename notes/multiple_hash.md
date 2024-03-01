# Multiple Hashing Function

[Multiple Hashing Function](https://chat.openai.com/share/c6745e63-f59b-49a4-8d5f-c92b18c02231)

To modify the `hash_with_salt` function to hash the input multiple times, you can introduce a loop that repeatedly hashes the result of the previous hash operation. This approach can be useful for adding additional security by making brute-force attacks more computationally expensive. Here's how you can modify the function to include a parameter for specifying the number of times the input should be hashed:

```python
import hashlib

def hash_with_salt(input_value, salt, num_hashes=1):
    # Combine the input value and the salt
    combined = f"{input_value}{salt}".encode()

    # Initialize the hash object with the combined input and salt
    hash_object = hashlib.sha256(combined)

    # Perform additional hash iterations
    for _ in range(num_hashes - 1):
        # Take the current hash, encode it, and hash it again
        hash_object = hashlib.sha256(hash_object.digest())

    # Return the hexadecimal representation of the final digest
    return hash_object.hexdigest()
```

In this modified version, the `num_hashes` parameter controls how many times the hashing process is applied. The default value is `1`, meaning that if the parameter is not specified, the function will behave as it originally did, applying the hash operation only once. For each additional hash iteration (beyond the first), the function takes the digest of the current hash object, re-encodes it, and hashes it again.

This approach effectively increases the computational work needed to reverse the hashing process, adding a layer of security. However, it's important to balance security with performance, as excessively high values for `num_hashes` can significantly slow down the hashing process.