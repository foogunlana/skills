---
name: backlog-grooming
description: Break down an epic into well-refined subtasks. Use when the user wants to groom a backlog, create subtasks from an epic, break down an epic into tickets, or refine tasks from user stories. Triggers on "groom", "backlog grooming", "break down epic", "create subtasks from epic", or any request to turn an epic's user stories into individual tickets.
---

# Backlog Grooming

Turn an epic into well-refined subtasks through a structured, conversational process.

## Configuration

This skill works with any issue tracker. Configure for your project:

| Setting | Default | Options |
|---------|---------|---------|
| **Issue tracker** | GitHub Issues | GitHub Issues, GitLab Issues, Jira, Linear, ClickUp |

Use your tracker's API or CLI to fetch, create, and update tasks.

## Workflow

### Step 1: Get the Epic

Ask the user for the epic URL or task ID. Fetch it using your issue tracker's API. Extract:
- Task ID, project/list, tags, status
- The user stories or work items listed in the description

Present the extracted user stories to the user for confirmation before proceeding.

### Step 2: Create Subtasks in Bulk

Create all subtasks at once using the **create-ticket** skill workflow for each one:
- Set `parent` to the epic's task ID
- Use the same project/list as the epic
- Fill in what you can from the epic context; leave template sections as `...` when unknown
- Skip the preview/confirmation step per ticket — bulk creation happens first, refinement follows

### Step 3: Refine One by One

Walk through each subtask in order with the user:
1. Show the current content (title, description, acceptance criteria)
2. Ask what to change
3. Apply updates via the issue tracker API
4. Ask about status, priority, team, tags, dependencies
5. Move to the next task when the user is satisfied

Add dependencies between tasks as they are identified during refinement.

### Step 4: Summary

After all tasks are refined, show a summary table:

| # | Task | Status | Dependencies |
|---|------|--------|-------------|
