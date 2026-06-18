import dns.resolver
from concurrent.futures import ThreadPoolExecutor
import threading

mx_cache = {}
mx_lock = threading.Lock()

resolver = dns.resolver.Resolver()
resolver.lifetime = 3
resolver.timeout = 3


def get_mx(domain):
    # fast path (safe read)
    if domain in mx_cache:
        return mx_cache[domain]

    try:
        answers = resolver.resolve(domain, "MX")
        mx = str(answers[0].exchange).rstrip(".")

        # safe write
        with mx_lock:
            mx_cache[domain] = mx

        return mx

    except:
        with mx_lock:
            mx_cache[domain] = None
        return None


def validate(email):
    try:
        domain = email.split("@")[1]
        mx = get_mx(domain)

        if not mx:
            return False, "no mx"

        return True, mx

    except Exception as e:
        return False, str(e)