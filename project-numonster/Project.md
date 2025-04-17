# COMP1010 - Major Project

This is the template for your COMP1010 project. Over the course of the term,
you will need to plan, design, build, test and showcase a software project
using the tools taught by COMP1010.

## Project overview

Over the course of the term, you will submit various parts of your project as
assignments.

| Task           | Type         | Due     | Marks |
| -------------- | ------------ | ------- | ----: |
| Check-in 1     | Lab exercise | Week 3  | 3     |
| Registration   | Assignment   | Week 4  |       |
| Proposal       | Assignment   | Week 5  | 10    |
| Check-in 2     | Lab exercise | Week 7  | 1     |
| Check-in 3     | Lab exercise | Week 8  | 1     |
| Check-in 4     | Lab exercise | Week 9  | 1     |
| Implementation | Assignment   | Week 10 | 20    |
| Demonstration  | Assignment   | Week 10 | 0*    |
| Feedback       | Assignment   | Week 10 | 5     |

Note that check-in lab exercises are intended to help you plan your project,
and help us ensure you are on-track, but are not themselves part of the
major project.

Additionally, note that the demonstration is worth zero marks, as you are not
assessed on your ability to present your project. However, attending it is
still compulsory, and is required for you to complete the feedback task.
Failure to attend the demonstration may impact your implementation mark.

## Late Penalties

The late penalty is a per-day mark reduction equal to 5% of the max assessment
mark.

For example, if an assignment which would receive an on-time mark of 7/10 is
submitted 3 days (or 2 and a bit days) late it should receive a mark of 5.5/10.

This applies to the Proposal, Implementation and Feedback assessments.

## Data safety and backups

Over the term, you will spend a significant amount of time working on your
project. As such, it's essential that you take frequent backups of your work so
that you don't lose data if you make a mistake. In most cases, special
consideration will not be granted in cases of data loss if you didn't take
reasonable steps to make backups.

Here is some advice to ensure you don't accidentally lose data.

