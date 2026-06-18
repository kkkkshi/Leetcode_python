# 535. Encode and Decode TinyURL

# Hashmap Counter
# Time: encode: O(1), decode: O(1)
# Space: O(n)
# notes: map each long url to an incrementing id and store both ways;
#        decode looks the short url back up
class Codec:

    def __init__(self):
        self.urls = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.counter += 1
        key = "http://tinyurl.com/" + str(self.counter)
        self.urls[key] = longUrl
        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]


# Tests:
for codec in (Codec(),):
    url = "https://leetcode.com/problems/design-tinyurl"
    assert codec.decode(codec.encode(url)) == url
    assert codec.decode(codec.encode("https://a.com")) == "https://a.com"
    assert codec.encode(url) != codec.encode(url)
