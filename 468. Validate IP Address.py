# 468. Validate IP Address

# String parsing
# Time: O(n)
# Space: O(1)
# notes: split on '.' for IPv4 and ':' for IPv6, then validate each
#        chunk against the rules for that format
class Solution:
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        if self.is_ipv4(queryIP):
            return "IPv4"
        if self.is_ipv6(queryIP):
            return "IPv6"
        return "Neither"

    def is_ipv4(self, ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if not p.isdigit():
                return False
            if len(p) > 1 and p[0] == '0':
                return False
            if int(p) > 255:
                return False
        return True

    def is_ipv6(self, ip):
        parts = ip.split(':')
        if len(parts) != 8:
            return False
        hexdigits = '0123456789abcdefABCDEF'
        for p in parts:
            if not 1 <= len(p) <= 4:
                return False
            if any(c not in hexdigits for c in p):
                return False
        return True


# Tests:
for sol in (Solution(),):
    assert sol.validIPAddress("172.16.254.1") == "IPv4"
    assert sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert sol.validIPAddress("256.256.256.256") == "Neither"
    assert sol.validIPAddress("192.168.01.1") == "Neither"
    assert sol.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == "Neither"
