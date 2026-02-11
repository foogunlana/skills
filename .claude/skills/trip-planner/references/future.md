# Future Enhancements

Roadmap for Trip Planner — features to add over time.

## Near Term

- **Hotel search** — After flights, search for accommodation near destination. Same assumption-first approach: assume mid-range, city centre, show options.
- **Car hire** — Detect when destination requires driving (e.g. road trips, rural destinations). Search rental options with pickup/dropoff at airport.
- **Price alerts** — "Notify me if flights to Tokyo drop below 400" — save to a watchlist, remind user to check periodically.
- **Trip history** — Save past searches to `.claude/modules/trip-history.md` so the skill can reference previous trips ("same dates as last year's Tokyo trip").

## Medium Term

- **Calendar integration** — Check Google Calendar / Apple Calendar for free windows before suggesting dates. Avoid proposing travel during existing commitments.
- **Visa & entry requirements** — WebSearch visa requirements for destination based on user's nationality (add `nationality` to config). Flag if visa needed, processing time, cost.
- **Travel advisories** — Check government travel advice for destination. Flag warnings.
- **Loyalty programs** — Add frequent flyer numbers and alliance preferences to config. Prioritise alliance partners in results.
- **Baggage comparison** — Include checked bag allowance in flight comparison. Important for budget airlines where bag fees change the real cost.

## Long Term

- **Full itinerary builder** — Combine flights + hotels + car hire + activities into a single trip plan. Export as shareable document or calendar events.
- **Group trip coordination** — Multiple travellers with different origins. Find optimal meeting point or coordinated flights.
- **Flexible date grid** — Show price calendar for +/- 3 days around target dates. Highlight cheapest combination.
- **Airport transfer** — Search for transport from airport to accommodation (train, bus, taxi estimates).
- **Travel insurance** — Compare travel insurance options based on trip details (destination, duration, activities).
- **Packing list** — Generate contextual packing list based on destination weather, trip duration, and activities.
- **Currency & budget tracker** — Convert budget to destination currency, estimate daily spending, track against budget.

## Design Principles for New Features

Every new feature should follow the same core patterns:
1. **Assume first** — Don't ask, infer. Show what you assumed.
2. **Value first** — Deliver results before asking for setup.
3. **Corrections over questions** — Let user fix assumptions, not answer interrogations.
4. **Graceful degradation** — If a data source fails, fall back and note it. Never block on a failed fetch.
