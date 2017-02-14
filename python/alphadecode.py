# !/usr/bin/engv python3
'''
    Memorable_pin decode machine. 

    Author: Zhipeng Xie

    Credits: 'python.org' official document

    Input encoded combinations of vowels and
    consonants, output the original PIN.
'''
class Memorable_pin(object):

    def __init__(self, Tone):
        '''
        (String) -> None

        Initialize the list of vowels and consonants.
        Setting the Tone and call decodetor function.

        Input: String, encoded Pin

        Output(printed): Int, decoded Pin

        >>> example = Memorable_pin('hi')
        27
        >>> example = Memorable_pin('bomelela')
        3464140
        >>> example = Memorable_pin('')
        TypeError: Tone is not in correct format.
        '''
        self.vowels_list = 'aeiou'

        self.consonants_list = ''
        temp = ''
        exception = self.vowels_list + 'x'
        for i in range(97,97+26):
            temp = chr(i).strip(exception)
            self.consonants_list = self.consonants_list + temp

        self.encoded_Pin = Tone
        print(self.decoded_Pin)

    @property
    def encoded_Pin(self):
        '''
        (None) -> String

        Getter function, part of this property.

        It is using to get the Tone.
        No Input.
        Output the Tone.

        >>> self.encoded_Pin = 'hi'
        >>> print(self.encoded_Pin)
        'hi'
        '''
        return self._tone

    @encoded_Pin.setter
    def encoded_Pin(self, Tone):
        '''
        (String) -> None

        Setter function, part of this property.

        It is using to set the Tone, and check whether
        the Tone is legal or not. Then call the alphapinDecode()
        to do the job.
        
        Input: Tone, encoded Pin
        No output.

        >>> self.encoded_Pin = ''
        'Tone is not in correct format.'
        '''
        if len(Tone) == 0:
            raise TypeError('Tone is not in correct format.')
        self._tone = Tone
        self.alphapinDecode()
        return None

    @property
    def decoded_Pin(self):
        '''
        (None) -> Int

        Getter function, part of this property.

        It is using to get the decoded Pin.

        No input/ output.

        >>> self.decoded_Pin = 3
        >>> print(self.decoded_Pin)
        3
        '''
        return self._decodedPin

    @decoded_Pin.setter
    def decoded_Pin(self, value):
        '''
        (Int) -> None

        Setter function, part of this property.

        It is using to set the Tone.
        
        Input: Int, calculated result.
        No output.

        Cannot provide example.
        '''
        self._decodedPin = value
        return None

    def get_vowel(self, arg = None):
        '''
        (None) -> list
        (int) -> String
        (String) -> int

        It's used to get certain vowel or whole list
        of vowels or the position of certain vowel*.
        *Assuming inputed letter is a vowel.

        Inputing the position number or a letter, or 
        leave it blank.

        return that position character in the vowel list, or
        the position number of that letter, or the whole vowel
        list.

        >>> print(self.get_vowel())
        'aeiou'
        >>> print(self.get_vowel(0))
        'a'
        >>> print(self.get_vowel('a'))
        0

        '''
        if arg  == None:
            return self.vowels_list
        elif isinstance(arg, str):
            return self.vowels_list.find(arg)
        return self.vowels_list[arg]

    def get_consonants(self, arg = None):
        '''
        (None) -> list
        (int) -> String
        (String) -> int

        It's used to get certain consonant or whole list
        of consonans or the position of certain consonant*.
        *Assuming inputed letter is a consonant.

        Inputing the position number or a letter, or 
        leave it blank.

        return that position character in the consonant list, or
        the position number of that letter, or the whole consonant
        list.

        >>> print(self.get_consonants())
        'bcdfghjklmnpqrstvwyz'
        >>> print(self.get_consonants(0))
        'b'
        >>> print(self.get_consonants('b'))
        0

        '''
        if arg == None:
            return self.consonants_list
        elif isinstance(arg, str):
            return self.consonants_list.find(arg)
        return self.consonants_list[arg]

    def brain(self, Temp_pin):
        '''
        (String) -> int

        It is used to decode 2-letter String to original number.

        Inputing integer pin, calling get_consonants() and 
        get_vowel() to get the result.

        output the original number of the combination of vowel 
        and consonant.

        >>> print(self.brain('hi'))
        27
        >>> print(self.brain('ja'))
        30
        '''
        if isinstance(Temp_pin, str):
            owel_letter = Temp_pin[1]
            conson_letter = Temp_pin[0]
            owel_pos = self.get_vowel(owel_letter)
            conson_pos = self.get_consonants(conson_letter)
            result = 5 * conson_pos + owel_pos
            return result

    def get_two_chr(self, TXT):
        '''
        (String) -> None (Generator)

        This is a generator of 2-letter String of
        inputed String. It keeps dividing the TXT
        into 2-letter String, and yield the result.

        Input: String that needed to be handled,
        assuming TXT has even number of character.

        Output: Keep collecting two letter of
        TXT untill everything has been collected.

        >>> for ch in get_two_chr('abcdef'):
                print(ch)
        ef
        cd
        ab
        >>> print(next(get_two_chr('ab')))
        ab

        '''
        tmp = ''
        tmp = TXT
        Last_letter = -1
        while len(tmp) > 0:
            result = tmp[Last_letter - 1] + tmp[Last_letter]
            tmp = tmp[:Last_letter - 1]
            yield result

    def alphapinDecode(self):
        '''
        (None) -> None

        Main function of decoding the alphapin, it calls get_two_str(),
        and use its result to call brain, accumulating every 2-letter result.

        No Input, it uses the class property,

        No Output, it directly write the class property.

        Cannot provide example
        '''
        count = 0
        self.decoded_Pin = 0
        for ch2 in self.get_two_chr(self.encoded_Pin):
            self.decoded_Pin = self.brain(ch2) * pow(100,count) + self.decoded_Pin
            count += 1
        return None


example = Memorable_pin('hi')
example = Memorable_pin('lo')
example = Memorable_pin('bomeluco')
example = Memorable_pin('bomelela')
#example = Memorable_pin('')