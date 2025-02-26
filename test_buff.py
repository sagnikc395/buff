from buff import InfiniteTape

def test_tape_increment():
    tape = InfiniteTape()

    tape.increment()
    assert not tape.is_zero()
    tape.decrement()
    assert tape.is_zero()


if __name__ == '__main__':
    test_tape_increment()
    print("Tests Passed ✅")

    
    
