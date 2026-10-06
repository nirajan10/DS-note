// Builds slides/unit-01-intro.pptx (Unit I slides). Run: node build_unit01.js
// Look: the notes' own palette (deep blue, marigold, blue/orange/aqua series), short phrases only.
const fs = require("fs");
const path = require("path");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");
const pptxgen = require("pptxgenjs");
const fa = require("react-icons/fa");
const { applyTheme } = require("./apply_theme.js");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(__dirname, "unit-01-intro.pptx");

// ---- theme: same colours as docs/stylesheets/extra.css and the figures ----------------------
const THEME = {
  name: "DSC 481 Notes",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "14202E",    // ink
    lt1: "F7F8FA",    // paper
    dk2: "0D366B",    // deep blue
    lt2: "E4ECF8",    // card tint
    accent1: "2A78D6", // blue
    accent2: "EB6834", // orange
    accent3: "1BAF7A", // aqua
    accent4: "EDA100", // marigold
    accent5: "566175", // muted ink
    accent6: "C93C3C", // red (errors)
    hlink: "1C5CAB",
    folHlink: "4A3AA7",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
pres.title = "Unit I: Introduction to Data Science and Python";
pres.author = "DSC 481";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const CODE_FONT = "Courier New";

// ---- layouts: one light, one dark ---------------------------------------------------------
pres.defineSlideMaster({
  title: "LIGHT",
  background: { color: THEME.colors.lt1 },
  slideNumber: { x: 9.1, y: 5.2, w: 0.5, h: 0.3, fontSize: 10, color: THEME.colors.accent5, align: "right" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 8.8, h: 0.8, fontSize: 36, bold: true, color: C.text1, align: "left", valign: "middle", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "DARK",
  background: { color: THEME.colors.dk2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 8.8, h: 0.8, fontSize: 36, bold: true, color: C.background1, align: "left", valign: "middle", margin: 0 }, text: "" } },
  ],
});

// ---- helpers ------------------------------------------------------------------------------
const iconCache = {};
async function icon(name, hex = "FFFFFF") {
  const key = name + hex;
  if (iconCache[key]) return iconCache[key];
  if (!fa[name]) throw new Error("no such icon: " + name);
  const svg = renderToStaticMarkup(React.createElement(fa[name], { color: "#" + hex, size: "256" }));
  const buf = await sharp(Buffer.from(svg)).resize(256, 256, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toBuffer();
  return (iconCache[key] = "image/png;base64," + buf.toString("base64"));
}

const shadow = () => ({ type: "outer", color: "000000", opacity: 0.12, blur: 6, offset: 2, angle: 90 });

function card(slide, x, y, w, h, name) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, rectRadius: 0.12, fill: { color: C.background2 }, line: { color: C.background2, width: 0 }, shadow: shadow(), objectName: name,
  });
}

async function badge(slide, iconName, x, y, d, fillColor, name) {
  slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fillColor }, line: { color: fillColor, width: 0 }, objectName: name + " circle" });
  const s = d * 0.5;
  slide.addImage({ data: await icon(iconName, fillColor === C.accent4 ? "14202E" : "FFFFFF"), x: x + (d - s) / 2, y: y + (d - s) / 2, w: s, h: s, altText: name, objectName: name });
}

function numberBadge(slide, n, x, y, d, fillColor, fontSize = 16) {
  slide.addText(String(n), {
    shape: pres.shapes.OVAL, x, y, w: d, h: d, fill: { color: fillColor }, line: { color: fillColor, width: 0 },
    align: "center", valign: "middle", fontSize, bold: true, color: fillColor === C.accent4 ? C.text1 : C.background1, margin: 0, isTextBox: true, objectName: "Number " + n,
  });
}

function text(slide, str, x, y, w, h, opts = {}) {
  slide.addText(str, { x, y, w, h, margin: 0, valign: "top", isTextBox: true, color: C.text1, fontSize: 14, ...opts });
}

