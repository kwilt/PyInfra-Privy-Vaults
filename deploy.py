from pyinfra.operations import files
from getpass import getpass
import privy
from pathlib import Path

password = getpass('Enter decryption password: ')

def get_secret(encrypted_secret):
    secret_filepath = Path(f"vault/{encrypted_secret}")
    with open(secret_filepath, "rb") as secret:
        decrypted_secret = privy.peek(secret.read().decode("utf-8"), password)
        if isinstance(decrypted_secret, bytes):
            return decrypted_secret.decode("utf-8")
        return decrypted_secret

your_encrypted_value = get_secret("encrypted_value_filename")

files.template(
  name="Create file from template",
  src="templates/template_example.j2",
  dest="/path/to/destination",
  your_encrypted_value=your_encrypted_value,
)
