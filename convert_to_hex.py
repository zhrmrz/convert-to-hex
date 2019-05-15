class Sol:
    def convert_to_hex(self,n):
        if n==0:
            return "0"
        if n<0:
            n+=2**32
        result=[]
        while n!=0:
            while n != 0:
                r = n % 16
                n = n // 16
                if r < 10:
                    result.append(str(r))
                else:
                    result.append(chr(ord('a') + r-10))

        return "".join(result[::-1])

if __name__ == '__main__':
    p1=Sol()
    print(p1.convert_to_hex(32))
