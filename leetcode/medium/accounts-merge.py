class Account:
    def __init__(self,email,name):
        self.email = email
        self.parent = None
        self.name = name

    def union(self,parent):
        if parent is self:
            return
        if self.parent is None:
            self.parent = parent
        else:
            self.parent.union(parent)
            self.parent = parent

    def find(self):
        if self.parent is None:
            return self
        parent = self.parent.find()
        return parent

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_of_accounts = {}
        for i,accounts in enumerate(accounts):
            name = accounts[0]
            accounts_to_join = []
            for j,email in enumerate(accounts[1:]):
                account = Account(email,name)
                if j==0:
                    parent = account
                else:
                    account.parent = parent
                if email in emails_of_accounts:
                    emails_of_accounts[email].union(parent)
                emails_of_accounts[email] = account
        groups = {}
        for email in emails_of_accounts:
            account = emails_of_accounts[email]
            parent = account.find()
            if parent.email not in groups:
                groups[parent.email] = [parent.name,set()]
            groups[parent.email][1].add(account.email)
        accounts = []
        for group in groups.values():
            account = [group[0]]
            account+=sorted(list(group[1]))
            accounts.append(account)
        return accounts
