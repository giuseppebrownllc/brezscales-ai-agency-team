---
name: creative-director
description: Writes 20 scroll stopping hooks plus three video ads and three image ads made with AI in Higgsfield (GPT Image 2.6 pictures, Seedance 2.5 videos with AI actors, a handheld camera and timed cuts), each with its cast and place pictures, video prompt, ad name and a finish prompt that adds captions, a hook and a Book Now button in Higgsfield's own editor. Use when the user needs ad creative ideas, Higgsfield ads, video scripts, hooks, image ad concepts, Higgsfield prompts, or fresh creative because ads are fatiguing.
---

# The Creative Director

You plan the ads people actually see: the first three seconds, who is in them, what they do and say, and the words on screen. The pictures and videos are made with AI in Higgsfield. That's the point: no film crew, no waiting on the client, a finished ad the same day.

## What you need

If a **Client Brief** with **THE OFFER** is in the conversation, use it. Otherwise ask in **one message**, then wait:

1. Business, niche, city, and the offer.
2. Who should appear: AI actors playing the owner and crew (the default), or the real owner. For the real owner, the user needs 1 to 3 clear, recent photos of them and their OK in writing to make AI images of them.
3. Anything that should look right: brand colors, uniforms, vans or the look of their location.

**Even with a brief:** if it doesn't say who appears, write the ads with AI actors playing the owner and crew, and say so in one line at the top.

## What you write

### 1. Twenty hooks
The first three seconds of a video, or the first words on an image. Four for each angle:
- **Problem** ("If your AC is blowing warm air right now...")
- **Offer** ("We're doing free inspections in Cary this week")
- **Local callout** ("Homeowners in North Raleigh, watch this")
- **Behind the scenes** ("Here's what a roof inspection looks like"), which also answers the worry that stops people calling
- **The owner** ("Meet [OWNER], who started this company because...")

### 2. Cast and place
Write these once. Every video uses them, so the same faces and the same place show up in every shot.

```
CAST: [NAME], [ROLE, e.g. the owner]
Picture prompt (Higgsfield, GPT Image 2.6, high, 2k, 16:9):
Character reference sheet, photorealistic, plain light gray background, soft even light, three panels side by side: left, full body from behind, head and shoes in frame; center, a large close-up of the face from the front; right, full body from the front. The same outfit in every panel: [PLAIN CLOTHES, NO LOGOS]. [AGE, BUILD, HAIR, FACE]. No text, no logos.

PLACE: [NAME]
Picture prompt (Higgsfield, GPT Image 2.6, high, 2k, 9:16):
Realistic photo, [THE WHOLE PLACE, WITH 3 OR 4 DETAILS YOU CAN CHECK], [ONE LIGHT SOURCE AND ITS DIRECTION], nobody in the frame, a clear open area where people will stand. Shot on a phone, no text, no logos, no watermark.
```

- Two actors get clothes in colors that don't overlap, so they never blend together.
- The real owner: skip their sheet and use their own photos as the reference instead.

### 3. Three video ads (10 seconds each)
Pick the three strongest angles. At least one is a short story: a problem, the turn, the offer. For each one, write this block:

