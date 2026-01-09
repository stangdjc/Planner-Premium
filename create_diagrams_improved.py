#!/usr/bin/env python3
"""
Create improved professional diagrams with enhanced line rendering
Fixes: Line formatting, arrow quality, connection smoothness
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.lines as mlines
import numpy as np

# Medtronic Brand Colors
COLORS = {
    'deepNavy': '#140F4B',
    'primaryBlue': '#1010EB',
    'charcoal': '#3C3C3C',
    'cyan': '#0FC9F7',
    'teal': '#00DCB9',
    'orange': '#FFAD00',
    'red': '#ED002A',
    'lightGray': '#F5F5F5',
    'white': '#FFFFFF'
}

def set_figure_style(fig, ax):
    """Configure figure with professional styling"""
    fig.patch.set_facecolor(COLORS['white'])
    ax.set_facecolor(COLORS['white'])
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # Remove axes
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

def draw_rounded_box(ax, x, y, width, height, color, text, text_color='white', text_size=10):
    """Draw a rounded rectangle box with text"""
    # Use FancyBboxPatch for professional rounded corners
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.1",
                         edgecolor='none',
                         facecolor=color,
                         linewidth=2,
                         antialiased=True)
    ax.add_patch(box)

    # Add text
    ax.text(x, y, text, ha='center', va='center',
            fontsize=text_size, fontweight='bold',
            color=text_color, family='sans-serif',
            wrap=True)

def draw_diamond(ax, x, y, width, height, color, text, text_color='white', text_size=9):
    """Draw a diamond shape (decision point)"""
    diamond = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                     boxstyle="round,pad=0.05",
                                     edgecolor='none',
                                     facecolor=color,
                                     linewidth=2,
                                     antialiased=True)
    ax.add_patch(diamond)

    ax.text(x, y, text, ha='center', va='center',
            fontsize=text_size, fontweight='bold',
            color=text_color, family='sans-serif')

def draw_arrow(ax, x1, y1, x2, y2, color, width=0.08, style='->'):
    """Draw smooth arrow with anti-aliasing"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle=style,
                           color=color,
                           linewidth=width,
                           mutation_scale=20,
                           antialiased=True,
                           linestyle='-',
                           zorder=1)
    ax.add_patch(arrow)

