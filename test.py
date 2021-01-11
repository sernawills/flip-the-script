from text_converter.flip_the_script import (
    gender_plural, 
    re_plural, 
    re_ES, 
    flip_the_script,
    m_f,
)

for x in m_f: 
    print(x)

#print(list(gender_plural('brotherS', 'sisterS')))
#print('test')

#for x in gender_plural('brotherS', 'sisterS'): 
#    print(x)

#for x in [1, 2, 3]:
#    print(x)

def gender_plural_2(m, f):
    return [
        [re_plural.sub("",m), re_plural.sub("",f)],
        [re_ES.sub("es",m), re_ES.sub("es",f)],
        [re_plural.sub("s",m), re_plural.sub("s",f)],
    ]

def test():
    print(flip_the_script('brother'))
    assert flip_the_script('brother') == 'sister'
    print(flip_the_script('brothers'))
    assert flip_the_script('brothers') == 'sisters'
    print(flip_the_script('gods'))
    assert flip_the_script('gods') == 'goddesses'
    
test()