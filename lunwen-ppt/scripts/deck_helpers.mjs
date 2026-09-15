import fs from 'node:fs/promises';

export async function imageBytes(filePath) {
  const bytes = await fs.readFile(filePath);
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

export function addText(slide, { name, text, x, y, w, h, size = 22, color = '#172B4D', bold = false, align = 'left', font = 'Microsoft YaHei' }) {
  const shape = slide.shapes.add({
    geometry: 'textbox', name,
    position: { left: x, top: y, width: w, height: h },
    fill: 'none', line: { style: 'solid', fill: 'none', width: 0 },
  });
  shape.text = text;
  shape.text.style = { fontFamily: font, fontSize: size, color, bold, alignment: align, verticalAlignment: 'middle' };
  return shape;
}

export function addPanel(slide, { name, x, y, w, h, fill = '#FFFFFF', line = '#CEDCE6', radius = 'rounded-xl' }) {
  return slide.shapes.add({
    geometry: 'roundRect', name,
    position: { left: x, top: y, width: w, height: h },
    fill, line: { style: 'solid', fill: line, width: line === 'none' ? 0 : 1.2 },
    borderRadius: radius,
  });
}

export function addHeader(slide, { section, title, page, theme }) {
  addText(slide, { name: `section-${page}`, text: section, x: 64, y: 28, w: 300, h: 28, size: 14, color: theme.colors.cyan, bold: true });
  addText(slide, { name: `title-${page}`, text: title, x: 64, y: 58, w: 1100, h: 58, size: theme.font_sizes.title, color: theme.colors.navy, bold: true });
  slide.shapes.add({ geometry: 'rect', name: `rule-${page}`, position: { left: 64, top: 122, width: 1152, height: 3 }, fill: theme.colors.cyan, line: { style: 'solid', fill: 'none', width: 0 } });
  addText(slide, { name: `page-${page}`, text: String(page).padStart(2, '0'), x: 1170, y: 660, w: 46, h: 24, size: 13, color: theme.colors.muted, bold: true, align: 'right' });
}

export function addBullets(slide, { name, items, x, y, w, h, size = 22, color = '#172B4D' }) {
  return addText(slide, { name, text: items.map((item) => `• ${item}`).join('\n'), x, y, w, h, size, color });
}
