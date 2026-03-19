def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Kiro (AI) identified Hard range 1-50 was easier than Normal 1-100.
    # Verified by comparing range values in a test: test_hard_range_is_harder_than_normal
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome: "Win", "Too High", or "Too Low"
    """
    # FIX: Kiro (AI) caught that app.py was casting secret to str on even attempts,
    # causing string vs int comparisons ("9" > "50" = True). Refactored into logic_utils
    # using Kiro Agent mode so secret is always an int. Verified with test_check_guess_always_uses_int_comparison.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: Kiro (AI) flagged that even-attempt wrong guesses rewarded +5 points.
    # AI suggested always deducting for wrong guesses. Verified with test_wrong_guess_always_deducts_score.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
