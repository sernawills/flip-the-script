from text_converter.flip_the_script import (
    flip_the_script,
)


def test():
    print(flip_the_script('brother'))
    assert flip_the_script('brother') == 'sister'
    print(flip_the_script('brothers'))
    assert flip_the_script('brothers') == 'sisters'
    print(flip_the_script('gods'))
    assert flip_the_script('gods') == 'goddesses'

 
test()
