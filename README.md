# Ticket Price Alert

A lightweight Python service that monitors ticket prices for a specific event and sends an email alert when tickets drop below a defined price threshold.

The app is designed to run on a schedule via GitHub Actions and notify users quickly when a qualifying ticket becomes available.

---

## What It Does

- Fetches ticket listings for a specific event from Gametime
- Filters listings by section group (e.g. lower-level seats)
- Identifies the best available ticket based on price
- Sends an email alert when a ticket meets the configured price threshold
- Persists alert state to avoid duplicate or unnecessary notifications
- Runs automatically on a scheduled GitHub Actions workflow or via manual trigger

This project is **alert-only**. It does not automate ticket purchases.

---

## How It Works (High Level)

1. A scheduled GitHub Actions workflow runs the price check every 30 min
2. The app fetches current listings for the event
3. Listings are filtered and evaluated against pricing rules
4. If a qualifying ticket is found and alert conditions are met:
   - an email notification is sent
5. Alert state is persisted so the same opportunity is not repeatedly sent

---

## Configuration & Secrets

All configuration is provided via **environment variables**.

- In GitHub Actions, values are injected using **GitHub Secrets**
- No secrets or personal data are committed to the repository

Required environment variables include:
- `GMAIL_FROM`
- `GMAIL_PASSWORD`

---

## Limitations (Current)

- The event being monitored is currently hardcoded in the Gametime client
- Supports a single event at a time
- Email is the only notification channel
- Supports one ticket provider (Gametime)

---

## Planned Improvements

- Make the event URL configurable (instead of hardcoded)
- Include direct “buy” links in alert emails
- Support multiple events and users
- Add alternative intake methods (e.g. form-based submission)
- Optional API layer (FastAPI) for managing watches
