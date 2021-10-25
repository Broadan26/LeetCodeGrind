class Codec:

    def __init__(self):
        self.encoded = {}
        self.decoded = {}
    
    def generate_random(self) -> str:
        s = string.ascii_letters+string.digits
        return ''.join(random.sample(s,6))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.encoded:
            shortened = "http://tinyurl.com/"
            shortened += self.generate_random()
            self.encoded[longUrl] = shortened
            self.decoded[shortened] = longUrl
            return shortened
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.decoded[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))