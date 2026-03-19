from logic_utils import check_guess, update_score, get_range_for_difficulty, parse_guess

# --- existing tests (fixed: check_guess returns a tuple) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Bug fix: secret was cast to str on even attempts, breaking comparisons ---

def test_check_guess_always_uses_int_comparison():
    # Before the fix, passing a str secret caused wrong outcomes via string comparison
    # e.g. str comparison: "9" > "50" is True, so guess=9 would wrongly return "Too High"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low", "int comparison should say Too Low, not Too High"

def test_check_guess_correct_message_too_high():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # before fix the emoji/direction was also swapped

def test_check_guess_correct_message_too_low():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# --- Bug fix: update_score was rewarding +5 for wrong guesses on even attempts ---

def test_wrong_guess_always_deducts_score():
    # even attempt number — used to give +5, should now deduct
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 95, "Wrong guess on even attempt should deduct, not reward"

def test_wrong_guess_odd_attempt_deducts_score():
    score = update_score(100, "Too Low", attempt_number=3)
    assert score == 95

# --- Bug fix: Hard difficulty range was 1-50 (easier than Normal 1-100) ---

def test_hard_range_is_harder_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard should have a larger range than Normal"

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

# --- Bug fix: parse_guess off-by-one / edge cases ---

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert not ok and val is None

def test_parse_guess_valid_int():
    ok, val, err = parse_guess("42")
    assert ok and val == 42

def test_parse_guess_float_string():
    ok, val, err = parse_guess("7.9")
    assert ok and val == 7

def test_parse_guess_non_numeric():
    ok, val, err = parse_guess("abc")
    assert not ok and "not a number" in err.lower()
