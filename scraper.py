import requests
from bs4 import BeautifulSoup

def get_price_amazon(product_name):
    url = f"https://www.amazon.in/s?k={product_name}"
    headers = {
        'Authority': 'www.amazon.in',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        price = soup.find('span', attrs={'class': 'a-price-whole'}).text.strip()
        product_title = soup.find('h2', attrs={'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).text.strip()
        print(f"Product on Amazon: {product_title}")
        print(f"Price on Amazon: {price}")
    except AttributeError:
        print("Product not found on Amazon")


def get_price_flipkart(product_name):
    url = f"https://www.flipkart.com/search?q={product_name}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        product_title = soup.find('div', attrs={'class': '_4rR01T'}).text.strip()
        print(f"Product on Flipkart: {product_title}")
        print(f"Price on Flipkart: {price}")
    except AttributeError:
        print("Product not found on Flipkart")


def main():
    print("1. Amazon")
    print("2. Flipkart")
    print("3. Both")
    choice = int(input("Enter your choice: "))

    product_name = input("Enter product name: ")

    if choice == 1:
        get_price_amazon(product_name)
    elif choice == 2:
        get_price_flipkart(product_name)
    elif choice == 3:
        get_price_amazon(product_name)
        get_price_flipkart(product_name)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()