# Decision Frameworks

Calendar Audit supports multiple scoring frameworks. Choose the one that fits your thinking style.

## 5-Dimension (default)

The most comprehensive framework. Scores 5 factors per meeting.

### Dimensions

Each dimension is scored 1-3:

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Decision Power** | I'm the decision maker | I influence decisions | I'm an observer/FYI |
| **Delegation** | Only I can attend | Someone could rep me with prep | Anyone on my team could attend |
| **Async Potential** | Must be synchronous | Could be hybrid (async + short sync) | Could be fully async |
| **Frequency Fit** | Current frequency is right | Could be less frequent (e.g. weekly → biweekly) | Could be monthly or ad-hoc |
| **Duration Fit** | Duration is right | Could be 50% shorter | Could be 75% shorter |

### Zones

Total score: 5-15.

| Score | Zone | Action |
|-------|------|--------|
| **5-7** | Green | Keep as-is. Core meeting. |
| **8-9** | Yellow | Optimise: shorten, batch, or tighten agenda |
| **10-11** | Orange | Restructure: reduce frequency, delegate, or convert to async |
| **12-15** | Red | Eliminate or fully delegate. You shouldn't be in this meeting. |

### Scoring Guidelines

- **1:1s with direct reports** → almost always Green (5-7). You're the decision maker and can't delegate.
- **Large group standups** where you don't speak → likely Red (12+).
- **Information-only meetings** (all-hands) → high Async Potential.
- **Recurring ceremonies** (retros, groomings) → may score Orange if you attend every instance but only need every other.
- **Cross-functional meetings** where you represent your function → lower Delegation score.

### Best For

Comprehensive weekly audits. Gives the most nuanced view of each meeting.

### Output Columns

`| Meeting | Day/Time | Duration | Score | D | Del | Asy | Frq | Dur | Suggestion |`

---

## Eisenhower

Simple 2-dimension grid. Urgency vs Importance.

### Dimensions

Each dimension is scored 1-3:

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Urgency** | Urgent — time-sensitive decisions, blockers | Moderate — matters this week but not today | Not urgent — could happen anytime |
| **Importance** | Important — directly advances your goals or responsibilities | Moderate — useful but not critical | Not important — no meaningful impact if skipped |

### Zones

Total score: 2-6.

| Score | Zone | Action | Eisenhower Quadrant |
|-------|------|--------|---------------------|
| **2** | Green | Do — attend and engage fully | Q1: Urgent + Important |
| **3** | Yellow | Schedule — keep but move to a better slot if needed | Q2: Important (not urgent) or Q1 edge |
| **4-5** | Orange | Delegate — send someone else or get async summary | Q3: Urgent (not important) or Q4 edge |
| **6** | Red | Delete — skip entirely | Q4: Not urgent + Not important |

### Scoring Guidelines

- **Crisis meetings / escalations** → Urgency 1, Importance 1 → Do.
- **Strategic planning, 1:1s with reports** → Urgency 2-3, Importance 1 → Schedule.
- **Status updates someone else could give** → Urgency 1-2, Importance 3 → Delegate.
- **FYI meetings with no action items** → Urgency 3, Importance 3 → Delete.

### Best For

Quick decisions. People who prefer simplicity over nuance. Good for a rapid first pass.

### Output Columns

`| Meeting | Day/Time | Duration | Score | Urg | Imp | Quadrant | Suggestion |`

---

## RACI

No numeric scoring — classifies your role in each meeting.

### Roles

| Role | Meaning | Attend? |
|------|---------|---------|
| **Accountable** | You own the outcome. The buck stops with you. | Must attend |
| **Responsible** | You do the work. You're executing or presenting. | Must attend |
| **Consulted** | Your input is requested. You provide expertise. | Optional — could provide input async |
| **Informed** | You receive updates. No input needed from you. | Skip — get notes instead |

### Zone Mapping

| Role | Zone | Action |
|------|------|--------|
| **Accountable** | Green | Keep. You own this. |
| **Responsible** | Green | Keep. You're doing the work. |
| **Consulted** | Yellow | Consider async. Send your input before the meeting, skip if possible. |
| **Informed** | Red | Skip. Ask for meeting notes or a 2-line summary. |

### Scoring Guidelines

- **1:1s with direct reports** → Accountable (you own the relationship).
- **Sprint ceremonies you run** → Responsible.
- **Design reviews where you give feedback** → Consulted.
- **Company all-hands, org announcements** → Informed.
- **Meetings where you sit silently** → almost certainly Informed.

