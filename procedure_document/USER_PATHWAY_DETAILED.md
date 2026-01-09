# Part III: User Pathway
## Complete Step-by-Step Procedures for Regional PMs, SMEs, and Team Members

**Purpose:** Operational procedures for executing day-to-day NPI project work in Microsoft Planner Premium

**Audience:** Regional PMs, Subject Matter Experts (SMEs), Coordinators, and team members who work on NPI projects

---

## III.A: Getting Started with Planner Premium

### III.A.1: Access & Setup

#### Who Gets Access?
- **Regional PMs** - Full access (create cards, assign tasks, move between phases)
- **Main PMs** - Full access (governance oversight)
- **Functional SMEs** - Limited access (work on assigned sub-tasks, view project cards)
- **Regional Service Leaders** - View-only access (portfolio oversight)

#### Getting Planner Premium Access

**Step 1: Submit Access Request**
1. Email your Regional Service Leader or Main PM
2. Provide: Your full name, email, role, project name
3. Expected timeline: 2-3 business days

**Step 2: Accept Invitation**
1. Check your email for "You've been invited to Microsoft Planner Premium"
2. Click the link and log in with your company account
3. Bookmark the site: **planner.cloud.microsoft.com**

**Step 3: Verify Access**
1. Open planner.cloud.microsoft.com
2. You should see your project board(s) listed
3. If not, check that you're logged into the correct company account

**Troubleshooting:** If you still can't access after 3 days, contact IT Help Desk with your account email and project name.

#### Licensing Requirements
- Planner Premium requires a Microsoft 365 subscription with the Planner Premium add-on
- Your organization pays for this at the user level
- You don't need to do anything — IT handles the licensing

---

#### Browser & Technical Requirements

**Recommended Setup:**
- **Browser:** Microsoft Edge (latest version) — most compatible with Planner Premium
- **Alternatives:** Google Chrome, Safari, Firefox (all work but Edge is optimized)
- **Minimum Requirements:** HTML5 support, JavaScript enabled, cookies enabled

**System Requirements:**
- Internet connection (broadband recommended for timeline views)
- Screen resolution: 1024 x 768 minimum (1920 x 1080 recommended for comfortable viewing)
- No special plugins or software needed

**To Check Your Browser Version:**
- In Edge: Click **Settings** → **About Microsoft Edge** → Auto-updates to latest
- Restart browser after updates

**Technical Issues?** Contact IT Help Desk. Common fixes:
- Clear browser cache and cookies
- Try a different browser
- Disable browser extensions temporarily
- Restart your computer

---

#### First Login: Step-by-Step

**Step 1: Navigate to Planner**
1. Open your browser
2. Go to **planner.cloud.microsoft.com**
3. Log in with your company email/password

**Step 2: Explore Your Dashboard**
- You'll see a list of projects you have access to
- Each project appears as a card with project name and thumbnail
- Recent projects appear at the top

**Step 3: Open Your First Project Board**
1. Click on a project card (ex: "PLC - RR - Calima - 01 Singapore")
2. The board view opens with all tasks for that project
3. You'll see cards organized by phase (Pipeline, GA, RA, Engage, Kick-off, Execute, Hypercare, Close-out)

**Step 4: Personalize Your Settings**
1. Click your profile picture (top right)
2. Select **Settings**
3. **Language:** Choose your preferred language
4. **Notifications:** 
   - Keep "Email notifications" ON to stay informed
   - You'll get emails when someone assigns a task to you or mentions you
5. **Theme:** Choose Light or Dark mode (personal preference)
6. Click **Save**

**Step 5: Set Up Teams Integration**
1. Open your project's Teams channel
2. Look for a **Planner** tab at the top
3. If it doesn't exist, click **+** → search for "Planner" → add to channel
4. Now you can access Planner directly from Teams

---

#### Teams Integration: Connected but Separate

**How Planner & Teams Work Together:**
- **Planner is source of truth:** All project data lives here
- **Teams is communication hub:** Use Teams channel for discussions
- **They sync:** Changes in Planner trigger Teams notifications

**To Find Your Planner Board in Teams:**
1. Open your project Teams channel
2. Click the **Planner** tab
3. See the same board as planner.cloud.microsoft.com
4. Can work directly from Teams or jump to full Planner view

**Notifications:**
- When someone creates a card assigned to you → Teams notification
- When someone mentions you in a comment → Teams notification
- When a card you're watching moves to new bucket → (if you enabled it)

---

### III.A.2: Board Navigation Basics

#### Understanding Board Views

**Every Planner board has 4 main views.** You choose which to use based on your current task.

---

##### View 1: GRID VIEW (Default)

**What it looks like:** Table format, all cards visible at once

**How to read it:**
- **Rows** = Individual cards (one row per card)
- **Columns** = Card properties (Title, Assigned to, Due date, Status, Priority, etc.)
- **Color coding** = Visual indicators (Green = on track, Red = at risk, Gray = not started)

**When to use Grid View:**
- ✓ Searching for a specific card
- ✓ Reviewing all cards at once (overview)
- ✓ Sorting or filtering by date, person, priority
- ✓ Updating card details quickly
- ✗ NOT best for understanding dependencies
- ✗ NOT best for timeline visualization

**How to access Grid View:**
1. Open your board
2. Look for view selector at top left (Grid icon)
3. Click **Grid** (default view)

**Key actions in Grid View:**
- **Click any cell** to edit (ex: click Due Date to change it)
- **Click card name** to open full card detail
- **Sort/Filter:** Use dropdown menus above columns
- **Change columns:** Right-click column header → select which to display

---

##### View 2: BOARD VIEW (Kanban)

**What it looks like:** Swimlanes (vertical columns), each column is a Bucket (Pipeline, GA, RA, etc.)

**How to read it:**
- **Columns** = Buckets (phases of project)
- **Cards within column** = Cards in that phase
- **Card position left-to-right** = Your choice to organize
- **Card color** = Priority (Red = urgent, Yellow = important, Gray = normal)

**When to use Board View:**
- ✓ Moving cards between phases (drag & drop)
- ✓ Understanding which phase cards are in
- ✓ Visual status at a glance
- ✓ Organiz cards within a phase
- ✗ NOT good for detailed timelines

**How to access Board View:**
1. Open your board
2. Look for view selector at top left
3. Click **Board**

**Key actions in Board View:**
- **Drag a card** from one bucket to another = Move to next phase (see Section III.C.4)
- **Click a card** = Open detail view (edit fields, add comments)
- **Right-click a card** = Quick options (move, duplicate, delete)
- **Rearrange cards within bucket** = Drag up/down to prioritize

**Quick Tip:** Use Board View at the start of your week to see overall progress, then switch to Grid View for detailed work.

---

##### View 3: TIMELINE VIEW (Gantt Chart)

**What it looks like:** Gantt chart, horizontal timeline with bars representing card durations

**How to read it:**
- **Horizontal axis** = Calendar/timeline
- **Vertical axis** = Cards (rows)
- **Bar length** = Duration from start date to due date
- **Connecting lines** = Dependencies (when one card depends on another)

**Timeline Features:**
- **Blue bars** = Cards on schedule
- **Orange bars** = Cards at risk (approaching deadline, no progress)
- **Red lines** = Dependency broken (predecessor late, dependent card now at risk)
- **Green lines** = Dependency healthy (predecessor on track)

