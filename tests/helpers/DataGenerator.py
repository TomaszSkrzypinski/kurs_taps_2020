from random import randint, choice
import re
import string
import rstr


class DataGenerator:
    phoneNumberReg = r'^[1-9][0-9]{8,12}(#[0-9]{1,6}?$)'
    mobileNumberReg = r'^[1-9][0-9]{8,12}$'
    improperPhoneNumberRegs = [r'^\+[1-9][0-9]{0,2} 0[0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^[0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^\+[1-9][0-9]{3,4} [1-9][0-9]{8,12}(#[0-9]{1,6}?$)',
                               r'^\+[1-9][0-9]{0,2} [1-9][0-9]{13,15}(#[0-9]{1,6}?$)']
    improperMobileNumberRegs = [r'^\+[1-9][0-9]{0,2} 0[0-9]{8,12}$',
                                r'^\+[1-9][0-9]{3,5} [1-9][0-9]{8,12}$',
                                r'^\+[1-9][0-9]{0,2} [1-9][0-9]{13,15}$']

    @staticmethod
    def generateProperName(minLength=1, maxLength=35):
        return rstr.rstr(string.ascii_letters, minLength, maxLength).strip().replace('  ', '')

    def generateWrongName(self, maxLength=35):
        case = randint(1, 2)
        if case == 1:
            improperCharacters = '!@#$%^&*()_+=[]{}\|/?;:.,><`~'
            return 'chars', \
                   rstr.rstr(string.ascii_letters + " '-" + string.digits, 1, maxLength,
                             include=choice(improperCharacters)).strip()
        else:
            return 'length', \
                   self.generateProperName(minLength=maxLength + 1, maxLength=maxLength + 5)

    @staticmethod
    def generateProperEmail():
        improperDotPattern = re.compile('^\.')  # to verify if dot is not on beginning of returned string
        while True:
            email = '{0}{1}@{2}.{3}'.format(choice(string.ascii_letters),
                                            rstr.rstr(string.ascii_letters + string.digits + '-_.', 2, 20),
                                            rstr.rstr(string.ascii_letters + string.digits),
                                            choice(['pl', 'com', 'net', 'uk', 'gov', 'us']))
            if not improperDotPattern.match(email):
                return email

    @staticmethod
    def generateWrongEmail():
        improperCharacters = '\():;"><[]@~ \t\n\r\x0b\x0c'
        case = randint(1, 2)
        if case == 1:
            return '{0}@{1}.{2}'.format(rstr.rstr(string.printable, include=choice(improperCharacters),
                                                  exclude='\n\t\r"'),
                                        rstr.rstr(string.printable, include=choice(improperCharacters),
                                                  exclude='\n\t\r"'),
                                        choice(['pl', 'com', 'net', 'uk', 'gov', 'us']))
        else:
            return rstr.rstr(string.printable, exclude='\n\t\r"')

    def generateProperPhoneNumber(self):
        return rstr.xeger(self.phoneNumberReg)

    def generateWrongPhoneNumber(self):
        case = randint(1, 2)
        if case == 1:
            return rstr.xeger(choice(self.improperPhoneNumberRegs))
        else:
            return rstr.rstr(string.printable, include=choice(string.ascii_letters), exclude='\n\t\r"')

    def generateProperMobileNumber(self):
        return rstr.xeger(self.mobileNumberReg)

    def generateWrongMobileNumber(self):
        case = randint(1, 2)
        if case == 1:
            return rstr.xeger(choice(self.improperMobileNumberRegs))
        else:
            return rstr.rstr(string.printable, include=choice(string.ascii_letters), exclude='\n\t\r"')

