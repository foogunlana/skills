# Trip Recommendation Output Template

Use this structure when presenting flight recommendations. Replace `{placeholders}` with actual values.

---

## Single Destination Template

```markdown
# Flights: {origin} → {destination}

**{depart_date} — {return_date}** | {passengers} | {class} | {currency}

---

### Best Value

| Airline | Route | Depart | Arrive | Duration | Stops | Price |
|---------|-------|--------|--------|----------|-------|-------|
| {airline} | {origin}→{dest} | {time} | {time} | {duration} | {stops} | {price} |

[Book on {platform}]({booking_url})

---

### Cheapest

| Airline | Route | Depart | Arrive | Duration | Stops | Price |
|---------|-------|--------|--------|----------|-------|-------|
| {airline} | {origin}→{dest} | {time} | {time} | {duration} | {stops} | {price} |

[Book on {platform}]({booking_url})

---

### Fastest

| Airline | Route | Depart | Arrive | Duration | Stops | Price |
|---------|-------|--------|--------|----------|-------|-------|
| {airline} | {origin}→{dest} | {time} | {time} | {duration} | {stops} | {price} |

[Book on {platform}]({booking_url})

---

### Tips

- {tip_1}
- {tip_2}
- {tip_3}
```

**Tips to include (pick relevant ones):**
- Date flexibility: "Shifting departure by +/- 2 days could save up to {amount}"
- Day of week: "Tuesday/Wednesday departures are typically cheapest"
- Time of day: "Early morning and late evening flights are often cheaper"
- Airline: "{airline} frequently runs sales on this route"
- Route: "Consider {alt_airport} — sometimes cheaper than {primary_airport}"
- Booking timing: "Book 4-8 weeks ahead for best prices on this route"
- Stops: "A 1-stop via {hub} saves {amount} vs direct"
- Season: "{month} is peak/shoulder/off-season — prices reflect this"

---

## Multi-City Template

```markdown
# Multi-City Trip: {city_1} → {city_2} → ... → {city_n}

**{start_date} — {end_date}** | {passengers} | {class} | {currency}

---

## Itinerary Overview

| Leg | Route | Dates | Duration | Est. Price |
|-----|-------|-------|----------|------------|
| 1 | {origin} → {city_1} | {date} | {flight_duration} | {price} |
| 2 | {city_1} → {city_2} | {date} | {flight_duration} | {price} |
| ... | ... | ... | ... | ... |
| **Total** | | **{total_days} days** | | **{total_price}** |

---

## Leg 1: {origin} → {city_1}

**{date}** | {days_in_city} days in {city_1}

### Best Value

| Airline | Route | Depart | Arrive | Duration | Stops | Price |
|---------|-------|--------|--------|----------|-------|-------|
| {airline} | {route} | {time} | {time} | {duration} | {stops} | {price} |

[Book on {platform}]({booking_url})

### Cheapest

| Airline | Route | Depart | Arrive | Duration | Stops | Price |
|---------|-------|--------|--------|----------|-------|-------|
| {airline} | {route} | {time} | {time} | {duration} | {stops} | {price} |

[Book on {platform}]({booking_url})

---

## Leg 2: {city_1} → {city_2}

<!-- Repeat per-leg format -->

---

### Tips

- {multi_city_tip_1}
- {multi_city_tip_2}
```

**Multi-city tips to include (pick relevant ones):**
- "Booking legs separately is often cheaper than a single multi-city booking"
- "Consider {budget_airline} for the {city_1}→{city_2} leg — short-haul specialists"
- "Train might be cheaper/faster for {city_1}→{city_2} ({distance}km) — check {rail_platform}"
- "{city} has multiple airports — {airport_1} is closer to centre, {airport_2} is cheaper to fly into"
- "Allow at least {hours}h between arriving and departing {city} for transfers"

---

## Data Quality Indicators

Use these labels to indicate confidence in pricing:

| Label | Meaning |
|-------|---------|
| **(live)** | Price from booking platform fetch |
| **(approx)** | Price from web search results — may vary |
| **(estimate)** | Inferred from similar routes — treat as rough guide |

Always include the label next to each price so the user knows what to trust.

---

## Assumption Card Template

Always show before searching:

```markdown
## Assumptions

| Field | Value | Source |
|-------|-------|--------|
| Destination | {dest} ({airport_codes}) | You said |
| Origin | {origin} ({airport_code}) | Config / Default / You said |
| Dates | {depart} — {return} | {source_description} |
| Passengers | {n} adult(s), {n} child(ren) | You said / Default |
| Class | {class} | Config / Default / You said |
| Budget | {budget} | Config / Default / You said |
| Stops | {stops_pref} | Config / Default / You said |

Anything wrong? Say so and I'll re-search. Otherwise I'll find flights.
```

Source descriptions:
- **You said** — Explicitly mentioned by user
- **Config** — From `.claude/trip-planner.md`
- **Inferred** — Contextual inference (explain: e.g. "city break = 3 days")
- **Default** — Smart default (no other signal)