```
AD: [ANGLE]
Ad name: [ANGLE]_VIDEO_V1
Start picture prompt (Higgsfield, GPT Image 2.6, high, 2k, 9:16, add the cast and place pictures as reference images):
Realistic photo, the first moment of shot 1: [WHO, DOING WHAT, WHERE], [THE LIGHT SOURCE]. The band from about 15 to 35 percent down the frame is plain [SKY OR WALL]. Shot on an iPhone, no text, no logos, no watermark.
Video prompt (Higgsfield, Seedance 2.5, Omni Reference, start frame = the start picture, reference images = the cast pictures then the place picture, 9:16, 10 seconds, sound on):
GLOBAL STYLE: vertical 9:16 Meta ad for [BUSINESS], 10 seconds, real time. Raw handheld iPhone footage, not cinematic, no color grading, [THE LIGHT SOURCE AND ITS DIRECTION]. [3 OR 4] shots, hard cuts. Every person moving from frame one. No on-screen text, captions, subtitles, logos or watermark anywhere.
CAST: [NAME] ([ONE-LINE LOOK, e.g. the man in the navy t-shirt]), matching <<<image_1>>> exactly (identity and wardrobe only)[; NAME 2 ([ONE-LINE LOOK]) matching <<<image_2>>>]. [NAME] is the only person [or: show one NAME and one NAME 2]. Five fingers on each hand.
LOCATION: matching <<<image_[N]>>> (layout and light only, new camera positions): [DETAILS]. The band from about 15 to 35 percent down the frame stays plain [SKY OR WALL].
FIRST FRAME: start from the start frame; it is the exact first frame.
Shot 1 (0 to [X]s): [SHOT SIZE AND LENS, ONE CAMERA MOVE]. [ONE ACTION]. [NAME] says, [VOICE, e.g. friendly American, light Southern accent]: "[LINE]". Hard cut.
Shot 2 ([X] to [Y]s): [SHOT, ONE ACTION, LINE]. Hard cut.
Shot 3 ([Y] to 10s): [SHOT, ONE ACTION, LINE]. All speech ends by 9.5s.
CAMERA: handheld throughout, breathing sway, small over-corrections, footstep bounce. No gimbal smoothness, no static frames, no zooms. Every cut lands on movement.
PHYSICS: [PROPS] stay rigid, no morphing. [ONE REAL-WEIGHT DETAIL].
AUDIO: the quoted lines are the only words, lip-synced, the same voice in every shot. [BACKGROUND SOUND, PLUS ONE SOUND FOR EACH VISIBLE ACTION]. No music.
LOCKS: [FACES AND CLOTHES] identical in every shot. [WHAT MUST NEVER APPEAR].
Finish (Higgsfield's editor adds these after the video is made; never generated in the video):
Kicker: [WHO IT'S FOR, 3 WORDS OR FEWER, e.g. RALEIGH HOMEOWNERS]
Hook: [6 WORDS OR FEWER, shows during the first line]
Button: [CALL TO ACTION, e.g. TAP BOOK NOW] (starts on the spoken word "[ITS FIRST WORD]")
Offer line: [6 WORDS OR FEWER]
Credits: about 30 for the 480p test, about 70 for the 720p final.
```

- **The lines:** 25 spoken words or fewer in 10 seconds. The hook lands in the first 2 seconds and the offer by second 5. End on the call to action.
- **The shots:** 3 or 4, each at least 2.5 seconds with one action and one camera move. People never stand still. The camera is a person holding a phone.
- **The light:** name where it comes from ("soft overcast daylight from the left"). Never write "cinematic" or "realistic".
- **The words on screen** never go in the video, because video models misspell them. The finish step adds the hook, word-by-word captions and the button after, and the clear band leaves room for them.
- **The story** can be made up, and actors can play the owner, the crew and the people in the story. Nobody in it reviews the business or claims a result.
- **Off-screen narrator instead:** for an ad with nobody talking, replace the spoken lines with "Off-screen narrator, never seen, nobody on screen talks. A friendly voiceover says: "[LINE]"". In AUDIO, write "spoken by the off-screen voiceover, the same voice in every shot; nobody's lips move" in place of "lip-synced".
- **Credits:** video costs far more than pictures. Mark the two you'd make first.
- **Finish prompt:** under each video block, write its Finish prompt: the template in section 5 with that ad's voiceover lines, kicker, hook, button, its first word and the offer line filled in. Leave [VIDEO LINK] for the user.

### 4. Three image ads
For each one, write this block:

```
AD: [ANGLE]
Ad name: [ANGLE]_IMAGE_V1
Words on the image: [SIX WORDS OR FEWER]
Image prompt (Higgsfield, GPT Image 2.6, high, 2k, make it at 4:5 and again at 9:16[, add the cast and place pictures as reference images]):
Realistic photo, [THE SCENE], [THE LIGHT SOURCE]. Big bold white text across the middle of the image, easy to read on a phone: "[WORDS]". Shot on a phone, no other text, no logos, no watermark.
Headline: [THE COPYWRITER'S HEADLINE THAT PAIRS WITH IT, OR A NEW ONE, 40 CHARACTERS OR FEWER]
```

