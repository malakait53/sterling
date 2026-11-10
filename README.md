# Sterling: build and install on your iPhone

Sterling uses the same Capacitor setup as Lock In. Pick whichever route you used before.

## Try it first (no build)
Open `www/index.html` in any browser. Live stock prices and news only load inside the iPhone app (a browser blocks them); the browser shows clearly labeled DEMO data.

## No Mac: GitHub Actions
1. Create a new GitHub repo and push this folder (keep the hidden `.github` folder).
2. Repo → Actions → "Build unsigned IPA" → Run workflow.
3. Download `Sterling-ipa` from the run's Artifacts, then sideload `Sterling.ipa` with Sideloadly or AltStore.

## With a Mac
```bash
npm install
npx cap add ios
npx cap sync ios
npx cap open ios
```
Then in Xcode: App → Signing & Capabilities → pick your Apple ID team → Run on your phone. Free accounts expire after 7 days.

## Where the data comes from
- **Prices:** Yahoo Finance's public chart endpoint, with Stooq as a fallback (US tickers). No key needed.
- **News:** Google News RSS search per ticker, plus the Business topic feed. No key needed.
- These are unofficial public endpoints. They can change, rate-limit, or lag. If prices stop loading, tell me and I'll swap the source (Finnhub, Alpha Vantage or Polygon with a free key are the stable options).
- `CapacitorHttp` is enabled in `capacitor.config.json` so the app can fetch these without browser CORS limits.

## Your data
Everything (transactions, goals, watchlist, holdings) is stored on the phone only. Use Settings → Backup to export a copy.
