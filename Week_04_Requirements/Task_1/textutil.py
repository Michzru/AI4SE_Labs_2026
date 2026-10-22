"""Text helpers shared by the nodes."""
import unicodedata


def squash(text: str) -> str:
    """Normalize for quote matching: Unicode-fold, lowercase, keep letters and digits only.

    Makes the check immune to line wrapping, e-mail '>' prefixes, quote styles and dashes.
    """
    text = unicodedata.normalize("NFKC", text).casefold()
    return "".join(ch for ch in text if ch.isalnum())


def squash_with_positions(text: str) -> tuple[str, list[int]]:
    """Like squash, but also returns, for each kept character, its index in the original text."""
    chars, positions = [], []
    for i, ch in enumerate(text):
        for folded in unicodedata.normalize("NFKC", ch).casefold():
            if folded.isalnum():
                chars.append(folded)
                positions.append(i)
    return "".join(chars), positions
