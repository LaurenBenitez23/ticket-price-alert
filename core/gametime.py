import requests

GAMETIME_URL = "https://mobile.gametime.co/v3/listings/689e83945b20e1a53fdd89ac?all_in_pricing=true&quantity=1&jitter_cheapest=0"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

LOWER_LEVEL_GROUPS = set(['Bungalow Suites', 'Club', 'Floor', 'Main', 'Suite'])

def get_cheapest_lower_level():
    response = requests.get(GAMETIME_URL, headers=HEADERS, timeout=20)
    response.raise_for_status()
    data = response.json()

    listings = data.get("listings") or data.get("data", {}).get("listings", [])
    if not listings:
        raise ValueError("No listings found")

    lower = [
        l for l in listings
        if l.get("spot", {}).get("section_group") in LOWER_LEVEL_GROUPS
        and isinstance(l.get("price", {}).get("total"), int)
    ]

    if not lower:
        return None

    cheapest = min(lower, key=lambda l: l["price"]["total"])

    return {
        "price_cents": cheapest["price"]["total"],
        "section": cheapest.get("spot", {}).get("section"),
        "row": cheapest.get("spot", {}).get("row"),
        "section_group": cheapest.get("spot", {}).get("section_group"),
    }
