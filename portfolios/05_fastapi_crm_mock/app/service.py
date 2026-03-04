from .schemas import TicketOut


KEYWORDS = {
    "billing": ["請求", "支払い", "invoice"],
    "bug": ["不具合", "エラー", "落ちる"],
}


def classify_message(message: str) -> TicketOut:
    text = message.lower()
    if any(k in text for k in KEYWORDS["billing"]):
        return TicketOut(category="billing", priority="high")
    if any(k in text for k in KEYWORDS["bug"]):
        return TicketOut(category="bug", priority="high")
    return TicketOut(category="general", priority="normal")
