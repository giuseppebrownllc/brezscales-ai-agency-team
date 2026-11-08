#!/usr/bin/env python3
"""finish_ad.py: turns a generated 9:16 ad video into a finished Meta ad with Higgsfield's Higgsedit.

Adds a hook (kicker pill + big title that builds word by word), word-by-word captions
(spoken word highlighted), and an end card (CTA button + offer line). Runs inside the
Higgsfield sandbox. Usage:
  python3 finish_ad.py spec.json            -> writes <proj>/edit.jsx (preview frames)
  python3 finish_ad.py spec.json --render   -> writes <proj>/edit.jsx that renders <proj>/renders/final.mp4
  Default <proj> = /home/user/finishad/proj (set "proj" in the spec to change it).

spec.json:
{
  "video": "/home/user/ad/final.mp4",
  "words": "/home/user/ad/w1.json",          # audio_to_captions.py --max-words 1 --json output
  "kicker": "RALEIGH HOMEOWNERS",
  "hook": "ROOF 15+ YEARS OLD?",
  "hook_words": 6,                            # how many spoken words the hook covers
  "cta": "TAP BOOK NOW",
  "cta_first_word": "Tap",                    # spoken word where the end card starts
  "offer": "FREE ROOF INSPECTION + PHOTOS",
  "shots": [{"start": 0, "end": 2.458, "captions": "top"}, ...],   # "top" = sky band, "low" = under the subject
  "duration": 10.04,                         # ffprobe video stream duration
  "accent": "#FFD400",
  "low_y": 1295, "endcard_y": 1270, "top_y": 300, "hook_y": 290   # optional pixel tops (1080x1920); smaller numbers sit higher; nudge low_y/endcard_y down (up to about 1400) to clear a hand
}
"""
import json, math, sys
from PIL import ImageFont

spec = json.load(open(sys.argv[1]))
RENDER = "--render" in sys.argv
FONT = "/opt/fable/fonts-kit/inter-900.woff2"   # same face the project vendors with `higgsedit fonts add . "Inter:900"`
import os
PROJ = spec.get("proj", "/home/user/finishad/proj")
os.makedirs(PROJ + "/renders", exist_ok=True)
ACC = spec.get("accent", "#FFD400")
TOP_Y, LOW_Y = spec.get("top_y", 300), spec.get("low_y", 1295)
HOOK_Y, END_Y = spec.get("hook_y", 290), spec.get("endcard_y", 1270)
_F = {}


def mw(t, size, ls=0, sw=0):
    if size not in _F:
        _F[size] = ImageFont.truetype(FONT, size)
    return int(_F[size].getlength(t) + ls * len(t) + 2 * sw + 8)


def esc(t):
    return t.upper().replace("{", "").replace("}", "").replace("<", "").replace(">", "")


caps = json.load(open(spec["words"]))["captions"]
W = [(c["text"], float(c["start"]), float(c["end"])) for c in caps]


def silences(path):
    """[(start, end)] of silent stretches in the voice track (ffmpeg silencedetect, -35 dB, 0.2 s)."""
    import subprocess, re
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "highpass=f=120,silencedetect=noise=-35dB:d=0.2",
                        "-f", "null", "-"], capture_output=True, text=True)
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    return list(zip(st, en))


# Whisper word clocks fold the pause before a word into that word. Move each start to the end of any
# silence inside it, so captions light up and the end card lands when the word is actually heard.
SIL = [] if spec.get("no_silence_fix") else silences(spec["video"])
fixed = []
for t, s, e in W:
    for a, b in SIL:
        if s - 0.05 <= a < e and s + 0.05 < b < e:
            s = max(s, b - 0.04)
    fixed.append((t, s, e))
W = fixed
END = float(spec["duration"])          # the video stream's duration from ffprobe
shots = spec["shots"]


def band_at(t):
    for s in shots:
        if s["start"] - 1e-6 <= t < s["end"]:
            return s["captions"]
    return shots[-1]["captions"]


def cuts():
    return [s["end"] for s in shots[:-1]]


# ---- word groups for captions (after the hook, before the CTA) ----
hook_n = int(spec.get("hook_words", 0))
cta_i = next((i for i in range(hook_n, len(W)) if W[i][0].strip(".,!?").lower() == spec["cta_first_word"].lower()), len(W))
body = W[hook_n:cta_i]
phrases, cur = [], []
for w in body:
    cur.append(w)
    if w[0][-1] in ",.?!;:":
        phrases.append(cur); cur = []
