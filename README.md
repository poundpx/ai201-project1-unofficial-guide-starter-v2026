# The Unofficial Guide

# Minh Nguyen - corpus : Advice_threads

> This file is your submission. Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in RUNNING.md.
> Leave that file alone.
>
> Paste everything as text. No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The <!-- --> comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

> The corpus i choose is advice thread and it mostly about life in campus


     Milestone 5. -->

## Chunking Strategy

Chunk size: Thread length one per chunk
Overlap: no in between thread

## Sample Chunks


======================================================================
Chunk 1  |  source: thread_bike_commute.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

--- reply 3 (22 votes) ---
Both true. I keep a cheap bike for September to November and walk the rest of the year. Total cost was about $120 for the bike and I don't care what happens to it.

--- reply 4 (5 votes) ---
If you do get one, the campus does free registration and it's the only reason I got mine back after it was taken.

======================================================================
Chunk 2  |  source: thread_first_gen.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Anything specific for first-generation students?

--- reply 1 (33 votes) ---
The advising office has a specific programme and it is genuinely good, but it is opt-in and badly publicised. Ask for it by name.

--- reply 2 (41 votes) ---
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

--- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.

======================================================================
Chunk 3  |  source: thread_laptop_specs.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: How much laptop do I actually need for CS courses?

--- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice.

--- reply 2 (18 votes) ---
Adding: the lab machines exist and are better than anything you'll buy. For the heavy assignments people just use those.

