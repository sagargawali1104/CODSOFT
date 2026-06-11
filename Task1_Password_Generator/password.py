import random
import string

def password_generator():
    print("=== Advanced Password Generator ===")
    
    # Step 1: Ask user for desired length
    length = int(input("Enter desired password length: "))
    
    # Step 2: Ask user for complexity level
    print("\nChoose complexity level:")
    print("1. Only letters")
    print("2. Letters + digits")
    print("3. Letters + digits + symbols")
    choice = int(input("Enter choice (1/2/3): "))
    
    # Step 3: Build character pool based on choice
    if choice == 1:
        characters = string.ascii_letters
    elif choice == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    # Step 4: Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Step 5: Display password
    print("\n✅ Your Generated Password:")
    print(password)
    
    # Step 6: Extra feature — password strength check
    strength = "Weak"
    if any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        strength = "Medium"
    
    print(f"🔒 Password Strength: {strength}")

# Run the generator
password_generator()