function arrow(slide, x1, y1, x2, y2, color = C.accent5, width = 2) {
  const x = Math.min(x1, x2), y = Math.min(y1, y2);
  slide.addShape(pres.shapes.LINE, {
    x, y, w: Math.abs(x2 - x1), h: Math.abs(y2 - y1), flipH: x2 < x1, flipV: y2 < y1,
    line: { color, width, endArrowType: "triangle" },
  });
}

function code(slide, lines, x, y, w, h, fontSize = 14) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: C.text2 }, line: { color: C.text2, width: 0 } });
  slide.addText(lines.map((t, i) => ({ text: t, options: { breakLine: i < lines.length - 1 } })), {
    x: x + 0.2, y: y + 0.12, w: w - 0.4, h: h - 0.24, fontFace: CODE_FONT, fontSize, color: C.background1, valign: "middle", margin: 0, isTextBox: true,
  });
}

function titleSlide(master, section, title, notes) {
  const s = pres.addSlide({ masterName: master, sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  return s;
}

(async () => {
  // =========================================================================================
  pres.addSection({ title: "Opening" });
  // 1. Title ---------------------------------------------------------------------------------
  {
    const s = pres.addSlide({ masterName: "DARK", sectionTitle: "Opening" });
    text(s, "UNIT I", 0.6, 1.1, 4.6, 0.4, { fontSize: 16, bold: true, color: C.accent4, charSpacing: 4 });
    text(s, "Introduction to Data Science and Python", 0.6, 1.6, 5.0, 1.9, { fontSize: 38, bold: true, color: C.background1, valign: "top" });
    text(s, "DSC 481  ·  BCSIT  ·  3 hours", 0.6, 3.9, 5.0, 0.4, { fontSize: 18, color: C.background2 });
    // graphic: three linked circles
    const cx = 7.6, pts = [[cx - 0.2, 1.1, 1.5, "FaDatabase", C.accent1], [cx + 0.9, 2.25, 1.3, "FaChartBar", C.accent3], [cx - 0.6, 3.1, 1.6, "FaPython", C.accent4]];
    for (const [x, y, d, ic, col] of pts) await badge(s, ic, x, y, d, col, ic.replace("Fa", "") + " icon");
    s.addNotes("Welcome. Unit I has two parts: what data science is, and how to get Python running. Full text is on the Unit I page of the notes.");
  }

  // 2. What you will learn -------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Opening", "What You Will Learn", "Four goals for this unit. Matches the learning objectives on the page.");
    const tiles = [["FaLightbulb", "Data science", "What it is, where it is used", C.accent1], ["FaProjectDiagram", "The workflow", "From question to result", C.accent3], ["FaPython", "Why Python", "The tools we use", C.accent2], ["FaLaptopCode", "Setup", "Run your first cell", C.accent4]];
    for (let i = 0; i < 4; i++) {
      const x = 0.6 + i * 2.267, y = 1.6, w = 2.0, h = 3.0;
      card(s, x, y, w, h, "Goal card " + (i + 1));
      await badge(s, tiles[i][0], x + 0.25, y + 0.3, 0.9, tiles[i][3], tiles[i][1]);
      text(s, tiles[i][1], x + 0.25, y + 1.5, w - 0.4, 0.6, { fontSize: 20, bold: true });
      text(s, tiles[i][2], x + 0.25, y + 2.1, w - 0.4, 0.7, { fontSize: 14, color: C.accent5 });
    }
  }

  // =========================================================================================
  pres.addSection({ title: "Data science" });
  // 3. What is data science -------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "What Is Data Science?", "Data is a record of facts. Data science uses data to answer questions and make better decisions. Example: the teacher with 40 students' marks.");
    const steps = [["FaDatabase", "Data", "Marks in a register", C.accent1], ["FaSearch", "Patterns", "Weak in English", C.accent3], ["FaCheckCircle", "Decisions", "Extra English class", C.accent2]];
    for (let i = 0; i < 3; i++) {
      const x = 0.9 + i * 3.1;
      await badge(s, steps[i][0], x, 1.7, 1.5, steps[i][3], steps[i][1]);
      text(s, steps[i][1], x - 0.4, 3.35, 2.3, 0.5, { fontSize: 24, bold: true, align: "center" });
      text(s, steps[i][2], x - 0.4, 3.9, 2.3, 0.4, { fontSize: 16, color: C.accent5, align: "center" });
      if (i < 2) arrow(s, x + 1.7, 2.45, x + 2.9, 2.45, C.accent5, 3);
    }
  }

  // 4. Question: mobile data chart -------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "Question", "Ask the class. Your phone records data use every day. What question could that record answer? Real numbers: first 7 days of mobile_data.csv.");
    const rows = fs.readFileSync(path.join(ROOT, "docs/assets/data/mobile_data.csv"), "utf8").trim().split("\n").slice(1, 8).map((l) => l.split(","));
    await badge(s, "FaQuestion", 0.6, 1.6, 1.1, C.accent4, "Question mark");
    text(s, "Your phone counts the data you use.", 0.6, 3.0, 3.3, 0.9, { fontSize: 22, bold: true });
    text(s, "What question can it answer?", 0.6, 3.95, 3.3, 0.7, { fontSize: 18, color: C.accent5 });
    s.addChart(pres.charts.BAR, [{ name: "MB used", labels: rows.map((r) => "Day " + r[0]), values: rows.map((r) => Number(r[1])) }], {
      x: 4.3, y: 1.5, w: 5.1, h: 3.4, barDir: "col", chartColors: [THEME.colors.accent1], showLegend: false,
      showTitle: true, title: "Mobile data used (MB)", titleFontSize: 14, titleColor: THEME.colors.dk1,
      showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 12, dataLabelColor: THEME.colors.dk1,
      catAxisLabelFontSize: 12, valAxisLabelFontSize: 12, catAxisLabelColor: THEME.colors.accent5, valAxisLabelColor: THEME.colors.accent5,
      valGridLine: { color: "DFE4EC", size: 0.75 }, catGridLine: { style: "none" }, valAxisMinVal: 0, barGapWidthPct: 60,
    });
  }

  // 5. Where used ------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "Where It Is Used", "Each row starts with a question, uses data that already exists, and ends with a better decision.");
    const cards = [["FaCloudSun", "Weather", "Will it rain tomorrow?", C.accent1], ["FaStore", "Shop", "How much rice to stock?", C.accent2], ["FaUniversity", "Bank", "Is this payment strange?", C.accent3],
      ["FaHospital", "Hospital", "Which days are busiest?", C.accent2], ["FaMountain", "Tourism", "When do visitors come?", C.accent1], ["FaSchool", "College", "Which subject has most fails?", C.accent3]];
    for (let i = 0; i < 6; i++) {
      const col = i % 3, row = Math.floor(i / 3);
      const x = 0.6 + col * 3.0, y = 1.55 + row * 1.75, w = 2.8, h = 1.55;
      card(s, x, y, w, h, cards[i][1] + " card");
      await badge(s, cards[i][0], x + 0.2, y + 0.22, 0.7, cards[i][3], cards[i][1]);
      text(s, cards[i][1], x + 1.05, y + 0.28, w - 1.2, 0.5, { fontSize: 20, bold: true, valign: "middle" });
      text(s, cards[i][2], x + 0.2, y + 1.0, w - 0.4, 0.45, { fontSize: 14, color: C.accent5 });
    }
  }

  // 6. Workflow ring ----------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "The Workflow", "Six steps, and the cycle starts again because every answer raises a new question. Units VII to X follow these steps.");
    const steps = [["Ask", "question"], ["Collect", "data"], ["Clean", "data"], ["Explore", "data"], ["Model", "predict"], ["Share", "results"]];
    for (let i = 0; i < 6; i++) {
      const x = 0.7 + i * 1.5;
      numberBadge(s, i + 1, x, 1.7, 1.0, i === 5 ? C.accent2 : C.accent1, 28);
      text(s, steps[i][0], x - 0.25, 2.8, 1.5, 0.4, { fontSize: 18, bold: true, align: "center" });
      text(s, steps[i][1], x - 0.25, 3.2, 1.5, 0.35, { fontSize: 14, color: C.accent5, align: "center" });
      if (i < 5) arrow(s, x + 1.05, 2.2, x + 1.45, 2.2, C.accent5, 2.5);
    }
    // loop back: runs below the labels and points up at step 1
    s.addShape(pres.shapes.LINE, { x: 8.2, y: 3.75, w: 0, h: 0.6, line: { color: C.accent4, width: 3 } });
    s.addShape(pres.shapes.LINE, { x: 1.2, y: 4.35, w: 7.0, h: 0, line: { color: C.accent4, width: 3 } });
    arrow(s, 1.2, 4.35, 1.2, 3.75, C.accent4, 3);
    text(s, "New question, start again", 3.3, 4.2, 3.2, 0.3, { fontSize: 14, bold: true, align: "center", color: C.text1, fill: { color: C.background1 }, valign: "middle" });
  }

  // 7. Shop example ------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "Example: A Shop in Butwal", "Follow one example through the six steps. The owner wants to know what to stock.");
    const rows = [["Ask", "Top 3 items each week?"], ["Collect", "Sales book, spreadsheet"], ["Clean", "Fix missing, repeated rows"], ["Explore", "Totals, averages, charts"], ["Model", "Predict next week's sales"], ["Share", "A chart for the owner"]];
    for (let i = 0; i < 6; i++) {
      const col = Math.floor(i / 3), row = i % 3;
      const x = 0.6 + col * 4.6, y = 1.6 + row * 1.15;
      numberBadge(s, i + 1, x, y, 0.65, i === 5 ? C.accent2 : C.accent1, 20);
      text(s, rows[i][0], x + 0.9, y - 0.02, 3.4, 0.4, { fontSize: 20, bold: true });
      text(s, rows[i][1], x + 0.9, y + 0.38, 3.4, 0.4, { fontSize: 14, color: C.accent5 });
    }
  }

  // 8. Messy data ----------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Data science", "Real Data Is Messy", "One mark was typed as the word absent. Adding the marks fails. This is why the cleaning step exists.");
    code(s, ['marks = [78, 64, "absent", 92]', "print(sum(marks))"], 0.6, 1.7, 4.2, 1.4, 15);
    arrow(s, 4.95, 2.4, 5.45, 2.4, C.accent5, 3);
    card(s, 5.6, 1.7, 3.8, 1.4, "Error card");
    await badge(s, "FaExclamationTriangle", 5.8, 1.9, 0.6, C.accent6, "Warning");
    text(s, "TypeError", 6.6, 1.88, 2.7, 0.35, { fontSize: 18, bold: true, color: C.accent6 });
    text(s, "unsupported operand type(s) for +: 'int' and 'str'", 6.6, 2.25, 2.7, 0.75, { fontSize: 12, fontFace: CODE_FONT });
    text(s, "Clean the data first", 0.6, 3.7, 8.8, 0.6, { fontSize: 30, bold: true, color: C.text2 });
    text(s, "Missing  ·  repeated  ·  mistyped", 0.6, 4.35, 8.8, 0.4, { fontSize: 18, color: C.accent5 });
  }

  // =========================================================================================
  pres.addSection({ title: "Python" });
  // 9. Why Python -----------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Python", "Why Python?", "Python is a programming language, a way of giving instructions to a computer. Five reasons it suits beginners and professionals.");
    const items = [["FaBookOpen", "Easy to read", "Like plain English", C.accent1], ["FaGift", "Free", "No cost", C.accent3], ["FaBoxOpen", "Many libraries", "Ready-made code", C.accent2], ["FaUsers", "Big community", "Help everywhere", C.accent4], ["FaGlobe", "Runs everywhere", "Windows, macOS, Linux", C.accent1]];
    for (let i = 0; i < 5; i++) {
      const x = 0.6 + i * 1.8, y = 1.6, w = 1.6, h = 3.0;
      card(s, x, y, w, h, items[i][1] + " card");
      await badge(s, items[i][0], x + 0.25, y + 0.3, 0.85, items[i][3], items[i][1]);
      text(s, items[i][1], x + 0.2, y + 1.4, w - 0.35, 0.7, { fontSize: 16, bold: true });
      text(s, items[i][2], x + 0.2, y + 2.1, w - 0.35, 0.8, { fontSize: 14, color: C.accent5 });
    }
  }

  // 10. Libraries ------------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Python", "Libraries We Use", "A library is a ready-made toolbox of code written by other people. These are the ones this course uses.");
    const libs = [["pandas", "Tables of data", "Units VII–VIII", C.accent1], ["numpy", "Fast number work", "Unit VIII", C.accent3], ["matplotlib", "Charts", "Units VIII, X", C.accent2],
      ["seaborn", "Statistical charts", "Units VIII, X", C.accent1], ["scikit-learn", "Machine learning", "Unit IX", C.accent3], ["plotly + dash", "Dashboards", "Unit X", C.accent2]];
    for (let i = 0; i < 6; i++) {
      const col = i % 3, row = Math.floor(i / 3);
      const x = 0.6 + col * 3.0, y = 1.55 + row * 1.75, w = 2.8, h = 1.55;
      card(s, x, y, w, h, libs[i][0] + " card");
      text(s, libs[i][0], x + 0.25, y + 0.2, w - 0.5, 0.45, { fontSize: 20, bold: true, fontFace: CODE_FONT });
      text(s, libs[i][1], x + 0.25, y + 0.7, w - 0.5, 0.35, { fontSize: 14, color: C.accent5 });
      s.addText(libs[i][2], { x: x + 0.25, y: y + 1.08, w: 1.55, h: 0.3, shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.15, fill: { color: libs[i][3] }, line: { color: libs[i][3], width: 0 }, color: C.background1, fontSize: 12, bold: true, align: "center", valign: "middle", margin: 0, isTextBox: true });
    }
  }

  // 11. First look at Python --------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Python", "A First Look at Python", "Only a taste. Unit II teaches each idea in detail. Notice how plain the code looks.");
    const demos = [
      ["Variable", ['name = "Asha"', "marks = 78", "print(name, marks)"], "Asha 78"],
      ["Data type", ["print(type(78))", 'print(type("Asha"))'], "<class 'int'>\n<class 'str'>"],
      ["Operator", ["avg = (78+64+85)/3", "print(round(avg, 2))"], "75.67"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = 0.6 + i * 3.0, w = 2.8;
      s.addText(demos[i][0], { x, y: 1.5, w, h: 0.4, shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1, fill: { color: [C.accent1, C.accent3, C.accent2][i] }, line: { color: C.background1, width: 0 }, color: C.background1, fontSize: 16, bold: true, align: "center", valign: "middle", margin: 0, isTextBox: true });
      code(s, demos[i][1], x, 2.05, w, 1.45, 13);
      text(s, "OUTPUT", x, 3.65, w, 0.25, { fontSize: 11, bold: true, color: C.accent5, charSpacing: 3 });
      card(s, x, 3.95, w, 0.85, "Output " + (i + 1));
      text(s, demos[i][2], x + 0.2, 4.0, w - 0.4, 0.75, { fontSize: 15, fontFace: CODE_FONT, valign: "middle" });
    }
  }

  // =========================================================================================
  pres.addSection({ title: "Setup" });
  // 12. Where do I write Python -------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Setup", "Where Do I Write Python?", "Four ways to get Python. Anaconda and Miniconda need conda. Plain Python does not. Colab needs nothing installed. Disk sizes are from Anaconda's documentation.");
    const opts = [["FaBoxes", "Anaconda", "Everything ready", "About 9.7 GB", C.accent1], ["FaBox", "Miniconda", "Small start", "About 900 MB", C.accent3], ["FaPython", "Plain Python", "Smallest, no conda", "venv + pip", C.accent2], ["FaCloud", "Google Colab", "In the browser", "Nothing to install", C.accent4]];
    for (let i = 0; i < 4; i++) {
      const x = 0.6 + i * 2.267, y = 1.55, w = 2.0, h = 2.6;
      card(s, x, y, w, h, opts[i][1] + " card");
      await badge(s, opts[i][0], x + 0.25, y + 0.25, 0.8, opts[i][4], opts[i][1]);
      text(s, opts[i][1], x + 0.25, y + 1.2, w - 0.4, 0.4, { fontSize: 18, bold: true });
      text(s, opts[i][2], x + 0.25, y + 1.65, w - 0.4, 0.4, { fontSize: 14, color: C.accent5 });
      text(s, opts[i][3], x + 0.25, y + 2.08, w - 0.4, 0.35, { fontSize: 14, bold: true, color: opts[i][4] === C.accent4 ? C.text1 : opts[i][4] });
    }
    s.addText([{ text: "Then write code in ", options: {} }, { text: "Jupyter Notebook", options: { bold: true } }, { text: " (browser) or ", options: {} }, { text: "VS Code", options: { bold: true } }, { text: " (editor)", options: {} }], { x: 0.6, y: 4.4, w: 8.8, h: 0.5, fontSize: 18, color: C.text1, margin: 0, valign: "middle", isTextBox: true });
  }

  // 13. Decision flowchart -------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Setup", "Which One Should I Use?", "Same decision diagram as the Setting Up Python page. VS Code is an editor you add after choosing how to get Python.");
    const dia = (x, y, w, h, t) => s.addText(t, { shape: pres.shapes.DIAMOND, x, y, w, h, fill: { color: C.accent4 }, line: { color: C.accent4, width: 0 }, color: C.text1, fontSize: 12, bold: true, align: "center", valign: "middle", margin: 0, isTextBox: true });
    const box = (x, y, w, h, t1, t2, col) => s.addText([{ text: t1, options: { bold: true, fontSize: 14, breakLine: !!t2 } }].concat(t2 ? [{ text: t2, options: { fontSize: 12 } }] : []), { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.1, x, y, w, h, fill: { color: col }, line: { color: col, width: 0 }, color: col === C.accent4 ? C.text1 : C.background1, align: "center", valign: "middle", margin: 0, isTextBox: true });
    dia(0.5, 1.7, 2.3, 1.3, "Can you install software?");
    arrow(s, 1.65, 3.0, 1.65, 3.55, C.accent5, 2.5);
    text(s, "No", 1.8, 3.1, 0.5, 0.3, { fontSize: 12, bold: true });
    box(0.5, 3.55, 2.3, 0.7, "Google Colab", null, C.accent4);
    arrow(s, 2.8, 2.35, 3.4, 2.35, C.accent5, 2.5);
    text(s, "Yes", 2.88, 2.0, 0.5, 0.3, { fontSize: 12, bold: true });
    dia(3.4, 1.7, 2.3, 1.3, "What suits you?");
    const opts = [["Anaconda", "Everything ready", C.accent1, 1.4], ["Miniconda", "Smaller, uses conda", C.accent3, 2.2], ["Plain Python", "Smallest, no conda", C.accent2, 3.0]];
    for (const [t1, t2, col, y] of opts) {
      box(6.3, y, 2.6, 0.7, t1, t2, col);
      arrow(s, 5.7, 2.35, 6.28, y + 0.35, C.accent5, 2);
    }
    // final step band
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 3.4, y: 4.3, w: 5.5, h: 0.75, rectRadius: 0.1, fill: { color: C.background2 }, line: { color: C.background2, width: 0 } });
    text(s, "Then write code in:", 3.6, 4.3, 1.9, 0.75, { fontSize: 14, bold: true, valign: "middle" });
    box(5.45, 4.43, 1.7, 0.5, "Jupyter", "browser", C.text2);
    box(7.25, 4.43, 1.5, 0.5, "VS Code", "editor", C.text2);
  }

  // 14. Jupyter screenshot -----------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Setup", "A Jupyter Notebook", "A notebook has text cells and code cells. Run a cell and the result appears right below it. This is a real screenshot from Jupyter Notebook.");
    const shot = path.join(__dirname, "assets/jupyter-notebook.png"); // real screenshot, 640 x 450 css px
    const w = 5.2, h = w * 450 / 640, k = w / 640; // k = inches per css pixel
    s.addImage({ path: shot, x: 0.6, y: 1.5, w, h, altText: "Jupyter notebook with a text cell, a code cell that prints Hello, Data Science!, and a code cell that works out an average", shadow: shadow() });
    for (const [n, cy] of [[1, 130], [2, 251], [3, 423]]) numberBadge(s, n, 0.6 + 603 * k - 0.16, 1.5 + cy * k - 0.16, 0.32, C.accent2, 14);
    const legend = [["Text cell", "Notes for people"], ["Code cell", "You type Python"], ["Result", "Shown right below"]];
    for (let i = 0; i < 3; i++) {
      const y = 1.95 + i * 1.1;
      numberBadge(s, i + 1, 6.4, y, 0.5, C.accent2, 18);
      text(s, legend[i][0], 7.1, y - 0.03, 2.4, 0.35, { fontSize: 20, bold: true });
      text(s, legend[i][1], 7.1, y + 0.32, 2.4, 0.4, { fontSize: 14, color: C.accent5 });
    }
  }

  // =========================================================================================
  pres.addSection({ title: "Wrap-up" });
  // 15. Recap -------------------------------------------------------------------------------------------------
  {
    const s = titleSlide("LIGHT", "Wrap-up", "Quick Recap", "Five takeaways. Ask the class to say each one in their own words.");
    const items = ["Data science turns data into decisions", "Six steps, and the cycle repeats", "Python: easy, free, many libraries", "Pick one setup: Anaconda, Miniconda, plain Python or Colab", "Write code in Jupyter or VS Code"];
    for (let i = 0; i < items.length; i++) {
      const y = 1.5 + i * 0.7;
      await badge(s, "FaCheck", 0.6, y, 0.5, [C.accent1, C.accent3, C.accent2, C.accent1, C.accent3][i], "Check " + (i + 1));
      text(s, items[i], 1.35, y, 8.0, 0.5, { fontSize: 20, valign: "middle" });
    }
  }

  // 16. Next --------------------------------------------------------------------------------------------------
  {
    const s = pres.addSlide({ masterName: "DARK", sectionTitle: "Wrap-up" });
    s.addText("Next", { placeholder: "title" });
    await badge(s, "FaRocket", 0.6, 1.7, 1.2, C.accent4, "Rocket");
    text(s, "Lab 1", 2.2, 1.65, 6.5, 0.6, { fontSize: 32, bold: true, color: C.background1 });
    text(s, "Set up Python and run a first script", 2.2, 2.3, 6.5, 0.5, { fontSize: 22, color: C.background2 });
    text(s, "Then: Unit II, Python basics and operators", 2.2, 3.5, 6.5, 0.5, { fontSize: 18, color: C.accent4 });
    s.addNotes("Hand out Lab 1 from the Lab Sheets page. Unit II starts with variables, data types and operators.");
  }

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})().catch((e) => { console.error(e); process.exit(1); });
