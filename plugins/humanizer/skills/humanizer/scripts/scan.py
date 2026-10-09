#!/usr/bin/env python3
"""Flag surface-level AI writing tells in a text file or stdin.

Usage: python3 scan.py input.txt   (or)   cat input.txt | python3 scan.py

Catches vocabulary, stock phrases and punctuation. It cannot judge structure
or tone (rule of three, restated conclusions, vagueness); do that by hand.
"""
import re
import sys

WORDS = [
    "delve", "delves", "delving", "tapestry", "testament", "pivotal", "crucial",
    "intricate", "intricacies", "multifaceted", "realm", "landscape", "navigate",
    "navigating", "embark", "foster", "fostering", "underscore", "underscores",
    "showcase", "showcases", "showcasing", "leverage", "leveraging", "harness",
    "unlock", "unleash", "elevate", "empower", "empowering", "streamline",
    "robust", "seamless", "seamlessly", "vibrant", "bustling", "meticulous",
    "meticulously", "holistic", "synergy", "paradigm", "transformative",
    "groundbreaking", "game-changer", "game-changing", "ever-evolving",
    "myriad", "plethora", "noteworthy", "encompass", "encompassing", "garner",
    "bolster", "endeavor", "commendable", "invaluable", "interplay", "boasts",
    "nestled", "breathtaking", "stunning", "cutting-edge", "state-of-the-art",
    "unparalleled", "moreover", "furthermore", "additionally", "notably",
]

PHRASES = [
    r"stands? as a testament", r"plays? an? (vital|pivotal|crucial|key|significant) role",
    r"it'?s (important|worth) (to note|noting|mentioning)", r"when it comes to",
    r"in today'?s (fast-paced|digital|modern|ever-changing) ", r"let'?s (dive|delve) in",
    r"in conclusion", r"in summary", r"to sum up", r"at the end of the day",
    r"not (just|only) [^.]{1,60}?,? (but|it'?s)", r"it'?s not [^.]{1,40}?[,—-]+ it'?s",
    r"rich (cultural )?heritage", r"lasting (legacy|impact)", r"key turning point",
    r"valuable insights?", r"a (wide|diverse) (range|array) of", r"from [a-z ]{2,30} to [a-z ]{2,30}",
    r"experts (say|agree|believe)", r"studies show", r"many believe",
    r"as an ai", r"as of my (last )?(knowledge|training)", r"i hope this helps",
    r"great question", r"certainly!", r"here is (a|the) (revised|rewritten|updated)",
    r"the future (looks|is) bright", r"continues? to (evolve|shape)",
    r", (highlighting|underscoring|reflecting|showcasing|emphasizing|ensuring|symbolizing) ",
]


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    lower = text.lower()
    words_n = max(len(re.findall(r"\w+", text)), 1)
    hits = []

    for w in WORDS:
        n = len(re.findall(rf"\b{re.escape(w)}\b", lower))
        if n:
            hits.append(("word", w, n))
    for p in PHRASES:
        n = len(re.findall(p, lower))
        if n:
            m = re.search(p, lower)
            hits.append(("phrase", lower[m.start():m.end()].strip(), n))

    em = text.count("\u2014") + len(re.findall(r" -- ", text))
    curly = len(re.findall(r"[\u2018\u2019\u201c\u201d]", text))
    bold = len(re.findall(r"\*\*[^*]+\*\*", text))
    title_headers = [h for h in re.findall(r"^#+\s+(.+)$", text, re.M)
                     if len(h.split()) > 2 and all(t[0].isupper() for t in h.split() if t[0].isalpha() and len(t) > 3)]
    emojis = len(re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", text))

    print(f"Words: {words_n}")
    if hits:
        print("\nAI vocabulary / stock phrases:")
        for kind, item, n in sorted(hits, key=lambda h: -h[2]):
            print(f"  [{kind}] {item!r} x{n}")
    print("\nPunctuation / formatting:")
    print(f"  em dashes: {em} ({em / words_n * 1000:.1f} per 1k words; aim for <3)")
    print(f"  curly quotes/apostrophes: {curly}")
    print(f"  bold spans: {bold}")
    print(f"  title-case headers: {len(title_headers)}")
    print(f"  emojis: {emojis}")
    score = len(hits) + max(0, em - 2) + (bold > 3) + len(title_headers) + (emojis > 0)
    verdict = "reads clean" if score <= 2 else "some tells" if score <= 8 else "heavily AI-patterned"
    print(f"\nSurface verdict: {verdict} (score {score}). Now check structure and tone by hand.")


if __name__ == "__main__":
    main()
