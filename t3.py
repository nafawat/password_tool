def pass_gen():
    print("PASSWORD GENERATOR --->")

import random
import string

def check_password_strength(password):
    # Initialize criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def generate_complex_password(length=106):
    # 1. Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    
    # 2. Guarantee at least one of each type
    guarantee = [
        random.choice(lower),
        random.choice(upper),
        random.choice(num),
        random.choice(symbols)
    ]
    
    # 3. Create a pool for the remaining characters
    all_chars = lower + upper + num + symbols
    
    # 4. Generate the remaining characters
    # We subtract 4 because we already guaranteed 4 characters
    remaining_length = length - len(guarantee)
    remaining_chars = random.choices(all_chars, k=remaining_length)
    
    # 5. Combine the guaranteed characters with the random remainder
    password_list = guarantee + remaining_chars
    
    # 6. SHUFFLE the entire list to make the guaranteed characters random positions
    random.shuffle(password_list)
    
    # 7. Join and return the password
    return "".join(password_list)

# Example usage:

le = int(input("ENTER THE LENGTH THAT U WANT : "))
complex_pass = generate_complex_password(le)
strength_pass= check_password_strength(complex_pass)
print(f"Generated Password: {complex_pass}")
print(f"Password: {strength_pass}")
