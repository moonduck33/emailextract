import re

EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"
)

def extract_emails(file_path: str):
    emails = set()

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            found = EMAIL_REGEX.findall(line)
            for email in found:
                emails.add(email)

    return list(emails)