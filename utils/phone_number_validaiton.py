from phonenumbers.phonenumberutil import region_code_for_country_code as country, COUNTRY_CODE_TO_REGION_CODE as code_dict
import phonenumbers as pn

choices = [
    (str(code), f"{region} +{code}")
    for code in code_dict.keys()
    if (region := country(code))  # Assign and filter out None values
]


def valid_phone_number(
        number: str,
        code: str = None
):
    """ Validates if a number is valid acording to a country code"""
    try:
        code = country(code)
        phone_parsed = pn.parse(number, code)
        if not pn.is_valid_number(phone_parsed):
            raise pn.NumberParseException
        else:
            return True
    except pn.NumberParseException:
        return False
