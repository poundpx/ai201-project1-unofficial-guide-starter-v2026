# The Unofficial Guide

# Minh Nguyen - corpus : Advice_threads

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
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

**Chunk size: Thread length one per chunk**
**Overlap: no in between thread**

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

**My relevance cutoff:**

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

**1.**
     For this work i have been used ai to keep track for me on my progress because there so many files that am not well familiarize with it and it very usefull to be my mentor and guide me through each question with doubtfull instead of giving me helping hand it only give hint and lets me do all the step by myself and drive me to the answer i feel like it was right. This give me room that i want to see more in other way. The way i ask for it to do many thing for me like generate path and guide but it only help on exploring instead so i have to stick with one path and drive up onto decision all by my self 

     moment 1 : when i stumble on expecting and i though it mean like what the ai going to answer back but those keyword never show up but just like expectation and i misunderstanding it my ai teacher clarify and walk me through which one with real evidence of what my llm output ask look like 

**2.**
     The real gem on this project that i can use ai to explore later after i have know the work flow what i would change next time is instead of lecturing me theres another ai serve as visualizer side by side that help me see what possibilities while drafting for answer instead.



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

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