* Follow the [3-2-1 rule](https://www.veeam.com/blog/321-backup-rule.html) for
  backups.
    * Maintain three copies of your data. Your working copy, and two backups.
    * Store your backups on at least two different mediums. For example, one
      could be on your laptop, and another could be in the cloud.
    * Ensure at least one copy is off-site. For example, you could sync your
      data using a service such as Google Drive or iCloud. Note that UNSW
      offers lots of free storage on OneDrive for all students.
* Always make a backup before making a big change to your work. That way if
  anything goes wrong you can revert to your original copy.
* Check that your backups actually exist before relying on them. There's
  nothing worse than finding out that your backups aren't actually working at
  the moment when you need them the most.

If you'd like further advice on backups and data safety, feel free to ask on
the [EdStem forum](https://edstem.org/au/join/WjMAmq).

## Choosing a project

You'll be working on your project for the majority of the term, so it's crucial
that you pick something that:

* Matches your interests. For example, if you enjoy painting, perhaps you could
  make a tool to suggest colour palettes inspired by user's images.
* Has room to grow/shrink, so that you can adapt the idea over the term and
  still end up with a viable product by the end of term even if you
  over/under-estimated how complex it was.
* Has a "unique twist" that makes it yours. We don't want you to reinvent the
  wheel, and your project will be much more fun if there are aspects that set
  it apart from "the competition".
* Will work as a server-rendered web app. For example, real-time games or
  terminal applications are not appropriate.
* Accepts and responds to user inputs. For example, an "about page"-style site
  is not appropriate, but sites where users can generate data, or explore a
  large data-set are.

You should explore some project ideas in your week 3 "check-in" lab. Make sure
you get your tutor's feedback on your ideas.

### Example projects

Here are some ideas for projects. Feel free to use these as inspiration or a
starting point for your own project.

* ***A UNSW club event planner***, which allows club executives to plan events
  which club members can add to their calendars. Users can follow societies to
  automatically add their events as they are released.

* ***A course website content management system***, which allows tutors to
  create and edit pages for tutorials, labs and assignments, which can be
  scheduled for release upon unsuspecting students on specified dates during
  the term.

* ***A Wikipedia guesser game***, where players compete to identify popular
  Wikipedia articles given their opening paragraph.

* ***A UNSW electives review app***, where students can leave and view reviews
  for various UNSW courses to help each other decide which electives to take.

* ***A share-house chore manager***, allowing you and your housemates to
  distribute chores with the aim of avoiding a slow descent into chaos. An app
  like this could ideally track who did which tasks to ensure that everything
  remains fair.

## Technical requirements

In COMP1010, we teach specific tools, and we expect you to use them to complete
your project. While we encourage you to make use of your existing skills and
learn beyond the scope of the course content, the majority of your project's
work should be done using the course's "tech stack".

* Your project must use a Flask web-server, and produce its entire user
  interface within HTML webpages served to visiting web browsers.
* Your project must generate HTML using PyHTML. You must not use Flask's
  templating system (`render_template`, and similar functions).
* Your project should use plain CSS, without external libraries such as
  Bootstrap. Your CSS can be written using static CSS files, or generated using
  PyHTML. Using external libraries for icon sets such as LineAwesome is
  permitted.
* While you can use JavaScript for interactivity in the user's web browser,
  this should not be the majority of your project's work. Make sure features
  that require JavaScript are "stretch goals" which aren't central to your app.
  Using JavaScript is not required to achieve full marks in the project.

## Code generation and attribution

***The majority of your project must be your own work***. However, as software
engineers, it is common to include code written by others as a part of your
work. When you do this, you ***must*** correctly attribute it by making its
origin clear. For code generated by a large language model, you should ensure
that this is clear. Failing to provide correct attribution for work that isn't
your own is copyright infringement and plagiarism, and has serious academic
penalties.

Here is an example of a correctly-attributed snippet of code taken from a
programming help website.

```py
def random_towards_zero(max: int, squash_factor: int) -> int:
    """
    Random sample with distribution towards zero, adapted from
    https://stackoverflow.com/a/41852266/6335363
    CC BY-SA 4.0
    """
    return random.choices(
        range(1, max),
        weights=[i**squash_factor for i in range(max - 1, 0, -1)],
    )[0]
```

In this snippet, it is clear that the code is inspired by the linked answer on
StackOverflow with some modifications to suit my own needs. The `CC BY-SA 4.0`
means that the original code uses the
[Creative Commons attribution-sharealike license](https://creativecommons.org/licenses/by-sa/4.0/),
meaning that I am free to use and adapt the work, as long as I provide
attribution and make my modifications similarly available.

Here is an example of a correctly-attributed snippet of code generated by
ChatGPT.

```py
def generate_random_bell_curve(midpoint: float, variance: float) -> float:
    """
    Generates a random number distributed about a bell curve.

    Generated using ChatGPT. Prompt:
    > Write a Python function that generates a random number distributed about
    > a bell curve, given a midpoint and a "variance" value. It must only use
    > the standard library.
    """
    standard_deviation = variance**0.5
    return random.gauss(midpoint, standard_deviation)
```

In this snippet, it is clear that the code was generated by a large language
model. The prompt is included in the documentation, which makes it clear how
the function was generated.

Importantly, borrowed code should comprise at most a ***clear minority*** of
the code in your project. Anything which we teach you in lectures, tutorials
and labs should be written by yourself, as you are expected to demonstrate
these skills during the final exam (where resources such as AI will not be
available).

## Collaboration and assistance

While you are encouraged to help, and get feedback from, other students in the
course, the code you submit must be your own work (and possibly the work of
your partner). Submission of code partially or completely derived from any
other person or jointly written with any other person is not permitted. The
penalties for such an offence may include negative marks, automatic failure of
the course and possibly other academic discipline. Assignment submissions will
be examined both automatically and manually for such submissions. Relevant
scholarship authorities will be informed if students holding scholarships are
involved in an incident of plagiarism or other misconduct.

Do not provide or show your code to any other person, except for the teaching
staff of COMP1010. If you knowingly provide or show your code to another person
for any reason, and code derived from it is submitted, you may be penalised,
even if the work was submitted without your knowledge or consent. This may
apply even if your work is submitted by a third party unknown to you.

Note, you will not be penalised if your work was taken without your consent or
knowledge.

Please refer to [UNSW's Plagiarism and academic integrity policy](https://www.student.unsw.edu.au/plagiarism/integrity)
for more information.

During lab time, your tutor will be happy to assist you with your project. Feel
free to ask questions, request debugging help, or bounce ideas off course
staff.

## An overview of the starter code

This is your first big project, so there's a lot to wrap your head around. If
you're confused by anything, you can always post on the [EdStem forum](https://edstem.org/au/join/WjMAmq) or ask your
tutor. For now, here is an overview of your code.

* `proposal`: the proposal folder is where you can put any files associated
  with the proposal assignment. In it, you can find `Proposal.md`, which you
  should fill out and submit for your project proposal.
* `README.md` is similar to the "readme" files in your lab work, but with a
  small twist: you get to write it yourself. As you complete your project, you
  should fill out this file with information about your work. We've added a
  template there that should help you out.
* `src`: the "source directory" is the folder where your program's code lives.
  We've added a file `server.py` with a simple web server here, but you can add
  more files here if you want to. We cover multi-file projects in the week 8
  tutorial.
* `feedback`: the feedback folder is where you can put any files associated
  with the feedback assignment. In it, you can find two files:
  `Feedback1.md` and `Feedback2.md`. You will need to fill out these files to
  complete the feedback assignment.

## Stages

### 0. Registration

Before you begin the project, there are a couple of quick tasks you need to
complete.

* Enter your demonstration time preferences using the form linked on the
  project page of [WebCMS](https://webcms3.cse.unsw.edu.au/COMP1010/25T1/).
* If you intend to work in a pair, make sure to let your tutor know, so they
  can set this up on the marking spreadsheet.

You must complete these tasks before the end of week 4 so that we can best
accommodate you.

### 1. Proposal

For your project proposal, you must decide on your project, document your
project's goals, and make a start on the code for your implementation.

* You must fill out the proposal template in `proposal/Proposal.md`.
* You should create UI designs for your project, and add these into the
  `proposal` folder. To reduce submission sizes, please upload these as JPG
  images.
* Any additional drawings, designs or notes should also be placed inside the
  `proposal` folder.
* While there is no specific word count, you should make sure that you cover
  all sections in sufficient depth. Marks may not be awarded for sections that
  aren't detailed enough. If you're unsure, post on the [EdStem forum](https://edstem.org/au/join/WjMAmq) or ask your
  tutor for advice.
* You shouldn't assume any technical knowledge beyond the content taught in the
  course. Your proposal should be understandable to your fellow students.
* You should start working on the code for your app in the `src` folder. We
  don't expect your app to be close to complete at this stage, but you should
  make a start on some meaningful aspect of it. For example, if you were making
  a UNSW club event planner, you could make it display information for some
  example events, and show a form for scheduling new events. There is no
  expectation that your app will handle user inputs beyond basic navigation at
  this point. We just want to see that you've made a start.
* At this point, you shouldn't need to change any information in your project's
  `README.md` file, but you could start filling out some of the basic sections
  if you want to.

To submit your project proposal, you should zip up your entire project folder
and upload it on [WebCMS](https://webcms3.cse.unsw.edu.au/COMP1010/25T1/). If your submission is too large to upload to
WebCMS, we also permit you to submit it by emailing it to the course email
account at `cs1010@cse.unsw.edu.au`. If possible, try to submit it on WebCMS,
as this will allow us to mark your work more efficiently.

#### Proposal marking criteria

| Criteria | Mark |
| -------------------------------------------------------- | ---- |
| Clearly defined problem to be solved                                     |     1 |
| Background includes information necessary for building a prototype       |     2 |
| Appropriate set of target users                                          |     1 |
| MVP is both minimal and viable                                           |     1 |
| The user interface design clearly conveys what will be visible upon completion of the MVP implementation | 1 |
| Code in first stage of project produces an appropriate result            |     2 |
| Comprehensive list of "nice to have" features                            |     1 |
| Appropriate ambitious stretch goals                                      |     1 |

### 2. Implementation

For your project implementation, you should attempt to complete your project
according to the goals you set during the proposal. It's completely reasonable
for your goals to change or adapt over the course of your project, but this
should be documented in your project's `README.md` file.

* Before you submit your project, you should ensure that it is documented
  according to the template in `README.md`. In particular, you should document
  all additional libraries or APIs that your app requires in order to run. This
  is essential so that your tutor can properly understand and assess your work.
* Note that your `README.md` is not assessed directly, but is instead used as a
  "tour guide" for your marker to discover and test the features you have
  built. As such, while there are no length requirements, you should make sure
  to document all of your features so that your marker does not miss anything.
* Your project's source code should remain in the `src` folder.
* To reduce submission sizes, try to minimise the size of additional assets
  that your project requires, for example, by storing images in JPG format, and
  by streaming media such as audio and videos from other websites (eg by
  embedding a YouTube video).

To submit your project implementation, you should zip up your entire project
folder and upload it on [WebCMS](https://webcms3.cse.unsw.edu.au/COMP1010/25T1/). If your submission is too large to upload
to WebCMS, we also permit you to submit it by emailing it to the course email
account at `cs1010@cse.unsw.edu.au`. If possible, try to submit it on WebCMS,
as this will allow us to mark your work more efficiently.

#### Implementation marking criteria

The table below is only a *guideline*. Owing to the open-endedness of this
project, how marks are awarded may vary slightly from what is below. In
particular, full marks are unlikely to be awarded for unambitious projects.

Examples of how these variations may apply:

* Marks awarded for stability are capped at the mark awarded for functionality.
  This way, students who get a simple project working with 100% stability, but
  then in attempting more complex features, don't get penalised if their more
  complex features aren't completely stable.
* The above also applies for interactivity.

**Functionality** (10 marks)

* Lacks any real functionality (0-2 marks)
* Offers some functionality, but not enough to be useful to any user (2-4 marks)
* Working MVP (4-6 marks)
* Contains some "nice-to-have" features (6-8 marks)
* An ambitious "stretch goal" has been met (8-10 marks)

Partial marks will be awarded for features with significant bugs or stability
issues. Higher marks may be awarded for projects where especially advanced
features are implemented, even if they are not entirely stable.

**Programming** (5 marks)

* Code is not in Python or application consists entirely of static HTML pages
  (0-1 marks)
* Code almost entirely consists of snippets copied from elsewhere (1-2 marks)
* Code does not use appropriate control or data structures (e.g. using lists
  when a dictionary would be more appropriate) (3-4 marks)
* Appropriate use of Python control structures, data structures, functions,
  modules, and libraries. Appropriate abstractions for data (eg using data
  files over hard-coded values). (5 marks)

**Interactivity** (5 marks)

* Interface is indecipherable and/or many usability heuristics have been
  violated (0-1 marks)
* Interface is usable, but not without looking at the code and/or some other
  resource to figure out how (2-3 marks)
* Interface is usable, but some usability heuristics have been violated (4
  marks)
* Interface does not violate any usability heuristics, makes appropriate use of
  CSS to improve application aesthetics, and is generally easy to use (5 marks)

#### Additional notes

* If you submit an application which does not meet the technical requirements
  listed above, your mark may be capped at 50%.
* Up to 2 marks may be deducted off of your total marks for not following good
  code style.

### 3. Demonstration

Your project demonstration is your opportunity to showcase your hard work to
the course staff and your peers. You should plan a 3-5 minute demonstration
where you explain what your app is, walk through its features and show how it
works. After this demonstration, we will do a short Q&A where students and
tutors will have the opportunity to ask you about certain aspects of your
project. For example, you may be asked to explain an interesting design choice,
or an algorithm that you used.

Importantly, ***you are not marked on your demonstration skills***. Instead,
you should consider the demonstration as a way to celebrate your hard work, and
help the course staff understand your project such that they consider all of
your best features when marking your implementation. This is helpful to course
staff if we are unable to get your app fully working ourselves, as we will use
a recording of the demonstration to see your app in-action if we can't run it
on our own systems. The project demonstration should not be a stressful task.
If you are nervous about it, please chat to your tutor, who will be happy to
address any concerns you may have.

Additionally, during your project demonstration's time-slot, you will need to
complete the feedback task for your peers' projects. As such, you are expected
to be present for the full hour of your time-slot.

Failure to attend or demonstrate your project may result in a penalty being
applied to your implementation mark. If you are working in a pair, both members
need to attend and participate in the demonstration.

### 4. Feedback

During the demonstrations, you will be allocated 2 projects to give feedback
about. *This part of the project is to be completed individually*. You should
write feedback in the given `Feedback1.md` and `Feedback2.md` files, which can
be found in the `feedback` folder.

Your feedback should:

* Include your name and zID.
* Include the name of the student or group you are giving feedback on.
* Be specific to the app you are providing feedback on.
    * For example, instead of saying "the UI is bad", you could say "the top
      menu bar is cluttered, which makes it difficult to understand how to
      navigate the website".
* Cover both the app's functionality and its user interface design.
* Include both:
    * Positive feedback: things which were implemented well in the
      demonstrated project.
    * Constructive feedback: things which could be improved in the demonstrated
      project, including how to improve it.
* Detail the impact of the aspect/feature and (where applicable) the impact of
  the suggested improvement.

Your feedback may contain diagrams or drawing to supplement your written
feedback, however these are not required to achieve full marks. If you include
diagrams, please ensure they are placed in the `feedback` folder, and are in
JPG format.

Upon completion of the course, students may request to see their feedback. Any
feedback passed on to students will be anonymised (will not include the details
of the student giving the feedback).

To submit your feedback, you should zip up the `feedback` folder and upload it
to [WebCMS](https://webcms3.cse.unsw.edu.au/COMP1010/25T1/). If you encounter any issues while submitting, you can
alternately email your submission to `cs1010@cse.unsw.edu.au`.
