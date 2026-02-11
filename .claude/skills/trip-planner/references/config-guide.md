# Configuration Guide

Create `.claude/trip-planner.md` in your project to customize the trip-planner skill.

## Full Configuration Example

```yaml
name: "Foluso"
home_airport: "LHR"

preferences:
  class: "economy"
  budget: "flexible"
  currency: "GBP"
  stops: "any"
  preferred_airlines:
    - "British Airways"
    - "KLM"
  time_preference: "any"

platform:
  primary: "skyscanner"
```

## Configuration Fields

### Identity

| Field | Description | Default |
|-------|-------------|---------|
| `name` | Your name (used in output headers) | "" |
| `home_airport` | Default departure airport code | "LHR" |

### Preferences

| Field | Description | Default |
|-------|-------------|---------|
| `preferences.class` | Cabin class | "economy" |
| `preferences.budget` | Budget constraint | "flexible" |
| `preferences.currency` | Display currency | "GBP" |
| `preferences.stops` | Stop preference | "any" |
| `preferences.preferred_airlines` | Airlines to prioritise in results | [] |
| `preferences.time_preference` | Preferred departure time of day | "any" |

#### Class Options

| Value | Description |
|-------|-------------|
| `economy` | Standard economy class |
| `premium economy` | Premium economy / economy plus |
| `business` | Business class |
| `first` | First class |

#### Budget Values

| Value | Meaning |
|-------|---------|
| `"flexible"` | No hard limit, show range of options |
| `"under 200"` | Hard cap per person per leg |
| `"100-300"` | Range per person per leg |
| `"budget"` | Prioritise cheapest options, include budget airlines |
| `"premium"` | Prioritise comfort, willing to pay more |

#### Stops Options

| Value | Meaning |
|-------|---------|
| `"any"` | No preference |
| `"direct"` | Direct flights only |
| `"max 1"` | At most 1 stop |
| `"max 2"` | At most 2 stops |

#### Time Preference Options

| Value | Meaning |
|-------|---------|
| `"any"` | No preference |
| `"morning"` | Departures before 12:00 |
| `"afternoon"` | Departures 12:00-18:00 |
| `"evening"` | Departures after 18:00 |
| `"red-eye"` | Overnight flights (often cheaper for long-haul) |

### Platform

| Field | Description | Default |
|-------|-------------|---------|
| `platform.primary` | Booking platform for URLs | "skyscanner" |

#### Supported Platforms

| Platform | URL Pattern |
|----------|-------------|
| `skyscanner` | `skyscanner.net/transport/flights/...` |
| `google-flights` | `google.com/travel/flights?q=...` |
| `kayak` | `kayak.com/flights/...` |

## Minimal Configuration

For most users, this is enough:

```yaml
home_airport: "LHR"
```

Everything else uses sensible defaults.

## Common Airport Codes

| Code | City |
|------|------|
| LHR | London Heathrow |
| LGW | London Gatwick |
| STN | London Stansted |
| JFK | New York JFK |
| EWR | Newark |
| LAX | Los Angeles |
| SFO | San Francisco |
| CDG | Paris Charles de Gaulle |
| AMS | Amsterdam Schiphol |
| FRA | Frankfurt |
| FCO | Rome Fiumicino |
| BCN | Barcelona |
| NRT | Tokyo Narita |
| HND | Tokyo Haneda |
| SIN | Singapore Changi |
| DXB | Dubai |
| LOS | Lagos Murtala Muhammed |
| ABV | Abuja Nnamdi Azikiwe |
| ACC | Accra Kotoka |
| JNB | Johannesburg OR Tambo |
| CPT | Cape Town |
| NBO | Nairobi Jomo Kenyatta |