### Best For

Cutting meetings where you're just "Informed". Especially useful for senior leaders who get invited to everything. Forces the question: "What is my actual role here?"

### Output Columns

`| Meeting | Day/Time | Duration | Role | Attend? | Suggestion |`

---

## Value vs Effort

2-dimension quadrant model. Value generated vs effort invested.

### Dimensions

Each dimension is scored 1-3:

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Value** | High — decisions made, problems solved, relationships built, blockers removed | Moderate — useful information exchanged, some progress | Low — no decisions, no learning, no relationship value |
| **Effort** | Low — short, no prep, minimal context switch | Moderate — some prep or causes a context switch | High — long duration, heavy prep, fragments a focus block |

### Quadrants

| Value | Effort | Quadrant | Zone | Action |
|-------|--------|----------|------|--------|
| High (1) | Low (1) | Quick Win | Green | Keep — high ROI, low cost |
| High (1) | High (3) | Strategic | Yellow | Keep but optimise — reduce duration or prep |
| Low (3) | Low (1) | Filler | Orange | Cut or batch — low value even if low cost |
| Low (3) | High (3) | Trap | Red | Eliminate — worst ROI on your calendar |
| Mixed (2) | Any | Evaluate | Yellow/Orange | Look for ways to increase value or reduce effort |

### Zone Mapping

Total score: 2-6 (Value + Effort).

| Score | Zone | Action |
|-------|------|--------|
| **2** | Green | Quick Win — keep as-is |
| **3** | Yellow | Optimise — good value but reduce effort, or low effort but increase value |
| **4-5** | Orange | Restructure — the value doesn't justify the effort |
| **6** | Red | Trap — eliminate or fully delegate |

### Scoring Guidelines

- **High-value meetings**: decisions get made, you leave with clear actions, or the relationship is critical.
- **High-effort meetings**: long duration (60min+), require prep, or sit in the middle of a focus block.
- **Traps to watch for**: recurring meetings that were once valuable but haven't produced a decision in weeks.

### Best For

Product-minded thinkers. People who think in terms of ROI. Good for identifying "Trap" meetings — high effort, low value — that quietly drain your week.

### Output Columns

`| Meeting | Day/Time | Duration | Value | Effort | Quadrant | Suggestion |`

---

## Custom

Define your own dimensions and scoring.

### Config Structure

In `.claude/calendar-audit.md`:

```yaml
framework:
  name: "custom"
  custom:
    dimensions:
      - name: "Strategic Alignment"
        scale: [1, 3]
        labels:
          1: "Directly advances Q1 goals"
          2: "Indirectly related"
          3: "No connection to goals"
      - name: "Energy Cost"
        scale: [1, 3]
        labels:
          1: "Energising"
          2: "Neutral"
          3: "Draining"
      - name: "Replaceability"
        scale: [1, 3]
        labels:
          1: "Only I can do this"
          2: "Could delegate with effort"
          3: "Anyone could do this"
    zones:
      green: [3, 4]
      yellow: [5, 6]
      orange: [7, 8]
      red: [9, 9]
```

### Guided Creation

During onboarding, if user picks Custom:

1. Ask how many dimensions (2-5 recommended)
2. For each dimension, ask:
   - Name
   - What does 1 mean? (best case)
   - What does 3 mean? (worst case)
3. Auto-calculate zone ranges based on total possible score
4. Confirm with user before saving

### Zone Auto-Calculation

For N dimensions, total range is N to 3N:
- Green: N to N + floor(2N * 0.25)
- Yellow: above Green to N + floor(2N * 0.50)
- Orange: above Yellow to N + floor(2N * 0.75)
- Red: above Orange to 3N

### Best For

Power users who want full control. Teams with specific meeting culture or values they want to score against.

---

## Framework Comparison

| Framework | Dimensions | Speed | Nuance | Best For |
|-----------|-----------|-------|--------|----------|
| 5-Dimension | 5 | Medium | High | Comprehensive weekly audits |
| Eisenhower | 2 | Fast | Low | Quick decisions, simplicity |
| RACI | 1 (role) | Fast | Medium | Cutting "Informed" meetings |
| Value vs Effort | 2 | Fast | Medium | ROI thinkers, identifying traps |
| Custom | N | Varies | Varies | Power users, team-specific values |
