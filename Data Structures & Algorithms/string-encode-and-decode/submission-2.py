class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += word + "/n"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = s.split('/n')
        return decoded_string[:-1]