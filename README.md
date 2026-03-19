# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run tests: `pytest tests/ -v`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** Move the logic into `logic_utils.py`, run `pytest`, keep fixing until all tests pass.

## 📝 Document Your Experience

**Purpose:**
A Streamlit number-guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the number range and attempt limit.

**Bugs found:**

1. `check_guess` — secret was cast to `str` on every even-numbered attempt, causing broken string comparisons (e.g. `"9" > "50"` is `True` in Python, so hints were wrong every other turn).
2. `update_score` — "Too High" guesses on even attempts rewarded +5 points instead of deducting, so wrong guesses could increase your score.
3. `get_range_for_difficulty` — Hard mode used range 1–50, which is actually easier than Normal (1–100). Fixed to 1–200.
4. New game reset — `attempts` was reset to `0` but the game initializes at `1`, causing an off-by-one error on attempt counting.
5. `logic_utils.py` — all four functions were stubs raising `NotImplementedError`, so tests failed immediately.
6. Tests — the starter tests asserted `check_guess` returned a plain string, but the function returns a tuple `(outcome, message)`.

**Fixes applied:**

- Refactored all game logic (`check_guess`, `parse_guess`, `update_score`, `get_range_for_difficulty`) into `logic_utils.py` using Kiro Agent mode.
- Fixed all 4 logic bugs listed above.
- Updated `app.py` to import from `logic_utils` and removed duplicate inline logic.
- Fixed the hint display to show the dynamic range instead of hardcoded "1 to 100".
- Fixed the 3 starter tests and added 11 new targeted tests (14 total, all passing).

## 📸 Demo

**pytest results (14/14 passing):**

```
tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_check_guess_always_uses_int_comparison PASSED
tests/test_game_logic.py::test_check_guess_correct_message_too_high PASSED
tests/test_game_logic.py::test_check_guess_correct_message_too_low PASSED
tests/test_game_logic.py::test_wrong_guess_always_deducts_score PASSED
tests/test_game_logic.py::test_wrong_guess_odd_attempt_deducts_score PASSED
tests/test_game_logic.py::test_hard_range_is_harder_than_normal PASSED
tests/test_game_logic.py::test_easy_range PASSED
tests/test_game_logic.py::test_parse_guess_empty PASSED
tests/test_game_logic.py::test_parse_guess_valid_int PASSED
tests/test_game_logic.py::test_parse_guess_float_string PASSED
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED
14 passed in 0.01s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
