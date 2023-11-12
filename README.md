# PassCracker

## Overview
PassCracker is a powerful and versatile password-cracking tool designed to decode various cryptographic hash functions commonly used in cybersecurity. Developed using Python, PassCracker provides an efficient and user-friendly solution for security professionals and ethical hackers to test the strength of passwords stored in hash formats.

## Features

- **Multi-Hash Support:** PassCracker supports a wide range of hash algorithms, including md5, sha1, sha256, NTLM, and more, making it adaptable to diverse cybersecurity scenarios.
  
- **User-Friendly Interface:** The program offers a straightforward command-line interface, making it accessible to both experienced security practitioners and those new to password cracking.

- **Dynamic Hash Identification:** PassCracker can automatically identify the hash type based on the provided input, streamlining the cracking process.

- **Efficient Decryption:** Leveraging advanced cryptographic techniques, PassCracker excels in decrypting hashed passwords, demonstrating its effectiveness in penetration testing and security assessments.

## Example Usage

```PowerShell
PS F:\PYTHON PROJECTS> password_cracker.py

WELCOME TO PassCracker

Enter the target hash: bb28ee86eabbbb4004d2fa7326f12bd0

Identified hash type: md5
Password Cracked Successfully: YOU ARE HACKED
```

## How It Works

1. **User Input:** The user inputs the target hash that needs to be cracked.
  
2. **Hash Identification:** PassCracker automatically identifies the hash type, ensuring compatibility with various encryption algorithms.

3. **Decryption Process:** The program employs advanced decryption techniques to decipher the hashed password.

4. **Success Message:** Upon successful decryption, PassCracker displays a success message along with the cracked password.

## Security and Ethics

PassCracker is intended for ethical and legal use, primarily in the field of cybersecurity. It serves as a tool for security professionals to assess and strengthen the security of systems with the explicit consent of the system owners.

**Note:** Unauthorized and malicious use of password cracking tools is strictly prohibited and illegal. Always ensure that you have the legal right and authorization to use PassCracker on any system.

**Disclaimer:** The developers and contributors of PassCracker are not responsible for any misuse or illegal activities carried out with this tool. Use it responsibly and in accordance with applicable laws and regulations.
