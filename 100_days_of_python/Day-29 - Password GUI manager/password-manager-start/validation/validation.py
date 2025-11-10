from email_validator import validate_email, EmailNotValidError
import validators 

def check_email(email):
    """This function is used to check if the user inputted a valid email."""
    try:
        validate_email(email,check_deliverability=False)
        return True
    
    except EmailNotValidError:
        return False
