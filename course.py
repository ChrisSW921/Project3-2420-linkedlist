"""Course module"""

class Course:
    """This is the course class, or what would be a single node in a linked list"""
    def __init__(self, cnumber=0, cname="", ccredit_hr=0.0, cgrade=0.0, cnext=None):
        if isinstance(cname, str):
            self.cname = cname
        else:
            raise ValueError
        if isinstance(cnumber, int):
            self.cnumber = cnumber
        else:
            raise ValueError
        if isinstance(ccredit_hr, float) and isinstance(cgrade, float) and cgrade >= 0.0:
            self.ccredit_hr = ccredit_hr
            self.cgrade = cgrade
        else:
            raise ValueError
        self.next = cnext

    def name(self):
        """Get Name Of Course"""
        return self.cname

    def number(self):
        """Get Course Number"""
        return self.cnumber

    def credit_hr(self):
        """Get Credit Hours"""
        return self.ccredit_hr

    def grade(self):
        """Get Grade"""
        return self.cgrade

    def __str__(self):
        return f"cs{str(self.number())} {self.name()} " \
               f"Grade:{str(self.grade())} Credit Hours: {str(self.credit_hr())}"

