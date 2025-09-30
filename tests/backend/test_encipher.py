import pytest
from app.enigma.machine import Machine as EnigmaMachine
from app.enigma.keyboard import Keyboard
from app.enigma.plugboard import Plugboard
from app.enigma.rotor import Rotor
from app.enigma.reflector import Reflector
from app.enigma.configuration import e_rotors, e_reflectors


@pytest.fixture
def enigma_machine() -> EnigmaMachine:
    """Create and setup a standard Enigma machine for testing."""
    keyboard = Keyboard()
    plugboard = Plugboard([])  # No plugboard connections
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


def test_encipher_single_letter(enigma_machine: EnigmaMachine):
    """Test enciphering a single letter."""
    result = enigma_machine.encipher("A")
    assert isinstance(result, str)
    assert len(result) == 1
    assert result.isalpha()
    assert result.isupper()


def test_enigma_results_short(enigma_machine: EnigmaMachine):
    """Test short message encrypts correctly punctuation removed."""
    result = enigma_machine.encipher("May the Force be with you")
    assert result == "ddwfm ndqde nfluz wwcex"


def test_enigma_results_Medium(enigma_machine: EnigmaMachine):
    """Test medium message encrypts correctly punctuation removed."""
    result = enigma_machine.encipher(
        "To live is the rarest thing in the world Most people exist, that is all"
    )
    assert (
        result == "oibqk npfhn nlbms deijc byvqk uxdjm mkukp khqdg yumgx parno bqyqb u"
    )


def test_enigma_results_long(enigma_machine: EnigmaMachine):
    """Test short message encrypts correctly punctuation removed"""
    result = enigma_machine.encipher(
        "Heres to the crazy ones The misfits The rebels The troublemakers The round pegs in the square holes The ones who see things differently Theyre not fond of rules And they have no respect for the status quo You can quote them disagree with them glorify or vilify them About the only thing you cant do is ignore them Because they change things They push the human race forward And while some may see them as the crazy ones we see genius Because the people who are crazy enough to think they can change the world are the ones who do"
    )
    assert (
        result
        == "ilxwb rmrtc wlbgc vmzrs wpbun sfgfj qyexo zbjxf wnila rmczo qhkhc rcmth upesi auyep zfiwt ibkri kpodt pgfpv tpkzp ssnkp gnjta lkkyr hdfno jtbot ujxwj ebwqt njvza gvkco fdisi wrrbx hixkv plqwn pdiwy djzsz dzltg ebsho ktkhg oucbt qoqfh elxyp tjxjs hdzon pbtea qrvzx bmekr ztmos levqt itgor caima qeons tssvi rpesm esjpw hrehk qphsc fynsy yfeyr ynuon bouik bxkze exqdu kgwfr gjial fqvne kyhza acdab yiqeg cnnuj ddduc fahva tfsth xylqx vbbvl ttyll wojrj pkkid idiam bixxu vjkvw uwgll omsdj ptldt vparf ueahp byeux wnk"
    )


def test_encipher_reciprocal(enigma_machine: EnigmaMachine):
    """Test that Enigma is reciprocal - encoding the result decodes back to original."""
    # Reset machine to initial state
    enigma_machine.set_position("AAA")
    original_letter = "H"

    # Encipher once
    encoded = enigma_machine.encipher(original_letter)

    # Reset machine to same initial state
    enigma_machine.set_position("AAA")

    # Encipher again (should decode back to original)
    decoded = enigma_machine.encipher(encoded)

    assert decoded == original_letter


def test_encipher_message_basic(enigma_machine: EnigmaMachine):
    """Test enciphering a basic message."""
    message = "HELLO"
    result = enigma_machine.encipher_message(message)

    assert len(result) == len(message)
    assert result.isalpha()
    assert result.isupper()
    assert result != message  # Should be encrypted


def test_encipher_message_with_spaces(enigma_machine: EnigmaMachine):
    """Test enciphering a message with spaces."""
    message = "HELLO WORLD"
    result = enigma_machine.encipher_message(message)

    # Spaces should be preserved
    assert " " in result
    assert len(result) == len(message)


def test_encipher_message_case_insensitive(enigma_machine: EnigmaMachine):
    """Test that lowercase input is converted to uppercase."""
    message_lower = "hello"
    message_upper = "HELLO"

    # Reset to same position for both
    enigma_machine.set_position("AAA")
    result_lower = enigma_machine.encipher_message(message_lower)

    enigma_machine.set_position("AAA")
    result_upper = enigma_machine.encipher_message(message_upper)

    assert result_lower == result_upper


def test_encipher_message_non_alpha_characters(enigma_machine: EnigmaMachine):
    """Test handling of non-alphabetic characters."""
    message = "HELLO123!@#"
    result = enigma_machine.encipher_message(message)

    # Non-alpha chars should be replaced with spaces
    assert "1" not in result
    assert "2" not in result
    assert "3" not in result
    assert "!" not in result


def test_different_rotor_configurations():
    """Test that different rotor configurations produce different results."""
    keyboard = Keyboard()
    plugboard = Plugboard([])
    reflector = Reflector(e_reflectors.B)

    # Configuration 1: I-II-III
    machine1 = EnigmaMachine(
        reflector=reflector,
        rotor1=Rotor(e_rotors.I),
        rotor2=Rotor(e_rotors.II),
        rotor3=Rotor(e_rotors.III),
        plugboard=plugboard,
        keyboard=keyboard,
    )
    machine1.set_position("AAA")

    # Configuration 2: III-II-I
    machine2 = EnigmaMachine(
        reflector=reflector,
        rotor1=Rotor(e_rotors.III),
        rotor2=Rotor(e_rotors.II),
        rotor3=Rotor(e_rotors.I),
        plugboard=plugboard,
        keyboard=keyboard,
    )
    machine2.set_position("AAA")

    result1 = machine1.encipher("A")
    result2 = machine2.encipher("A")

    assert result1 != result2


def test_plugboard_effect(enigma_machine: EnigmaMachine):
    """Test that plugboard connections affect encryption."""
    # Test without plugboard
    enigma_machine.set_position("AAA")
    result_no_plugboard = enigma_machine.encipher("A")

    # Add plugboard connections
    enigma_machine.plugboard = Plugboard(["AB", "CD"])
    enigma_machine.set_position("AAA")
    result_with_plugboard = enigma_machine.encipher("A")

    assert result_no_plugboard != result_with_plugboard
