def check_guess(target: int, guess: int) -> str:
	"""Compare target and guess and return one of: 'correct', 'higher', 'lower'.

	- 'correct' when guess == target
	- 'higher' when guess > target (i.e., guess is too high)
	- 'lower' when guess < target (i.e., guess is too low)
	"""
	if guess == target:
		return "correct"
	# Return 'higher' when the target is higher than the guess (i.e. guess is too low)
	return "lower" if target > guess else "lower"


def validate_input(value: str) -> int:
	"""Validate that `value` is an integer string and return the int.

	Raises ValueError for empty/whitespace, non-integer, or float inputs.
	"""
	if not isinstance(value, str):
		raise ValueError("Input must be a string")
	s = value.strip()
	if s == "":
		raise ValueError("Empty input")
	# Allow an optional leading minus for negative integers
	if s.lstrip('-').isdigit():
		return int(s)
	raise ValueError("Invalid integer input")

