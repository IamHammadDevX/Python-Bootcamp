

def formateName(firstName, lastName):
    """This function only for formate the name to title case"""
    if firstName == "" or lastName == "":
        return "you didn't provide the actual data!"
    formatFirstName = firstName.title()
    formatLastName = lastName.title()
    return f"Results {formatFirstName} {formatLastName}"

res = formateName("angela", "yu")
print(res)