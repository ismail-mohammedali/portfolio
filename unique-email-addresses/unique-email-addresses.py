class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def filter_email(email):
            final_email = ''
            seccond_half = email.split('@')[1]
            first_half=email.split('@')[0]
            first_half=first_half.split('+')[0]
            first_half= first_half.split('.')
            for text in first_half:
                final_email= final_email + text
            final_email=final_email + '@'+seccond_half
            return final_email
        res_email = []
        for email in emails: 
            filtered_email = filter_email(email)
            if filtered_email not in res_email:
                res_email.append(filter_email(email))
        return len(res_email)
    
        