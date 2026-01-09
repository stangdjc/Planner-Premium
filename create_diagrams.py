#!/usr/bin/env python3
"""
Create branded process flow diagrams for NPI Planner Premium procedure document
Uses Medtronic brand colors and professional styling
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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

# Common settings
DPI = 300
FONT_FAMILY = 'sans-serif'

def set_style():
    """Set matplotlib styling"""
    plt.rcParams['font.family'] = FONT_FAMILY
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['ytick.left'] = False

# ============= DIAGRAM 1: NPI LIFECYCLE PROCESS FLOW =============

def create_npi_lifecycle():
    """Create the NPI Lifecycle progression diagram"""
    fig, ax = plt.subplots(figsize=(14, 3), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    # Title
    ax.text(7, 2.7, 'NPI Lifecycle: Phase Progression', 
            fontsize=16, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    phases = [
        ('Initiate', COLORS['deepNavy']),
        ('GA', COLORS['primaryBlue']),
        ('RA', COLORS['primaryBlue']),
        ('Engage', COLORS['cyan']),
        ('Kick-off', COLORS['teal']),
        ('Execute', COLORS['orange']),
        ('Close-out', COLORS['red'])
    ]
    
    x_positions = np.linspace(0.5, 13.5, len(phases))
    y = 1.5
    
    # Draw boxes and text
    for i, (phase, color) in enumerate(phases):
        x = x_positions[i]
        
        # Box
        box = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=color,
                            facecolor=color,
                            alpha=0.8,
                            linewidth=2)
        ax.add_patch(box)
        
        # Text
        ax.text(x, y, phase, fontsize=10, weight='bold',
               color=COLORS['white'] if color != COLORS['cyan'] else COLORS['deepNavy'],
               ha='center', va='center', fontfamily=FONT_FAMILY)
        
        # Arrow to next phase
        if i < len(phases) - 1:
            next_x = x_positions[i+1]
            ax.annotate('', xy=(next_x-0.45, y), xytext=(x+0.45, y),
                       arrowprops=dict(arrowstyle='->', lw=2,
                                      color=COLORS['charcoal']))
    
    # Add feedback loop annotation
    ax.text(7, 0.3, '↻ Feedback loops: RA↔GA | Engage↔RA | Execute↔Kick-off when issues found',
           fontsize=9, style='italic', color=COLORS['charcoal'],
           ha='center', fontfamily=FONT_FAMILY)
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_01_npi_lifecycle.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 1: NPI Lifecycle created")

# ============= DIAGRAM 2: CARD HIERARCHY =============

def create_card_hierarchy():
    """Create Upstream → Regional → Sub-tasks hierarchy"""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Card Hierarchy: Project Structure in Planner', 
            fontsize=14, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    # Level 1: Upstream Card
    upstream_box = FancyBboxPatch((1.5, 7.5), 7, 1.2,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=COLORS['deepNavy'],
                                 facecolor=COLORS['deepNavy'],
                                 alpha=0.9,
                                 linewidth=2)
    ax.add_patch(upstream_box)
    ax.text(5, 8.4, 'UPSTREAM CARD (Project Level)', fontsize=11, weight='bold',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    ax.text(5, 7.95, '"NPI - Calima - CAL-001" | Created by Main PM | Moves through all phases',
           fontsize=9, style='italic', color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    
    # Arrow down
    ax.annotate('', xy=(5, 7.3), xytext=(5, 6.8),
               arrowprops=dict(arrowstyle='->', lw=3, color=COLORS['charcoal']))
    
    # Level 2: Regional Cards (3 columns)
    regional_y = 5.5
    regional_boxes = [
        (1.5, "Singapore"),
        (3.8, "India"),
        (6.1, "Australia")
    ]
    
    for x, region in regional_boxes:
        box = FancyBboxPatch((x-0.8, regional_y-0.5), 1.6, 1,
                           boxstyle="round,pad=0.08",
                           edgecolor=COLORS['primaryBlue'],
                           facecolor=COLORS['primaryBlue'],
                           alpha=0.85,
                           linewidth=2)
        ax.add_patch(box)
        ax.text(x, regional_y+0.15, region, fontsize=10, weight='bold',
               color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
        ax.text(x, regional_y-0.25, 'Regional Card', fontsize=8, style='italic',
               color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
        
        # Arrow down to sub-tasks
        ax.annotate('', xy=(x, 4.8), xytext=(x, regional_y-0.6),
                   arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['charcoal']))
    
    # Level 3: Sub-tasks
    subtask_y = 3.8
    subtasks = [
        ((0.5, subtask_y), "Training\nPlan"),
        ((1.8, subtask_y), "Service\nProcs"),
        ((3.1, subtask_y), "Spare\nParts"),
        ((4.4, subtask_y), "Training\nPlan"),
        ((5.7, subtask_y), "Service\nProcs"),
        ((7, subtask_y), "Spare\nParts"),
    ]
    
    for (x, y), label in subtasks:
        box = FancyBboxPatch((x-0.4, y-0.4), 0.8, 0.8,
                           boxstyle="round,pad=0.05",
                           edgecolor=COLORS['cyan'],
                           facecolor=COLORS['cyan'],
                           alpha=0.8,
                           linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=7, weight='bold',
               color=COLORS['deepNavy'], ha='center', va='center',
               fontfamily=FONT_FAMILY)
    
    ax.text(8.5, 3.8, "Sub-tasks\n(owned by SMEs)", fontsize=9,
           color=COLORS['charcoal'], fontfamily=FONT_FAMILY, weight='bold')
    
    # Legend/Annotations
    ax.text(0.5, 2.2, "Ownership:", fontsize=10, weight='bold', color=COLORS['charcoal'])
    ax.text(0.5, 1.85, "• Upstream: Main PM (global oversight)", fontsize=9, color=COLORS['charcoal'])
    ax.text(0.5, 1.5, "• Regional: Regional PM (regional management)", fontsize=9, color=COLORS['charcoal'])
    ax.text(0.5, 1.15, "• Sub-tasks: SMEs (functional execution)", fontsize=9, color=COLORS['charcoal'])
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_02_card_hierarchy.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 2: Card Hierarchy created")

# ============= DIAGRAM 3: PHASE GATE DECISION TREE =============

def create_phase_gate_decision():
    """Create decision tree for phase progression"""
    fig, ax = plt.subplots(figsize=(13, 10), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6.5, 9.5, 'Phase Gate Decision: Ready to Move to Next Phase?', 
            fontsize=13, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    # Start decision
    start_box = FancyBboxPatch((5, 8.5), 3, 0.7,
                              boxstyle="round,pad=0.08",
                              edgecolor=COLORS['primaryBlue'],
                              facecolor=COLORS['primaryBlue'],
                              alpha=0.85,
                              linewidth=2)
    ax.add_patch(start_box)
    ax.text(6.5, 8.85, 'Reviewing Phase Completion', fontsize=10, weight='bold',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    
    questions = [
        ("All ⭐ fields\nfilled?", 2.5, 7.5, "No", "Stop", COLORS['red']),
        ("Deliverables\nstarted/done?", 2.5, 6.2, "No", "Wait", COLORS['orange']),
        ("Critical\nblockers?", 5.5, 7.5, "Yes", "Escalate", COLORS['red']),
        ("Stakeholders\napproved?", 5.5, 6.2, "No", "Get Approval", COLORS['orange']),
        ("Timeline\nrealistic?", 8.5, 7.5, "No", "Adjust or Delay", COLORS['orange']),
        ("Resources\navailable?", 8.5, 6.2, "No", "Get Resources", COLORS['orange']),
    ]
    
    # Draw decision diamonds
    for question, x, y, no_label, no_action, no_color in questions:
        # Diamond shape
        diamond = mpatches.FancyBboxPatch((x-0.7, y-0.35), 1.4, 0.7,
                                         boxstyle="round,pad=0.05",
                                         edgecolor=COLORS['deepNavy'],
                                         facecolor=COLORS['lightGray'],
                                         linewidth=1.5)
        ax.add_patch(diamond)
        ax.text(x, y, question, fontsize=8, weight='bold',
               color=COLORS['charcoal'], ha='center', va='center',
               fontfamily=FONT_FAMILY)
        
        # "Yes" path (up/right)
        ax.text(x+1, y+0.3, "Yes ✓", fontsize=8, color=COLORS['teal'], weight='bold')
        
        # "No" path (down)
        ax.text(x-0.5, y-0.7, "No: " + no_label, fontsize=7, color=no_color, weight='bold')
    
    # Final decision
    final_box = FancyBboxPatch((5, 4.5), 3, 0.8,
                              boxstyle="round,pad=0.08",
                              edgecolor=COLORS['teal'],
                              facecolor=COLORS['teal'],
                              alpha=0.85,
                              linewidth=2)
    ax.add_patch(final_box)
    ax.text(6.5, 4.95, '✓ READY TO MOVE', fontsize=11, weight='bold',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    ax.text(6.5, 4.65, 'Move card to next bucket', fontsize=9, style='italic',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    
    # Process flow
    ax.annotate('', xy=(6.5, 8.5), xytext=(6.5, 8.2),
               arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['charcoal']))
    ax.annotate('', xy=(6.5, 5.3), xytext=(6.5, 4.5),
               arrowprops=dict(arrowstyle='->', lw=3, color=COLORS['teal']))
    
    # Success criteria
    ax.text(0.5, 3.5, 'SUCCESS CRITERIA:', fontsize=9, weight='bold', color=COLORS['deepNavy'])
    criteria = [
        "✓ All required fields populated",
        "✓ Deliverables for phase started or complete",
        "✓ No critical blockers",
        "✓ Stakeholder approval received",
        "✓ Timeline is realistic",
        "✓ Resources allocated for next phase"
    ]
    for i, criterion in enumerate(criteria):
        ax.text(0.7, 3.1 - (i * 0.35), criterion, fontsize=8, color=COLORS['charcoal'])
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_03_phase_gate_decision.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 3: Phase Gate Decision created")

# ============= DIAGRAM 4: ESCALATION DECISION TREE =============

def create_escalation_decision():
    """Create escalation decision tree"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.7, 'Escalation Decision Tree: Who Should I Ask?', 
            fontsize=13, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    # Central question
    central_box = FancyBboxPatch((5.5, 6.8), 3, 0.6,
                               boxstyle="round,pad=0.08",
                               edgecolor=COLORS['primaryBlue'],
                               facecolor=COLORS['primaryBlue'],
                               alpha=0.85,
                               linewidth=2)
    ax.add_patch(central_box)
    ax.text(7, 7.1, 'I have a problem', fontsize=10, weight='bold',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    
    # Escalation paths
    escalations = [
        {
            'question': 'About MY sub-task?\n(confused, blocked)',
            'x': 1.5,
            'contact': '→ Regional PM\n(24 hrs)',
            'color': COLORS['cyan']
        },
        {
            'question': 'Team member\nnot responding?',
            'x': 4,
            'contact': '→ Regional Service Leader\n(24 hrs)',
            'color': COLORS['teal']
        },
        {
            'question': 'Timeline\nunrealistic?',
            'x': 6.5,
            'contact': '→ Main PM + Service Leader\n(48 hrs)',
            'color': COLORS['orange']
        },
        {
            'question': 'Planner not\nworking?',
            'x': 9,
            'contact': '→ IT Help Desk\n(4 hrs)',
            'color': COLORS['lightGray']
        },
        {
            'question': 'Strategic\ndecision?',
            'x': 11.5,
            'contact': '→ Service Leader\n→ Main PM\n→ Leadership',
            'color': COLORS['red']
        }
    ]
    
    for esc in escalations:
        x = esc['x']
        
        # Question box
        q_box = FancyBboxPatch((x-0.65, 5.7), 1.3, 1,
                             boxstyle="round,pad=0.06",
                             edgecolor=esc['color'],
                             facecolor=esc['color'],
                             alpha=0.75,
                             linewidth=1.5)
        ax.add_patch(q_box)
        ax.text(x, 6.2, esc['question'], fontsize=8, weight='bold',
               color=COLORS['charcoal'] if esc['color'] == COLORS['lightGray'] else COLORS['white'],
               ha='center', va='center', fontfamily=FONT_FAMILY)
        
        # Arrow down
        ax.annotate('', xy=(x, 5.5), xytext=(x, 5.7),
                   arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['charcoal']))
        
        # Contact box
        c_box = FancyBboxPatch((x-0.7, 4.3), 1.4, 1,
                             boxstyle="round,pad=0.06",
                             edgecolor=COLORS['deepNavy'],
                             facecolor=COLORS['lightGray'],
                             linewidth=1.5)
        ax.add_patch(c_box)
        ax.text(x, 4.8, esc['contact'], fontsize=7, weight='bold',
               color=COLORS['charcoal'], ha='center', va='center',
               fontfamily=FONT_FAMILY)
    
    # Bottom guidance
    guidance_y = 3.2
    ax.text(7, guidance_y, 'KEY PRINCIPLE: Escalate early, don\'t hide problems', fontsize=10,
           weight='bold', color=COLORS['red'], ha='center', fontfamily=FONT_FAMILY)
    ax.text(7, guidance_y-0.5, 'Red/Blocked status = Immediate escalation to your PM and Regional Service Leader',
           fontsize=8, style='italic', color=COLORS['charcoal'], ha='center', fontfamily=FONT_FAMILY)
    
    # Timeline guidance
    ax.text(0.5, 1.8, 'RESPONSE EXPECTATIONS:', fontsize=9, weight='bold', color=COLORS['deepNavy'])
    timings = [
        ('Regional PM', '24 hours'),
        ('Regional Service Leader', '24-48 hours'),
        ('Main PM', '24-48 hours'),
        ('IT Help Desk', '4 hours'),
        ('Strategic Decision', '48-72 hours'),
    ]
    for i, (contact, timing) in enumerate(timings):
        ax.text(0.7, 1.4 - (i * 0.25), f"• {contact}: {timing}", fontsize=7.5, color=COLORS['charcoal'])
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_04_escalation_tree.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 4: Escalation Decision Tree created")

