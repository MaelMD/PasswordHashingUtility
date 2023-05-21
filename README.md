# PasswordHashingUtility

This is a Python utility for password hashing using the pbkdf2_sha256 algorithm from the Passlib library.

## Features

- Securely hashes passwords using the pbkdf2_sha256 algorithm.
- Provides a function for comparing a cracked password hash with a newly generated hash.
- Supports customization of hashing rounds and salt.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MaelMD/password-hashing-utility.git
   
2. Install the required dependencies:

   ```pip install passlib

## Usage

1. Import the necessary modules:

   ```python
   from passlib.hash import pbkdf2_sha256
   from base64 import b64decode
   from passlib.utils.binary import ab64_encode

2. Use the hashAndCompare(crackedHash) function to compare a cracked password hash with a newly generated hash:

   ```hashAndCompare('get-hash-from=:your-password')

