"""Ridiculous Real Pitch.

Writes a single-sentence startup pitch to /output/entry.txt.

The pitch is deliberately absurd at first glance — renting
emotional-support peacocks to divorce lawyers' waiting rooms — yet
the business logic survives a second look: calmer clients settle
faster, so law firms will happily pay $200 a visit for a bird that
screams less than their clients do. The odd thing sold, who pays,
and why it holds together are all in the one sentence.
"""

import os

PITCH = (
    "We rent emotional-support peacocks to divorce lawyers' waiting rooms: "
    "calmer clients settle faster, so firms pay $200 a visit for a bird "
    "that screams less than their clients do."
)


def self_check(pitch):
    """Validate the pitch: one non-empty sentence, 1-200 characters.

    The gate accepts 1-200 characters of non-whitespace UTF-8 text; we
    additionally require exactly one sentence so the entry always lands
    as a single pitch line, never a fragment or a paragraph.
    """
    assert isinstance(pitch, str), "pitch must be a string"
    assert pitch.strip(), "pitch must not be empty or whitespace-only"
    assert pitch == pitch.strip(), "pitch must have no leading/trailing space"
    assert 1 <= len(pitch) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in pitch and "\r" not in pitch, (
        "pitch must contain no newline"
    )
    # Exactly one sentence: a single terminal period, and no other
    # sentence-ending punctuation inside the text.
    assert pitch.endswith("."), "pitch must end with a period"
    assert pitch.count(".") == 1, "pitch must contain exactly one period"
    assert "!" not in pitch and "?" not in pitch, (
        "pitch must be a single sentence with no extra sentence endings"
    )
    return True


def write_entry(pitch):
    """Write ``pitch`` plus a trailing newline to the entry file.

    Tries /output first, then falls back to a local ./output directory.
    Returns the path that was written.
    """
    for directory in ("/output", "output"):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(pitch + "\n")
            return path
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


def main():
    self_check(PITCH)
    path = write_entry(PITCH)
    print(PITCH)
    print("Wrote entry to:", path)


if __name__ == "__main__":
    main()
