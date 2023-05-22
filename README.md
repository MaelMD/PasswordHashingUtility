# PasswordHashingUtility

This is a Python utility for password hashing using the pbkdf2_sha256 algorithm from the Passlib library.

## Function Arguments

The `hashAndCompare(crackedHash)` function takes two arguments:

1. **crackedHash**: The first argument is the cracked password hash obtained from a website called ["Illicit Services"](https://search.illicit.services). This website searches your email through leaked databases on the web. If a match is found, the associated leaked password will appear in hash form. You need to provide this hash as the first argument of the `hashAndCompare` function.

2. **password**: The second argument is the password you suspect to be leaked. You should provide this password as the second argument of the `hashAndCompare` function.

## Features

- Securely hashes passwords using the pbkdf2_sha256 algorithm.
- Provides a function for comparing a cracked password hash with a newly generated hash.
- Supports customization of hashing rounds and salt.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MaelMD/password-hashing-utility.git
   
2. Install the required dependencies:

   ```python   
   pip install passlib

## Usage

1. Import the necessary modules:

   ```python
   from passlib.hash import pbkdf2_sha256
   from base64 import b64decode
   from passlib.utils.binary import ab64_encode

2. Use the hashAndCompare(crackedHash) function to compare a cracked password hash with a newly generated hash:

   ```hashAndCompare('get-hash-from=:your-password')

