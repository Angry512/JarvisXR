# Browser And Search Strategy

Jarvis should search the web when Wi-Fi exists without becoming just Safari.

## Current Rule

The Jarvis app remains native. Browser/search is a controlled module or handoff, not the product interface.

## Online Flow

- User asks a search command in Jarvis.
- Jarvis checks online mode and privacy state.
- Jarvis either opens an in-app search flow, uses `SFSafariViewController`, or performs a controlled external Safari handoff depending on ownership mode and build path.
- The UI should make returning to Jarvis obvious.

## Offline Flow

Offline mode uses local knowledge, saved notes, local memory, and locally bundled reference material only. It must not queue every search for later and pretend the task is done.

## Hard Lockdown

If supervised Single App Mode prevents external Safari, search must stay in a Jarvis-native or in-app browser/search flow. External app escape is blocked unless explicitly allowed by setup.

## Classification

- Online search: available online native when Wi-Fi exists.
- Offline fallback: local knowledge and memory only.
- External browser handoff: available in soft ownership, blocked in hard lockdown unless allowed or integrated.
