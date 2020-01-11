from email_validator import validate_email, EmailNotValidError
import re

email = "cpratik025@gmail.com"

try:
    v = validate_email(email) # validate and get info
    email = v["email"] # replace with normalized form
except EmailNotValidError as e:
    # email is not valid, exception message is human-readable
    print(str(e))

patter = re.compile(r"[a-zA-Z0-9!@#$]{8,}[0-9]")
reg_ex =(r"[a-zA-Z0-9!@#$]{8,}[0-9]")
passw= 'prchorsi@025'
check = patter.fullmatch(passw)
print(check)