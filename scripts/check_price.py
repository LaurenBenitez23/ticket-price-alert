from core.gametime import get_cheapest_lower_level
import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]  # repo root
STATE_FILE = BASE_DIR / "alert_state.json"

def load_alert_state() -> dict[str, Any]:
    if STATE_FILE.exists():
        try:
            with STATE_FILE.open("r") as f:
                data = json.load(f)
            if isinstance(data, dict) and isinstance(data.get("alerts_sent"), dict):
                return data
        except json.JSONDecodeError:
            pass  # empty or corrupt file
    return {"alerts_sent": {}}

def save_alert_state(state: dict[str, Any]) -> None:
    with STATE_FILE.open("w") as f:
        json.dump(state, f, indent=2, sort_keys=True)

BUY_THRESHOLD_CENTS = 20000

def main():
    alert_state = load_alert_state()

    result = get_cheapest_lower_level()

    if result is None:
        print("No lower-level tickets found")
        return

    price_cents = result["price_cents"]
    section_group = result.get("section_group")

    if price_cents < BUY_THRESHOLD_CENTS:
        last_alert_cents = alert_state["alerts_sent"].get(section_group)

        # Alert the first time, or again only if it drops further
        if last_alert_cents is None or price_cents < last_alert_cents:
            print("🚨 BUY SIGNAL 🚨")
            alert_state["alerts_sent"][section_group] = price_cents

    print(
        f"Cheapest lower level: ${price_cents / 100:.2f} "
        f"(Section {result['section']}, "
        f"Row {result['row']}, "
        f"{result['section_group']})"
    )

    save_alert_state(alert_state)

if __name__ == "__main__":
    main()
