# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game ran but gave wrong hints half the time, it would say "go higher" when it should say "go lower." Also, Hard mode was actually easier than Normal because it used a smaller number range.

---

## 2. How did you use AI as a teammate?

I used Kiro (AI assistant) throughout this project — first to read and analyze the code, then in Agent mode to refactor logic from `app.py` into `logic_utils.py` and apply fixes.

**Correct AI suggestion:** Kiro identified that `check_guess` in `app.py` was casting the secret to a string on every even-numbered attempt, which caused broken string-vs-int comparisons (e.g. `"9" > "50"` is `True` in Python string comparison, so guess 9 would wrongly return "Too High"). I verified this by writing `test_check_guess_always_uses_int_comparison` — before the fix it would have failed, after the fix it passes cleanly.

**Incorrect/misleading AI suggestion:** The original AI-generated `update_score` function had a branch that gave +5 points for a "Too High" guess on even attempts. The code looked intentional and structured, as if it were a bonus mechanic, so it wasn't obviously wrong. I only caught it by tracing through the logic manually and writing `test_wrong_guess_always_deducts_score`, which confirmed the score was going up instead of down on even attempts.

---

## 3. Debugging and testing your fixes

I verified each fix by writing a pytest case that would have failed on the buggy code and passes on the fixed version. For example, `test_check_guess_always_uses_int_comparison` passes `check_guess(9, 50)` and asserts the outcome is "Too Low" — the old string-comparison bug would have returned "Too High" instead. Running `pytest -v` confirmed all 14 tests pass, including the 3 original starter tests (which also needed a small fix since they were asserting a plain string but `check_guess` returns a tuple). AI helped design the tests by suggesting edge cases like float strings (`"7.9"`) and empty input for `parse_guess`.

---

## 4. What did you learn about Streamlit and state?

Every time you click a button, Streamlit reruns the entire script from top to bottom — so any plain variable you set gets wiped. `st.session_state` is a dictionary that persists across those reruns, which is how the game remembers your score, attempt count, and secret number between clicks. Without it, every button press would reset the game to zero. The tricky part is that state bugs are invisible until you trace through what survives a rerun and what doesn't.

---

## 5. Looking ahead: your developer habits

One habit I want to keep: run the tests before touching any logic. In this project, running `pytest` immediately showed that `logic_utils.py` was completely unimplemented — that single command saved me from debugging in the wrong place. Next time I work with AI on a coding task, I'd ask it to explain its reasoning for any conditional branch that looks unusual, rather than assuming it's intentional. This project changed how I read AI-generated code — I now treat it like a pull request from a junior dev: probably mostly right, but worth a careful line-by-line review before merging.
