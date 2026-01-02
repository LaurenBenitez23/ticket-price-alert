from core.gametime import get_cheapest_lower_level

BUY_THRESHOLD_CENTS = 20000

def main():
    result = get_cheapest_lower_level()

    if result is None:
        print("No lower-level tickets found")
        return

    price_cents = result["price_cents"]

    if price_cents < BUY_THRESHOLD_CENTS:
        print("🚨 BUY SIGNAL 🚨")

    print(
        f"Cheapest lower level: ${price_cents / 100:.2f} "
        f"(Section {result['section']}, "
        f"Row {result['row']}, "
        f"{result['section_group']})"
    )

if __name__ == "__main__":
    main()
