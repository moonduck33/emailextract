from extractor import extract_emails
from validator import validate
from utils import save_list
from concurrent.futures import ThreadPoolExecutor

def main():

    file_path = input("File path: ").strip()

    emails = extract_emails(file_path)

    print(f"\nFound {len(emails)} emails\n")

    valid = []
    invalid = []

    total = len(emails)
    done = 0

    def process(email):
        return email, validate(email)

    with ThreadPoolExecutor(max_workers=50) as ex:
        for email, (ok, msg) in ex.map(process, emails):
            done += 1

            if ok:
                valid.append(email)
            else:
                invalid.append(email)

            if done % 1000 == 0 or done == total:
                print(f"Processed {done}/{total}")

    save_list("valid.txt", valid)
    save_list("invalid.txt", invalid)

    print("\nDone")
    print("Valid:", len(valid))
    print("Invalid:", len(invalid))


if __name__ == "__main__":
    main()