import os
import math
from PIL import Image, ImageDraw, ImageFont

# Brand color palette (Connex / Roy's brand)
NAVY = (15, 27, 45)      # #0F1B2D (Canvas Background)
DARK_BLUE = (22, 37, 59)  # #16253B (Card Background)
TEAL = (0, 134, 155)      # #00869B (Primary Accents / Happy path / Agent borders)
GOLD = (192, 158, 90)     # #C09E5A (Highlights / Sandbox / Release borders)
WHITE = (255, 255, 255)
LIGHT_GRAY = (142, 156, 174) # #8E9CAE (Calibri body text)
CRIMSON = (211, 47, 47)    # #D32F2F (Audit/Test failures - re-routing)
SUCCESS_GREEN = (0, 150, 136) # #009688

# Setup paths for Windows system fonts
FONT_TITLE_PATH = "C:/Windows/Fonts/georgiab.ttf"
FONT_HEADER_PATH = "C:/Windows/Fonts/georgiab.ttf"
FONT_BODY_PATH = "C:/Windows/Fonts/calibri.ttf"
FONT_BODY_BOLD_PATH = "C:/Windows/Fonts/calibrib.ttf"

# Create Canvas
canvas_width = 1600
canvas_height = 1000
image = Image.new("RGB", (canvas_width, canvas_height), NAVY)
draw = ImageDraw.Draw(image)

# Load Fonts with fallbacks
try:
    font_title = ImageFont.truetype(FONT_TITLE_PATH, 38)
    font_subtitle = ImageFont.truetype(FONT_BODY_PATH, 18)
    font_card_header = ImageFont.truetype(FONT_HEADER_PATH, 18)
    font_card_body = ImageFont.truetype(FONT_BODY_PATH, 14)
    font_card_body_bold = ImageFont.truetype(FONT_BODY_BOLD_PATH, 14)
    font_label = ImageFont.truetype(FONT_BODY_PATH, 13)
    font_label_bold = ImageFont.truetype(FONT_BODY_BOLD_PATH, 13)
    font_legend = ImageFont.truetype(FONT_BODY_PATH, 14)
except IOError:
    # Fallback to default
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_card_header = ImageFont.load_default()
    font_card_body = ImageFont.load_default()
    font_card_body_bold = ImageFont.load_default()
    font_label = ImageFont.load_default()
    font_label_bold = ImageFont.load_default()
    font_legend = ImageFont.load_default()

# Header Rendering
draw.text((80, 50), "THE AI COUNCIL CONSENSUS PROTOCOL", fill=GOLD, font=font_title)
draw.text((80, 105), "Multi-Agent Autonomous Pipeline & Quality Gates for Production-Grade Code", fill=LIGHT_GRAY, font=font_subtitle)

# Helper function to draw text with word wrapping or list items
def draw_card_contents(draw, x, y, title, bullets, border_color):
    card_w, card_h = 240, 250
    # Card Background
    draw.rounded_rectangle(
        [(x, y), (x + card_w, y + card_h)],
        radius=12,
        fill=DARK_BLUE,
        outline=border_color,
        width=2
    )
    
    # Title
    draw.text((x + 20, y + 20), title, fill=WHITE, font=font_card_header)
    # Divider line
    draw.line([(x + 20, y + 55), (x + card_w - 20, y + 55)], fill=border_color, width=1)
    
    # Bullet points
    current_y = y + 70
    for bullet in bullets:
        # Check if we should bold the prefix before the colon
        if ":" in bullet:
            parts = bullet.split(":", 1)
            prefix = parts[0] + ":"
            suffix = parts[1]
            draw.text((x + 20, current_y), prefix, fill=GOLD if border_color == GOLD else TEAL, font=font_card_body_bold)
            # Calculate offset of prefix
            prefix_w = draw.textlength(prefix, font=font_card_body_bold)
            draw.text((x + 20 + prefix_w + 4, current_y), suffix, fill=LIGHT_GRAY, font=font_card_body)
        else:
            draw.text((x + 20, current_y), bullet, fill=LIGHT_GRAY, font=font_card_body)
        current_y += 35

