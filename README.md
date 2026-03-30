[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xdcIkjOc)
# Homework 1: Code with AI

## My Website

- Homepage: `https://johnsonw625.github.io/index.html`
- Pac-Man page: `https://johnsonw625.github.io/pacman.html`
- arXiv page: `https://johnsonw625.github.io/arxiv.html`

## BST236 Midterm: Tutorial and video (on this blog)

- Written tutorial (workflow design, agents/skills): https://minitim222.github.io/bst236-midterm-project/tutorial/
- Tutorial video: https://www.youtube.com/watch?v=Rdb_bQ0VkDM
- Same content is linked and embedded on the homepage: `https://johnsonw625.github.io/index.html#bst236-tutorial`

## Progress

- Problem 1 (GitHub blog homepage): Completed
- Problem 2 (Valentine Pac-Man): Completed
  - Maze with pellets, ghosts, and lives
  - Rose power-up that appears randomly
  - Heart projectiles while powered-up
- Problem 3 (arXiv auto-updating page): Completed

## AI Copilot Report

### Problem 1: GitHub Website for Coding Blog

**How I used Copilot CLI**
- I asked Copilot to scaffold a clean static homepage with reusable styles and navigation links for all three problems.
- I then iterated on the prompt to make the design more modern and expandable.

**Prompts I gave**
1. "Create a stylish but simple `index.html` and `styles.css` for a coding blog homepage, with links to Pac-Man and arXiv pages."
2. "Keep the page responsive and easy to expand for future assignments."
3. "Adjust the visual style to look modern but still lightweight for GitHub Pages."

**What worked well / required iteration**
- Worked well: generating a complete starter layout quickly.
- Iteration needed: polishing typography/colors and making navigation structure future-proof.

### Problem 2: Valentine-themed Pac-Man

**How I used Copilot CLI**
- I decomposed the game into mechanics first (maze, movement, ghosts, lives), then added Valentine's features (rose + hearts).
- I asked Copilot for a complete playable single-page implementation and then refined behavior.

**Prompts I gave**
1. "Build a full Pac-Man game in `pacman.html` with maze, pellets, ghost chasing logic, score, and lives."
2. "Add a rose power-up that appears randomly; when eaten, Pac-Man enters a temporary powered-up mode."
3. "During powered-up mode, continuously shoot heart projectiles in the facing direction; hearts should eliminate ghosts."

**What worked well / required iteration**
- Worked well: core gameplay loop and rendering in one file.
- Iteration needed: balancing timing/speeds and checking edge cases like collision/reset/game-over flow.

### Problem 3: Auto-updating arXiv Feed

**How I used Copilot CLI**
- I used Copilot to plan data flow first: fetch arXiv data -> store JSON -> render in webpage -> schedule automation.
- I then implemented each component separately and connected them.

**Prompts I gave**
1. "Create a Python script using only the standard library to fetch latest arXiv papers by keyword and export title/authors/abstract/pdf link to JSON."
2. "Build a static arXiv feed webpage that fetches local JSON and renders cards with loading, empty, and error states."
3. "Create a GitHub Actions workflow to run every midnight, update the JSON file, and commit only when data changed."

**What worked well / required iteration**
- Worked well: dependency-free Python script made CI reliable.
- Worked well: static JSON rendering fits GitHub Pages well.
- Iteration needed: add `workflow_dispatch` for manual testing and clarify that cron runs at midnight UTC.

The due date is Feb 17 at midnight. If you are using the late days, please note in the head of README.md that “I used XX late days this time, and I have XX days remaining”.

The main purpose of this homework is to help you:

- Get experience with AI coding
- Learn how to decompose a problem into smaller tasks and find the right tools to solve them with the help of AI
- Improve your prompt engineering skills
- Conduct the coding task you have never learned before with the help of AI
- Learn the agentic programming paradigm

**Remark**: We expect you to complete the homework with the help of AI. The tips we provide are just suggestions, and you can use other tools to complete the tasks. This homework might take longer than you expect if you have no experience with game/web development or GitHub Actions. Though this is exactly what we expect you to experience: to finish the coding tasks that you have never learned before, we suggest you **start early** in case you face unexpected issues. 

