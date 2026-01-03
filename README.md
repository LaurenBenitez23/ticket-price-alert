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

# Running Locally

This project is primarily designed to run on a schedule via GitHub Actions, but it can also be run locally for development, testing, or experimentation.

---

## Requirements

- Python 3.11+
- Poetry

You can verify your Python version with:

```bash
python --version
```

You can install Poetry following the official instructions:
https://python-poetry.org/docs/#installation

---

## Install Dependencies

From the root of the repository:

```bash
poetry install
```

This will create a virtual environment and install all required dependencies.

---

## Environment Variables

This project relies on environment variables for email notifications.

An example file is provided in the repository:

```
.env.example
```

This file documents the required variables but does **not** contain any real credentials.

### Local setup

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

### Required variables

```env
# Email address alerts are sent from
GMAIL_FROM=

# App password for the Gmail account (generate this in your Google Account settings)
GMAIL_APP_PASSWORD=
```

## Gmail App Password

This project sends email using Gmail SMTP and **requires a Gmail App Password**.  
Normal Gmail account passwords will not work.

To create an App Password:

1. Make sure **2-Step Verification** is enabled on your Google account
2. Go to Google’s App Passwords page:  
   https://myaccount.google.com/apppasswords
3. Enter an app name (for example: `ticket-price-alert`)
4. Use the generated password as `GMAIL_APP_PASSWORD`

Do **not** commit this value to the repository.  
When running in GitHub Actions, store it as a repository secret.

---

## Run the Price Checker

To run the price check locally:

```bash
poetry run python -m scripts.check_price
```

If a qualifying ticket is found:
- a BUY signal will be printed to the console
- an email notification will be sent

---

## Notes

- Local runs are intended for development and debugging.
- Scheduled runs and automation are handled via GitHub Actions.
- No secrets should be committed to the repository.