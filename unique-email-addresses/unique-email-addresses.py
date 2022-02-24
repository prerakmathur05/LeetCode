class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for email in emails:
            name,domain=email.split('@')
            rname=""
            for character in name:
                if character=="+":
                    break
                if character==".":
                    continue
                else:
                    rname+=character
            res.add(rname+'@'+domain)
        return len(res)