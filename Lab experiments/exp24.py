"""
Experiment 4: Dialog Act Recognition
----------------------------------------
Recognize the dialog act of each utterance in a conversation.

Dialog acts recognized:
  GREETING, QUESTION (Yes/No or Wh-), REQUEST, THANKS, APOLOGY,
  AGREEMENT, DISAGREEMENT, EXCLAMATION/OPINION, STATEMENT (default),
  FAREWELL

Approach: a rule-based classifier using lexical cues and surface patterns
(punctuation, sentence-initial words, keyword sets) -- a common baseline
technique in dialog-act tagging (cf. the DAMSL / Switchboard tag set),
implemented without external NLP libraries.
"""

import re

GREETING_WORDS = {"hi", "hello", "hey", "greetings", "good morning",
                   "good afternoon", "good evening"}
FAREWELL_WORDS = {"bye", "goodbye", "see you", "take care", "good night"}
THANKS_WORDS = {"thanks", "thank you", "thx", "much appreciated"}
APOLOGY_WORDS = {"sorry", "apologize", "apologies", "my bad"}
AGREEMENT_WORDS = {"yes", "yeah", "sure", "ok", "okay", "of course",
                    "absolutely", "agreed", "certainly"}
DISAGREEMENT_WORDS = {"no", "nope", "i disagree", "not really", "i don't think so"}
REQUEST_STARTERS = ("please", "could you", "can you", "would you",
                     "will you", "kindly")
WH_WORDS = ("what", "who", "when", "where", "why", "how", "which", "whom")


def normalize(utterance):
    return utterance.strip().lower().rstrip(".")


def contains_any(text, phrase_set):
    return any(phrase in text for phrase in phrase_set)


def recognize_dialog_act(utterance):
    text = normalize(utterance)
    ends_with_q = utterance.strip().endswith("?")
    ends_with_excl = utterance.strip().endswith("!")

    # Order matters: more specific cues are checked first.
    if contains_any(text, GREETING_WORDS) and len(text.split()) <= 4:
        return "GREETING"
    if contains_any(text, FAREWELL_WORDS):
        return "FAREWELL"
    if contains_any(text, THANKS_WORDS):
        return "THANKS"
    if contains_any(text, APOLOGY_WORDS):
        return "APOLOGY"
    if text.startswith(REQUEST_STARTERS) or "please" in text.split():
        return "REQUEST"
    if ends_with_q and text.startswith(WH_WORDS):
        return "QUESTION-WH"
    if ends_with_q:
        return "QUESTION-YN"
    if text.split() and text.split()[0] in AGREEMENT_WORDS:
        return "AGREEMENT"
    if contains_any(text, DISAGREEMENT_WORDS):
        return "DISAGREEMENT"
    if ends_with_excl:
        return "EXCLAMATION/OPINION"
    return "STATEMENT"


if __name__ == "__main__":
    print("=" * 70)
    print(" EXPERIMENT 4: DIALOG ACT RECOGNITION ")
    print("=" * 70)

    conversation = [
        "Hi there!",
        "Hello! How can I help you today?",
        "Could you tell me the train timings to Chennai?",
        "The next train departs at 6:45 PM from platform 3.",
        "What time does it arrive?",
        "It arrives at 11:30 PM.",
        "Great, thank you so much!",
        "You're welcome. Is there anything else you need?",
        "No, that's all.",
        "Sorry, actually one more thing -- is the train AC or non-AC?",
        "It's fully air-conditioned.",
        "Wonderful!",
        "Alright, goodbye!",
    ]

    print(f"{'Speaker Turn':45s} | Dialog Act")
    print("-" * 70)
    for utt in conversation:
        act = recognize_dialog_act(utt)
        print(f"{utt:45s} | {act}")