def draw_curved_arrow(ax, x1, y1, x2, y2, color, width=0.08, curve=0.3):
    """Draw curved arrow for feedback loops"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           connectionstyle=f"arc3,rad={curve}",
                           arrowstyle='->',
                           color=color,
                           linewidth=width,
                           mutation_scale=20,
                           antialiased=True,
                           linestyle='-',
                           zorder=1)
    ax.add_patch(arrow)

def add_text_label(ax, x, y, text, color=COLORS['charcoal'], size=8):
    """Add descriptive text label"""
    ax.text(x, y, text, ha='center', va='top',
            fontsize=size, color=color, family='sans-serif',
            style='italic')

# ============================================================================
# DIAGRAM 1: NPI Lifecycle Process Flow
# ============================================================================
def create_npi_lifecycle():
    """Create NPI Lifecycle with improved rendering"""
    fig, ax = plt.subplots(figsize=(14, 6), dpi=300)
    set_figure_style(fig, ax)

    # Phase boxes
    phases = [
        (1, 5, 'Pipeline', COLORS['deepNavy']),
        (2, 5, 'GA', COLORS['primaryBlue']),
        (3, 5, 'RA', COLORS['primaryBlue']),
        (4, 5, 'Engage', COLORS['primaryBlue']),
        (5, 5, 'Kick-off', COLORS['cyan']),
        (6, 5, 'Execute', COLORS['teal']),
        (7, 5, 'Hypercare', COLORS['orange']),
        (8, 5, 'Close-out', COLORS['charcoal']),
    ]

    for x, y, label, color in phases:
        draw_rounded_box(ax, x, y, 0.9, 0.8, color, label, text_size=9)

    # Forward arrows
    for i in range(len(phases) - 1):
        x1, y1 = phases[i][0] + 0.45, phases[i][1]
        x2, y2 = phases[i+1][0] - 0.45, phases[i+1][1]
        draw_arrow(ax, x1, y1, x2, y2, COLORS['deepNavy'], width=0.06)

    # Feedback loop
    draw_curved_arrow(ax, 8.45, 4.5, 0.55, 4.5, COLORS['red'], width=0.06, curve=-0.5)
    add_text_label(ax, 4.5, 3.8, 'Issues/Changes', COLORS['red'], 8)

    # Title
    ax.text(4.5, 6.5, 'NPI Lifecycle Process Flow', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_01_npi_lifecycle.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: NPI Lifecycle Process Flow")

# ============================================================================
# DIAGRAM 2: Card Hierarchy
# ============================================================================
def create_card_hierarchy():
    """Create 3-level card hierarchy with improved lines"""
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    set_figure_style(fig, ax)

    # Level 1: Upstream Card
    draw_rounded_box(ax, 5, 8, 2.5, 0.7, COLORS['deepNavy'],
                     'Upstream Card\n(Project Level)', text_size=10)

    # Connecting lines to Level 2
    draw_arrow(ax, 3.5, 7.65, 2.5, 6.8, COLORS['primaryBlue'], width=0.05)
    draw_arrow(ax, 5, 7.65, 5, 6.8, COLORS['primaryBlue'], width=0.05)
    draw_arrow(ax, 6.5, 7.65, 7.5, 6.8, COLORS['primaryBlue'], width=0.05)

    # Level 2: Regional Cards
    regions = [
        (2.5, 6.3, 'Singapore\nRegional Card'),
        (5, 6.3, 'North America\nRegional Card'),
        (7.5, 6.3, 'Europe\nRegional Card')
    ]

    for x, y, label in regions:
        draw_rounded_box(ax, x, y, 1.8, 0.8, COLORS['primaryBlue'], label, text_size=9)

    # Level 3: Sub-tasks under each region
    subtask_sets = [
        [(1.2, 5), (2.5, 5), (3.8, 5)],  # Singapore
        [(3.7, 5), (5, 5), (6.3, 5)],    # North America
        [(6.2, 5), (7.5, 5), (8.8, 5)]   # Europe
    ]

    subtask_colors = [COLORS['cyan'], COLORS['teal'], COLORS['orange']]

    for region_idx, subtasks in enumerate(subtask_sets):
        # Draw connecting arrows
        region_x = regions[region_idx][0]
        draw_arrow(ax, region_x - 0.4, 5.8, subtasks[0][0], 5.3, COLORS['charcoal'], width=0.04)
        draw_arrow(ax, region_x, 5.8, subtasks[1][0], 5.3, COLORS['charcoal'], width=0.04)
        draw_arrow(ax, region_x + 0.4, 5.8, subtasks[2][0], 5.3, COLORS['charcoal'], width=0.04)

        # Draw sub-task boxes
        for idx, (x, y) in enumerate(subtasks):
            tasks = ['Training', 'Service', 'Ops']
            draw_rounded_box(ax, x, y, 1, 0.6, subtask_colors[region_idx],
                           tasks[idx], text_color='white', text_size=8)

    # Title
    ax.text(5, 9.3, 'Card Hierarchy: Three-Level Structure', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    # Legend
    ax.text(0.5, 3, 'Level 1: One Upstream card per project', fontsize=8, color=COLORS['charcoal'])
    ax.text(0.5, 2.6, 'Level 2: One Regional card per region', fontsize=8, color=COLORS['charcoal'])
    ax.text(0.5, 2.2, 'Level 3: Sub-tasks for deliverables', fontsize=8, color=COLORS['charcoal'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_02_card_hierarchy.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: Card Hierarchy")

# ============================================================================
# DIAGRAM 3: Phase Gate Decision Tree
# ============================================================================
def create_phase_gate_decision():
    """Create phase gate decision tree with improved arrows"""
    fig, ax = plt.subplots(figsize=(13, 9), dpi=300)
    set_figure_style(fig, ax)

    # Start
    draw_rounded_box(ax, 5, 8.5, 1.5, 0.6, COLORS['deepNavy'], 'Ready to Progress?', text_size=9)

    # Decision diamonds (quality checks)
    checks = [
        (1.5, 7, 'Required\nFields?'),
        (3.5, 7, 'Deliverables\nDone?'),
        (5.5, 7, 'Blockers\nResolved?'),
        (7.5, 7, 'Approval\nGot?'),
        (9, 7, 'Timeline\nOK?'),
    ]

    for x, y, text in checks:
        draw_diamond(ax, x, y, 1.2, 0.9, COLORS['primaryBlue'], text, text_size=8)

    # Arrows from start to checks
    y_from = 8.2
    for i, (x, y, _) in enumerate(checks):
        draw_arrow(ax, 4.3 + (i * 0.7), y_from, x, 7.4, COLORS['charcoal'], width=0.04)

    # Decision paths
    x_positions = [1.5, 3.5, 5.5, 7.5, 9]
    for x in x_positions:
        # No arrow (down-left)
        draw_curved_arrow(ax, x - 0.4, 6.5, 2, 5, COLORS['red'], width=0.04, curve=0.2)
        # Yes arrow continues right
        if x < 9:
            draw_arrow(ax, x + 0.6, 7, x + 1.3, 7, COLORS['teal'], width=0.04)

    # Final decision box
    draw_rounded_box(ax, 9.5, 5, 1.5, 0.7, COLORS['teal'], 'READY TO\nMOVE PHASE', text_size=9)
    draw_arrow(ax, 9, 6.7, 9.5, 5.35, COLORS['teal'], width=0.05)

    # Block/Escalate box
    draw_rounded_box(ax, 2, 4.5, 1.8, 0.7, COLORS['red'], 'BLOCKED -\nEscalate', text_color='white', text_size=9)

    # Title
    ax.text(5, 9.5, 'Phase Gate Decision Tree', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_03_phase_gate_decision.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: Phase Gate Decision Tree")

# ============================================================================
# DIAGRAM 4: Escalation Decision Tree
# ============================================================================
def create_escalation_decision():
    """Create escalation decision tree"""
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    set_figure_style(fig, ax)

    # Root decision
    draw_rounded_box(ax, 5, 8.5, 1.8, 0.7, COLORS['deepNavy'], 'Need to Escalate?', text_size=10)

    # 5 escalation paths
    escalations = [
        (0.8, 6.8, 'My Sub-task\nBlocked', COLORS['orange']),
        (2.5, 6.8, 'Team Member\nNot Responding', COLORS['orange']),
        (4.2, 6.8, 'Timeline\nUnrealistic', COLORS['orange']),
        (5.9, 6.8, 'Tool Not\nWorking', COLORS['orange']),
        (7.6, 6.8, 'Strategic\nDecision Needed', COLORS['orange']),
    ]

    for x, y, label, color in escalations:
        draw_rounded_box(ax, x, y, 1.3, 0.8, color, label, text_size=8)
        draw_arrow(ax, 4.2 + (x-3.5), 8.1, x, 7.2, COLORS['charcoal'], width=0.04)

    # Escalation contacts and response times
    contacts = [
        (0.8, 5.8, 'Regional PM\n(24 hrs)', COLORS['teal']),
        (2.5, 5.8, 'Service Leader\n(48 hrs)', COLORS['teal']),
        (4.2, 5.8, 'Main PM\n(24 hrs)', COLORS['teal']),
        (5.9, 5.8, 'IT Support\n(2 hrs)', COLORS['cyan']),
        (7.6, 5.8, 'Exec Sponsor\n(48 hrs)', COLORS['teal']),
    ]

    for x, y, label, color in contacts:
        draw_rounded_box(ax, x, y, 1.3, 0.9, color, label, text_size=8)
        for ex_x, ex_y, _, _ in escalations:
            if abs(ex_x - x) < 0.1:
                draw_arrow(ax, x, ex_y - 0.4, x, y + 0.45, COLORS['charcoal'], width=0.04)

    # Title
    ax.text(5, 9.5, 'Escalation Decision Tree & Contact Matrix', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_04_escalation_tree.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: Escalation Decision Tree")

# ============================================================================
# DIAGRAM 5: System Integration Architecture
# ============================================================================
def create_system_integration():
    """Create system integration with improved arrow rendering"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    set_figure_style(fig, ax)

    # Central system
    draw_rounded_box(ax, 5, 5, 2.2, 1, COLORS['primaryBlue'],
                     'PLANNER\nPREMIUM\n(Source of Truth)', text_size=11)

    # Peripheral systems
    systems = [
        (1.5, 7.5, 'PLANISWARE', COLORS['deepNavy'], 'Planisware ID,\nStatus, Dates,\nResources'),
        (8.5, 7.5, 'TEAMS', COLORS['teal'], 'Notifications,\nComments,\nReal-time'),
        (5, 2, 'SHAREPOINT', COLORS['cyan'], 'Documents,\nFolders,\nReferences'),
        (1.5, 2.5, 'NPI PLAYBOOK', COLORS['orange'], 'Process Docs,\nSection Tracking,\nGovernance'),
    ]

    for x, y, label, color, description in systems:
        draw_rounded_box(ax, x, y, 1.6, 0.8, color, label, text_size=9)

    # Connection lines with labels
    connections = [
        ((1.5, 7.1), (3.5, 5.5), 'Fully', COLORS['charcoal']),
        ((8.5, 7.1), (6.5, 5.5), 'Real-time', COLORS['charcoal']),
        ((5, 2.8), (5, 4.5), 'Document Links,\nFolder URLs', COLORS['charcoal']),
        ((2.3, 2.9), (4, 4.7), 'Process tracking', COLORS['charcoal']),
    ]

    for (x1, y1), (x2, y2), label, color in connections:
        draw_arrow(ax, x1, y1, x2, y2, color, width=0.04)
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        add_text_label(ax, mid_x + 0.3, mid_y + 0.3, label, color, 7)

    # Integration points box
    ax.text(0.5, 0.8, 'INTEGRATION POINTS:', fontsize=10, fontweight='bold', color=COLORS['deepNavy'])
    ax.text(0.5, 0.4, '• Planisware: Financial tracking, resource costing, project-level data', fontsize=7, color=COLORS['charcoal'])
    ax.text(0.5, 0.1, '• Teams: Communication, notifications, team messaging within cards', fontsize=7, color=COLORS['charcoal'])

    ax.text(5, 0.4, '• SharePoint: Document storage, project folders, reference materials', fontsize=7, color=COLORS['charcoal'])
    ax.text(5, 0.1, '• Playbook: Process documentation, section tracking, governance', fontsize=7, color=COLORS['charcoal'])

    # Title
    ax.text(5, 9, 'System Integration Architecture', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_05_system_integration.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: System Integration Architecture")

# ============================================================================
# DIAGRAM 6: Organizational Roles & Responsibilities
# ============================================================================
def create_roles_matrix():
    """Create roles and responsibilities matrix"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    set_figure_style(fig, ax)

    # Roles
    roles = [
        (1.5, 7, 'MAIN PM', COLORS['deepNavy'], [
            'Global project owner',
            'Define global timeline',
            'Phase gate approvals',
            'Executive reporting'
        ]),
        (4, 7, 'REGIONAL PM', COLORS['primaryBlue'], [
            'Regional ownership',
            'Regional team management',
            'Regional reporting',
            'Service leader alignment'
        ]),
        (6.5, 7, 'SME', COLORS['teal'], [
            'Functional expertise',
            'Task execution',
            'Quality assurance',
            'Team coordination'
        ]),
        (9, 7, 'SERVICE LEADER', COLORS['orange'], [
            'Resource approval',
            'Regional readiness',
            'Stakeholder alignment',
            'Risk escalation'
        ]),
    ]

    for x, y, role_name, color, responsibilities in roles:
        draw_rounded_box(ax, x, y, 2, 1.2, color, role_name, text_size=10)

        # Add responsibilities below
        for i, resp in enumerate(responsibilities):
            ax.text(x, y - 1.5 - (i * 0.4), f'• {resp}', fontsize=7,
                   ha='center', color=COLORS['charcoal'], wrap=True)

    # Title
    ax.text(5, 9, 'Organizational Roles & Responsibilities', ha='center', va='bottom',
            fontsize=14, fontweight='bold', color=COLORS['deepNavy'])

    plt.tight_layout(pad=0.5)
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_06_roles_matrix.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['white'])
    plt.close()
    print("✅ Created: Organizational Roles Matrix")

# ============================================================================
# MAIN EXECUTION
# ============================================================================
def main():
    print("\n🎨 Generating Improved Professional Diagrams...\n")
    print("Enhancement Focus:")
    print("  • Better anti-aliasing for all lines")
    print("  • Smooth arrow rendering")
    print("  • Improved connection quality")
    print("  • Professional rounded boxes")
    print("  • Consistent spacing and alignment\n")

    create_npi_lifecycle()
    create_card_hierarchy()
    create_phase_gate_decision()
    create_escalation_decision()
    create_system_integration()
    create_roles_matrix()

    print("\n✅ All diagrams generated with improved formatting!")
    print("📍 Location: /Users/casild1/Documents/VS_Vault/projects/brand-sop/")
    print("\n📊 Diagrams created:")
    print("  1. diagram_01_npi_lifecycle.png (300 DPI)")
    print("  2. diagram_02_card_hierarchy.png (300 DPI)")
    print("  3. diagram_03_phase_gate_decision.png (300 DPI)")
    print("  4. diagram_04_escalation_tree.png (300 DPI)")
    print("  5. diagram_05_system_integration.png (300 DPI)")
    print("  6. diagram_06_roles_matrix.png (300 DPI)")
    print("\n🎨 All diagrams use Medtronic brand colors with improved rendering")

if __name__ == '__main__':
    main()
