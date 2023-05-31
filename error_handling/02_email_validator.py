import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NoDomainError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]


pattern_name = r'^[a-z][a-z0-9_.\'\-]+@'
# ^ indicates that the name pattern must be found in the beginning
# Usernames must start with a letter, can only contain lowercase letters (a-z),
# numbers (0-9), dashes (-), underscores (_), apostrophes ('), and periods (.)
pattern_domain = r'\.[a-z]{2,}$'
# $ indicates that the domain pattern must be found in the end


def validate_email(email):
    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Valid emails contain only one @ symbol!")
    elif "@" not in email:
        raise MustContainAtSymbolError("Valid emails contain @ symbol!")

    name_match = re.search(pattern_name, email)
    if not name_match:
        raise InvalidNameError("Email name is not valid!")
    elif len(name_match.group()) < MIN_LENGTH:
        raise NameTooShortError("Email name must contain at least 4 symbols!")

    domain_match = re.search(pattern_domain, email)
    if not domain_match or domain_match.start() <= email.index("@") + 2:
        raise NoDomainError("Email is lacking domain or domain is invalid!")
    elif domain_match.group().lower() not in [domain.lower() for domain in VALID_DOMAINS]:
        raise InvalidDomainError(f"Top-level domain must be one of the following: "
                                 f"{', '.join(VALID_DOMAINS)}!")


email = input("Type email you wish to validate: ")

while email != "End":
    try:
        validate_email(email)
        print("Email is valid")  # Hooray!
    except (
        MoreThanOneAtSymbolError,
        MustContainAtSymbolError,
        InvalidNameError,
        NameTooShortError,
        NoDomainError,
        InvalidDomainError,
    ) as e:
        print(f"Invalid email: {str(e)}")

    email = input("Type email you wish to validate or 'End' to terminate: ")
