'''
Chracter for Seven Segment :
0123456789ACEFHJLPU

ASCII Printable characters :
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''

class Basen:
    A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    def __init__(self, char:str= A, base:int = None) -> None:
        if char == 'S' :
            self.__char = '0123456789ACEFHJLPU'
            self.__char_default = False
        if char != 'S' and not char == self.A:
            self.__char = char
            self.__char_default = False
        if char == self.A :
            self.__char = char
            self.__char_default = True

        if base == None :
            self.base = len(self.__char)
        if not base == None :            
            self.base = base
        if self.base < 2 :
            exit('Base number tidak boleh dibawah 2')
        if self.base > len(self.__char) :
            exit(f'base number ({self.base}) tidak boleh lebih dari jumlah karakter ({len(self.__char)})')
        self.__len_char = len(self.__char)
        self.__show = None

    def base_n(self, dec:int):
        b = self.base
        c = self.__char
        if dec == 0 :
            return '0'
        x = ''
        while dec > 0 :
            l = dec % b
            x = c[l]+x
            dec = dec // b
        self.__show = x
        return self

    def to_dec(self, basen:str):
        b = self.base
        if self.__char_default and b <= 36:
            basen = basen.upper()
        e = len(basen)-1
        c = self.__char
        dec = 0
        for i in basen :
            dec += c.index(i)*b**e
            e -= 1        
        self.__show = dec
        return self
    
    @property
    def table(self):
        self.__show = ''
        for i, v in enumerate(self.__char):
            self.__show += (str(i)+ ' : ' + str(v) + '\n')
        return self

    @property
    def len_char(self):
        self.__show = self.__len_char
        return self

    @property
    def char(self):
        self.__show = self.__char
        return self
    
    @property
    def show(self):
        print(str(self.__show))

    @property
    def value(self):
        return self.__show


