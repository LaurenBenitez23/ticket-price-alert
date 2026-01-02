from core.gametime import get_cheapest_lower_level


def main():
    result = get_cheapest_lower_level()

    if result is None:
        print("No lower-level tickets found")
        return

    price_dollars = result["price_cents"] / 100

    print(
        f"Cheapest lower level: ${price_dollars:.2f} "
        f"(Section {result['section']}, "
        f"Row {result['row']}, "
        f"{result['section_group']})"
    )


if __name__ == "__main__":
    main()
