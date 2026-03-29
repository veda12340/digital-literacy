import string

def analyze_password(password):
    # Criteria tracking
    length_ok = len(password) >= 12
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_digit = any(char in string.digits for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Scoring logic
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    # Feedback mapping
    if score <= 2:
        strength = "🔴 WEAK"
        advice = "Your password is too simple. Use more than 12 characters and mix symbols."
    elif score <= 4:
        strength = "🟡 MEDIUM"
        advice = "Getting better! Try adding more unique special characters (!@#$)."
    else:
        strength = "🟢 STRONG"
        advice = "Great job! This password is hard for 'Brute Force' attacks to crack."

    return strength, advice

# User Interface
print("--- Digital Literacy: Security Analyzer ---")
user_input = input("Enter a password to test its strength: ")
result, tips = analyze_password(user_input)

print(f"\nStrength Rating: {result}")
print(f"Expert Advice: {tips}")
