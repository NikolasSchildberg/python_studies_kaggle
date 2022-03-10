from signMod import sign

def test_sign():
    assert sign(1) == 1, "Sign of 1 sould be +1"
    assert sign(-1) == -1, "Sign of -1 sould be -1"
    assert sign(10) == 1, "Sign of 10 should be +1"
    assert sign(0) == 0, "Sign of 0 should be 0"

test_sign()
print("Everything passed")