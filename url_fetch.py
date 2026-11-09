from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


FIREFOX_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
    "Gecko/20100101 Firefox/131.0"
)


def main():
    url = input("Enter a URL: ").strip()

    if not url:
        print("Please enter a URL.")
        return

    try:
        request = Request(url, headers={"User-Agent": FIREFOX_USER_AGENT})
        with urlopen(request, timeout=10) as response:
            content = response.read()
    except HTTPError as error:
        print(f"HTTP error {error.code}: {error.reason}")
        return
    except URLError as error:
        print(f"Could not load URL: {error.reason}")
        return
    except TimeoutError:
        print("The request timed out.")
        return

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        print("The response could not be decoded as UTF-8.")
        return

    print(text[:500])


if __name__ == "__main__":
    main()