Enjoy your vibe coding!

Your homework repository should have all the source code for the problems below, though the real website could be based on the repository hosted under your own GitHub account.

In the `README.md` of your homework repository, you can write the report section as a case-study tutorial on how to use AI copilot for the following three problems. You can list the AI tools you used, and how you designed and adjusted your prompts. You can add screenshots or even share the video of how you used these AI tools and the intermediate products generated by AI if you believe it will help the readers learn.



## Problem 1. Github Website for Your Coding Blog

Create a homepage for a website for your **coding blog**. The website should be hosted on [GitHub Pages](https://pages.github.com/). You can design the homepage by yourself in any proper style you like. You may need to make the design expandable to add more content from our future assignments. The link to the homepage should be added to the `README.md` of your homework repository so that anyone can access the homepage and the following two webpages from the Internet using this link.


## Problem 2. Game Coding: Pac-Man (Valentine's Special 💘)

Add a new page to your website for a Valentine's-themed [Pac-Man](https://en.wikipedia.org/wiki/Pac-Man) game. The users can directly play the game on your webpage. The link to the game webpage should be added to the homepage in Problem 1. Your game should include the following core features:

1. **Classic Pac-Man Mechanics**: A maze with dots (pellets) for Pac-Man to eat, and ghosts that chase Pac-Man. The game ends when Pac-Man loses all lives. You can decide the maze layout by yourself (classic ok, but maybe even 3D).
2. **Valentine's Power-Up — Rose** 🌹: A rose randomly appears on the maze from time to time. When Pac-Man eats the rose, it enters a powered-up state for a limited duration (e.g., a few seconds), during which Pac-Man **continuously shoots hearts** in its current facing direction.
3. **Heart Projectiles** 💕: The hearts travel across the maze and eliminate any ghost they hit. Once the power-up expires, Pac-Man returns to normal until it picks up another rose.

As long as the game is recognizable as a Pac-Man game by common sense, with the features roughly following the above requirements, you will get full credit.

Beyond these requirements, you are free (but will not be graded) to add your own creative touches — such as Valentine's-themed visuals, sound effects, scoring bonuses, or additional power-ups.

## Problem 3. Data Scaffolding from the Internet

In this problem, you will build an auto-updating arXiv paper feed for your website. **You must use Copilot CLI as your primary coding tools** to scaffold, implement, and automate this task. The goal is to practice the agentic programming paradigm: break the task into agent-friendly steps, prompt the agent effectively, and wire everything together.

We suggest you to follow the steps we showed in the class: plan first with AI to decide the workflow and agents orchestration, then ask AI to implement the plan.

### Deliverables

Add a new page to your website that displays the latest arXiv papers. The page must include:

1. **Paper Listing**: The latest arXiv papers matching keywords of your choice. Design the layout as you see fit.
2. **Paper Details**: Each entry must show the paper title, authors, abstract, and a direct link to the PDF.
3. **Auto-Update**: The paper list must refresh automatically every midnight via a GitHub Actions workflow.
4. **Homepage Link**: A link to this page must appear on your homepage from Problem 1.
5. **Page Design**: Style the page in any way you think readers would appreciate.

Your homework repository **must include the `.github` directory** with all agent configurations and workflow files used for this problem.

In your report (`README.md`), describe how you used Copilot CLI to build each component. Include the prompts you gave the agent and note what worked well or required iteration.

### Tips

**Tip 1**: You can ask AI how to deploy the website by [GitHub Pages](https://pages.github.com/). 

**Tip 2**: You can ask AI to teach you how to use [arXiv API](https://arxiv.org/help/api/user-manual) to fetch the latest papers from arXiv.

**Tip 3**: You can ask AI to teach you how to use [GitHub Actions](https://docs.github.com/en/actions) to automate the process of updating the webpage. Or even leave the job to agents.

**Tip 4**: You can use [Copy Coder](https://copycoder.ai/) to help you design the webpage UI from the style you like.


