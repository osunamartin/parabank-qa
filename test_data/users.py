import random
import string

# Pre-seeded demo user available on every fresh ParaBank instance
VALID_USER = {
    "username": "john",
    "password": "demo",
}

INVALID_USER = {
    "username": "john",
    "password": "wrong_password",
}


def generate_new_user():
    """Return a dict with unique registration data; call once per test to avoid collisions."""
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "phone": "5551234567",
        "ssn": "123456789",
        "username": f"testuser_{suffix}",
        "password": "Test@1234",
    }
