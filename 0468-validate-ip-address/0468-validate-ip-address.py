class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) == 4:  
                for part in parts:
                    if not part.isdigit() or len(part) > 1 and part[0] == '0' or not (0 <= int(part) <= 255):
                        return "Neither"
                return "IPv4"
        
        elif ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) == 8:  
                hex_pattern = re.compile(r'^[0-9a-fA-F]{1,4}$')  
                for part in parts:
                    if not hex_pattern.match(part):
                        return "Neither"
                return "IPv6"
        
        return "Neither"
