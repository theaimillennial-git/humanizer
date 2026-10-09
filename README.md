# humanizer

A Claude skill that makes AI-written text read like a person wrote it.

It strips the patterns that give AI text away: words like *delve*, *tapestry* and *testament*, reflexive three-item lists, "it's not just X, it's Y", throat-clearing intros, conclusions that repeat the intro, em-dash and bold overuse, and leftover chatbot lines like "I hope this helps!"

It doesn't swap words for synonyms. It rewrites vague sentences to say something concrete, or cuts them, while keeping your meaning, facts and order intact. It never invents stats, quotes or anecdotes to sound human.

## Before and after

**Before**
> In today's fast-paced digital landscape, social media marketing has become more crucial than ever. It's not just about posting content — it's about building meaningful connections, fostering engagement, and driving growth. Our platform serves as a powerful tool, empowering businesses to unlock their full potential. In conclusion, leveraging AI is a game-changer.

**After**
> Small businesses need to post on social media regularly, and most don't have time to make the posts. Our platform uses AI to draft them, so you spend your time reviewing instead of creating.

## Install

### Claude Code

```
/plugin marketplace add theaimillennial-git/humanizer
/plugin install humanizer@theaimillennial
```

### Claude Desktop (Cowork)

In plugin settings, add a marketplace, enter `theaimillennial-git/humanizer`, then install **humanizer** from the list.

### Claude.ai

1. Download `humanizer.skill` from the [latest release](https://github.com/theaimillennial-git/humanizer/releases/latest).
2. Go to **Settings → Capabilities → Skills** and upload it.

Or download this repo, zip the `plugins/humanizer/skills/humanizer` folder, and upload the zip.

### Manual (Claude Code)

```bash
git clone https://github.com/theaimillennial-git/humanizer.git
cp -r humanizer/plugins/humanizer/skills/humanizer ~/.claude/skills/
```

## Use it

- Type `/humanizer` and paste your text.
- Or say "humanize this", "make this sound less like ChatGPT", or "remove the AI tells".
- Ask it to **check** or **audit** text if you only want the tells listed, without a rewrite.
- It also applies by default when Claude drafts long-form writing for you. Say "skip the humanizer" to turn it off for a piece.

Each rewrite comes with a short note on what changed, plus flags wherever the original was too vague to fix without real details from you.

## What's inside

```
plugins/humanizer/skills/humanizer/
├── SKILL.md                  # rules and workflow
├── references/ai-tells.md    # full catalogue of 16 tell categories with fixes
└── scripts/scan.py           # quick scanner for AI vocabulary, stock phrases, punctuation
```

You can run the scanner on its own:

```bash
python3 plugins/humanizer/skills/humanizer/scripts/scan.py your-draft.txt
```

## A note on AI detectors

This skill is built to make writing better, not to game detectors. Detector scores are inconsistent, and no rewrite can guarantee a result.

## License

MIT
