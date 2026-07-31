# Sort & Shine website

One-page site for a home organizing business (Sahar & Savannah, serving Metro Detroit). Owner: Tyler, building this as a trial run for his mom's business — practice for future paying freelance clients, not a live production site yet. Plain HTML/CSS, no build tools or frameworks. Files: `SandS.html`, `styles.css`, `images/`.

Brand basics: tagline "Less Clutter, More Calm," cream background `#FAF6EF`, sage green accent `#3D4A2A`, headings in Cormorant Garamond, body text in Lato.

## How to work with Tyler on this project

**Do not write or paste implementation code (HTML/CSS/etc.) for him unless he explicitly asks you to.** Default mode is: diagnose the issue, explain the relevant concept, point to the specific file/line/property involved, and let him make the edit himself — then review what he wrote and say what's right or still off. This is a deliberate learning exercise for him, not just a means to a finished site. Plain factual/conceptual questions ("what does X do," "what is this selector") can be answered directly — the restraint is specifically about not writing his code for him. Copywriting/design brainstorming (phrasing, color choices) is fine to give concrete options for.

He works on this from multiple machines (work + home) and syncs via `git push`/`git pull` on `origin/main` — this file is the intended way a new session on either machine picks the above rule back up without him re-explaining it.

## Status (as of 2026-07-31)

Done: single `<h1>`/clean heading hierarchy, working `<meta name="description">`, sticky full-width nav (`<nav>` sits outside a `<main>` wrapper so it can span full width while `<main>` stays centered at `max-width: 700px`) with anchor links to `#transformations`, `#services`, `#process`, `#about`, `#contact`, solid green nav background with light text, flexbox horizontal nav layout (links centered with a `gap`, not stretched via `space-between`); Back to Top link fixed to use bare `#` instead of anchoring to the (always-visible, sticky) nav itself; real Sahar and Savannah bios written (replacing "Placeholder"), bio text left-aligned, body copy bumped to `1.2rem`; Services section filled in with four real categories (Closets & Wardrobes, Pantries & Kitchens, Garages & Storage Areas, Home and Moving Support), each a heading + description nested inside its `<li>`; Our Process filled in with a three-step explanation (no need to pre-clean, initial consultation call, follow-up with scope/cost); general `section` spacing opened up (`margin-top: 3rem`) so content-heavy sections don't run together, with `#contact` pushed down further still (`margin-top: 10rem`) as its own more-specific rule.

Still open: no responsive/mobile pass done yet; file is still named `SandS.html` — will need renaming to `index.html` before actual hosting (not urgent for local dev); "Book a consultation" text (currently plain `<p>`, not a link) still needs to become a real `<a>` pointing at `#contact` until Sahar/Savannah have a real booking flow; Services list items aren't marked up with a real heading tag for the category name yet (currently bare text above the nested `<p>`), worth revisiting for both semantics and visual hierarchy.

## Business setup follow-ups (not website code, but blocking a real launch)

Sahar and Savannah still need to sort out, before this can go live for real clients:

- A booking tool — free Calendly ("Basic" plan) or Google Calendar's built-in free "Appointment schedule" feature (they already have a Google account via their Voice number, so this may be less friction).
- Their shared Google Voice number is causing missed/misrouted calls (Savannah's supposed to take them, sometimes lands on mom's phone). Worth checking whether Voice is set up to forward-ring multiple phones at once rather than fully untangling the shared account.
- Sign up for Nextdoor — strong free channel for a hyper-local service business like this.