# Card Data Definition
cards = [
    # Column 0
    {
        "id": "OP", "col": 0, "row": 0,
        "title": "OPERATOR (YOU)", "border": TEAL,
        "bullets": [
            "Input: Submit Prompt",
            "Target: Done-When Criteria",
            "Monitor: Consensus Logs",
            "Role: Human-in-the-Loop"
        ]
    },
    # Column 1
    {
        "id": "PM", "col": 1, "row": 0,
        "title": "PRODUCT MANAGER", "border": TEAL,
        "bullets": [
            "Input: User Instructions",
            "Output: Feature Spec",
            "Specs: EARS Requirements",
            "Gate: Define Done-When"
        ]
    },
    # Column 2
    {
        "id": "ENG", "col": 2, "row": 0,
        "title": "LEAD ENGINEER", "border": TEAL,
        "bullets": [
            "Input: Feature Spec",
            "Action: Code Scaffolding",
            "Paradigm: TDD & Types",
            "Target: Write Sandbox Tests"
        ]
    },
    # Column 3
    {
        "id": "SEC", "col": 3, "row": 0,
        "title": "SECURITY OFFICER", "border": TEAL,
        "bullets": [
            "Audit: 5 Security Rules",
            "Checks: SQLi, Secrets, Auth",
            "Filter: Verify Inputs",
            "Action: Approve / Reject"
        ]
    },
    # Column 3, Row 1
    {
        "id": "QA", "col": 3, "row": 1,
        "title": "QA LEAD", "border": TEAL,
        "bullets": [
            "Action: Build Compilation",
            "Execution: Run Test Suite",
            "Analysis: Stack Traces",
            "Verify: Benchmarks & RTT"
        ]
    },
    # Column 2, Row 1
    {
        "id": "SANDBOX", "col": 2, "row": 1,
        "title": "ISOLATION SANDBOX", "border": GOLD,
        "bullets": [
            "Env: scratch/ Directory",
            "Scope: One concern per fn",
            "State: No side effects",
            "Testing: Real execution logs"
        ]
    },
    # Column 1, Row 1
    {
        "id": "TW", "col": 1, "row": 1,
        "title": "TECHNICAL WRITER", "border": TEAL,
        "bullets": [
            "Input: Passed Sandbox Code",
            "Output: walkthrough.md",
            "Docs: API & Setup Guides",
            "Links: Clickable relative path"
        ]
    },
    # Column 0, Row 1
    {
        "id": "REL", "col": 0, "row": 1,
        "title": "VERIFIED RELEASE", "border": GOLD,
        "bullets": [
            "Status: VERIFIED Release",
            "Promote: Deploy to Prod",
            "Git: Stage, Commit, Push",
            "Log: Append-only History"
        ]
    }
]

# Grid Configuration
col_x = [80, 440, 800, 1160]
row_y = [180, 560]

# Render Cards
card_coords = {}
for card in cards:
    x = col_x[card["col"]]
    y = row_y[card["row"]]
    draw_card_contents(draw, x, y, card["title"], card["bullets"], card["border"])
    card_coords[card["id"]] = (x, y)

# Helper function to draw lines with arrows
def draw_arrow(draw, start, end, color, width=2, head_size=10, double_ended=False):
    draw.line([start, end], fill=color, width=width)
    x1, y1 = start
    x2, y2 = end
    
    # Calculate arrowhead at end
    angle = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head_size * math.cos(angle - math.pi/6), y2 - head_size * math.sin(angle - math.pi/6))
    p2 = (x2 - head_size * math.cos(angle + math.pi/6), y2 - head_size * math.sin(angle + math.pi/6))
    draw.polygon([end, p1, p2], fill=color)
    
    if double_ended:
        angle_rev = angle + math.pi
        p1_rev = (x1 - head_size * math.cos(angle_rev - math.pi/6), y1 - head_size * math.sin(angle_rev - math.pi/6))
        p2_rev = (x1 - head_size * math.cos(angle_rev + math.pi/6), y1 - head_size * math.sin(angle_rev + math.pi/6))
        draw.polygon([start, p1_rev, p2_rev], fill=color)

# Draw Labels on arrows
def draw_label(draw, text, pos, bg_color=NAVY, fg_color=LIGHT_GRAY, bold=False):
    font_to_use = font_label_bold if bold else font_label
    text_w = draw.textlength(text, font=font_to_use)
    text_h = 14
    x, y = pos
    # Draw background box for text legibility
    draw.rectangle([(x - text_w/2 - 4, y - text_h/2 - 2), (x + text_w/2 + 4, y + text_h/2 + 2)], fill=bg_color)
    # Draw text centered
    draw.text((x - text_w/2, y - text_h/2 - 2), text, fill=fg_color, font=font_to_use)