if cur:
    phrases.append(cur)
groups = []
for ph in phrases:
    n = len(ph); k = max(1, math.ceil(n / 4)); size = math.ceil(n / k)
    for j in range(0, n, size):
        groups.append(ph[j:j + size])


def word_node(t, ws, we, c0, dur, size=84):
    sw = max(6, size // 9)
    kf = [{"at": 0, "value": "#FFFFFF", "easing": "hold"}]
    a = max(0.001, ws - c0); b = max(a + 0.05, we - c0)
    if a < dur - 0.002:
        kf.append({"at": a, "value": ACC, "easing": "hold"})
        if b < dur - 0.001:
            kf.append({"at": b, "value": "#FFFFFF", "easing": "hold"})
    anim = (' animate={[{property:"color",keyframes:%s}]}' % json.dumps(kf)) if len(kf) >= 2 else ""
    return ('<text width={%d} height={%d} align="center" fontFamily="Inter" fontWeight={900} fontSize={%d} color="#FFFFFF" '
            'strokeColor="#000000" strokeWidth={%d} shadow={{y:5,blur:14,color:"rgba(0,0,0,0.55)"}}%s>%s</text>'
            ) % (mw(esc(t), size, 0, sw), int(size * 1.25), size, sw, anim, esc(t))


def caption(seg, a, b):
    y = TOP_Y if band_at(a) == "top" else LOW_Y
    inner = "".join(word_node(t, ws, we, a, b - a) for t, ws, we in seg)
    return ('<frame layout="none"><frame x={65} y={%d} width={950} height={120} layout="row" gap={16} align="center" '
            'justify="center" wrap={true} origin="center" motion={{enter:{from:{scale:0.86,opacity:0},duration:0.14}}}>%s</frame></frame>'
            ) % (y, inner)


def pop(txt, at, size):
    return ('<text width={%d} height={%d} align="center" fontFamily="Inter" fontWeight={900} fontSize={%d} color="#FFFFFF" '
            'strokeColor="#000000" strokeWidth={14} shadow={{y:6,blur:16,color:"rgba(0,0,0,0.55)"}} '
            'animate={[{property:"opacity",keyframes:[{at:0,value:0,easing:"hold"},{at:%.3f,value:1}]},'
            '{property:"scale",keyframes:[{at:0,value:0.6,easing:"hold"},{at:%.3f,value:0.6},{at:%.3f,value:1.08},{at:%.3f,value:1}]}]}>%s</text>'
            ) % (mw(txt, size, 0, 14), int(size * 1.2), size, max(0.001, at), max(0.001, at), at + 0.10, at + 0.18, txt)


out = ["export default async ({ project }) => {",
       ' const p = await project({ size: "1080x1920", fps: 24, background: "#000000" });',
       ' const v = await p.add("%s");' % spec["video"],
       ' p.cut(v, { from: 0, dur: %.3f, at: 0, fit: "cover" });' % END]

# ---- hook ----
hook_end = W[hook_n][1] if hook_n < len(W) else min(2.5, END)
if spec.get("hook"):
    hw = esc(spec["hook"]).split()
    size = 128
    while True:  # split into at most 2 balanced lines that fit 950 px
        best = None
        for k in range(1, len(hw)):
            l1, l2 = " ".join(hw[:k]), " ".join(hw[k:])
            m = max(mw(l1, size, 0, 14), mw(l2, size, 0, 14))
            if best is None or m < best[0]:
                best = (m, k)
        if len(hw) == 1:
            best = (mw(hw[0], size, 0, 14), 1)
        if best[0] <= 950 or size <= 72:
            break
        size -= 8
    k = best[1]
    # each title word pops on its spoken word when the counts line up, otherwise spread across the spoken line
    spoken = [w[1] for w in W[:hook_n]] if hook_n else []
    if spoken and len(hw) <= len(spoken):
        times = spoken[:len(hw)]
    else:
        t0 = W[0][1] if W else 0.1
        t1 = W[hook_n - 1][2] if hook_n else t0 + 1.5
        times = [t0 + i * max(0.3, t1 - t0) / max(1, len(hw)) for i in range(len(hw))]
    l1 = "".join(pop(w, times[i], size) for i, w in enumerate(hw[:k]))
    l2 = "".join(pop(w, times[k + i], size) for i, w in enumerate(hw[k:]))
    kick = ""
    if spec.get("kicker"):
        kt = esc(spec["kicker"]); kw = mw(kt, 46, 2)
        kick = ('<frame x={0} y={%d} width={1080} height={80} layout="row" justify="center" align="center">'
                '<frame background="%s" radius={14} padding={{top:10,right:26,bottom:10,left:26}} width={%d} height={70} layout="row" '
                'justify="center" align="center" motion={{enter:{from:{y:-20,opacity:0},duration:0.25}}}>'
                '<text width={%d} height={58} align="center" fontFamily="Inter" fontWeight={900} fontSize={46} letterSpacing={2} '
                'color="#000000">%s</text></frame></frame>') % (HOOK_Y, ACC, kw + 60, kw, kt)
    title = ('<frame x={65} y={%d} width={950} height={%d} layout="column" align="center" justify="start">'
             '<frame layout="row" gap={28} justify="center" align="center" width={950} height={%d}>%s</frame>'
             '<frame layout="row" gap={28} justify="center" align="center" width={950} height={%d}>%s</frame></frame>'
             ) % (HOOK_Y + 75, int(size * 2.5), int(size * 1.1), l1, int(size * 1.1), l2 if l2 else "")
    out.append(' p.compose(<frame layout="none">%s%s</frame>, { at: 0, dur: %.3f, name: "Hook" });' % (kick, title, hook_end))

# ---- captions, split at shot cuts so each part sits in its shot's band ----
for g in groups:
    c0, c1 = g[0][1], g[-1][2]
    edges = [c0] + [c for c in cuts() if c0 < c < c1] + [c1]
    for a, b in zip(edges, edges[1:]):
        if b - a >= 0.02:
            out.append(" p.compose(%s, { at: %.3f, dur: %.3f });" % (caption(g, a, b), a, b - a))

# ---- end card ----
if cta_i < len(W) and spec.get("cta"):
    ts = W[cta_i][1]
    ct, of = esc(spec["cta"]), esc(spec.get("offer", ""))
    cw = mw(ct, 70)
    card = ('<frame layout="none"><frame x={140} y={%d} width={800} height={130} layout="row" justify="center" align="center" '
            'origin="center" motion={{enter:{from:{scale:0.7,opacity:0},duration:0.3}}}>'
            '<frame background="%s" radius={70} padding={{top:22,right:54,bottom:22,left:54}} width={%d} height={120} justify="center" '
            'layout="row" gap={18} align="center" shadow={{y:8,blur:24,color:"rgba(0,0,0,0.45)"}}>'
            '<text width={%d} height={86} align="center" fontFamily="Inter" fontWeight={900} fontSize={70} color="#000000">%s</text>'
            '</frame></frame>') % (END_Y, ACC, cw + 108, cw, ct)
    if of:
        card += ('<frame x={65} y={%d} width={950} height={70} layout="row" justify="center" align="center" '
                 'motion={{enter:{from:{y:16,opacity:0},duration:0.3}}}><text width={%d} height={58} align="center" fontFamily="Inter" '
                 'fontWeight={900} fontSize={44} color="#FFFFFF" strokeColor="#000000" strokeWidth={7} letterSpacing={1}>%s</text></frame>'
                 ) % (END_Y + 150, mw(of, 44, 1, 7), of)
    card += "</frame>"
    out.append(' p.compose(%s, { at: %.3f, dur: %.3f, name: "EndCard" });' % (card, ts, END - ts))

if RENDER:
    out.append(' const r = await p.render("renders/final.mp4", { bitrate: 10000000 });')
    out.append(' console.log(JSON.stringify({frames: r.frames, dur: r.durationSeconds}));')
else:
    marks = [round(hook_end - 0.05, 2)]
    for g in groups:
        marks.append(round((g[0][1] + g[-1][2]) / 2, 2))
    if cta_i < len(W):
        marks.append(round(min(END - 0.1, W[cta_i][1] + 0.4), 2))
    out.append(" for (const t of %s) await p.frame(t, `renders/f_${t}.png`);" % json.dumps(sorted(set(marks))))
out.append("};")
open(PROJ + "/edit.jsx", "w").write("\n".join(out))
print(json.dumps({"words": len(W), "groups": [" ".join(x[0] for x in g) for g in groups], "end": END,
                  "hook_end": hook_end, "cta_at": W[cta_i][1] if cta_i < len(W) else None}))
