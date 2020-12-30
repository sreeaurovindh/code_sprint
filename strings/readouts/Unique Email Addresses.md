# Unique Email Addresses

```python
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_recognized = set()
        for mail in emails:
            local_name,domain_name = mail.split('@')
            processed_name = ''.join(local_name.split('.'))
            if '+' in processed_name:
                processed_name  = processed_name.split('+')[0]
            emails_recognized.add(processed_name+domain_name)
        return len(emails_recognized)
```



Things to Remember

`set` has `add()`  method to add elements.

