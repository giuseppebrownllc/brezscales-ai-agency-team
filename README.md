# Your AI BrezScales Agency Team

Ten Claude skills that run a paid ads client from the kickoff call to month two. Each skill is one employee with one job. Sign a client, and the whole team is working that afternoon.

## The team

| # | Skill | Stage | What it does |
|---|---|---|---|
| 1 | [The Onboarder](skills/client-onboarder/SKILL.md) | Onboarding | Turns your kickoff call into a one page Client Brief plus the access checklist your client finishes on day one. |
| 2 | [The Offer Builder](skills/offer-builder/SKILL.md) | Onboarding | Writes the one offer the ads will run, with a real reason to act now. |
| 3 | [The Copywriter](skills/ad-copywriter/SKILL.md) | Creative | Writes the ads in your client's voice: five angles, each with primary text, headlines and a description. |
| 4 | [The Creative Director](skills/creative-director/SKILL.md) | Creative | Writes 20 hooks plus three video ads and three image ads, with the prompts to make them in Higgsfield and a finish prompt that adds captions and a Book Now button. |
| 5 | [The Page Writer](skills/page-writer/SKILL.md) | Creative | Writes the landing page, lead form and thank you page the ads send people to. |
| 6 | [The Media Buyer](skills/media-buyer/SKILL.md) | Campaigns | Lays out the campaign (budget, audience, structure, naming, tracking) as a build sheet for Ads Manager. |
| 7 | [The Speed to Lead Rep](skills/speed-to-lead/SKILL.md) | Campaigns | Writes the call script, texts and emails that reply to every new lead in five minutes. |
| 8 | [The Analyst](skills/ad-analyst/SKILL.md) | Reporting | Reads the week's numbers and tells you what to kill, keep and scale, and why. |
| 9 | [The Account Manager](skills/account-manager/SKILL.md) | Reporting | Turns the numbers into a plain English weekly report and a text for your client. |
| 10 | [The Renewal Rep](skills/renewal-rep/SKILL.md) | Retention | Builds the 30 day review and the conversation that keeps the client for month two. |

## How they work together

```
Kickoff call → 1 Onboarder → Client Brief
                               ↓
              2 Offer Builder → THE OFFER
                               ↓
     3 Copywriter + 4 Creative Director + 5 Page Writer
                               ↓
          6 Media Buyer → launch ← 7 Speed to Lead Rep
                               ↓
        every week: 8 Analyst → 9 Account Manager
                               ↓
                   day 30: 10 Renewal Rep
```

The Onboarder writes the **Client Brief**. Every other skill reads it, so you answer the client questions once. Keep the brief in the client's folder with the rest of their work.

## Install (about 5 minutes)

You need a paid Claude plan: Pro or Max. The free plan doesn't include Claude Code.

1. Download the Claude desktop app at [claude.ai/download](https://claude.ai/download) and sign in.
2. Click the **Code** tab at the top.
3. If it asks for a folder, open any folder. Your Desktop is fine.
4. Paste this and press Enter:
   ```
   Install all the skills from https://github.com/giuseppebrownllc/brezscales-ai-agency-team
   ```
5. Click Allow when Claude asks to run a command or create files.
6. When it says it's done, start a new session and type `/skills`. All ten should be on the list.

That's it. No downloads, no zip files, no terminal.

## Use it

Open the **Code** tab and just talk to Claude. The skills turn on when the job matches.

- "Here's my kickoff call with a roofer in Raleigh, build the client brief." → The Onboarder
- "Write the offer for this client." → The Offer Builder
- "Give me five ad angles for the free inspection offer." → The Copywriter
- "Here are this week's numbers, what do I change?" → The Analyst
- "Write this week's client report." → The Account Manager
- "Their first 30 days end Friday, build the review." → The Renewal Rep

Keep each client in its own folder so the Client Brief and the client's work stay together.

To update later, paste the same line again. Claude replaces the old copies with the new ones.

## For Claude: how to install these skills

When someone asks you to install the skills from this repo:

1. Download the repo into a temporary folder. Use `git clone --depth 1 https://github.com/giuseppebrownllc/brezscales-ai-agency-team.git`. If git isn't installed, download https://github.com/giuseppebrownllc/brezscales-ai-agency-team/archive/refs/heads/main.zip and unzip it instead.
2. Create the personal skills folder if it doesn't exist: `~/.claude/skills` (on Windows, `%USERPROFILE%\.claude\skills`).
3. Copy every folder inside `skills/` into that personal skills folder. Each one holds a `SKILL.md`. If a folder with the same name already exists, replace it. Copy nothing else from the repo.
4. Check that all ten folders are there, each with its `SKILL.md`: client-onboarder, offer-builder, ad-copywriter, creative-director, page-writer, media-buyer, speed-to-lead, ad-analyst, account-manager, renewal-rep.
5. Delete the temporary download.
6. Tell the user, in plain words, that the ten skills are installed, list them by their team names (The Onboarder, The Offer Builder, and so on), and tell them to start a new session and type `/skills` to see them. Don't show them commands or file paths unless they ask.

## Rules every skill follows

- No fake numbers, fake reviews, fake results or fake urgency. Missing information gets asked for, never guessed.
- Everything the client sees is written in plain English, in the owner's own voice.
- Ad spend is paid by the client straight to Meta. The agency's retainer is a separate line.
- Leads are only texted with consent from the form, with STOP honored and no texts at night.
- Meta policy: no ads that imply they know a viewer's personal traits, and Special Ad Categories are flagged for housing, credit and jobs.

## Using Claude in the browser instead?

The desktop app is the easy way. If you only use claude.ai in a browser, turn on **Code execution and file creation** in Settings, then upload each zip from the [`zips`](zips/) folder under **Skills**, **Upload skill**, one at a time.

---

The compliance notes in these skills are practical guardrails, not legal advice.

v1.0, October 2026. Built for the BrezScales 8 Week Bootcamp. Do not resell.
