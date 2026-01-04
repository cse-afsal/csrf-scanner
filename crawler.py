import requests
from bs4 import BeautifulSoup

def scan_csrf(url):
    print("Scanning:", url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    forms = soup.find_all("form")
    print("Total forms found:", len(forms))

    for index, form in enumerate(forms, start=1):
        inputs = form.find_all("input")
        csrf_found = False

        for i in inputs:
            name = i.get("name", "")
            if "csrf" in name.lower() or "token" in name.lower():
                csrf_found = True

        if csrf_found:
            print(f"[SAFE] Form {index} has CSRF token")
        else:
            print(f"[VULNERABLE] Form {index} missing CSRF token")

if __name__ == "__main__":
    scan_csrf("http://localhost/dvwa/vulnerabilities/csrf/")