**When to use Timeline View:**
- ✓ Planning project schedule
- ✓ Seeing dependencies visually
- ✓ Identifying critical path (what's blocking what?)
- ✓ Finding bottlenecks (cards all ending same day)
- ✓ Presenting to leadership (clear visual schedule)
- ✗ NOT good for daily task updates

**How to access Timeline View:**
1. Open your board
2. Click view selector (top left)
3. Click **Timeline**
4. Dates appear automatically from your card start/due dates

**Key actions in Timeline View:**
- **Drag bar left/right** = Change start date or due date
- **Hover over bar** = See card details
- **Click bar** = Open card detail
- **Follow a red line** = Trace the dependency

---

##### View 4: MY TASKS VIEW (Personal List)

**What it looks like:** Personalized task list, only your assignments

**How to read it:**
- **Shows only cards assigned to you**
- **Organized by project** (first by due date, then alphabetical)
- **Status indicator** = Current phase of each card
- **Due date** = When it's due

**When to use My Tasks View:**
- ✓ Morning planning (what do I work on today?)
- ✓ Checking your workload across multiple projects
- ✓ Prioritizing your week
- ✗ NOT for viewing team progress
- ✗ NOT for project overview

**How to access My Tasks View:**
1. Click **My Tasks** (usually in left sidebar or top menu)
2. You'll see all cards assigned to you across all projects
3. Filter by project, due date, or status

**Example Daily Routine with My Tasks:**
1. Open My Tasks view
2. Scan for cards due this week
3. Find the 2-3 highest priority
4. Click each to see what needs doing
5. Update status as you complete work
6. Add comments if progress to share

---

#### Sorting & Filtering Options

**When you have lots of cards, use filters to find what matters.**

**How to Sort (Order cards by...)**
- By **Due Date** (soonest first)
- By **Priority** (urgent first)
- By **Assigned To** (group by person)
- By **Status** (custom field values)

**How to Filter (Show only...)**
- Cards assigned to **me**
- Cards **due this week**
- Cards with **high priority**
- Cards by **custom field value** (ex: "Complexity = Large")
- Multiple filters together (ex: assigned to me AND due this week)

**Example Filters You'll Use Often:**
- Filter 1: "Assigned to me" + "Due next 14 days" = Your urgent work
- Filter 2: "Bucket = Execute" + "Risk Status = Red" = At-risk cards needing attention
- Filter 3: "Goal = NPI" + "Complexity = XL" = Your biggest projects

**Saving Custom Views:**
1. Set up your filters
2. Click **Save view** 
3. Give it a name (ex: "My Week Ahead")
4. Next time, click that saved view name to load it instantly

---

#### Your Planner Premium Workspace: Board Structure

**You'll work with multiple boards. Here's what they are:**

##### Board Type 1: PLC-Specific Boards (Main Boards)

**Name format:** "PLC - RR - [ProjectName] - [Region]"  
**Example:** "PLC - RR - Calima - 01 Singapore"

**Content:**
- **Upstream card** (1 per project) = Project-level summary
- **Regional cards** (multiple) = One per participating region
- **Sub-tasks** = Under each regional card (team deliverables)

**Who accesses:**
- Regional PMs (full access)
- Main PM (full access)
- Regional SMEs (can view and update assigned sub-tasks)

**Structure inside board:**
- **Buckets:** Pipeline → GA → RA → Engage → Kick-off → Execute → Hypercare → Close-out
- **Each bucket** contains cards in that phase

**Your role:**
- If you're Regional PM: You own/manage the regional card
- If you're SME: You work on assigned sub-tasks
- If you're Main PM: You oversee the whole board

---

##### Board Type 2: Pipeline Board (Organization-Wide)

**Name:** "PLC - RR - Pipeline" (or similar, organization-wide)

**Content:**
- All Upstream cards that haven't yet entered GA
- Cards in very early concept phase

**Who accesses:**
- Portfolio leads (view progress)
- Main PMs (move cards in/out)
- Your regional PM may check here for new projects

**Your role:**
- Usually view-only
- Unless you're a PM/Portfolio lead

---

##### Board Type 3: OU-Specific Boards (Optional)

**Name format:** "[OU Name] - Deliverables" or "[OU Name] - Training"

**Content:**
- OU-specific work (training coordination, ops readiness, etc.)
- May have regional sub-tasks

**Who accesses:**
- OU PM/coordinator
- Functional leads
- Regional team members (for their region's work)

**Your role:**
- Depends on your function
- Training SME? Access the training board
- Ops manager? Access the ops board

---

#### Finding & Accessing Your Board

**Method 1: Direct Search**
1. Go to planner.cloud.microsoft.com
2. Type board name in search box (ex: "Calima")
3. Click the board when it appears

**Method 2: Recent Boards**
1. Boards you used recently appear at top
2. Click to open instantly

**Method 3: Teams Channel**
1. Open your project Teams channel
2. Click **Planner** tab
3. Same board appears in Teams context

**Method 4: Bookmarks**
1. Once you find a board, bookmark it in your browser
2. Create a folder: "NPI Projects"
3. Bookmark your main boards there
4. Quick access from your browser favorites

**Pro Tip:** Star your 3-5 main boards so they appear first when you log in.

---

### III.A.3: Technical Tips & Troubleshooting

#### Common Issues & Quick Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| "Can't see a board" | Access not granted | Email your PM or Regional Service Leader requesting access |
| "Card won't save" | Unsaved changes, internet issue | Refresh page (Ctrl+R), check internet connection |
| "Notifications not working" | Settings turned off | Settings → Notifications → Enable email notifications |
| "Timeline view not showing dates" | Start/due dates not filled | Add dates to cards (see III.C.3) |
| "Can't move card between buckets" | No permission, or card has errors | Check that all required fields are filled; verify you have edit access |

#### Best Practices for Reliability

1. **Keep 2-3 browser tabs open** (backup in case one freezes)
2. **Refresh every 2 hours** (keeps data synced, especially if others editing)
3. **Save before closing browser** (finish edits, add comment, hit save)
4. **Use Edge browser** (most compatible, fewest issues)
5. **Check internet connection** (if things seem broken, you're likely offline)

---

## III.B: Understanding the NPI Card Structure

### Context: Why Three Levels of Cards?

Planner Premium uses three levels of cards to mirror the NPI project structure:

1. **Upstream card** (project level) = What's the overall project?
2. **Regional cards** (regional level) = What's our region delivering?
3. **Sub-tasks** (functional level) = What's each team member doing?

This structure helps:
- **Main PM** see the complete picture (Upstream card)
- **Regional PM** see their region's work (Regional card + sub-tasks)
- **SME** focus on their deliverable (sub-task assigned to them)

---

### III.B.1: Upstream Card (Project-Level Summary)

#### What It Is
The **Upstream card** represents the entire NPI project at a global level.

- **One per project** (not one per region — one for the whole project)
- **Created by:** Main PM (during Pipeline phase)
- **Location:** Lives in the PLC-specific board (ex: "PLC - RR - Calima - 01 Singapore")
- **Moves through buckets:** Pipeline → GA → RA → Engage → Kick-off → Execute → Hypercare → Close-out
- **Shows overall progress:** As regional cards complete, upstream card progress updates

#### Card Details: What You'll See

**Title:**
- Format: "NPI - [PLC Name] - [Project Code]"
- Example: "NPI - Calima - CAL-001"
- **Your job:** Read it, don't change it

**Description:**
- Executive summary of the project
- What's the product? What service model?
- Who are the regions involved?
- **Your job:** Read for context

**Assigned to:**
- Usually the Main PM
- **Your job:** Escalate to this person if project-level issues

**Start Date & Due Date:**
- Start = Concept date or GA start date
- Due date = Global launch date
- **Your job:** Reference for timelines, don't change it

**Custom Fields (10 fields):**
- **Planisware ID:** Unique identifier for financial tracking
- **Global Service Model:** What service will we deliver? (Customer Pays, Included, etc.)
- **Complexity Rating:** Small, Medium, Large, or Extra-Large
- **Regions Involved:** Which regions are doing this? (Singapore, India, Australia, etc.)
- **Launch Date (Global):** When's the global launch?
- **Playbook Status:** Which sections are complete?
- **Risk Status:** Green (on track), Yellow (minor risk), Red (major risk), or Blocked
- **Stakeholder Contact:** Who's the key contact at corporate?
- *Plus 2 more fields specific to your organization*

**Progress Bar:**
- Shows % complete (increases as regional cards are completed)
- **Example:** 25% means 1 of 4 regions done with their deliverables

#### How to Read an Upstream Card

**Step 1: Open the card**
- Click the card title
- Detail view opens on right side (or full page)

**Step 2: Scan the key fields**
- What's the Global Service Model? (tells you what regions must deliver)
- When's the Global Launch Date? (critical timeline)
- What's the Complexity? (indicates scope)
- Which regions are involved? (how many you're coordinating)

**Step 3: Check Progress**
- Progress bar = % of regions complete
- If it's low (10-20%), project is early
- If it's high (80-90%), project is near launch

**Step 4: Look at Risk Status**
- Green = All regions on track
- Yellow = One region at risk, but manageable
- Red = Major issue, likely to miss launch
- Blocked = Can't proceed until something changes

**Step 5: Review Dependencies (if visible)**
- Are there other projects this depends on?
- Click dependencies to see related projects

#### When You'll Interact With Upstream Cards

| Situation | What You Do |
|-----------|-----------|
| Assigned as Regional PM | Reference for global context; update regional card sub-tasks |
| Assigned as SME | Read for context about product; focus on your sub-task |
| Assigned as Main PM | Own and manage the entire upstream card; move between phases |
| Reviewing project status | Check progress bar and risk status |
| Presentation to leadership | Use upstream card to show overall timeline |

---

### III.B.2: Regional Card (Operating Unit-Specific)

#### What It Is
The **Regional card** represents your specific region's work on the NPI project.

- **One per region, per project** (ex: Singapore has one, India has one)
- **Created by:** Regional PM (during Regional Alignment phase)
- **Depends on:** Upstream card (can't exist until GA is complete)
- **Location:** Same board as Upstream card
- **Shows regional progress:** As sub-tasks are completed, regional card progress increases

#### Card Details: What You'll See

**Title:**
- Format: "[PLC Name] - [Region] - Regional Readiness"
- Example: "Calima - Singapore - Regional Readiness"
- **Your job:** Read it, don't change it

**Description:**
- Regional service model (what service will Singapore deliver?)
- Regional scope (how many teams, locations, complexities?)
- Any regional constraints or considerations
- **Your job:** Read for context

**Assigned to:**
- Regional PM for that region
- **Your job:** Report to this person

**Start Date & Due Date:**
- Start = When RA phase begins for this region
- Due date = Regional launch date (may differ from global)
- Example: Global launch 6/15, but Singapore launches 6/8 (early adopter)
- **Your job:** Reference for your regional timeline

**Custom Fields (same 10 as Upstream):**
- **Planisware ID:** Regional Planisware line identifier
- **Regional Service Model:** What will this region deliver? (matches or customizes global model)
- **Complexity Rating:** Small, Medium, Large, or Extra-Large for this region
- **Playbook Status:** Which sections completed?
  - Section 1 (GA deliverables) = complete
  - Section 2 (Regional forecasts) = in progress
  - Section 3 (Service deliverables) = not started
  - Section 4 (Training/readiness) = not started
- **Launch Date (Regional):** Region's specific launch date
- **Risk Status:** Green/Yellow/Red/Blocked (at this region's level)
- **Stakeholder Contact:** Regional Service Leader or OU contact
- *Plus 2 more*

**Progress Bar:**
- Shows % of sub-tasks completed
- Increases as SMEs complete deliverables

**Sub-tasks Section:**
- Lists all functional deliverables (Training, Service SOPs, Ops procedures, etc.)
- Shows who's assigned
- Shows due dates
- Shows status (not started, in progress, completed)

#### How to Read a Regional Card

**Step 1: Open the card**
- Click the regional card name
- Full card detail opens

**Step 2: Understand the Regional Scope**
- Read the description
- What's the regional service model?
- Any unique regional challenges?

**Step 3: Check the Timeline**
- Due date = When this region must be ready
- Compare to global launch (may be same or different)

**Step 4: Review Assigned Sub-tasks**
- Scroll to sub-tasks section
- See what needs doing
- Who's responsible for each?
- What's due when?

**Step 5: Check Progress**
- Progress bar shows % complete
- If at 70%, three-quarters of deliverables are done

**Step 6: Understand Dependencies**
- This regional card depends on: Upstream card (global alignment must be done first)
- Other regional cards may depend on this one (if sequencing regions)

#### Common Sub-tasks Under Regional Cards

| Deliverable | Owner | Due Before |
|-------------|-------|-----------|
| Create Training Materials - Service Techs | Training SME | Kick-off |
| Develop Regional SOP - Service Procedures | Service Manager | Kick-off |
| Inventory & Spare Parts Readiness | Ops Manager | 6 weeks before launch |
| Launch Communications - Internal | Marketing | 2 weeks before launch |
| Regional Readiness Confirmation (sign-off) | Regional Service Leader | 1 week before launch |

#### When You'll Interact With Regional Cards

| Role | What You Do |
|------|-----------|
| Regional PM | Own the card; assign sub-tasks; track progress; manage risks |
| SME | Work on your assigned sub-task; update status weekly |
| Main PM | Monitor progress; escalate if at risk |
| Leadership | Check overall regional progress |

---

### III.B.3: Sub-Tasks (Functional Deliverables)

#### What They Are
**Sub-tasks** are individual deliverables that team members complete.

- **Live under a regional card** (not standalone)
- **Created by:** Regional PM or Main PM (should use template)
- **Owned by:** Functional SME (Training lead, Service manager, Ops manager, etc.)
- **Used for:** Tracking specific work pieces, not high-level phases

#### Sub-Task Structure

**Title:**
- Format: "[Deliverable Type] - [Function Area] - [Region]"
- Examples:
  - "Create Training Materials - Service Techs - Singapore"
  - "Develop Standard Operating Procedure - Regional Service - India"
  - "Spare Parts & Inventory Planning - Logistics - Australia"
- **Your job:** If assigned to you, this is YOUR deliverable

**Assigned to:**
- The person responsible for creating/completing this deliverable
- **If it's you:** You own getting this done

**Due Date:**
- When this deliverable must be complete
- **Usually:** Before next major phase gate
  - Deliverables due before Kick-off (so trainers can teach)
  - Training completion due before Launch (so reps ready)

**Status Indicators:**
- Not Started (default when created)
- In Progress (you started working on it)
- Completed (✓ done, ready for next step)

**Checklist Items (optional):**
- Sub-tasks can have checkboxes for sub-steps
- Example: "Create Training Materials" might have:
  - ☐ Outline created and approved
  - ☐ Draft materials written
  - ☐ Manager review complete
  - ☐ Final materials finalized

**Notes/Links Section:**
- Context, links to templates, requirements
- Example: "Use the training template at [SharePoint link]. Coordinate with Service Manager for approval. Due 3/15."

#### Common NPI Sub-Task Templates

Your organization should have templates for these (ask your Regional PM):

**Training Deliverables:**
- Create Training Plan - [Function]
- Develop Training Materials - [Function]
- Train the Trainers - [Function]
- Facilitate Training - [Function]
- Confirm Training Completion

**Service Deliverables:**
- Develop Service Procedures - [Function]
- Create Service Guides/Documentation
- Spare Parts & Inventory Readiness
- Field Service Training
- First Repair Protocol Definition

**Operational Deliverables:**
- Define Standard Operating Procedures
- Configure Systems/Tools
- Establish Inventory Processes
- Create Troubleshooting Guides
- Approval Routing Definition

**Marketing/Communications:**
- Develop Launch Communications
- Create Internal Announcements
- Prepare Customer Updates
- Coordinate Media/Press

**Business Process Changes:**
- Map Workflow Changes
- System Configuration
- Approval Routing Updates

#### How to Complete a Sub-Task (If Assigned to You)

**Step 1: Open the Card & Find Your Sub-Task**
1. Your Regional PM creates a regional card
2. They add your sub-task with your name and due date
3. You get notified in Teams/email
4. Click the notification or navigate to the card

**Step 2: Mark It "In Progress"**
1. Find your sub-task in the sub-tasks list
2. Click to open sub-task detail
3. Change status from "Not Started" → "In Progress"
4. Save

**Step 3: Work on Your Deliverable**
- This happens outside of Planner (you'll create docs, attend meetings, coordinate, etc.)
- Reference the sub-task notes for what you need to do
- Ask your PM if unclear

**Step 4: Update Progress in Planner**
- Weekly: Add a comment with your progress
  - "Training outline approved by manager. Draft modules 1-3 complete, working on module 4."
  - "All spare parts identified and on order. Expecting delivery by 2/28."
- If you hit a blocker: Add a comment asking for help
  - "Waiting for marketing approval on training materials. Can't finalize without their sign-off."

**Step 5: Mark Complete**
1. When deliverable is truly done
2. Click sub-task detail
3. Change status → "Completed" (or check the checkbox)
4. Add a completion note: "Training materials finalized and shared with all trainers. Ready for facilitation phase."
5. Save
6. Your Regional PM will see the completion and update their card progress accordingly

#### When You'll Interact With Sub-Tasks

| Scenario | What You Do |
|----------|-----------|
| Regional PM assigning work | Create sub-task, assign to functional SME, set due date |
| You're assigned a sub-task | Mark "In Progress," do the work, update weekly, mark "Completed" |
| You're managing sub-tasks | Monitor your team's progress; escalate blockers; celebrate completions |
| Leadership reviewing project | Sub-task completion shows real progress (not just promises) |

---

## III.C: Day-to-Day Tasks & Card Management

### III.C.1: Creating a New Card (Regional PM Perspective)

#### Scenario: Creating Your First Regional Card

You're the Regional PM for Singapore on the Calima project. Global Alignment is complete. Now it's time to create your regional card to kick off Regional Alignment phase.

#### Step-by-Step: Creating a Regional Card

**Step 1: Navigate to the Right Board**
1. Go to planner.cloud.microsoft.com
2. Find board: "PLC - RR - Calima - 01 Singapore"
3. Click to open
4. You should see Grid view with columns for each property

**Step 2: Locate the Upstream Card**
1. Look for card title: "NPI - Calima - CAL-001"
2. This is the global card created by Main PM in GA phase
3. You'll create your regional card in the same board
4. Read the upstream card to understand:
   - Global service model
   - Global launch date
   - Complexity of project
   - Which regions are participating

**Step 3: Click to Create New Card in RA Bucket**
1. Find the **RA** bucket (Regional Alignment)
2. Click **+ Add card** button at bottom of RA bucket
   - OR click in Grid view: **+ New** at bottom of grid
3. Card creation form opens

**Step 4: Fill in Basic Information**

**Title:** 
- Type: "[PLC Name] - [Region] - Regional Readiness"
- Example: "Calima - Singapore - Regional Readiness"
- **Important:** Keep format consistent across all projects

**Assigned to:**
- Click dropdown, select yourself (Regional PM)
- **This card is YOUR responsibility to manage**

**Start Date:**
- Click field, select date when Regional Alignment starts
- Usually 1-2 weeks after global alignment ends
- **Don't make it the same as Upstream card's start date**

**Due Date:**
- Click field, select when this region must be ready
- This is your **regional launch date** (may differ from global)
- Example: Global launch 6/15, but Singapore can launch 6/8
- **Critical timeline:** Set realistically based on your region's capability

**Description:**
1. Look at the template your Main PM provided
2. Copy it or use it as guide
3. Customize for Singapore
4. Include:
   - Regional service model (what service Singapore will deliver)
   - Regional scope (number of teams, locations, complexity)
   - Any regional constraints (language, time zones, holidays)
   - Regional stakeholders (who are the key players?)
5. Example:
   ```
   Singapore Regional Readiness for Calima NPI
   
   Regional Service Model: Customer Pays + Engineering Support
   Regions: Singapore, Malaysia
   Complexity: Large (training in 2 languages, 15 locations, multiple service models)
   Key Constraint: Training must be completed before Chinese New Year (2/10)
   Regional Stakeholder: Rajesh Kumar, Regional Service Leader
   ```

**Step 5: Add Custom Fields**

These are critical. Don't skip them.

1. Scroll down to **Custom Fields** section
2. **Planisware ID** (required):
   - Ask your Main PM for the regional Planisware line ID
   - Format: SVC-0145-SG (company-project-region)
   - If you don't know it: Leave blank temporarily, ask Main PM, add later
3. **Regional Service Model** (required):
   - Click dropdown
   - Select from: Customer Pays, Included, Limited, Engineering Support, Customized Training
   - Must match or customize the Global Service Model
4. **Complexity Rating** (required):
   - Small (SM): Single model, <5 locations, minimal training
   - Medium (Med): 1-2 models, 5-10 locations, standard training
   - Large (LRG): Mixed models, 10+ locations, significant training
   - XL: Multiple models, 20+ locations, major training, complex workflows
   - **Singapore example:** Large (multiple locations, 2 languages, complex training)
5. **Launch Date (Regional)** (required):
   - When Singapore goes live
   - May differ from global date
6. **Stakeholder Contact** (required):
   - Regional Service Leader name + email
   - Example: "Rajesh Kumar (Regional Service Leader) - rajesh.kumar@company.com"
7. **Playbook Status** (required):
   - Set to: "Section 1 Complete" (GA is done)
   - You'll update as you progress
8. **Risk Status** (optional for now):
   - Start as "Green" (assuming on track)
   - Update weekly if situation changes

**Step 6: Save the Card**
1. Click **Save** or **Create**
2. Card is now created in the RA bucket
3. You should see it appear in your board

**Step 7: Notify Your Team**
1. Go to Teams channel for this project
2. Post in general channel:
   ```
   Regional card created for Singapore! 
   Card: "Calima - Singapore - Regional Readiness"
   I'll start scheduling regional alignment meetings this week.
   Kick-off meeting invites coming soon.
   ```
3. This lets everyone know the region is now active

---

#### Common Mistakes to Avoid When Creating Cards

| Mistake | Problem | How to Fix |
|---------|---------|-----------|
| Wrong format in title | Inconsistent naming, hard to find | Use template: "[PLC] - [Region] - Regional Readiness" |
| Missing required custom fields | Card incomplete, governance blocks it | Fill all starred fields before saving |
| Due date unrealistic | Timeline fails, team stressed | Discuss with Regional Service Leader before setting |
| Wrong Planisware ID | Financial tracking breaks | Ask Main PM, get exact ID, update immediately |
| Not linked to Upstream card | Card seems isolated | Create dependency (see Section III.C.5) |
| No description | Others don't understand scope | Write 3-4 sentences about regional scope |

---

### III.C.2: Creating Sub-Tasks (Functional Deliverables)

#### Scenario: Breaking Down Your Regional Card Into Deliverables

Your regional card is created. Now you need to identify all the work your teams must complete before regional kick-off. You'll create sub-tasks for each major deliverable.

#### Standard Sub-Tasks for NPI Projects

**Before you create, know what you need:**

**Training Sub-Tasks:**
- [ ] Create Training Plan (by date X)
- [ ] Develop Training Materials (by date X)
- [ ] Train the Trainers (by date X)
- [ ] Facilitate Training to All Staff (by date X)

**Service/Operations Sub-Tasks:**
- [ ] Develop Regional Service Procedures (by date X)
- [ ] Identify & Order Spare Parts/Inventory (by date X)
- [ ] Configure Regional Service Model in Systems (by date X)
- [ ] Regional Readiness Sign-off (by date X)

**Communications Sub-Tasks:**
- [ ] Draft Regional Launch Communications (by date X)
- [ ] Finalize Communications with Marketing (by date X)
- [ ] Send Pre-Launch Internal Announcements (by date X)

**Business Process Sub-Tasks:**
- [ ] Map Regional Workflow Changes (by date X)
- [ ] Update Regional Approval Routing (by date X)

#### Step-by-Step: Creating Sub-Tasks

**Step 1: Open Your Regional Card**
1. Find your regional card: "Calima - Singapore - Regional Readiness"
2. Click to open detail view
3. Scroll down to **Sub-tasks** section

**Step 2: Add First Sub-Task**
1. Click **+ Add sub-task**
2. **Title field:** Type the deliverable
   - Example: "Create Training Plan - Service Technicians - Singapore"
   - Format: "[Deliverable Type] - [Function] - [Region]"
3. **Assigned to:** Click dropdown, select the functional SME
   - Example: Assign to "Sarah Chen, Training Manager"
   - **Important:** Only assign to someone who actually agreed to do it
4. **Due date:** Set when this deliverable is needed
   - Think about your critical path
   - Training plan due before training is created (2-3 months before launch)
   - Service procedures due before training (2-3 months before launch)
   - Actual training facilitation due 2-3 weeks before launch
   - **Example:** Regional launch 6/15, so training plan due 3/15, training materials due 4/15, training happens 5/1-6/1
5. **Add notes/context:** Click in notes section
   - "Please create a training plan that covers: [list modules]. Use the template at [link]. Coordinate with Service Manager for approval. Let me know if you have questions."
6. Click **Add** to create the sub-task

**Step 3: Create All Sub-Tasks**
Repeat Step 2 for each deliverable. You should have 6-10 sub-tasks total.

**Example Set for Singapore Calima:**
1. Create Training Plan - Service Techs - Due 3/1
2. Create Training Materials - Service Techs - Due 4/1
3. Train the Trainers - Service Mgmt - Due 4/20
4. Develop Service Procedures - Service Ops - Due 3/15
5. Identify Spare Parts & Inventory - Logistics - Due 3/20
6. Regional Readiness Confirmation (sign-off) - Regional Leader - Due 6/8

**Step 4: Communicate with Your Team**
1. Once all sub-tasks are created
2. Send email to your team:
   ```
   Hi team,
   
   I've created the regional readiness cards for Calima in Planner Premium.
   
   Please review your assigned sub-tasks in the card: "Calima - Singapore - Regional Readiness"
   
   Key dates:
   - Training plan due: 3/1
   - Training materials due: 4/1
   - Sign-off required: 6/8
   
   Questions? Reach out or comment in Planner.
   
   Let's crush this launch!
   ```

**Step 5: Check In Weekly**
1. Every Friday, review your sub-tasks
2. See which ones have progress updates
3. Identify any blockers
4. Escalate if SME is falling behind (see Section III.F.3)

---

#### When to Create Sub-Tasks

| Phase | What You Create |
|-------|-----------------|
| Regional Alignment | All major deliverables for the region |
| Regional Engage | Any sub-tasks discovered during engagement |
| Kick-off | Any final details before execution |
| Execute | Break down if major risks emerge |
| Do NOT create | Sub-tasks for tasks already in sub-tasks (no nesting) |

---

### III.C.3: Updating Card Status & Progress

#### Daily & Weekly Routine

**This is where real project management happens.** Card status is not set once — it's updated continuously.

#### Daily Check-In (5 minutes)

**Every morning or before meetings:**
1. Open your board (Grid or Board view)
2. **Scan for red cards** (at-risk, overdue, blockers)
3. **Click each red card** and read recent comments
   - What's the issue?
   - Who reported it?
   - When is it due?
4. **If it's yours:** Update status or add comment
   - If you resolved it overnight, mark green
   - If it's still red, add a comment: "Still working on this, update tomorrow"
5. **If it belongs to someone else:** Tag that person
   - Example: "@Sarah Chen - When will the training materials be ready? This is showing red."

#### Weekly Status Update (Thursday afternoon)

**Essential for governance calls:**

1. Open your board
2. **Review all cards in your pipeline** (if Regional PM)
3. For each card:
   - Is status still accurate?
   - Has anything changed since last week?
   - What's the next action?
4. **Update "Next Activity Date" field**
   - This field shows: "What's my next planned action on this card?"
   - Example: "01/20/2025 - Schedule SME kickoff meeting"
   - Example: "01/25/2025 - Review training draft from team"
   - Example: "TBD - Waiting for marketing approval" (if blocked)
5. **Add a comment** to the card if there's significant progress
   - Example: "Week 2 of Regional Alignment: Met with all regional stakeholders. Confirmed service model with 3 regions. One region (Malaysia) still needs director approval. Expecting that by 1/24. On track for RA completion by end of month."
6. **Check all sub-tasks**
   - Any due this coming week? Follow up with owner
   - Any overdue? Escalate
   - Any completed? Celebrate and move on

#### Marking Progress (When Sub-Tasks Complete)

**When someone completes a sub-task:**

1. **They mark it complete** in the sub-task detail
   - Changes status from "In Progress" → "Completed"
   - Card progress bar automatically increases
2. **They add a completion comment:**
   - "Training materials finalized and shared with all team leads"
   - "Service procedures approved by regional service manager"
3. **You (Regional PM) verify:**
   - Is it really complete? Or just 95% done?
   - If truly complete, it stays complete
   - If not complete, ask the SME to update their comment
4. **You confirm in governance call:**
   - "Training module 1 complete. 3 more modules in progress, on track for 4/15 deadline."

#### Understanding Risk Status Field

This field is **critical for escalation.**

**Status Options:**
- **Green** = On track, no issues, will be done on time
- **Yellow** = Minor risk, small issue, likely recoverable with adjustments
- **Red** = Major risk, likely to miss deadline, needs escalation
- **Blocked** = Can't proceed at all, waiting for something, urgent escalation

**When to Change Status:**

| Situation | Status | Action |
|-----------|--------|--------|
| Everything going well | Green | Nothing to escalate |
| One SME delayed, but catchable | Yellow | Give warning, plan mitigation |
| Timeline now unrealistic | Red | Escalate immediately to PM and leadership |
| Waiting for external approval | Blocked | Escalate, find workaround |
| Hit a technical issue | Red | Escalate to IT or Main PM |

**How to Update Risk Status:**
1. Open the card
2. Find **Risk Status** custom field
3. Click dropdown, select new status
4. **Always add a comment explaining why**
   - Red: "Training SME left the company. Hired replacement, but they need 2 weeks to ramp. New delivery date 4/30 vs. 4/15. Will miss kick-off unless we reduce scope or accelerate hiring."
   - Blocked: "Waiting for marketing approval on messaging. Marketing team backlogged, said 4-week timeline. Blocker: can't finalize communications without their sign-off."
5. Save

**Red Status = Escalate**
If you set a card to Red, you MUST notify:
1. Your Regional Service Leader (in 1:1 or email)
2. Your Main PM (in comment or email)
3. The team (in Teams channel)

Example escalation message:
```
🚨 ESCALATION: Calima Singapore Training Delayed

Card: "Calima - Singapore - Regional Readiness"
Issue: Training SME left; replacement being onboarded
Impact: Training delivery now 2 weeks late (4/30 vs. 4/15)
Consequence: May miss regional kick-off date unless scope is reduced
Action needed: Do we reduce training scope, or delay kick-off?

Let's discuss in tomorrow's governance call.
```

---

### III.C.4: Moving Cards Between Buckets (Phase Progression)

#### What Moving a Card Means

When a card moves from one bucket to another, **the project is advancing to the next phase.**

- **Pipeline → GA:** Project approved, moving to global alignment
- **GA → RA:** Global alignment complete, ready for regional alignment
- **RA → Engage:** Regional alignment done, start engaging with teams
- **Engage → Kick-off:** SME commitments received, formal kick-off happening
- **Kick-off → Execute:** Project plan approved, work is starting
- **Execute → Hypercare:** Launch day reached, monitoring support period
- **Hypercare → Close-out:** 30 days of go-live support complete, project closing

**Each move is a governance decision,** not automatic.

#### Who Can Move Cards?

- **Upstream cards:** Main PM only (controls global progression)
- **Regional cards:** Regional PM (controls regional progression)
- **Sub-tasks:** Anyone assigned to it (just mark complete, doesn't move to another bucket)

#### Before You Move a Card: The Checklist

**DO NOT move a card until you can answer YES to all of these:**

- ✓ All required custom fields are filled? (starred fields)
- ✓ All deliverables for THIS phase are at least started (or complete)?
- ✓ No critical blockers preventing next phase?
- ✓ Key stakeholders have approved? (Regional Service Leader, Main PM)
- ✓ Are there any risks that should be resolved first?
- ✓ Is the next phase's timeline realistic?
- ✓ Do we have the resources to execute the next phase?

**If you answered NO to ANY of these, DON'T move the card yet.** 
Instead: Fix the issue, document in card comments, escalate if needed.

#### Step-by-Step: Moving a Card

**Example:** Your regional card is ready to move from RA → Engage

**Step 1: Verify You're Ready**
- Run the checklist above
- All required fields filled? ✓
- Regional stakeholders approve? ✓
- Timeline realistic? ✓
- Clear to proceed? ✓

**Step 2: Open the Card**
1. Find the card: "Calima - Singapore - Regional Readiness"
2. Currently in **RA** bucket
3. Click to open detail view

**Step 3: Move the Card (Method 1: Board View)**
1. Go to **Board view** (swimlane view)
2. Find the card in **RA** bucket
3. **Drag the card** to the **Engage** bucket
4. The card visually moves to new bucket
5. **Confirm the move** if prompted

**Step 3: Move the Card (Method 2: Grid View or Detail View)**
1. In card detail, find **Bucket** field
2. Click dropdown
3. Select new bucket (Engage)
4. Click save

**Step 4: Update Timeline**
1. **Start date field:** Update to first day of Engage phase
   - Usually a few days after previous phase ended
   - Example: RA ends 3/31, Engage starts 4/2
2. **Due date field:** Update to end of Engage phase
   - Engage is typically 4-8 weeks
   - Example: Engage due date 5/31
3. **Next Activity Date field:** Set to your next action
   - Example: "04/02/2025 - Schedule pre-engagement call with SMEs"
4. Save

**Step 5: Add a Comment**
1. Click **Conversation** or **Comments** tab
2. Add this comment:
   ```
   ✅ PHASE PROGRESSION: RA → Engage
   
   Regional Alignment complete! All regional stakeholders confirmed service model.
   
   Moving to Regional Engage phase.
   
   Next: Schedule pre-engagement meeting with SMEs to confirm availability and timelines.
   ```
3. This creates a record of when and why the progression happened

**Step 6: Notify the Team**
1. In Teams channel for this project
2. Post:
   ```
   🎯 Phase Update: Calima Singapore moving to Engage phase
   
   Regional Alignment is complete. All stakeholders aligned on regional service model.
   
   Next steps:
   - Pre-engagement meeting with regional SMEs (week of 4/2)
   - Confirm team availability and timelines
   - Formal kick-off to follow
   ```
3. This keeps everyone informed

---

#### What If You Move a Card Backward?

**Moving backward is a RED FLAG.** It means something wasn't ready.

Example: You moved to Engage, but then discovered the regional service model is wrong. You move back to RA.

**If this happens:**
1. Document WHY in a detailed comment
2. Escalate immediately to Main PM and Regional Service Leader
3. Add a high-priority risk to the card
4. Work through the issue before moving forward again

This is normal (not a failure!), but it needs visibility and support.

---

### III.C.5: Understanding & Creating Dependencies

#### What Is a Dependency?

A **dependency** means one card depends on another card finishing (or starting) first.

**Real-world example:**
- You can't start Regional Engagement until Global Alignment is finished
- Regional card depends on Upstream card

**In Planner, a dependency:**
- Connects two cards with a visual line
- Shows which card must finish before the other starts
- Helps identify blockers and critical path

#### Dependency Types

Planner Premium supports 4 dependency types:

| Type | Meaning | When to Use |
|------|---------|-----------|
| **Finish-to-Start (FS)** | Card A must FINISH before Card B can START | Card A's work is prerequisite for Card B. Most common. |
| **Start-to-Start (SS)** | Card A must START before Card B can START | Cards start together but at different times. Rare. |
| **Finish-to-Finish (FF)** | Card A must FINISH before Card B can FINISH | Both cards must complete around same time. Rare. |
| **Start-to-Finish (SF)** | Card A must START before Card B can FINISH | Unusual, used for monitoring/support roles. Very rare. |

**99% of the time, you'll use Finish-to-Start (FS).**

#### Real-World NPI Dependencies

| Card A (Predecessor) | Type | Card B (Dependent) | Why? |
|-------|------|-------|------|
| Upstream card (GA complete) | FS | Regional card (RA start) | Can't plan regionally until global model is set |
| Training materials created | FS | Training delivery | Can't train people without materials |
| Service procedures finalized | FS | Service team training | Can't train reps on procedures that don't exist |
| All regional cards complete | FS | Upstream card moves to Hypercare | Project only goes live when all regions ready |

#### How to Create a Dependency

**Scenario:** You just created your regional card. Now you need to link it to the Upstream card so everyone knows: "This regional card can't progress until Upstream (GA) is complete."

**Step 1: Open Your Regional Card**
1. Find: "Calima - Singapore - Regional Readiness"
2. Click to open detail view

**Step 2: Find Dependencies Section**
1. Scroll down to find **Dependencies** section
   - May be called "Linked cards" or "Dependencies"
   - Usually near bottom of card detail
2. Click **+ Add dependency**

**Step 3: Select Dependency Type**
1. Click dropdown for relationship type
2. Select: **Finish-to-Start (FS)**
   - (Meaning: Upstream card must finish before this card starts)

**Step 4: Search for the Card It Depends On**
1. Type in search box: "Calima" or "CAL-001"
2. Results appear
3. Click: "NPI - Calima - CAL-001" (the Upstream card)

**Step 5: Save**
1. Click **Add** or **Save**
2. Dependency is now created
3. You should see the connected cards now show a line when in Timeline view

**Step 6: Verify in Timeline View**
1. Switch to **Timeline view**
2. Look for the Upstream card and your Regional card
3. A line should connect them
4. If green: Predecessor is on track
5. If red: Predecessor is at risk or late

---

#### When to Create Dependencies

**Create dependencies to show:**
- ✓ Upstream card → Regional cards (regional depends on global)
- ✓ Between regional cards (if regions have sequence, ex: India first, then Singapore)
- ✓ Between phases (Engage complete → Kick-off can start)
- ✓ Between deliverables (Training materials done → Training facilitation can start)

**Do NOT create dependencies for:**
- ✗ Sub-tasks (they're children of cards, don't need separate dependencies)
- ✗ Things that are independent (if two regions can work parallel, don't link them)
- ✗ Everything (too many dependencies hide the real critical path)

#### Reading Dependencies in Timeline View

**Timeline view shows dependencies as connecting lines.**

- **Green line:** Everything is fine, predecessor is on track
- **Red line:** ALERT! Predecessor is at risk or late, dependent card is now blocked

**What to do if you see a red line:**
1. Click the predecessor card (the one on the left of the red line)
2. Check its status
3. If it's red, update the blocker or escalate
4. Once predecessor is on track, line turns green

---

## III.D: Custom Fields & Required Information

### Understanding Custom Fields

Custom fields are **NPI-specific data** that help with governance and reporting.

**Key principle:** 
- Some fields are **required** (marked with ★) — fill before moving forward
- Some are **informational** (nice to have) — fill when you know the info
- Some are **updated regularly** (Risk Status) — change weekly
- Some are **set once** (Planisware ID) — don't change after creation

---

### III.D.1: Master Custom Field Definitions

#### FIELD 1: Planisware ID ⭐ (Required)

**What it is:** Unique identifier linking Planner to Planisware financial system

**Format:** [OU Code]-[Project Code]-[Region Code]
- **OU Code:** 3-letter operating unit code (SVC, FLD, etc.)
- **Project Code:** 4-digit unique project number
- **Region Code:** 2-letter country/region code
- **Example:** SVC-0145-SG (Service OU, Project 145, Singapore)

**Who fills it:** Main PM (Upstream), Regional PM (Regional cards)

**When it's due:** 
- Upstream: By end of GA phase
- Regional: By end of RA phase

**Why it matters:**
- Links project timeline to financial tracking
- Enables budget monitoring
- Supports capacity planning (financial resource allocation)
- Required for governance reporting

**If you don't know it:** 
- Ask your Main PM or Finance contact
- Don't leave it blank
- Update immediately once you get the ID

**Can you change it?** 
- NO. Set it once in RA, don't change. Contact Finance if you discover an error.

---

#### FIELD 2: Global Service Model ⭐ (Upstream card only)

**What it is:** What service will we deliver globally?

**Options:**
1. **Customer Pays:** Customer pays for each service visit
2. **Included:** Service included with product purchase
3. **Limited:** Limited service included, additional costs for extras
4. **Engineering Support:** Remote engineering support only
5. **Customized Training:** Custom training tailored to customer

**Who fills it:** Main PM (during GA phase)

**When it's due:** End of GA phase (required before moving to RA)

**Why it matters:**
- Determines what regions MUST offer (some regions may not have all service capabilities)
- Drives regional scope and costs
- Shapes training and SOP requirements
- Regional PM will customize this for their region (if allowed)

**Example:** 
- Global model: "Included + Customer Pays extra"
- Singapore can offer: "Included + Customer Pays extra" (has capabilities)
- India can offer: "Included only" (doesn't have customer-pay infrastructure yet)

**Can you change it?**
- YES, but only Regional PM for their regional card (customizing is allowed)
- NO, Regional PM cannot change the Upstream card's Global Service Model
- Contact Main PM if you think the global model is wrong

---

#### FIELD 3: Regional Service Model ⭐ (Regional cards only)

**What it is:** What service will THIS region deliver?

**Options:** Same as Global Service Model (Included, Customer Pays, Limited, Engineering Support, Customized Training)

**Who fills it:** Regional PM (during RA phase)

**When it's due:** End of RA phase (before moving to Engage)

**Why it matters:**
- Tells your teams exactly what to deliver
- Drives scope of training, procedures, and support
- Must be approved by Regional Service Leader
- If different from global, you need documented exception

**When Regional Service Model differs from Global:**
- Sometimes a region CAN'T offer all options (no infrastructure, skills, regulations)
- Document the limitation and exception
- Get Regional Service Leader approval
- Escalate if it impacts revenue or commitments

**Example:**
- Global: "Customer Pays available"
- Malaysia: "Engineering Support only" (can't support on-site service visits)
- This is documented as a regional exception

**Can you change it?**
- YES, anytime before or during execution if situation changes
- But requires Regional Service Leader approval
- Make a comment explaining why you're changing it

---

#### FIELD 4: Complexity Rating ⭐ (Upstream & Regional)

**What it is:** How complex is this project?

**Scale:**
- **SM (Small):** Single service model, <5 locations, minimal training (1-2 days)
- **Med (Medium):** 1-2 service models, 5-10 locations, standard training (3-5 days)
- **LRG (Large):** Mixed models, 10+ locations, significant training (1-2 weeks), some workflow changes
- **XL (Extra Large):** Multiple models, 20+ locations, major training (2-4 weeks), complex workflow changes, multiple languages

**Who fills it:** Main PM (Upstream), Regional PM (Regional)

**When it's due:** 
- Upstream: In GA phase
- Regional: In RA phase

**Why it matters:**
- Drives resource allocation (bigger projects need more people)
- Influences timeline feasibility
- Escalates risk management (XL projects get more scrutiny)
- Helps with capacity planning

**Sizing Checklist:**
- How many regions involved?
- How many service models?
- How many locations/teams?
- How much training needed?
- Any workflow/system changes?
- Language translations required?
- Regulatory/compliance considerations?

**Example:**
- Calima Singapore: LRG (15 locations, 2 service models, training in 2 languages, 2-week training program, some SOPs need localization)

**Can you change it?**
- YES, during RA. You may discover it's bigger than initially thought
- Make a comment explaining: "Complexity upgraded from Med to LRG. Discovered 5 additional locations and 2 service models not originally planned."
- If you downgrade (LRG → Med), this is a red flag. Justify it.

---

#### FIELD 5: Regions Involved ⭐ (Upstream card only)

**What it is:** List of all regions participating in this NPI

**Format:** Comma-separated list of region names
- **Example:** "Singapore, India, Australia, Vietnam, Malaysia"
- **Not:** "APAC" (too vague) — list actual regions
- **Not:** "5 regions" (too vague) — list them

**Who fills it:** Main PM (during GA phase)

**When it's due:** In GA (updated as regional cards created)

**Why it matters:**
- Shows scope: How many regions are we coordinating?
- Portfolio visibility: How many NPI projects in APAC region?
- Resource planning: If we have 50 SMEs and 10 concurrent NPIs with 5 regions each, that's 250 person-slots needed
- Dependency tracking: If three regions doing same NPI, may have sequencing dependencies

**Example:**
- Calima: "Singapore, Malaysia, India, Australia, New Zealand"
- This means 5 regional cards will be created, one per region

**Can you change it?**
- NO, don't change this. Contact Main PM if a region needs to be added/removed
- This is determined during GA and shouldn't change

---

#### FIELD 6: Launch Date (Global) ⭐ (Upstream card)

**What it is:** When does this product go live globally?

**Format:** MM/DD/YYYY (e.g., 06/15/2025)

**Who fills it:** Main PM (during Pipeline/GA)

**When it's due:** In Pipeline or early GA

**Why it matters:**
- **THE critical date** — everything flows from this
- Drives all regional timelines
- Marketing schedules announcements
- Financial books product launch
- Supply chain prepares inventory
- Regions plan backwards from this date

**When Launch Date is firm vs. flexible:**
- **Firm:** Announced to customers/market (don't change without executive approval)
- **Flexible:** Still being negotiated with leadership (may adjust in GA)
- **Always assume firm** unless told otherwise

**Regional dates may differ from global:**
- Global: 6/15/2025
- APAC regions may launch earlier (6/1) if ahead of schedule
- APAC regions may launch later (6/30) if behind schedule
- But all dates should be close together (within 2-4 weeks)

**Can you change it?**
- NO, don't change the Global Launch Date
- If timeline changes, escalate to Main PM and leadership
- Document the issue as a Red Risk and escalate immediately

---

#### FIELD 7: Launch Date (Regional) ⭐ (Regional cards only)

**What it is:** When does THIS region go live?

**Format:** MM/DD/YYYY (e.g., 06/08/2025)

**Who fills it:** Regional PM (during RA phase)

**When it's due:** End of RA phase (before Engage)

**Why it matters:**
- Your region's "line in sand"
- All deliverables must be complete by this date
- This is usually same as Global Launch Date, but can differ

**When Regional Launch Date differs from Global:**
- You can launch earlier (if ready) → good for learning
- You can launch later (if not ready) → but why? Escalate if delays are unavoidable
- Spread of 2 weeks max (all regions should launch within 2 weeks of each other)

**Realistic Dating:**
- DON'T over-promise
- DON'T date that depends on everything going perfectly
- Build in buffer (one week minimum)
- Example: "Global is 6/15, so I'm committing to 6/8 to give myself a buffer"

**Can you change it?**
- YES, but only in RA and Engage phases (before Kick-off)
- Once in Kick-off, this becomes firm
- If you need to change after Kick-off, escalate immediately
- Make a comment: "Regional Launch Date moved from 6/15 to 6/30. Reason: One critical SME unavailable 6/1-6/15 due to competing project. Escalating for approval."

---

#### FIELD 8: Playbook Status ⭐ (Regional cards)

**What it is:** Which Global NPI Playbook sections is your region completing?

**NPI Playbook Background:**
- Global NPI Playbook is a comprehensive process guide (separate from Planner)
- It has 4 major sections:
  - **Section 1:** Global Service Model & Product Details
  - **Section 2:** Regional Forecasts & Capabilities
  - **Section 3:** Service Deliverables & Procedures
  - **Section 4:** Training & Launch Readiness

**Options (Pick the current status):**
1. Section 1 Pending
2. Section 1 Complete ✓
3. Section 2 Pending
4. Section 2 Complete ✓
5. Section 3 Pending
6. Section 3 Complete ✓
7. Section 4 Pending
8. Section 4 Complete ✓

**Who fills it:** Regional PM (tracking progress)

**When to update:**
- **RA phase:** Section 1 should be complete by end of GA (you're updating it as RA starts)
- **Engage phase:** Section 2 should be completed
- **Kick-off phase:** Section 3 should be completed
- **Execute phase:** Section 4 should be completed
- **Before Launch:** All 4 sections complete

**Why it matters:**
- Playbook is governance requirement (auditable, compliant)
- Shows readiness: Can't launch if playbook sections missing
- Tracks where you are in regional readiness journey

**Example progression:**
- Month 1 (RA): Section 1 Complete, Section 2 Pending
- Month 2 (Engage): Section 1 Complete, Section 2 Complete, Section 3 Pending
- Month 3 (Kick-off): Sections 1-3 Complete, Section 4 Pending
- Month 4 (Execute): All 4 Sections Complete

**Can you change it?**
- YES, update weekly or when milestone completes
- Change in comment: "Section 2 now complete. All regional forecasts finalized and validated by Regional Service Leader."

---

#### FIELD 9: Risk Status ⭐ (Upstream & Regional) — CRITICAL FIELD

**What it is:** Current risk level of the card

**Status Options:**
1. **Green:** On track, no issues, will be done on time
2. **Yellow:** Minor risk, small issue, likely recoverable
3. **Red:** Major risk, likely to miss deadline
4. **Blocked:** Can't proceed, waiting for something external

**Who fills it:** Project owner (Main PM for Upstream, Regional PM for Regional)

**When to update:**
- **Every Friday:** Review progress, update if changed
- **Immediately:** If situation changes during week
- **Before governance call:** Status must be current

**Why it matters:**
- **Red or Blocked status = Immediate escalation**
- Leadership uses this to spot problems early
- Helps identify projects needing support/resources

**Decision Tree for Setting Status:**

```
Is everything on track?
├─ YES → Green
└─ NO → Is the issue recoverable?
    ├─ YES (small impact, can catch up) → Yellow
    ├─ NO (will miss deadline) → Red
    └─ Blocked (can't proceed until external thing happens) → Blocked
```

**Examples:**

| Situation | Status | Why |
|-----------|--------|-----|
| Deliverables on schedule, team productive | Green | No risks |
| One SME delayed, but can catch up by shifting tasks | Yellow | Recoverable |
| Training facility needs to be rented, only option available 2 weeks late | Red | Can't recover, will miss launch |
| Waiting for legal approval on service model, legal is backlogged, can't proceed | Blocked | Can't do anything until legal approves |

**When you change to Red or Blocked, you MUST:**
1. Add a detailed comment explaining the issue
2. Notify your PM and Regional Service Leader
3. Propose a mitigation: "Here's what we can do to fix it"
4. Set a date for resolution: "We need a decision by Friday"

---

#### FIELD 10: Stakeholder Contact ⭐ (Regional cards)

**What it is:** Name and email of regional decision-maker

**Format:** "First Last (Title) - email@company.com"
- **Example:** "Rajesh Kumar (Regional Service Leader) - rajesh.kumar@company.com"

**Who fills it:** Regional PM (during RA phase)

**When it's due:** End of RA phase

**Why it matters:**
- Clear escalation path (who to contact for regional approvals)
- Used for governance reporting
- Required for sign-offs and phase gates

**Who should it be?**
- Regional Service Leader, OR
- Regional PM (if you're both PM and decision-maker), OR
- Regional Finance/Director (if they're the escalation point)
- **Not:** Field manager or coordinator (too low in org)
- **Must be:** Someone with authority to approve timeline changes, scope adjustments, resource decisions

**Can you change it?**
- YES, if regional leadership changes or decision-maker changes roles
- Update immediately: "Stakeholder contact changed from [old name] to [new name] due to org restructure"

---

### III.D.2: How to Fill Custom Fields

#### When You Create a New Card

1. **Open card detail view**
2. **Scroll to Custom Fields section**
3. **For each field marked with ⭐ (required):**
   - Click the field
   - Enter or select the value
   - Click outside field or hit Tab to save
4. **For optional fields:**
   - Fill in if you have the info
   - Leave blank otherwise (you can add later)
5. **Before you save the card, verify:**
   - All ⭐ fields are filled
   - No fields have errors (red highlighting)
6. **Save the card**

#### Common Entry Methods

**Text Fields (type text):**
- Planisware ID: Type "SVC-0145-SG"
- Stakeholder Contact: Type "Rajesh Kumar (Regional Service Leader) - rajesh@company.com"

**Dropdown Fields (select from list):**
- Global Service Model: Click → Select "Included"
- Complexity Rating: Click → Select "Large"
- Risk Status: Click → Select "Green"

**Date Fields (pick a date):**
- Launch Date: Click → Calendar appears → Click desired date

**Multi-Select Fields (pick multiple):**
- Regions Involved: Type each region name, hit Enter/comma to add next

---

### III.D.3: Field Maintenance & Updates

#### Weekly Updates (Every Friday)

**These fields change frequently and need updating:**

| Field | Update When | How |
|-------|-----------|-----|
| **Risk Status** | Situation changes | Click field, select new status, add comment |
| **Playbook Status** | Section completed | Click field, select new section, add comment |
| **Next Activity Date** | You have new action | Click field, select/type new date |

#### Monthly Reviews (First of month)

**Check these fields once a month:**

| Field | Review | Action |
|-------|--------|--------|
| **Launch Date (Regional)** | Still realistic? | If changed significantly, escalate |
| **Complexity Rating** | Still accurate? | If you discovered it's bigger/smaller, update with explanation |
| **Regional Service Model** | Still what you're delivering? | If changed, make comment |

#### Never Change (Once Set)

**These fields should NOT change:**

| Field | Why |
|-------|-----|
| **Planisware ID** | Financial system depends on it being consistent |
| **Global Service Model** (on Upstream) | Only Main PM can change |
| **Regions Involved** (on Upstream) | Only Main PM can change |

If you think one of these needs to change:
1. Don't change it yourself
2. Contact Main PM or Finance
3. Document the reason
4. Get approval before any change

---

### III.D.4: Common Field Errors & How to Fix Them

| Error | Cause | Fix |
|-------|-------|-----|
| "Required field missing" | You left a ⭐ field blank | Find the blank field, fill it in |
| "Card won't save" | One or more required fields blank | Verify ALL ⭐ fields have values |
| "Planisware ID in wrong format" | You typed it incorrectly | Ask Main PM for correct format, update |
| "Date won't update" | Browser cache issue | Refresh page (Ctrl+R), try again |
| "Can't change Risk Status" | No permission to edit card | Only card owner or PM can change it |
| "Dropdown shows old values" | System hasn't refreshed | Close browser, reopen, try again |

---

## III.E: Tracking Progress & Timelines

### III.E.1: Understanding Your Card Timeline

#### Reading Timeline Information

**Every card has 3 dates that tell a story:**

1. **Start Date:** When work on this phase begins
2. **Due Date:** When work on this phase must be complete
3. **Days Remaining:** Countdown (how many days until due date)

**Color coding helps you see status:**
- **Green Bar:** On track (working along, not at risk)
- **Yellow Bar:** At risk (approaching deadline, progress is slow)
- **Red Bar:** Overdue or major risk (past due date or critical issue)
- **Gray Bar:** Not started (start date is in future)

#### Example Timeline

Let's say your regional card:
- **Start Date:** 3/1/2025 (Regional Alignment phase begins)
- **Due Date:** 3/31/2025 (RA phase must be complete)
- **Today:** 3/15/2025
- **Days Remaining:** 16 days

**What the dates tell you:**
- ✓ Midway through the phase (15 days elapsed, 16 days remaining)
- ✓ On track if progress is 50% complete
- ⚠️ At risk if progress is less than 50%
- 🚨 Overdue if progress is less than 50% and we're already past 3/31

#### Updating Dates As Phase Changes

When you move a card to a new bucket:

**Old phase dates:**
- Start: 3/1/2025
- Due: 3/31/2025

**New phase dates (after moving to Engage):**
- Start: 4/2/2025 (first day of new phase)
- Due: 5/31/2025 (end of new phase, typically 4-8 weeks)

---

### III.E.2: Using Timeline View for Schedule Management

#### When to Use Timeline View

**Best for:**
- Planning your schedule
- Seeing when everything happens
- Understanding critical path (what's blocking what)
- Spotting bottlenecks (too much happening same time)
- Presenting to leadership

**Not for:**
- Daily task updates (too high-level)
- Detailed deliverable tracking (need card detail view)

#### How to Read the Timeline

**Bars show duration:**
- **Bar length** = How long the phase lasts
- **Bar position** = When it happens (left = earlier, right = later)
- **Bar color** = Health (blue = good, orange = at risk, red = critical)

**Dependency lines show relationships:**
- **Lines connecting bars** = One depends on the other
- **Green line** = Dependency healthy (predecessor on track)
- **Red line** = ALERT! Predecessor at risk, dependent card is now blocked

**Reading a Healthy Dependency:**
```
Upstream (GA)  ════════════════
                              ├─ connector
                                  Regional (RA)  ═════════════════
```
Green line = Upstream finishes before Regional starts. Good!

**Reading a Broken Dependency:**
```
Upstream (GA)  ════════════════ [Late!]
                              ├─ RED LINE ALERT
                                  Regional (RA)  ═════════════════
```
Red line = Upstream is late, Regional can't start on time!

#### Actions You Can Take in Timeline View

| Action | How | When |
|--------|-----|------|
| **Change due date** | Drag bar endpoint left/right | Need to adjust timeline |
| **Move phase** | Drag entire bar left/right | Moving start date |
| **Click a bar** | Left-click the bar | To open card detail and edit |
| **See dependencies** | Hover over connecting lines | To understand relationships |
| **Zoom in/out** | Scroll wheel or zoom buttons | To see more detail or bigger picture |

#### Responding to Red Timeline Alerts

**If you see a red dependency line:**
1. Click the predecessor card (card on left of red line)
2. Check its status
3. Is it Red or Blocked? 
4. If yes, escalate immediately
5. Once predecessor gets back on track, red line turns green

**If your timeline shows overdue (past due date):**
1. Check your progress percentage
2. Is it 100% complete? Then move to next phase
3. Is it not 100%? Then you're overdue, escalate

---

### III.E.3: Next Activity Date Field

#### Why This Field Matters

**Next Activity Date is the single most important field for status tracking.**

It answers: "What are you doing next on this card?"

- **If empty:** Others don't know what's happening, assume you forgot
- **If old date:** Looks like you're stalled
- **If recent future date:** Shows card is actively managed

#### How to Use Next Activity Date

**Every Friday (in weekly status update):**
1. For each card you own
2. Ask: "What's my next action on this card?"
3. Update the field with that action's date
4. **Format:** MM/DD/YYYY
5. **Add a comment:** Brief description of action
   - "01/20 - Schedule kickoff meeting with SMEs"
   - "01/25 - Review training materials draft"
   - "02/03 - Confirm regional readiness from OU contact"

**Examples of good Next Activity Dates:**

| Date | Activity | Status |
|------|----------|--------|
| 01/17 (tomorrow) | Submit Planisware ID to Finance | Active |
| 01/22 | Collect SME timelines for Kick-off planning | On track |
| 01/29 | Regional Service Leader approval of service model | Awaiting |
| TBD | Waiting for marketing to finalize launch messaging | Blocked |

**If it says "TBD":**
- Add a comment: "Waiting for [thing]. Will update when [condition met]."
- Set a follow-up date to revisit
- This is acceptable ONLY if you're truly waiting for external input

#### Using Next Activity Date in Governance

**In governance calls, leadership asks:**
- "What's the next activity on your red-status cards?"
- You answer: "Next activity is 1/20, when we're scheduling the SME kickoff meeting. Once we have their availability, we can finalize the training timeline."

This shows you have a plan to move forward, not stalled.

---

## III.F: Communication & Collaboration

### III.F.1: In-Card Communication (Teams Integration)

#### How In-Card Messaging Works

Every Planner card has a **Conversation** tab where you can leave comments.

This is **NOT for casual chat.** It's for:
- ✓ Project updates ("Training draft reviewed, approved by manager")
- ✓ Decisions ("Regional Service Model confirmed: Customer Pays + Included")
- ✓ Questions ("Can you clarify timeline for Service Procedures?")
- ✓ Escalations ("This is now at risk, need PM input")
- ✗ NOT for off-topic chat (use Teams channel for that)
- ✗ NOT for back-and-forth arguments (take to 1:1 call)

#### Posting a Comment

**Step 1: Open the card**
- Click card title to open detail view

**Step 2: Go to Conversation tab**
- Usually at top of card detail (next to Overview, Activity, etc.)

**Step 3: Click in message box**
- You'll see a text field at bottom: "Write a message..."

**Step 4: Type your comment**
- Be specific and professional
- If mentioning someone, use @ to tag them
- Example: "@Sarah Chen - Can you confirm the training date you mentioned?"

**Step 5: Click Send or Post**
- Comment is added to card's history
- Everyone watching this card gets notified
- If you @mentioned someone, they get pinged

#### Tagging People in Comments

**Use @ to mention specific people:**
1. Type @ in message
2. Start typing name: "@Sarah"
3. Dropdown shows matching people
4. Click to select
5. They get notified in Teams: "@[Your Name] mentioned you in [Card Name]"

**When to tag people:**
- ✓ Need their input or decision
- ✓ Asking them a direct question
- ✓ Assigning them a task or follow-up
- ✗ Just notifying (they get notified anyway)
- ✗ In discussions that don't need their input

#### Example Comments in Cards

**Good comment - Update with context:**
```
Week 3 Regional Alignment Update:

✓ Met with all service managers, confirmed regional service model
✓ Identified 15 locations that need training (vs. 10 estimated)
✓ Training timeline now 4 weeks vs. 3 weeks estimated

⚠️ One region (Malaysia) has director approval pending. Expecting approval by 1/24.

Next: Schedule regional SME kickoff for week of 2/3.

Status: On track (Yellow if Malaysia doesn't approve by 1/24)
```

**Good comment - Asking a question:**
```
@Rajesh Kumar - Can you confirm the regional training budget?

We've discovered 5 additional locations need training, which increases our estimate from $50K to $75K. Need approval to proceed with trainer hiring.

Can you confirm budget by 1/20?
```

**Good comment - Recording a decision:**
```
✅ DECISION MADE: Regional Service Model

After discussion with regional stakeholders, we've decided to offer:
- Included service (standard coverage)
- Customer Pays for additional support

This differs from original plan (which was Included only). Approved by Rajesh Kumar.

Impact: Requires additional training on service ordering process.
Timeline impact: +1 week for training materials development.
```

**Poor comment - Too vague:**
```
update: things are happening
```
(Unhelpful. What things? What's the impact? What's next?)

#### Notifications & Watching Cards

**How notifications work:**
- You're automatically notified of:
  - Someone assigns a task to you
  - Someone mentions you with @
  - Card moves to new bucket (if you enabled watching)
- You get email notification + Teams notification

**To watch a card (enable all notifications):**
1. Open the card
2. Look for a "Watch" or "Follow" option (usually near title)
3. Click to enable
4. Now you get notified of ALL changes to that card

**To stop watching:**
1. Open card
2. Click "Stop watching" or uncheck Watch
3. Notifications stop

---

### III.F.2: Planner in Teams Channel

#### How Planner Integrates with Teams

**The same board accessible two ways:**
1. **In Planner:** planner.cloud.microsoft.com (full board interface)
2. **In Teams:** Click **Planner** tab in your project channel (same board, Teams context)

**Using Planner in Teams:**
- Less full-featured than planner.cloud.microsoft.com
- But convenient if you're already in Teams
- Good for quick updates, checking status
- Full editing available (can create, move, update cards)

#### Setting Up Planner Tab in Teams

**If your project channel doesn't have a Planner tab:**
1. Go to project Teams channel
2. Click **+** (add tab)
3. Search for "Planner"
4. Click "Planner"
5. Select your board from dropdown
6. Click **Save**
7. Now **Planner** tab appears in your channel

#### Using Planner from Teams

**To work on cards from Teams:**
1. Click **Planner** tab in channel
2. Same board appears
3. You can:
   - Create new cards
   - Click cards to open and edit
   - Move cards between buckets (drag/drop)
   - Add comments
   - Update fields
4. All changes sync back to planner.cloud.microsoft.com

**When to use Planner in Teams vs. planner.cloud.microsoft.com:**
- **Use Teams Planner:** Quick check-in, discussion context matters
- **Use planner.cloud.microsoft.com:** Detailed editing, seeing multiple boards, reporting

---

### III.F.3: Escalation Paths (When to Ask for Help)

#### Escalation Decision Tree

```
I have a problem or question. Who do I ask?

Is it about MY assigned sub-task?
├─ YES, I don't understand what to do → Ask your Regional PM (or click card notes)
├─ YES, I'm blocked and need help → Ask your Regional PM
└─ YES, Technical issue with Planner → Ask IT Help Desk

Is it about the Regional Card (if you're Regional PM)?
├─ YES, Need guidance on what to do next → Ask your Main PM (1:1 call)
├─ YES, Team member not responding → Escalate to Regional Service Leader
├─ YES, Timeline is unrealistic → Escalate to Main PM + Regional Service Leader
└─ YES, Regional stakeholder won't commit → Escalate to Regional Service Leader

Is it about the Upstream Card (if you're Main PM)?
└─ YES, Any issue → Governance team or PMO contact

Is it a process question (how should we use Planner)?
└─ Ask your Regional PM or Main PM (if unclear, ask in Teams)

Is it a technical/system question (Planner not working)?
└─ Ask IT Help Desk

Is it a strategic question (do we proceed with this project)?
└─ Ask Regional Service Leader → Main PM → Leadership

```

#### Escalation Contacts & Methods

**Quick Questions:**
- **Who:** Your Regional PM
- **How:** Teams chat or quick call
- **Example:** "What custom field goes in here?" "Can I move this card yet?"
- **Timeline:** Response within 24 hours

**Blockers (Can't Proceed):**
- **Who:** Your Regional PM (immediately)
- **How:** Teams message OR email (mark urgent)
- **Example:** "Training SME just quit. We can't create training materials without them."
- **Timeline:** Response same day

**Timeline Issues (Might Miss Deadline):**
- **Who:** Regional PM + Regional Service Leader
- **How:** Governance call or urgent 1:1
- **Example:** "Regional launch timeline is now unrealistic. We need to reduce scope or push launch by 2 weeks."
- **Timeline:** Decision within 48 hours

**Stakeholder Issues (Team Member Not Cooperating):**
- **Who:** Regional Service Leader (your escalation point)
- **How:** 1:1 meeting or email
- **Example:** "Service manager won't assign people to training. They say they can't spare anyone. Blocking deliverables."
- **Timeline:** Leadership makes decision/intervention

**Technical Issues (Planner Not Working):**
- **Who:** IT Help Desk
- **How:** Help ticket with details
- **Example:** "Can't save changes to custom fields. Tried refreshing browser, cleared cache."
- **Timeline:** IT responds in 4 hours

#### How to Escalate Professionally

**Use this template:**

```
ISSUE: [One-sentence problem statement]

CONTEXT: [2-3 sentences on how we got here]

IMPACT: [Why this matters; what happens if not fixed]

PROPOSED SOLUTION: [What you think should happen]

TIMELINE: [When do we need decision/action]

QUESTIONS:
- [Specific question #1]
- [Specific question #2]

Escalated to: [Names of people copied]
```

**Example escalation:**

```
ISSUE: Regional Launch Date at Risk

CONTEXT: During Regional Alignment, we discovered 5 additional locations that weren't 
included in initial scope. This increases training from 2 weeks to 4 weeks. 

IMPACT: Regional launch date was 6/15. With 4-week training timeline, we're now at 6/29. 
This is 2 weeks later than global launch, and later than our customers expect.

PROPOSED SOLUTION: Either (a) Reduce training scope by 50%, or (b) Hire additional trainers 
to run parallel sessions and hit 6/15, or (c) Officially postpone regional launch to 6/29.

TIMELINE: Need decision by Friday (1/24) so we can notify stakeholders.

QUESTIONS:
- Is reducing scope acceptable?
- Is $50K budget available for additional trainers?
- Will customers accept 6/29 vs. 6/15 launch?

@Rajesh Kumar, @[Main PM name] - Need your input here.
```

**This escalation:**
- ✓ Is specific (not vague)
- ✓ Shows you've thought about solutions
- ✓ States impact clearly
- ✓ Has clear timeline for decision
- ✓ Identifies decision-makers

---

## III.G: Common Scenarios & How to Handle Them

### III.G.1: Scenario 1 — You're a Regional PM Creating Your First Regional Card

#### The Situation
You've just been assigned as Regional PM for India on the Calima project. Global Alignment is complete. It's time to create your regional card and start Regional Alignment.

#### Step-by-Step Solution

**Step 1: Get the Template**
- Email Main PM: "Hi, I'm the new Regional PM for India on Calima. Can you send me the regional card template?"
- They'll send you:
  - A sample regional card to use as reference
  - Or a spreadsheet with field definitions
  - Instructions on custom fields

**Step 2: Create Your Regional Card** (See Section III.C.1 for detailed steps)
- Title: "Calima - India - Regional Readiness"
- Assigned to: You
- Start date: When RA begins (discuss with Main PM)
- Due date: When regional launch target is (discuss with Regional Service Leader)
- Description: Copy template, customize for India specifics
- Custom fields: Fill all ⭐ fields (Planisware ID, Service Model, Complexity, etc.)

**Step 3: Ask Your Main PM for Planisware ID**
- Email: "I've created the India regional card. Can you provide the Planisware ID so I can complete the custom fields?"
- They'll give you something like: "SVC-0145-IN"
- Add this to the Planisware ID field

**Step 4: Create Sub-Tasks for Regional Deliverables** (See Section III.C.2)
- Training Plan, Training Materials, Service Procedures, etc.
- Assign to functional leads in India
- Set due dates based on your regional launch date

**Step 5: Notify Your Team**
- Post in Teams:
```
🎯 Regional Card Live: Calima - India

We're now starting Regional Alignment for Calima in India.

Card: "Calima - India - Regional Readiness"
Target Launch: [Your date]
Key Dates:
- Sub-task deliverables due: [X date]
- Regional Alignment complete: [Y date]
- Regional Kick-off: [Z date]

Please review your assigned sub-tasks and let me know if timelines are realistic.

Questions? Reach out or comment in Planner.
```

**Step 6: Schedule First Governance Call With Main PM**
- You'll have weekly governance calls
- First call: Discuss India-specific considerations (language, culture, resources, risks)
- Confirm timeline is realistic

**Result:** Your regional card is live, team knows what to do, and you're ready to start Regional Alignment phase.

---

### III.G.2: Scenario 2 — A Sub-Task Owner Isn't Responding

#### The Situation
You assigned Sarah (Training Manager) to "Create Training Plan - India" due 3/1. It's now 2/25 and she hasn't started or updated the sub-task. You're getting concerned.

#### Step-by-Step Solution

**Step 1: Send a Friendly Reminder (by 2/25)**
- Method: Teams direct message to Sarah
- Message:
```
Hi Sarah,

I noticed the "Create Training Plan - India" sub-task (due 3/1) hasn't been started yet. 
I wanted to check in and see if you need any support or clarification.

Do you have any blockers? Or questions about what the training plan should include?

Let me know if you need anything from me.

Thanks!
```
- Goal: Understand if she's stuck or just hasn't started

**Step 2: Wait for Response (24-48 hours)**
- If she responds with "I'll start this week" → Good, she's on track
- If she responds with a blocker → Help solve it (see Scenario 4)
- If she doesn't respond → Move to Step 3

**Step 3: Follow Up Directly (if no response by 2/27)**
- Method: Quick call or email (mark important)
- Message:
```
Hi Sarah,

Following up on the Training Plan sub-task that's due 3/1.

I haven't heard back from my previous message. Are you okay? Is there something I can help with?

Please let me know ASAP so we can keep the project on track.

Thanks!
```

**Step 4: Escalate to Her Manager (if still no response by 2/28)**
- One day before deadline, if not started
- Email to Sarah's manager:
```
Hi [Manager Name],

I wanted to let you know that Sarah is assigned to create the Training Plan for Calima India 
(due 3/1). The sub-task is showing as "Not Started" and I haven't been able to reach her.

Can you help ensure this gets prioritized? It's a critical path item.

Let me know if there's a resource conflict or other issue I should know about.

Thanks!
```

**Step 5: Contingency Plan (if deadline is missed)**
- If 3/1 arrives and Training Plan isn't done:
  - Mark sub-task as Red/Blocked
  - Add comment: "ESCALATION: Training Plan not completed by deadline. Waiting for Sarah to deliver."
  - Email Regional Service Leader: "Training Plan is now 2 days late, impacts timeline"
  - Make a decision: Can you extend the deadline? Do you need to reassign? Do you reduce scope?

**Result:** Either Sarah delivers, or you escalate to her manager so they can solve the resource issue. Either way, it's now visible and being managed, not hidden.

---

### III.G.3: Scenario 3 — Go-Live Date Just Got Moved Up

#### The Situation
Global launch was 6/15. Marketing just announced we need to launch on 5/15 (one month earlier) to hit a customer deadline.

Your team is now in jeopardy.

#### Step-by-Step Solution

**Step 1: Reality Check (Immediately)**
- Can you really deliver in 1 month?
- Talk to your Regional Service Leader: "Marketing moved the launch up. Can we actually do this?"
- Honest answer: "Probably not at current pace" or "Only if we cut scope"

**Step 2: Escalate to Main PM (Same Day)**
- Email with subject: "URGENT: Launch Date Changed to 5/15"
- Message:
```
Launch date for Calima has been moved from 6/15 to 5/15 (one month earlier).

Current status:
- Regional Alignment: 30% complete (not done)
- Training materials: Not started
- Service procedures: Not started

Can we hit 5/15? 

Options:
1. Reduce training scope (train only critical staff, phase in rest later)
2. Hire additional trainers to run parallel sessions (cost $50K)
3. Postpone launch back to 6/15 (need customer approval)
4. Some combination

Can we get together tomorrow to discuss?
```

**Step 3: Update Card Timeline**
- Update "Launch Date (Regional)" from 6/15 to 5/15
- Update sub-task due dates to move forward by 1 month
- Add comment: "Launch date changed from 6/15 to 5/15 per marketing request. Assessing feasibility."

**Step 4: Status Change to Red/Blocked**
- Change Risk Status to Red (timeline now at risk)
- Add comment explaining the change

**Step 5: Escalate to Governance**
- If you have a governance call coming up, put this on the agenda
- If not, request an emergency call
- Leadership needs to decide: Scope cut? Budget increase? Or postpone?

**Step 6: Communicate to Your Team**
- Post in Teams:
```
⚠️ Timeline Update: Calima Launch Moved Up

Marketing has moved the global launch from 6/15 to 5/15.

This impacts our regional readiness timeline significantly.

We're currently assessing what's possible and what trade-offs we need to make.

More details coming in a team meeting tomorrow.

Please hold your calendars and be ready to discuss scope/resource options.
```

**Result:** Leadership is aware, timeline is updated in Planner, and team knows something has changed. You're not trying to silently absorb a one-month acceleration.

---

### III.G.4: Scenario 4 — You Discovered a Missing Requirement

#### The Situation
You're in Kick-off phase and just discovered that the regional service model requires a new certification that no one has. There's no way to train on it in time for launch.

#### Step-by-Step Solution

**Step 1: Confirm the Issue (Don't Assume)**
- Verify: Is this certification really required?
- Ask: "Can we launch without this certification temporarily?"
- Check: "Is there a workaround?" (Online module, phased implementation, etc.)

**Step 2: Create a Sub-Task for This Issue**
- Add new sub-task: "Urgent: [Certification Name] Requirement"
- Assign to: Yourself and Regional Service Leader
- Due: TODAY (this is urgent)
- Description: "Missing requirement discovered. Need urgent decision on approach."

**Step 3: Escalate Immediately**
- Don't wait for governance call
- Email Regional Service Leader:
```
URGENT: Missing Requirement Discovered

During Kick-off prep, we discovered that [Service Model] requires [Certification].

Current situation:
- No staff currently certified
- Training takes 4 weeks
- Launch is 3 weeks away
- Can't hit deadline at current pace

Options:
1. Get exemption from certification requirement (check if possible)
2. Hire already-certified contractor (time to recruit?)
3. Train fast-track module (compressed, lower quality?)
4. Delay regional launch by 4 weeks
5. Launch with limited service (exclude service that requires certification)

Can we discuss today? This is blocking our launch.
```

**Step 4: Update Card Risk Status**
- Set to Red or Blocked
- Add comment: "CRITICAL: Missing certification requirement discovered in Kick-off. Assessing options, need decision by [date]."

**Step 5: Don't Hide It**
- This WILL come back as a problem on launch day if not solved
- Better to surface it now with options than to launch unprepared

**Step 6: Make a Decision & Execute**
- Leadership decides: Which of the 5 options do we choose?
- You execute that decision immediately
- Update card with decision: "Leadership decision: [Option chosen]. Executing [Action]."

**Result:** Problem identified early, escalated appropriately, decision made at leadership level, execution planned. This is the NPI process working as designed.

---

## III.H: Quick Reference Checklists (Printable)

### III.H.1: Daily Task Checklist

Print this and do it every morning.

```
☐ Check My Tasks view for new assignments
☐ Scan for RED/BLOCKED cards (anything needing urgent attention)
☐ Click each red card and read recent comments
☐ Update status on cards assigned to me (if changed)
☐ Add comment if there's significant progress to report
☐ Check for @mentions from teammates
☐ Respond to any questions or requests

Time investment: 5-10 minutes
```

### III.H.2: Weekly Task Checklist

Do this every Friday afternoon (before governance calls).

```
☐ Open all MY cards (filter by "Assigned to me")
☐ For each card:
  ☐ Is status still accurate? (On track/At risk/Blocked)
  ☐ Has anything changed since last week?
  ☐ What's the next action?
  ☐ Update "Next Activity Date" field with next planned date
☐ Check all sub-tasks under my cards:
  ☐ Any due this coming week? (Follow up with owner)
  ☐ Any overdue? (Escalate)
  ☐ Any completed? (Celebrate, verify quality)
☐ Add a status comment to each card summarizing week:
  ✓ What got done
  ⚠️ What's at risk
  ⏭️ What's coming next

Time investment: 30-45 minutes
Result: You're ready for governance calls with complete status information
```

### III.H.3: Phase Gate Checklist (Before Moving Card to Next Bucket)

Use this before you move ANY card to a new bucket.

```
✓ REQUIRED FIELDS: All ⭐ custom fields are filled
  ☐ Planisware ID (or note when it's coming)
  ☐ Service Model
  ☐ Complexity Rating
  ☐ Launch Date
  ☐ Playbook Status
  ☐ Risk Status
  ☐ Stakeholder Contact

✓ DELIVERABLES: All sub-tasks for THIS phase are complete (or well-underway)
  ☐ List expected deliverables: _______________
  ☐ Are they all started? ☐ Yes ☐ Mostly ☐ No (don't move if No)
  ☐ Are critical ones at least 80% done? ☐ Yes ☐ No (don't move if No)

✓ NO CRITICAL BLOCKERS: Nothing preventing next phase
  ☐ Are there any open Red or Blocked issues? ☐ Yes ☐ No
  ☐ If Yes, can they be resolved quickly? ☐ Yes ☐ No (don't move if No)

✓ STAKEHOLDER APPROVAL: Key stakeholders have signed off
  ☐ Regional Service Leader approval? ☐ Yes ☐ No ☐ Not needed
  ☐ Main PM approval? ☐ Yes ☐ No ☐ Not needed
  ☐ Functional leads approval (if needed)? ☐ Yes ☐ No ☐ Not needed

✓ TIMELINE REALISTIC: Next phase's timeline is achievable
  ☐ Do we have resources for next phase? ☐ Yes ☐ Probably ☐ No
  ☐ Is timeline aggressive but doable? ☐ Yes ☐ Risky ☐ No (don't move if No)
  ☐ Have we factored in holidays/time off? ☐ Yes ☐ No (don't move if No)

✓ READY TO MOVE: All above checked and answers are YES/Good
  ☐ Add a comment explaining the move
  ☐ Move the card
  ☐ Notify team in Teams channel
```

---

**End of User Pathway Section (III.A - III.H)**

This completes the comprehensive User Pathway guide with all step-by-step procedures, scenarios, checklists, and best practices.
