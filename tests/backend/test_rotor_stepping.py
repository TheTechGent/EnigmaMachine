import pytest
from app.enigma.machine import Machine as EnigmaMachine
from app.enigma.keyboard import Keyboard
from app.enigma.plugboard import Plugboard
from app.enigma.rotor import Rotor
from app.enigma.reflector import Reflector
from app.enigma.configuration import e_rotors, e_reflectors


@pytest.fixture
def enigma_machine():
    """Create a standard Enigma machine for testing rotor stepping."""
    keyboard = Keyboard()
    plugboard = Plugboard([])
    rotor1 = Rotor(e_rotors.I)
    rotor2 = Rotor(e_rotors.II)
    rotor3 = Rotor(e_rotors.III)
    reflector = Reflector(e_reflectors.B)

    machine = EnigmaMachine(
        reflector=reflector,
        rotor1=rotor1,
        rotor2=rotor2,
        rotor3=rotor3,
        plugboard=plugboard,
        keyboard=keyboard,
    )
    machine.set_rings((1, 1, 1))
    machine.set_position("AAA")
    return machine


def test_single_rotor_step(enigma_machine):
    """Test that only the rightmost rotor steps on normal operation."""
    initial_pos = (
        enigma_machine.rotor1.left[0],
        enigma_machine.rotor2.left[0],
        enigma_machine.rotor3.left[0],
    )

    enigma_machine.encipher("A")

    final_pos = (
        enigma_machine.rotor1.left[0],
        enigma_machine.rotor2.left[0],
        enigma_machine.rotor3.left[0],
    )

    # Only rotor 3 should have stepped
    assert initial_pos[0] == final_pos[0]  # Rotor 1 unchanged
    assert initial_pos[1] == final_pos[1]  # Rotor 2 unchanged
    assert initial_pos[2] != final_pos[2]  # Rotor 3 stepped


def test_double_stepping():
    """Test the famous double-stepping mechanism."""
    keyboard = Keyboard()
    plugboard = Plugboard([])
    rotor1 = Rotor(e_rotors.I)
    rotor2 = Rotor(e_rotors.II)
    rotor3 = Rotor(e_rotors.III)
    reflector = Reflector(e_reflectors.B)

    machine = EnigmaMachine(
        reflector=reflector,
        rotor1=rotor1,
        rotor2=rotor2,
        rotor3=rotor3,
        plugboard=plugboard,
        keyboard=keyboard,
    )

    # Set up for double stepping: rotor2 at notch position
    machine.set_position("AEV")  # E is rotor II's notch

    # Record initial positions
    initial_r1 = machine.rotor1.left[0]
    initial_r2 = machine.rotor2.left[0]
    initial_r3 = machine.rotor3.left[0]

    # Encipher a letter to trigger stepping
    machine.encipher("A")

    # Check final positions
    final_r1 = machine.rotor1.left[0]
    final_r2 = machine.rotor2.left[0]
    final_r3 = machine.rotor3.left[0]

    # All rotors should have stepped due to double-stepping
    assert initial_r1 != final_r1  # Rotor 1 stepped
    assert initial_r2 != final_r2  # Rotor 2 stepped
    assert initial_r3 != final_r3  # Rotor 3 stepped


def test_rotor_turnover():
    """Test rotor turnover at notch positions."""
    keyboard = Keyboard()
    plugboard = Plugboard([])
    rotor1 = Rotor(e_rotors.I)
    rotor2 = Rotor(e_rotors.II)
    rotor3 = Rotor(e_rotors.III)
    reflector = Reflector(e_reflectors.B)

    machine = EnigmaMachine(
        reflector=reflector,
        rotor1=rotor1,
        rotor2=rotor2,
        rotor3=rotor3,
        plugboard=plugboard,
        keyboard=keyboard,
    )

    # Position rotor3 just before its notch (V)
    machine.set_position("AAU")  # V is rotor III's notch

    # Record positions
    initial_r2 = machine.rotor2.left[0]

    # Encipher to trigger stepping
    machine.encipher("A")

    # Rotor 2 should have stepped due to rotor 3 reaching notch
    final_r2 = machine.rotor2.left[0]
    assert initial_r2 != final_r2


def test_multiple_steps(enigma_machine):
    """Test that stepping works correctly over multiple operations."""
    enigma_machine.set_position("AAA")

    initial_r3_pos = enigma_machine.rotor3.left[0]

    # Encipher multiple letters
    for i in range(5):
        enigma_machine.encipher("A")

    final_r3_pos = enigma_machine.rotor3.left[0]

    # Rotor 3 should have stepped 5 times
    assert initial_r3_pos != final_r3_pos


def test_rotor_position_consistency(enigma_machine):
    """Test that rotor positions are consistent across operations."""
    enigma_machine.set_position("ABC")

    # Check that positions were set correctly
    assert enigma_machine.rotor1.left[0] == "A"
    assert enigma_machine.rotor2.left[0] == "B"
    assert enigma_machine.rotor3.left[0] == "C"

    # After one operation, only rotor 3 should change
    enigma_machine.encipher("X")

    assert enigma_machine.rotor1.left[0] == "A"
    assert enigma_machine.rotor2.left[0] == "B"
    assert enigma_machine.rotor3.left[0] == "D"
