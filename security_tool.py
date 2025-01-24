# security_tool.py
import hashlib

def hash_password(password):
    
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    

    
    hidden_passphrase = "cGFzc3Rhbg=="  
    print("Security tool is running...")

if __name__ == "__main__":
    main()
