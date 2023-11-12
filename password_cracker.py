import hashlib
import re


def identify_hash_type(inputHash):
    if re.match(r"^[0-9a-fA-F]{32}$", inputHash):
        return "md5"
    elif re.match(r"^[0-9a-fA-F]{40}$", inputHash):
        return "sha1"
    elif re.match(r"^[0-9a-fA-F]{64}$", inputHash):
        return "sha256"
    elif re.match(r"^[0-9a-fA-F]{32}:[0-9a-fA-F]{32}$", inputHash):
        return "ntlm"
    else:
        return None


def crackHash(inputHash):
    hash_type = identify_hash_type(inputHash)

    if hash_type:
        try:
            passFile = open("wordlist.txt", "r")
        except FileNotFoundError:
            print("Could not find the wordlist file.")
            return

        for password in passFile:
            encPass = password.encode("utf-8")
            if hash_type == "md5":
                digest = hashlib.md5(encPass.strip()).hexdigest()
            elif hash_type == "sha1":
                digest = hashlib.sha1(encPass.strip()).hexdigest()
            elif hash_type == "sha256":
                digest = hashlib.sha256(encPass.strip()).hexdigest()
            elif hash_type == "ntlm":
                import ntlm
                digest = ntlm.compute_lmhash(encPass.strip()) + ':' + ntlm.compute_nthash(encPass.strip())

            if digest == inputHash:
                print("Password Cracked Successfully: " + password)
                return

        print("Password not found in the wordlist.")
    else:
        print("Unsupported or invalid hash format.")


if __name__ == '__main__':
    print('')
    print("WELCOME TO PassCracker")
    print('')
    inputHash = input("Enter the target hash: ")
    hash_type = identify_hash_type(inputHash)
    if hash_type:
        print('')
        print(f"Identified hash type: {hash_type}")
        crackHash(inputHash)
    else:
        print("Unsupported or invalid hash format.")
