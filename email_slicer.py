"""A program that takes an email and slices it into username, domain, and extension
"""

def main():
    print("Welcome to the email slicer program!")
    print("")
    
    email_input = input("Input email address: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extansion: ", extension)

main()