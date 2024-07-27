# PassHash

This Python script allows you to encrypt (Cypher) and verify passwords (Descypher) using the SHA-3-256 algorithm.

## Description

The script provides an interactive terminal menu with the following options:
1. Encrypt a password to get its hash.
2. Verify a password by comparing it to a hash.
3. Exit the program.
4. Show the help menu.

## Usage

### Requirements

- Python 3.x

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Franmartin09/PassHash.git
    cd PassHash
    ```

2. Run the script:
    ```sh
    python3 script.py
    ```

### Execution

When you run the script, the following menu will be displayed:

```sh
    Usage: 
        1 - Cypher to get HASH
        2 - Verify the password 
        3 - Exit 
        4 - Usage 
```

1. **Encrypt a password:**
    - Select option `1`.
    - Enter the password you want to encrypt.
    - The script will display the hash of the password.

2. **Verify a password:**
    - Select option `2`.
    - Enter a password hash.
    - Enter the password you want to verify.
    - The script will inform you if the password is correct or incorrect.

3. **Exit the program:**
    - Select option `3`.

4. **Show the help menu:**
    - Select option `4`.

## Example

```sh
____________________________________________

Select the option what do you want : 1
Write the password: ********
Hash : e3d7b0c6fb6a7c7a1f0b9d2f1f9e4e8a2f7d7b2a5c3f6d1f4c5e7d1a1b3c4e5
____________________________________________

Select the option what do you want : 2
Write the Hash: e3d7b0c6fb6a7c7a1f0b9d2f1f9e4e8a2f7d7b2a5c3f6d1f4c5e7d1a1b3c4e5
Write the password to verify: ********
The password is correct!
```

## Contributions

Contributions are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the ([LICENSE](https://github.com/Franmartin09/PassHash/blob/main/LICENSE)) file for more details.

---
