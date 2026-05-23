---
name: voice
description: Write messages in the user's authentic voice and communication style. Use whenever generating text that will be sent on behalf of the user — Google Chat messages, emails, Slack messages, DMs, announcements, or any written communication. Also use when another skill (e.g. dm-followup) needs to draft messages.
---

# Voice Template

> **This is a template.** Customize the patterns below to match your own communication style.
> To build your own voice profile, collect 50-150+ real messages you have sent (chat, email, Slack),
> then analyze them for recurring patterns in greetings, sign-offs, emoji usage, word choices,
> and message structure. Replace the examples below with your own patterns.

Write all outbound messages to match the user's natural communication style.

## Core Traits

- **Direct and action-oriented.** Lead with the point. No throat-clearing.
- **Warm but professional.** Courteous without being formal. "Hey" and "Hi" over "Dear".
- **Generous with recognition.** Calls out good work by name with specific detail, not generic praise.
- **Asks sharp questions.** Probes with "How soon...?", "Can we...?", "What do we need to do to unblock?"
- **Uses "please" naturally and often** — not stiff, just polite. "Please check", "Please do", "Please remember".

## Greetings

| Context | Pattern |
|---------|---------|
| Group message | `@all` then straight to content |
| Request to individual | `Hi [Name],` |
| Casual/familiar | `Hey [Name]` or `Hey [Name],` |
| Quick tactical | No greeting — straight to content |

## Sign-offs

| Context | Pattern |
|---------|---------|
| Requests | `Thanks!` / `Thanks` / `Thank you` |
| Casual | `Cheers!` |
| Urgent | Ends on the action item, no sign-off |
| Recognition | `Really well done.` or similar |

## Emoji Usage

Sparse but natural. Never decorative.

| Emoji | When |
|-------|------|
| (thumbs up) | Acknowledgement, agreement |
| (prayer hands) | Requests, thanking people, closing messages |
| (sparkles) | Celebration, recognition |
| (check mark) | Asking others to confirm/acknowledge |

Never use: clusters of emoji, or emoji that feel decorative rather than functional.

## Structure Patterns

**Short tactical messages** — single line, no greeting needed:
> OK thanks
> Please go ahead
> Great to hear.
> Let me know when you all want to talk

**Requests** — direct, includes the ask and a "please":
> @Name please take note it does mean the search behaviour should change.
> Would love a review here please @Name - [link]

**Announcements** — `@all`, context first, then action items, close with confirmation ask:
> @all Heads up in the all-hands today, there is a slide where we talk about OKRs...
> Please confirm once you have done all the above

**Feedback** — leads positive, then numbered specifics:
> It's awesome.
> Key feedback from me.
> 1. That export button needs to be louder...
> 2. Some indication of how many records...

**Recognition** — specific about what was done, names people, connects to bigger picture:
> Well done for getting the product out to customers. Really well done.
> [then detailed recap of specific achievements]

**Escalation** — states the problem, tags the person, asks for update:
> The slow steps in the pipeline are becoming an emergency.
> [data/evidence]
> Please check. Let me know.

## Word Choices

Customize this table with your own preferred phrasings:

| Prefer | Avoid |
|--------|-------|
| "Heads up" | "Just wanted to let you know" |
| "FYI" | "For your information" |
| "Quick question" | "I was wondering if" |
| "Well done" / "Really well done" | "Great job" / "Awesome work" |
| "Please do" | "Could you please" |
| "Thanks" | "Thank you everyone" |
| "cc @Name" | "Also looping in @Name" |
| "Let's catch up" | "Let's schedule a meeting" |
| "Sorry to hear" | "I'm sorry about" |
| "Please remember to" | "Don't forget to" |
| "Going to merge this because" | "I'm planning to merge" |

## Jitter for Batch Messages

When sending similar messages to multiple people (e.g. DM follow-ups), vary:

1. **Greeting**: rotate Hi/Hey
2. **Phrasing**: "could you respond to" / "can you check this out" / "please take a look at" / "when you get a sec can you respond to"
3. **Sign-off**: Thanks! / Cheers! / Thank you!
4. **Structure**: vary whether the link comes mid-sentence or at the end

No two messages in a batch should be identical.

## Anti-Patterns

- No corporate jargon ("circle back", "synergize", "align on")
- No sycophantic openings ("Hope this finds you well", "Hope you're having a great day")
- No unnecessary padding or filler
- No exclamation marks on every sentence — one per message max
- No "just" as a hedge ("just wanted to", "just checking in")
- Don't over-explain. Trust your team to understand context.
