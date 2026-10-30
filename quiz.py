#!/usr/bin/env python3
"""CLI runner for the original CompTIA A+ practice quizzes in this repo.

These are homemade practice quizzes, NOT exam dumps or pirated questions.
Answer keys live in a separate private repo; pass one with --key to grade.
Standard library only.
"""
import argparse, json, random, sys


def load_key(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    ans = data.get("answers", data)
    key = {}
    if isinstance(ans, list):
        for item in ans:
            key[str(item["id"])] = item
    else:
        for qid, v in ans.items():
            key[str(qid)] = v if isinstance(v, dict) else {"answer": v}
    return key


def main():
    p = argparse.ArgumentParser(description="Take an A+ practice quiz (questions-only JSON).")
    p.add_argument("--quiz", required=True, help="path to quiz JSON, e.g. core1-full-90-a.json")
    p.add_argument("--key", help="optional answer key JSON (kept in the private answers repo)")
    p.add_argument("--shuffle", action="store_true", help="shuffle question order")
    a = p.parse_args()

    with open(a.quiz, encoding="utf-8") as f:
        quiz = json.load(f)
    qs = list(quiz["questions"])
    if a.shuffle:
        random.shuffle(qs)
    key = load_key(a.key) if a.key else None

    print(f"\n{quiz.get('title', a.quiz)}")
    print("Original practice quiz for study. Not CompTIA exam content or a dump.")
    print("Answer A-D, S to skip, Q to quit. Graded at the end" + ("." if key else " only if --key is given.") + "\n")

    picks = {}
    for i, q in enumerate(qs, 1):
        print(f"[{i}/{len(qs)}] ({q.get('domain', '')}) {q['stem']}")
        for letter, text in sorted(q["choices"].items()):
            print(f"   {letter}. {text}")
        while True:
            try:
                r = input("> ").strip().upper()
            except EOFError:
                r = "Q"
            if r in q["choices"] or r in ("S", "Q"):
                break
            print("Enter A, B, C, D, S, or Q.")
        if r == "Q":
            break
        if r != "S":
            picks[str(q["id"])] = r
        print()

    print(f"\nAnswered {len(picks)} of {len(qs)}.")
    if not key:
        print("No key loaded, so no score. Your picks:")
        print(", ".join(f"{k}:{v}" for k, v in picks.items()) or "(none)")
        return
    right, by_domain, missed = 0, {}, []
    for q in qs:
        qid = str(q["id"])
        k = key.get(qid)
        if not k:
            continue
        d = by_domain.setdefault(q.get("domain", "?"), [0, 0])
        d[1] += 1
        if picks.get(qid) == k["answer"]:
            right += 1
            d[0] += 1
        else:
            missed.append((q, picks.get(qid, "-"), k))
    total = sum(v[1] for v in by_domain.values())
    print(f"Score: {right}/{total} ({100 * right / max(total, 1):.0f}%)\n")
    for dom, (r, t) in sorted(by_domain.items()):
        print(f"  {dom}: {r}/{t}")
    if missed:
        print("\nMissed:")
        for q, mine, k in missed:
            print(f"  #{q['id']} you: {mine}  correct: {k['answer']}  {k.get('explain', '')}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nQuit.")