--- reply 3 (12 votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.

======================================================================
Chunk 4  |  source: thread_office_hours_etiquette.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.

--- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up.

--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.

======================================================================
Chunk 5  |  source: thread_professor_email.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Do professors actually answer email?

--- reply 1 (21 votes) ---
Varies enormously. General rule I've found: if the syllabus states a response window, it's honoured. If it doesn't, assume 48 hours and don't panic before then.

--- reply 2 (33 votes) ---
Office hours are dramatically more effective than email for anything that takes more than two sentences to answer. They're also usually empty.

--- reply 3 (15 votes) ---
Empty office hours is the biggest unused resource here and I say that having wasted a year not going.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?

## why?
The starter's chunker made 26 chunks from my 23 documents.
3 of them were fragments, the shortest being 2 characters.
My chunker keeps each thread whole, so it makes 23 chunks with a shortest of 317 characters.
reason being is these can have all important document inside so it feel whole it doesnt change much but as data expanding it could make more fragment and could be some missing case 
 

## Sample Answer

 python app.py ask "which meal plan tier should I get?"
  (best distance 0.286, cutoff 0.65)

If your building has a kitchen (like Fenwick, which has kitchenettes), you should go down a tier and cook two or three nights. Everywhere else, you should get the middle tier. (Source: thread_meal_plan_tier.txt)

Sources retrieved: thread_first_year_regret.txt, thread_laptop_specs.txt, thread_meal_plan_tier.txt, thread_pass_fail.txt, thread_study_spots.txt

My relevance cutoff:

>my recent cut off increase from 0.6 to 0.65 because i feel like this would be bit closer and give some room for right answer because if we look in case of of answer of textbook it very close like .59 so .65 is still within range and cutoff not near it too 
/*
> python app.py retrieve "is it ok to use a previous edition textbook for a math class?"

>Question: is it ok to use a previous edition textbook for a math class?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.5896     thread_textbook_editions.txt     THREAD: Does the edition of the textbook matter?  --...
2   0.6715     thread_printing.txt              THREAD: Is the printing quota enough?  --- reply 1 (...
3   0.6983     thread_first_gen.txt             THREAD: Anything specific for first-generation stude...
4   0.7445     thread_late_work.txt             THREAD: What actually happens if you hand something ...
5   0.7951     thread_group_project.txt         THREAD: How do you handle a group project where some...

Gate: best distance 0.590 is under the 0.65 cutoff

Lower is better. 0.3 is a close match, 0.9 is unrelated.
Milestone 4: run your five questions, then the five in OUT_OF_SCOPE
that your documents clearly don't cover, and look for the gap
between the two groups. Your cutoff goes in that gap.
(.venv) PS C:\Users\Poundpx\CodepathAI201\Codepath201x2\ai201-project1-unofficial-guide-starter-v2026> 
*/


| Question | In corpus? | Best distance |
|---|---|---|
| which meal plan tier should I get? | Yes | 0.286 |
| is there an app for the laundry machines? | Yes | 0.453 |
| is biking worth it in the winter? | Yes | 0.458 |
| is it common to go into office hours just to talk? | Yes | 0.557 |
| is it ok to use a previous edition textbook for a math class? | Yes | 0.590 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.828 |
| How do I write a for loop in Rust? | No | 0.871 |
| How do I change the oil in a diesel engine? | No | 0.930 |
| What is the capital of Mongolia? | No | 0.948 |
| Who won the 1994 World Cup? | No | 0.952 |

## How I Used AI

1.(Unit 1)
     For this work i have been used ai to keep track for me on my progress because there so many files that am not well familiarize with it and it very usefull to be my mentor and guide me through each question with doubtfull instead of giving me helping hand it only give hint and lets me do all the step by myself and drive me to the answer i feel like it was right. This give me room that i want to see more in other way. The way i ask for it to do many thing for me like generate path and guide but it only help on exploring instead so i have to stick with one path and drive up onto decision all by my self 

     moment 1 : when i stumble on expecting and i though it mean like what the ai going to answer back but those keyword never show up but just like expectation and i misunderstanding it my ai teacher clarify and walk me through which one with real evidence of what my llm output ask look like 

2.
     The real gem on this project that i can use ai to explore later after i have know the work flow what i would change next time is instead of lecturing me theres another ai serve as visualizer side by side that help me see what possibilities while drafting for answer instead.

3. (Unit 2)
     Used ai this unit mainly to help spot the pattern behind my two failing test questions instead of just guessing. It read the actual retrieved chunks and generated answers for both misses and pointed out they weren't the same kind of failure — one was my own typo in questions.py middles vs middle, the other was the model actually dropping a real fact from the source chunk. That second one is what pointed me at GROUNDING_INSTRUCTION's "be brief" line in generate.py as the thing to change, rather than picking a fix at random. It also caught that scorer.py's original judge() function had its logic backwards (answer in expects instead of expects in answer), which was silently failing every single question before I even got real data to diagnose.



<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

python run_eval.py --label before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks are complete threads | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Named source contains the stated fact | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

 Note on scorer.py  the version in the repo before this unit had judge() written backwards
if answer in expects checks whether the whole generated answer is literally a substring of
 the one-word expects keyword (e.g. "salt"), which can never be true. It scored every single
 question as a fail. I rewrote it to expects.strip().lower() in answer.lower() — does the
 expected keyword show up in the answer — before any of the numbers above are real.

Real output — run_once in run_eval.py, generation from generate.py::answer_from_chunks (before the fix):


### what meal plan available? — run 1
Best distance: 0.4626 (passed the gate)
Sources retrieved: thread_first_year_regret.txt, thread_laundry_timing.txt, thread_meal_plan_tier.txt, thread_roommate_conflict.txt, thread_study_spots.txt

Based on the provided documents, the meal plan options mentioned are the highest tier, the middle
tier, and a lower tier for buildings with kitchenettes like Fenwick.

Source: thread_meal_plan_tier.txt



### is it common to go into office hours just to talk? — run 1
Best distance: 0.5574 (passed the gate)
Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_sleep_schedule.txt

Yes, it is completely normal to go to office hours with no specific question, such as saying you
are following the lectures but do not feel like you understand the shape of it. This information
comes from thread_office_hours_etiquette.txt.


## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MISSED | 3/5 in all three runs, never once reaching 4/5. Consistent, not a fluke. |
| 2 | Every answer names a source | MET | Every one of the 15 answers across 3 runs ended with an explicit Source: line. |
| 3 | Gate stops out-of-corpus questions | MET | All 5 OUT_OF_SCOPE questions refused, distances 0.828–0.952, well clear of the 0.65 cutoff. |
| 4 | Sampled chunks are complete threads | MET | Chunker keeps one whole thread per chunk (Milestone 3 change); sampling any 5 of the 23 chunks gives 5 complete threads. |
| 5 | Named source contains the stated fact | MET | Checked each answer's cited file against what it claimed — the meal-plan tiers, the laundry-app quirk, the textbook numbering fact, the bike/salt fact, and the office-hours claim all match their cited thread. |

The close call was #1. Read plainly: 3/5 stayed 3/5 across all three runs, so it's a real miss, not a target set too tight that got unlucky once.

## Diagnoses

Criterion 1 (retrieved chunk contains the answer) — MISSED, and it's two different things wearing the same "fail" label:

- "what meal plan available?" — not a pipeline failure, a test-authoring bug. The retrieved
  chunks always include thread_meal_plan_tier.txt, and the generated answer always says "the
  middle tier" (all 3 runs). My expects keyword in questions.py is "middles" — a
  typo for "middle" — so the literal-keyword scorer can never match it. The retrieval and
  generation stages are both doing their job here; the miss is in my own test data. I'm leaving
  the typo in place rather than quietly fixing it (see the "one rule about changing your system"
  note — my test questions aren't part of the system I'm allowed to touch mid-unit), but it means
  this question can never pass criterion 1 as currently written regardless of what the system does.

- "is it common to go into office hours just to talk?" — a real generation-stage failure. The
  retrieved chunk (thread_office_hours_etiquette.txt) contains "They're usually empty," which is
  the specific supporting detail my expects keyword ("empty") targets. Across all 3 runs before
  the fix, the model's answer covered the "main" claim (going in with no question is normal) but
  dropped that detail every time. The cause traces to GROUNDING_INSTRUCTION in generate.py:
  "Be brief. Two or three sentences is usually enough." The model was told to compress, and
  compressing a multi-fact thread into 2–3 sentences means picking the most salient claim and
  cutting the rest — retrieval had the right chunk in hand the whole time.

Pattern across the two misses: retrieval is not the bottleneck (the correct source thread showed
up in the top-5 for all 5 questions, all 3 runs). One miss is a bug in my own test data; the other
is the prompt telling the model to be shorter than the source material supports.

## The Improvement

What I changed: In generate.py, replaced the grounding instruction's "Be brief. Two or
three sentences is usually enough." with an instruction to include every distinct fact from the
matching excerpt that bears on the question, explicitly ranking completeness over brevity.

Why I picked it: It follows directly from the office-hours diagnosis above — the retrieved
chunk already had the missing fact, so the fix belongs at generation, not retrieval or chunking.

### Run Log — After

python run_eval.py --label after 
| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks are complete threads | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Named source contains the stated fact | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

Real output, same question, after the prompt change:


### is it common to go into office hours just to talk? — run 3
Based on the provided documents, going to office hours without a specific question is not weird,
and it is the single most common thing first years get wrong (thread_office_hours_etiquette.txt).
Additionally, office hours are usually empty, so you are doing the instructor a favor by turning
up (thread_office_hours_etiquette.txt, thread_professor_email.txt). You can treat it as a standing
appointment by going every week for a month until it stops feeling like a thing, and it is
completely normal to say something like, "I'm following the lectures but I don't feel like I
understand the shape of it" (thread_office_hours_etiquette.txt).


Did it help? Yes, and precisely as the diagnosis predicted. The office-hours question went
from fail/fail/fail to pass/pass/pass across all 3 runs — the "empty" detail now shows up every
time. Criterion 1 moved from 3/5 (MISSED) to 4/5 (MET). The meal-plan question is still a fail in
every run, which is expected: that miss was never a generation problem, so a generation-side fix
correctly didn't touch it.

## What's Still Broken

- Criterion 1 is technically MET now (4/5) but only because 4/5 is the target, not 5/5. The
  meal-plan question will keep failing until questions.py's expects: "middles" is corrected to
  "middle" — that's a one-line fix, but it's a change to test data, not to the system, so it's
  out of scope for this unit's "one change" rule. Next unit (or right now, off the clock) I'd fix
  the typo and re-run to confirm it's really 5/5.
- The scorer is still a blunt instrument. It's an exact-substring keyword match against the
  full generated answer. It works here because my keywords are short and specific, but a model that
  says "the cost of the bike was about $120" instead of using my exact keyword would still fail
  even with a perfectly correct answer. I didn't build anything smarter (e.g. an LLM-as-judge)
  because the two failures I actually had were fully explained without needing one, and building
  one un-diagnosed would have been solving a problem I hadn't shown I had.

## What I'd Do Differently
Criterion 1's wording — "the retrieved chunks include one that contains the answer" — describes
retrieval, but the only automatic way to check it (scorer.py::judge) actually inspects the
generated answer, not the retrieved chunks in results. Those two things mostly agree, but they
disagree exactly on the interesting cases: this unit's office-hours miss was really about
generation dropping a fact retrieval had already found correctly. Next time I'd write two separate
criteria — one that checks results directly for whether the answer text is present in a
retrieved chunk (a true test of retrieval), and one that checks the final generated answer (a test
of generation) — instead of one criterion that quietly conflates both stages and pointed me toward
the wrong stage the first time I read the numbers.
