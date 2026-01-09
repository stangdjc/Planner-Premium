const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, AlignmentType, 
        WidthType, BorderStyle, ShadingType, VerticalAlign, HeadingLevel, PageBreak, PageOrientation,
        Header, Footer, PageNumber, LevelFormat } = require('docx');
const fs = require('fs');

// Medtronic Brand Colors (in hex without #)
const COLORS = {
  primaryBlue: "1010EB",
  deepNavy: "140F4B",
  charcoal: "3C3C3C",
  cyan: "0FC9F7",
  teal: "00DCB9",
  white: "FFFFFF",
  lightGray: "F5F5F5"
};

// Medtronic Font
const MEDTRONIC_FONT = "Avenir Next World";
const FALLBACK_FONT = "Helvetica Neue";

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "D3D3D3" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

// Create document
const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: FALLBACK_FONT, size: 24, color: COLORS.charcoal },
        paragraph: { spacing: { line: 360, lineRule: "auto" } }
      }
    },
    paragraphStyles: [
      {
        id: "Title",
        name: "Title",
        basedOn: "Normal",
        run: { size: 56, bold: true, color: COLORS.deepNavy, font: FALLBACK_FONT },
        paragraph: { spacing: { before: 240, after: 120 }, alignment: AlignmentType.CENTER }
      },
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 48, bold: true, color: COLORS.deepNavy, font: FALLBACK_FONT },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 32, bold: true, color: COLORS.primaryBlue, font: FALLBACK_FONT },
        paragraph: { spacing: { before: 180, after: 100 }, outlineLevel: 1 }
      },
      {
        id: "Heading3",
        name: "Heading 3",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 28, bold: true, color: COLORS.charcoal, font: FALLBACK_FONT },
        paragraph: { spacing: { before: 120, after: 80 }, outlineLevel: 2 }
      },
      {
        id: "Subtitle",
        name: "Subtitle",
        basedOn: "Normal",
        run: { size: 28, color: COLORS.primaryBlue, italics: true, font: FALLBACK_FONT },
        paragraph: { spacing: { after: 200 }, alignment: AlignmentType.CENTER }
      }
    ]
  },

  numbering: {
    config: [
      {
        reference: "bullet-list",
        levels: [
          {
            level: 0,
            format: LevelFormat.BULLET,
            text: "•",
            alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } }
          }
        ]
      }
    ]
  },

  sections: [{
    properties: {
      page: {
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        size: { orientation: PageOrientation.PORTRAIT }
      }
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            alignment: AlignmentType.RIGHT,
            spacing: { after: 100 },
            border: {
              bottom: { color: COLORS.deepNavy, space: 1, style: BorderStyle.SINGLE, size: 12 }
            },
            children: [new TextRun({ text: "Microsoft Planner Premium for NPI", size: 18, color: COLORS.deepNavy, bold: true })]
          })
        ]
      })
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            border: { top: { color: COLORS.deepNavy, space: 1, style: BorderStyle.SINGLE, size: 12 } },
            spacing: { before: 100 },
            children: [
              new TextRun({ text: "Page ", size: 18, color: COLORS.charcoal }),
              new TextRun({ text: "", children: [PageNumber.CURRENT], size: 18, color: COLORS.charcoal }),
              new TextRun({ text: " of 1", size: 18, color: COLORS.charcoal })
            ]
          })
        ]
      })
    },

    children: [
      // ===== COVER PAGE =====
      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),

      new Paragraph({
        heading: HeadingLevel.TITLE,
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [
          new TextRun({
            text: "Microsoft Planner Premium",
            size: 56,
            bold: true,
            color: COLORS.deepNavy,
            font: FALLBACK_FONT
          })
        ]
      }),

      new Paragraph({
        heading: HeadingLevel.TITLE,
        alignment: AlignmentType.CENTER,
        spacing: { after: 400 },
        children: [
          new TextRun({
            text: "for NPI Regional Readiness",
            size: 48,
            bold: true,
            color: COLORS.primaryBlue,
            font: FALLBACK_FONT
          })
        ]
      }),

      new Paragraph({
        style: "Subtitle",
        children: [new TextRun("Procedure & Implementation Guide")]
      }),

      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),

      // Version Control Block
      new Table({
        columnWidths: [2340, 2340, 2340, 2340],
        margins: { top: 100, bottom: 100, left: 180, right: 180 },
        rows: [
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Version", bold: true, color: COLORS.white, size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Date", bold: true, color: COLORS.white, size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Owner", bold: true, color: COLORS.white, size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Status", bold: true, color: COLORS.white, size: 22 })]
                })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "1.0", size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "01/07/2025", size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "[Your Name]", size: 22 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Draft", size: 22 })]
                })]
              })
            ]
          })
        ]
      }),

      new Paragraph({ children: [new TextRun("")] }),
      new Paragraph({ children: [new TextRun("")] }),

      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 300 },
        children: [
          new TextRun({
            text: "Next Review Date: [DATE]",
            size: 20,
            color: COLORS.charcoal,
            italics: true
          })
        ]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== QUICK START: FIND YOUR ROLE =====
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Quick Start: Find Your Role")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [
          new TextRun({
            text: "This document serves three audiences. Below, find your role and start reading the section that matters most to you. You can always explore other sections later.",
            italics: true
          })
        ]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("👤 I am a User (Regional PM, SME, Coordinator)")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Start with: ", bold: true }), new TextRun("Section III (User Pathway)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "You'll learn: ", bold: true }), new TextRun("Day-to-day tasks, card management, field completion, how to ask for help")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Time commitment: ", bold: true }), new TextRun("1 hour initial read, 15 minutes reference thereafter")]
      }),

      new Paragraph({ children: [new TextRun("")] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("📊 I am a Project Manager (Main PM, Portfolio Lead)")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Start with: ", bold: true }), new TextRun("Section II (Foundation), then Section IV (PM Pathway)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "You'll learn: ", bold: true }), new TextRun("Governance framework, quality standards, oversight mechanisms, reporting")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Time commitment: ", bold: true }), new TextRun("2 hours initial read, 30 minutes monthly reference")]
      }),

      new Paragraph({ children: [new TextRun("")] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("👔 I am a People Leader (Service Leader, Director, VP)")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Start with: ", bold: true }), new TextRun("Section V (Leader Pathway)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "You'll learn: ", bold: true }), new TextRun("Strategic alignment, portfolio health, resource implications, ROI")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Time commitment: ", bold: true }), new TextRun("30 minutes initial read, quarterly check-ins")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== TABLE OF CONTENTS =====
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Table of Contents")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part I: Front Matter & Orientation")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { before: 0 },
        indent: { left: 720 },
        children: [new TextRun("Quick Start: Find Your Role")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { before: 0 },
        indent: { left: 720 },
        children: [new TextRun("Table of Contents")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part II: Foundation (For All Audiences)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { before: 0 },
        indent: { left: 720 },
        children: [new TextRun("What is Microsoft Planner Premium?")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { before: 0 },
        indent: { left: 720 },
        children: [new TextRun("Core Concepts & Terminology")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { before: 0 },
        indent: { left: 720 },
        children: [new TextRun("System Integration Overview")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part III: User Pathway")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part IV: Project Manager Pathway")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part V: People Leader Pathway")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part VI: Shared Resources")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Part VII: Appendices")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== PART II: FOUNDATION =====
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part II: Foundation")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun({ text: "Shared knowledge for all audiences. Read this section to understand context and terminology.", italics: true })]
      }),

      // ===== II.A: What is Microsoft Planner Premium? =====
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("II.A: What is Microsoft Planner Premium?")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [
          new TextRun({
            text: "Planner Premium is a user-friendly project management tool built on Microsoft Planner that helps teams track and coordinate New Product Introduction (NPI) projects across global and regional teams. It simplifies task organization with features like summary tasks, sub-tasks, and clear timelines, allowing easy visualization of project progress and dependencies. Integrated with Microsoft Teams, it supports seamless communication within project cards. Unlike complex traditional tools, Planner Premium focuses on collaboration, quick updates, and tailored fields to fit NPI workflows, making it easier to manage multiple regions and operating units efficiently."
          })
        ]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Why We Use Planner Premium for NPI Projects")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Multi-region visibility and coordination", bold: false })]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Integration with Planisware for financial tracking")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Teams-native communication")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Custom field flexibility for NPI governance")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Timeline and dependency visualization")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Audit trail and change history")]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("What Planner Premium is NOT")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Not a replacement for Planisware ", bold: true }), new TextRun("(financial tracking, detailed project costing)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Not a replacement for SharePoint ", bold: true }), new TextRun("(document repository)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Not a replacement for Teams ", bold: true }), new TextRun("(primary communication channel)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun({ text: "Not a replacement for Global NPI Playbook ", bold: true }), new TextRun("(process documentation)")]
      }),

      // ===== II.B: Core Concepts & Terminology =====
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("II.B: Core Concepts & Terminology")]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("NPI Lifecycle Phases")]
      }),

      // Lifecycle flowchart as a visual table/diagram
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 200 },
        children: [
          new TextRun({
            text: "Initiate → Global Alignment → Regional Alignment → Regional Engage → Kick-off → Execute → Close-out",
            size: 22,
            bold: true,
            color: COLORS.primaryBlue
          })
        ]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun("Each phase has distinct objectives, timelines, and deliverables:")]
      }),

      // Phase Details Table
      new Table({
        columnWidths: [1560, 2340, 2340, 2340],
        margins: { top: 80, bottom: 80, left: 100, right: 100 },
        rows: [
          new TableRow({
            tableHeader: true,
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Phase", bold: true, color: COLORS.white, size: 20 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Duration", bold: true, color: COLORS.white, size: 20 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Owner", bold: true, color: COLORS.white, size: 20 })]
                })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.deepNavy, type: ShadingType.CLEAR },
                verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [new TextRun({ text: "Key Deliverable", bold: true, color: COLORS.white, size: 20 })]
                })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Initiate", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Variable", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Initiating OU", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Upstream card in Pipeline", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "GA", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "8-12 weeks", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Main PM", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Playbook Section 1", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "RA", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "4-8 weeks", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional PM", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional cards created", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Engage", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "4-8 weeks", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional PM", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "SME names received", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Kick-off", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "2-4 weeks", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional PM + SMEs", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Project plan reviewed", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Execute", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "4-12 months", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional PM + Team", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                shading: { fill: COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Deliverables completed", size: 20 })] })]
              })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({
                borders: cellBorders,
                width: { size: 1560, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Close-out", bold: true, size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "1-2 weeks", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Regional PM + Main PM", size: 20 })] })]
              }),
              new TableCell({
                borders: cellBorders,
                width: { size: 2340, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: "Lessons learned", size: 20 })] })]
              })
            ]
          })
        ]
      }),

      new Paragraph({ children: [new TextRun("")] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Planner Premium Terminology")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Board: ", bold: true }), new TextRun("Container for all project cards")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Card: ", bold: true }), new TextRun("Individual task or work item")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Upstream Card: ", bold: true }), new TextRun("Project-level summary card")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Bucket: ", bold: true }), new TextRun("Container within a board (Pipeline, GA, RA, etc.)")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Timeline View: ", bold: true }), new TextRun("Gantt-like visualization showing schedules")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun({ text: "Dependencies: ", bold: true }), new TextRun("Relationships between cards (when one must finish before another starts)")]
      }),

      // ===== II.C: System Integration Overview =====
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("II.C: System Integration Overview")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun("Planner Premium is one part of an integrated ecosystem. Understanding how it connects to other systems helps you use it effectively.")]
      }),

      // Integration Diagram as Text
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 200 },
        children: [new TextRun({
          text: "Planner Premium (Core Project Tracking) ↔ Planisware (Financial) ↔ Teams (Communication) ↔ SharePoint (Documents)",
          size: 22,
          bold: true,
          color: COLORS.primaryBlue
        })]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Key Integrations")]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 100 },
        children: [new TextRun({ text: "Planner ↔ Planisware", color: COLORS.primaryBlue, bold: true })]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Integration point: ", bold: true }), new TextRun("Planisware ID field on cards")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "What syncs: ", bold: true }), new TextRun("Project status, go-live dates, resource allocation")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun({ text: "What doesn't: ", bold: true }), new TextRun("Daily task detail (intentional boundary)")]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 100 },
        children: [new TextRun({ text: "Planner ↔ Teams", color: COLORS.primaryBlue, bold: true })]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Integration point: ", bold: true }), new TextRun("Planner tab in project Teams channel")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "What flows: ", bold: true }), new TextRun("Card updates trigger notifications, in-card messages")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun({ text: "What doesn't: ", bold: true }), new TextRun("Planner is source of truth for project data")]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 100 },
        children: [new TextRun({ text: "Planner ↔ SharePoint", color: COLORS.primaryBlue, bold: true })]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "Integration point: ", bold: true }), new TextRun("Folder URLs stored in card description")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun({ text: "What flows: ", bold: true }), new TextRun("Card links to project folder and reference documents")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun({ text: "What doesn't: ", bold: true }), new TextRun("Card data doesn't live in SharePoint")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== PLACEHOLDER SECTIONS =====
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part III: User Pathway")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun({ text: "[Detailed user procedures, checklists, and step-by-step instructions - To be completed]", italics: true, color: COLORS.primaryBlue })]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("III.A: Getting Started with Planner Premium")]
      }),

      new Paragraph({
        children: [new TextRun("Content outline prepared. Sections include:")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Access & Setup")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Board Navigation Basics")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Understanding Card Structure")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Day-to-Day Tasks")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Common Scenarios")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part IV: Project Manager Pathway")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun({ text: "[PM governance, oversight, quality standards, reporting - To be completed]", italics: true, color: COLORS.primaryBlue })]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("IV.A: PM Responsibilities & Governance")]
      }),

      new Paragraph({
        children: [new TextRun("Content outline prepared. Sections include:")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Your Responsibilities as PM")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Governance Framework")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Quality Gates & Checkpoints")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Risk Management")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Status Reporting & Communication")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part V: People Leader Pathway")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun({ text: "[Strategic alignment, portfolio health, resource decisions - To be completed]", italics: true, color: COLORS.primaryBlue })]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("V.A: Strategic Leadership Responsibilities")]
      }),

      new Paragraph({
        children: [new TextRun("Content outline prepared. Sections include:")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Portfolio Health Overview")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Executive Dashboards & Views")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Resource & Capacity Planning")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Strategic Decision-Making")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Quarterly Business Reviews")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part VI: Shared Resources")]
      }),

      new Paragraph({
        spacing: { after: 200 },
        children: [new TextRun("Tools and references for all audiences.")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Custom Field Master Definitions")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Board Structure Templates")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Process Maps & Decision Trees")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Quality Checklists")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Templates & Examples")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Troubleshooting Guide")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Glossary & Contact Directory")]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Part VII: Appendices")]
      }),

      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Planner Premium Licensing & Technical Requirements")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Integration with External Systems")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Change Log & Version History")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: [new TextRun("Keyboard Shortcuts & Pro Tips")]
      }),
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 200 },
        children: [new TextRun("Feedback & Continuous Improvement")]
      }),

      new Paragraph({
        spacing: { before: 400 },
        children: [new TextRun({ text: "— End of Document —", italics: true, alignment: AlignmentType.CENTER })]
      })
    ]
  }]
});

// Save document
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/Users/casild1/Documents/VS_Vault/projects/brand-sop/NPI_Planner_Premium_Procedure.docx", buffer);
  console.log("✅ Document created successfully!");
  console.log("📄 Location: /Users/casild1/Documents/VS_Vault/projects/brand-sop/NPI_Planner_Premium_Procedure.docx");
});
