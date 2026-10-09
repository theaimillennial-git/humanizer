---
name: humanizer
description: Rewrite or draft text so it reads like a person wrote it, by stripping the patterns that give away AI-generated text (inflated significance, AI vocabulary like delve/tapestry/testament, rule-of-three lists, "not just X but Y", throat-clearing intros, restate-the-intro conclusions, title-case headers, bold spam, em-dash overuse, chatbot leftovers). Use this skill whenever the user types /human or /humanizer, says "humanize", "make this sound human", "de-AI this", "remove AI tells", "sounds too ChatGPT", "make it less robotic", or pastes text and asks for a natural rewrite. Also apply it by default to any long-form prose Claude drafts for the user (blogs, articles, emails, landing-page copy, essays, reports, bios) unless the user says to skip it. Not for LinkedIn-specific posts when a dedicated LinkedIn humanizer skill exists.
---

# Humanizer

Rewrite text so it reads like a specific, thoughtful person wrote it, by removing the patterns that commonly show up in chatbot output.

## The one principle behind every rule

AI text is generic. It reaches for the most statistically likely word, structure and sentiment, so it inflates importance, hedges everything, lists in threes and summarises what it just said. Human text is specific. It states a thing, gives the concrete detail, and moves on.

So the fix is never just swapping banned words for synonyms. Swapping "delve" for "dig into" while keeping the hollow sentence around it fixes nothing. The fix is to make each sentence say something concrete, or cut it.

## Hard limits

- **Preserve meaning, facts, numbers, names and running order.** Never invent anecdotes, statistics, quotes, credentials or "personal experience" to sound human. If the source is vague, the rewrite stays vague but plain. Don't fill gaps with made-up specifics. Flag them instead (see Output).
- **Keep the user's voice.** If they've given samples or a style, match it. Don't flatten a casual writer into formal prose or vice versa.
- **Keep the format the content needs.** A spec stays structured; a legal doc keeps its precision. Humanizing is about removing tics, not removing clarity.
- **Don't promise detector scores.** AI detectors are unreliable and give inconsistent results. The goal is better writing. If the user asks for "0% AI", do the rewrite well and say plainly that no rewrite can guarantee a detector result.

## Workflow

1. **Read the whole text first.** Identify audience, purpose, and register (casual, professional, technical).
2. **Scan for tells.** For anything over a few paragraphs, run the scanner to catch vocabulary and punctuation patterns fast:
   ```bash
   python3 /path/to/humanizer/scripts/scan.py input.txt
   ```
   Then do a manual pass for the structural and tone patterns the script can't see. The full catalogue with examples and fixes is in `references/ai-tells.md`; read it on first use in a conversation, or whenever unsure whether something is a tell.
3. **Rewrite**, applying the rules below.
4. **Re-scan the rewrite** and fix anything that crept back in. Rewrites often reintroduce tells (especially rule-of-three and em dashes).
5. **Read it aloud in your head.** If a sentence sounds like a press release, a brochure or a school essay, fix it.

## Core rules (quick reference)

### Words and phrases
- Cut AI vocabulary: delve, tapestry, testament, pivotal, crucial, vibrant, robust, leverage, foster, underscore, showcase, intricate, multifaceted, realm, landscape (figurative), navigate (figurative), boast, seamless, elevate, unlock, harness, embark, journey (figurative), game-changer, ever-evolving, in today's fast-paced world. Full list in the reference.
- Cut significance inflation: "stands as a testament to", "plays a vital/pivotal role", "marks a significant milestone", "underscores the importance of", "leaves a lasting legacy", "a key turning point".
- Cut promotional adjectives: breathtaking, stunning, nestled, rich heritage, world-class, cutting-edge, unparalleled.
- Cut throat-clearing: "It's important to note that", "It's worth mentioning", "When it comes to", "In today's world", "Let's dive in".
- Cut signposting conclusions: "In conclusion", "In summary", "Overall", "Ultimately", "At the end of the day".
- Cut stacked hedges. One qualifier where uncertainty is real; none where it isn't.
- Prefer plain verbs. "is" and "has" beat "serves as", "stands as", "boasts", "features".
- Cut transition stacking: moreover, furthermore, additionally, in addition, notably.

### Structure
- **No reflexive triplets.** If a list has three items, check that there are really three. Two or four is fine. Never three adjectives in a row.
- **No "not just X, but Y" / "It's not X, it's Y"** constructions. State Y.
- **No trailing "-ing" commentary** ("..., highlighting the importance of X", "..., reflecting a broader trend", "..., ensuring that..."). Either make it its own sentence with a concrete claim, or delete it.
- **No intro that restates the question, no conclusion that restates the intro.** Start with the point. End when done.
- **Vary rhythm.** Mix short and long sentences. Avoid paragraphs that are all the same length.
- **Don't over-structure.** No headers or bullets on a 300-word piece. Sentence case for any headers, not Title Case.
- **No elegant variation.** If the subject is "the company", don't cycle through "the firm", "the organization", "the brand" to avoid repetition. Repeat the noun or use a pronoun.

### Tone
- No upbeat filler ("exciting", "a world of possibilities", "the future looks bright").
- No vague attribution ("experts say", "many believe", "studies show") without a source.
- No moralising or unrequested balance ("However, it's important to consider...") unless the content needs it.
- No sycophancy or chat leftovers ("Great question!", "I hope this helps", "Certainly!", "Here is a revised version:", "As an AI...", knowledge-cutoff disclaimers).

### Formatting and punctuation
- Em dashes: at most one per few paragraphs. Replace most with a comma, period, colon or parentheses.
- Bold: only for something the reader must not miss. Never bold phrases mid-paragraph for emphasis.
- No emojis in formal or professional text unless the user's own style uses them.
- Straight quotes and apostrophes, unless the destination styles them otherwise.

## Output

Default output:
1. The rewritten text, clean and ready to paste.
2. A short "What changed" note: 3 to 5 lines naming the main patterns removed. Skip this if the user asks for text only.
3. If the source had gaps the rewrite exposed (a claim with no evidence, a vague benefit), list them as one-line flags so the user can supply the specifics. Never fill them with invented detail.

When the user asks only to **check** or **audit** text, don't rewrite. List each tell found with the quoted phrase and a suggested fix, grouped by category, and end with an overall verdict (reads human / some tells / heavily AI-patterned).

When applying the skill silently to Claude's own drafts, just write clean prose. Don't add a "What changed" note.

## Example

**Before:**
> In today's fast-paced digital landscape, social media marketing has become more crucial than ever. It's not just about posting content — it's about building meaningful connections, fostering engagement, and driving growth. Our platform serves as a powerful tool, empowering businesses to unlock their full potential. In conclusion, leveraging AI is a game-changer.

**After:**
> Small businesses need to post on social media regularly, and most don't have time to make the posts. Our platform uses AI to draft them, so you spend your time reviewing instead of creating.

**What changed:** removed the "fast-paced landscape" opener and "In conclusion" closer; replaced "not just X, it's Y" and the triplet (connections/engagement/growth) with the actual problem; cut AI vocabulary (crucial, fostering, unlock, leveraging, game-changer).
**Flag:** the original has no concrete claim about results. Add a real number (time saved, posts per week) if you have one.