# 1. Operator -> PM (Horizontal happy path)
draw_arrow(draw, (320, 305), (440, 305), TEAL, width=3)
draw_label(draw, "1. Instruction", (380, 305), fg_color=WHITE)

# 2. PM -> ENG (Horizontal happy path)
draw_arrow(draw, (680, 305), (800, 305), TEAL, width=3)
draw_label(draw, "2. Spec Checklist", (740, 305), fg_color=WHITE)

# 3. ENG -> SEC (Horizontal happy path)
draw_arrow(draw, (1040, 305), (1160, 305), TEAL, width=3)
draw_label(draw, "3. Submit Audit", (1100, 305), fg_color=WHITE)

# 4. SEC -> QA (Vertical happy path down)
draw_arrow(draw, (1280, 430), (1280, 560), TEAL, width=3)
draw_label(draw, "4. Promote (Pass)", (1280, 495), fg_color=WHITE)

# 5. QA -> Sandbox (Horizontal happy path left)
draw_arrow(draw, (1160, 685), (1040, 685), TEAL, width=3)
draw_label(draw, "5. Run Tests", (1100, 685), fg_color=WHITE)

# 6. Sandbox -> TW (Horizontal happy path left)
draw_arrow(draw, (800, 685), (440, 685), TEAL, width=3)
draw_label(draw, "6. Documentation Promotion (Pass)", (620, 685), fg_color=WHITE)

# 7. TW -> REL (Horizontal happy path left)
draw_arrow(draw, (440, 685), (320, 685), TEAL, width=3)
draw_label(draw, "7. Stage Walkthrough", (380, 685), fg_color=WHITE)

# 8. REL -> Operator (Done! Vertical up arrow)
draw_arrow(draw, (200, 560), (200, 430), SUCCESS_GREEN, width=3)
draw_label(draw, "8. VERIFIED", (200, 495), fg_color=GOLD, bold=True)

# Loop: ENG -> Sandbox (Initial Sandbox Scaffolding)
draw_arrow(draw, (920, 430), (920, 560), GOLD, width=2)
draw_label(draw, "Prototype", (920, 495), fg_color=GOLD)

# Re-routing paths (Fails gates)
# 9. SEC -> ENG (Security Reject loop back)
# Draw arched path using multiple lines
draw.line([(1280, 180), (1280, 140), (920, 140), (920, 180)], fill=CRIMSON, width=2)
draw_arrow(draw, (920, 140), (920, 180), CRIMSON, width=2)
draw_label(draw, "REJECT (Security Fail)", (1100, 140), fg_color=CRIMSON, bold=True)

# 10. QA -> ENG (QA Test Suite Reject loop back)
# Diagonal line QA -> ENG
draw_arrow(draw, (1160, 560), (1040, 430), CRIMSON, width=2)
draw_label(draw, "REJECT (Test Fail)", (1090, 480), fg_color=CRIMSON, bold=True)


# Footer/Legend Section
legend_y = 870
draw.rectangle([(80, legend_y), (1520, legend_y + 80)], fill=DARK_BLUE, outline=GOLD, width=1)

# Legend Items
# Item 1: Happy Path
draw.line([(120, legend_y + 40), (180, legend_y + 40)], fill=TEAL, width=3)
draw_arrow(draw, (120, legend_y + 40), (180, legend_y + 40), TEAL, width=3)
draw.text((200, legend_y + 32), "Happy Path / Spec Execution Flow", fill=WHITE, font=font_legend)

# Item 2: Failure Re-route
draw.line([(550, legend_y + 40), (610, legend_y + 40)], fill=CRIMSON, width=2)
draw_arrow(draw, (550, legend_y + 40), (610, legend_y + 40), CRIMSON, width=2)
draw.text((630, legend_y + 32), "Audit Gate Failure / Code Re-route", fill=WHITE, font=font_legend)

# Item 3: Sandbox/Verified Boundaries
draw.rectangle([(980, legend_y + 30), (1010, legend_y + 50)], outline=GOLD, width=2)
draw.text((1030, legend_y + 32), "Isolation Sandbox & Production Release Gates", fill=WHITE, font=font_legend)

# Infrastructure disclosure info
infra_text = "System: Vibe Coding Pro • Isolated Process Sandboxing • Local SQLite Verification"
draw.text((80, 965), infra_text, fill=LIGHT_GRAY, font=font_subtitle)

# Save image
output_path = "C:/Users/roych/OneDrive/Pictures/Vibe coding/ai_council_architecture.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
image.save(output_path, "PNG")
print("SUCCESS: Image generated at", output_path)