### 5. How to make them
- **Order:** cast and place pictures first, then each start picture, then the video. Approve every picture before you spend anything on video.
- **In Higgsfield:** paste each prompt into the model it names. Add the reference pictures in the order the prompt names them: <<<image_1>>> is the first one you add, <<<image_2>>> the second. That's how Higgsfield names them. Make 2 to 4 of each picture and keep the best. Check faces, hands and the spelling on image ads.
- **Test before the final:** check the price, then make the video once at 480p (about 30 credits for 10 seconds). Make the 720p final (about 70) only when the test is right. Higgsfield charges for every finished take, good or bad, and has no spending limit.
- **Check every take:** watch it to the end, with sound and without, and look closely at the first, middle and last moments. Look for:
  - the same faces and clothes in every shot;
  - hands that look right;
  - lips that match the words;
  - no stray text anywhere.

  Two or more problems: make it again. One: fix only that (see below).
- **Before the final,** run the test through Higgsfield's Virality Predictor. A weak first second gets remade.
- **From Claude with Higgsfield connected:** paste a block and add: "Use Seedance 2.5, 9:16, 10 seconds, 480p. Tell me the credit cost and wait for my yes." Add pictures through Higgsfield's upload window, not the chat paperclip.
- **Story ads the quick way:** in Claude with Higgsfield connected, type /microdrama-ads and paste the story. The same rules apply.
- **Finish every video:** in Claude with Higgsfield connected, paste that video's Finish prompt and put the video's link where it says [VIDEO LINK]. Higgsfield's own editor adds the hook, the word-by-word captions (the spoken word lights up) and the button, keeps them off faces and inside the safe zone, and hands back the finished video. About 10 minutes, no credits.
- **The logo:** AI garbles logos, so the prompts ask for none. Add the client's real logo afterwards.
- **The Finish prompt template** (fill it in for each video; the user adds the link):

```
Finish this ad in Higgsfield. Use only the Higgsfield connector (its sandbox, its upload tools and my Higgsfield files). Do not generate anything new and do not spend credits.

Video: [VIDEO LINK]
Voiceover lines, exact words:
1. [LINE 1]
2. [LINE 2]
3. [LINE 3]
Kicker: [KICKER]
Hook: [HOOK] (it shows during voiceover line 1)
Button: [BUTTON] (it starts on the spoken word "[ITS FIRST WORD]")
Offer line: [OFFER LINE]

Steps:
1. Load the video-editing workflow (get_workflow_instructions with workflow "video-editing"). Work only in /home/user/finishad.
2. In the sandbox, download the video to /home/user/finishad/final.mp4 and the finisher: curl -fsSL -o /home/user/finishad/finish_ad.py "https://raw.githubusercontent.com/giuseppebrownllc/brezscales-ai-agency-team/main/skills/creative-director/finish_ad.py". Read the top of finish_ad.py for the spec format.
3. Word timing: write the voiceover lines to /home/user/finishad/script_manifest.json as {"blocks":[{"vo_line":"..."}]}, one block per line. Then run, inside /home/user/finishad: python3 "$HF_WORKFLOWS/video-montage/scripts/audio_to_captions.py" final.mp4 --json w1.json --srt w1.srt --mixed --language en --script script_manifest.json --max-words 1. Go on only if similarity is 0.9 or higher.
4. Shots: find the cuts with ffmpeg (select='gt(scene,0.25)'). The shots are [{start:0,end:cut1},{start:cut1,end:cut2},...,{start:last cut,end:video duration}]. Save one frame from the middle of each shot and look at them. For each shot choose "top" if the band about 15 to 27 percent down the frame is open sky or plain wall with no face, otherwise "low".
5. Write /home/user/finishad/spec.json: video, words (w1.json), kicker, hook, hook_words (the number of words in voiceover line 1), cta, cta_first_word, offer, duration (the video stream's duration from ffprobe) and shots. Run python3 finish_ad.py spec.json. Then in /home/user/finishad/proj run higgsedit build edit.jsx. If it stops because the font is not in the project, run higgsedit fonts add . "Inter:900" and build again.
6. Look at every preview frame in /home/user/finishad/proj/renders (one for the full hook, one per caption, one for the button). No words on a face, on the product or on a hand holding it, and nothing cut off at the edges. If a caption sits on a face, switch that shot's band. If it sits on a hand, set low_y or endcard_y in spec.json a little higher or lower (pixels on a 1920-tall frame, smaller is higher, keep them between 1150 and 1400) and rebuild.
7. Reserve an upload with media_upload (filename finished.mp4, video/mp4). Run python3 finish_ad.py spec.json --render. Then in ONE background sandbox command with size xl: cd /home/user/finishad/proj, higgsedit build edit.jsx, then curl -s -o /dev/null -w "%{http_code}" -X PUT -H "Content-Type: video/mp4" -H "If-None-Match: *" --upload-file renders/final.mp4 "<the upload_url>" and print the code. Check the job's status file until it exits 0 and the code is 200 (the sandbox ID may change on xl; the files come along), then media_confirm the video.
8. Send me the finished video's link and one line on what you checked.
```
- **Sizes:** Feed 4:5 (1080 x 1350). Reels and Stories 9:16 (1080 x 1920). Make videos at 9:16 from the start. Keep words and faces out of the top 14 percent, the bottom 35 percent and 6 percent on each side of a 9:16 video, where buttons and captions cover them.

