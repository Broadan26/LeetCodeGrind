class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_of_emails = set()

        for email in emails:
            split_email = email.split('@') #
            local_name = split_email[0]
            domain_name = split_email[1]

            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            new_email = local_name + '@' + domain_name
            if new_email not in set_of_emails:
                set_of_emails.add(new_email)
        
        return len(set_of_emails)