# ============= DIAGRAM 5: SYSTEM INTEGRATION ARCHITECTURE =============

def create_system_integration():
    """Create system integration architecture diagram"""
    fig, ax = plt.subplots(figsize=(12, 7), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(6, 6.7, 'System Integration Architecture', 
            fontsize=13, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    # Central system (Planner Premium)
    planner_box = FancyBboxPatch((4.5, 4), 3, 1.2,
                               boxstyle="round,pad=0.1",
                               edgecolor=COLORS['primaryBlue'],
                               facecolor=COLORS['primaryBlue'],
                               alpha=0.9,
                               linewidth=3)
    ax.add_patch(planner_box)
    ax.text(6, 4.75, 'PLANNER PREMIUM', fontsize=11, weight='bold',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    ax.text(6, 4.35, '(Source of Truth)', fontsize=9, style='italic',
           color=COLORS['white'], ha='center', fontfamily=FONT_FAMILY)
    
    # Connected systems
    systems = [
        {
            'name': 'PLANISWARE',
            'x': 1.5,
            'y': 4.6,
            'color': COLORS['deepNavy'],
            'sync': 'Planisware ID,\nStatus, Dates,\nResources',
            'frequency': 'Daily'
        },
        {
            'name': 'TEAMS',
            'x': 10.5,
            'y': 4.6,
            'color': COLORS['teal'],
            'sync': 'Notifications,\nComments,\nUpdates',
            'frequency': 'Real-time'
        },
        {
            'name': 'SHAREPOINT',
            'x': 6,
            'y': 2,
            'color': COLORS['cyan'],
            'sync': 'Document Links,\nFolder URLs,\nProject Folder',
            'frequency': 'Manual'
        },
        {
            'name': 'NPI PLAYBOOK',
            'x': 6,
            'y': 5.8,
            'color': COLORS['orange'],
            'sync': 'Playbook Status,\nSection Tracking',
            'frequency': 'Manual'
        }
    ]
    
    for system in systems:
        # System box
        sys_box = FancyBboxPatch((system['x']-0.7, system['y']-0.35), 1.4, 0.7,
                               boxstyle="round,pad=0.08",
                               edgecolor=system['color'],
                               facecolor=system['color'],
                               alpha=0.85,
                               linewidth=2)
        ax.add_patch(sys_box)
        ax.text(system['x'], system['y'], system['name'], fontsize=10, weight='bold',
               color=COLORS['white'], ha='center', va='center', fontfamily=FONT_FAMILY)
        
        # Connection line and sync info
        if system['name'] in ['PLANISWARE', 'TEAMS']:
            ax.annotate('', xy=(6, 4.5), xytext=(system['x']+0.75, system['y']),
                       arrowprops=dict(arrowstyle='<->', lw=2.5,
                                      color=system['color'], alpha=0.7))
            ax.text((system['x']+6)/2, (system['y']+4.5)/2 + 0.4, system['sync'],
                   fontsize=7.5, style='italic', color=system['color'],
                   ha='center', fontfamily=FONT_FAMILY, weight='bold')
            ax.text((system['x']+6)/2, (system['y']+4.5)/2 - 0.4, system['frequency'],
                   fontsize=7, color=COLORS['charcoal'], ha='center', fontfamily=FONT_FAMILY)
        elif system['name'] == 'SHAREPOINT':
            ax.annotate('', xy=(6, 4), xytext=(6, 2.35),
                       arrowprops=dict(arrowstyle='<->', lw=2.5,
                                      color=system['color'], alpha=0.7))
            ax.text(6.8, 3, system['sync'] + '\n' + system['frequency'],
                   fontsize=7.5, style='italic', color=system['color'],
                   ha='left', fontfamily=FONT_FAMILY, weight='bold')
        elif system['name'] == 'NPI PLAYBOOK':
            ax.annotate('', xy=(6, 5.2), xytext=(6, 5.45),
                       arrowprops=dict(arrowstyle='<->', lw=2.5,
                                      color=system['color'], alpha=0.7))
            ax.text(6.8, 5.7, system['sync'] + '\n' + system['frequency'],
                   fontsize=7.5, style='italic', color=system['color'],
                   ha='left', fontfamily=FONT_FAMILY, weight='bold')
    
    # Legend
    ax.text(0.5, 1.1, 'INTEGRATION POINTS:', fontsize=9, weight='bold', color=COLORS['deepNavy'])
    legend_items = [
        '• Planisware: Financial tracking, resource costing, project-level data',
        '• Teams: Communication, notifications, team messaging within cards',
        '• SharePoint: Document storage, project folders, reference materials',
        '• Playbook: Process documentation, section tracking, governance'
    ]
    for i, item in enumerate(legend_items):
        ax.text(0.7, 0.75 - (i * 0.25), item, fontsize=7.5, color=COLORS['charcoal'])
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_05_system_integration.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 5: System Integration created")

# ============= DIAGRAM 6: ORGANIZATIONAL ROLES MATRIX =============

def create_roles_matrix():
    """Create organizational roles and responsibilities matrix"""
    fig, ax = plt.subplots(figsize=(13, 7), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    # Title
    ax.text(6.5, 6.7, 'Organizational Roles & Responsibilities in Planner Premium', 
            fontsize=12, weight='bold', color=COLORS['deepNavy'],
            ha='center', fontfamily=FONT_FAMILY)
    
    # Role boxes with responsibilities
    roles = [
        {
            'title': 'MAIN PM',
            'x': 1.5,
            'color': COLORS['deepNavy'],
            'responsibilities': [
                '• Creates Upstream card',
                '• Manages global timeline',
                '• Sets Global Service Model',
                '• Oversees all regions',
                '• Governance ownership'
            ]
        },
        {
            'title': 'REGIONAL PM',
            'x': 4.5,
            'color': COLORS['primaryBlue'],
            'responsibilities': [
                '• Creates Regional card',
                '• Manages regional timeline',
                '• Creates sub-tasks',
                '• Assigns to SMEs',
                '• Regional escalation point'
            ]
        },
        {
            'title': 'FUNCTIONAL SME',
            'x': 7.5,
            'color': COLORS['cyan'],
            'responsibilities': [
                '• Owns assigned sub-tasks',
                '• Delivers training/SOPs',
                '• Updates progress',
                '• Escalates blockers',
                '• Executes the work'
            ]
        },
        {
            'title': 'SERVICE LEADER',
            'x': 10.5,
            'color': COLORS['teal'],
            'responsibilities': [
                '• Regional approval',
                '• Resource decisions',
                '• Escalation resolution',
                '• Portfolio oversight',
                '• Strategic alignment'
            ]
        }
    ]
    
    for role in roles:
        x = role['x']
        
        # Role title box
        title_box = FancyBboxPatch((x-0.95, 5.8), 1.9, 0.5,
                                 boxstyle="round,pad=0.08",
                                 edgecolor=role['color'],
                                 facecolor=role['color'],
                                 alpha=0.9,
                                 linewidth=2)
        ax.add_patch(title_box)
        ax.text(x, 6.05, role['title'], fontsize=10, weight='bold',
               color=COLORS['white'], ha='center', va='center',
               fontfamily=FONT_FAMILY)
        
        # Responsibilities box
        resp_box = FancyBboxPatch((x-0.95, 1.5), 1.9, 4,
                                boxstyle="round,pad=0.08",
                                edgecolor=role['color'],
                                facecolor=COLORS['lightGray'],
                                alpha=0.85,
                                linewidth=1.5)
        ax.add_patch(resp_box)
        
        # Responsibilities text
        y_offset = 5.3
        for resp in role['responsibilities']:
            ax.text(x, y_offset, resp, fontsize=7.5, color=COLORS['charcoal'],
                   ha='center', fontfamily=FONT_FAMILY)
            y_offset -= 0.7
    
    # Bottom guidance
    ax.text(6.5, 1, 'COLLABORATION PRINCIPLE: Each role is critical. Clear ownership prevents gaps.', 
           fontsize=9, weight='bold', color=COLORS['primaryBlue'], ha='center', fontfamily=FONT_FAMILY)
    
    plt.tight_layout()
    plt.savefig('/Users/casild1/Documents/VS_Vault/projects/brand-sop/diagram_06_roles_matrix.png',
               dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Diagram 6: Organizational Roles Matrix created")

# ============= MAIN EXECUTION =============

if __name__ == '__main__':
    set_style()
    
    print("\n🎨 Creating branded diagrams for NPI Planner Premium procedure document...\n")
    
    create_npi_lifecycle()
    create_card_hierarchy()
    create_phase_gate_decision()
    create_escalation_decision()
    create_system_integration()
    create_roles_matrix()
    
    print("\n✅ All diagrams created successfully!")
    print("📁 Location: /Users/casild1/Documents/VS_Vault/projects/brand-sop/")
    print("\nDiagrams created:")
    print("  1. diagram_01_npi_lifecycle.png")
    print("  2. diagram_02_card_hierarchy.png")
    print("  3. diagram_03_phase_gate_decision.png")
    print("  4. diagram_04_escalation_tree.png")
    print("  5. diagram_05_system_integration.png")
    print("  6. diagram_06_roles_matrix.png")
