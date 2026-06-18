# 271. Encode and Decode Strings

from six import unichr


# Non-ASCII Delimiter Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: no
# notes: join strings with a rare non-ASCII char as a delimiter and
#        split on it to decode; chr(258) marks the empty list
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return unichr(258)

        # encode here is a workaround to fix BE CodecDriver error
        return unichr(257).join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == unichr(258):
            return []
        return s.split(unichr(257))


# Chunked Transfer Encoding Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: no
# notes: prefix each string with its 4-byte length, then read that
#        many chars back when decoding; no delimiter needed
class Codec2:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x for x in strs)

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output


# Tests:
for codec in (Codec(), Codec2()):
    assert codec.decode(codec.encode(["Hello","World"])) == ["Hello","World"]
    assert codec.decode(codec.encode([])) == []
    assert codec.decode(codec.encode([""])) == [""]
    assert codec.decode(codec.encode(["a","","bc"])) == ["a","","bc"]