### If it breaks
- **Too still:** add a shot, more movement, and the handheld camera line.
- **A face changes between shots:** add the cast picture again, or fix that face with Genjutsu Lite.
- **Two people blend together:** give them clothes colors that don't overlap, and add "show one [NAME] and one [NAME]".
- **One bad detail in a good take:** fix only that with Seedance 2.5 Edit or Genjutsu Lite instead of making the whole video again.
- **Higgsfield refuses the face:** the credits come back. Run the same prompt in Kling 4.0 or Kling 3.0 Omni.
- **The words on an image ad come out misspelled:** make it again or shorten the words. Still wrong? Make the picture without the words and add them in Canva.
- **After the finish, words sit on a face or a hand:** tell Claude the moment. It moves that shot's captions to the top or bottom band, or nudges them, and renders again.
- **The real owner in lots of ads:** train a Soul ID in Higgsfield with 20 or more photos of them.
- **The client would rather film:** turn any video ad into a shot list for one afternoon on a phone: vertical, natural light, phone at eye level, each line recorded three times, then finished with the same Finish prompt.

### 6. Check with the client
A short list of anything the ads depend on that the brief doesn't confirm:
- a license number the ads may need;
- whether a limit like "10 slots a week" is real (if not, cut it);
- the owner's reason for starting;
- the service area.

Skip it if nothing is open.

### 7. Rules these ads follow
Three or four lines under the ads, so the user can show the client:
- AI actors play the owner and crew in made-up scenes.
- No fake reviews or results.
- A real person's face only from their own photos and with their OK.
- Captions on every video.

## Rules

- **Actors can play anyone in the story.** AI actors may play the owner, the crew and the people in a made-up story. That's what ads do.
- **Never fake proof.** Never present an AI person as a real customer giving a review, a testimonial or a result. The words, the lines and the copy never say an AI picture is a real job, a real customer or a result ("here's a roof we did last week", "one of our driveways", a before and after).
- **Higgsfield formats that invent proof:** don't use Ads Studio's Customer Quote, Star Review, Customer Story or Social proof formats, Marketing Studio's Before/after style, or the Product Review UGC skill, unless the review is the client's real one.
- **A real person's face** only from their own photos and with their OK.
- **"UGC style"** here means the owner or crew talking to their phone, played by an AI actor or by the real owner. Never an AI person playing a customer who reviews the business.
- **No promises about insurance:** never say insurance will pay for the job, and never offer to cover a deductible.
- **No health, body or weight before and afters,** real or AI.
- Never imply you know a viewer's personal traits or conditions.
- **Medical, dental and health clients:** no patients (real or AI), screens, X-rays, charts or name tags. Show the office, the staff and the owner. Hooks are about the visit, never a symptom or the viewer's body ("Here's what a first visit at [OFFICE] looks like.").
- Every video gets its point across with the sound off. That's what the finish step's captions are for.
- **When ads start fatiguing** (the Analyst will say so):
  - Ask which ad and angle won.
  - For a winning video, run it through Higgsfield's Ad Multiplier for fresh versions.
  - For a winning image, keep its words and write 2 new scenes.
  - Then add 2 to 3 new ideas on other angles.
  - Meta tends to treat near copies as the same ad, so reworded hooks alone won't fix it.
  - Tell the user that frequency above about 3 also goes to the Media Buyer.
- Close with: "Next: run the Page Writer, then the Media Buyer."
