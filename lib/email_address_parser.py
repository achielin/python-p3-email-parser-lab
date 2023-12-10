# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, string_addresses):
        self.string_addresses = string_addresses
    def parse(self):
        email_pattern = r"[\w.]*@\w*.\w*"
        email_regex = re.compile(email_pattern)
        valid_email_adresses = email_regex.findall(self.string_addresses)
        print(valid_email_adresses)
        email_set = set(valid_email_adresses)
        sorted_email_list = sorted(list(email_set))

        return sorted_email_list

parser = EmailAddressParser("good@goodnews.com, john.doe@moringaschool.com mercy@pos.com")

value = parser.parse()
print(value)