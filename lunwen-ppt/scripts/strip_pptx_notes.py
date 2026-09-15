#!/usr/bin/env python
import argparse
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
ET.register_namespace("", REL_NS)
ET.register_namespace("p", P_NS)
ET.register_namespace("", CT_NS)


def clean_xml(name, data):
    if name == "[Content_Types].xml":
        root = ET.fromstring(data)
        for item in list(root):
            if item.tag.endswith("Override") and item.attrib.get("PartName", "").startswith("/ppt/notes"):
                root.remove(item)
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)
    if name == "ppt/presentation.xml":
        root = ET.fromstring(data)
        for item in list(root):
            if item.tag == f"{{{P_NS}}}notesMasterIdLst":
                root.remove(item)
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)
    if name.endswith(".rels"):
        root = ET.fromstring(data)
        changed = False
        for item in list(root):
            rel_type = item.attrib.get("Type", "")
            if rel_type.endswith("/notesSlide") or rel_type.endswith("/notesMaster"):
                root.remove(item)
                changed = True
        if changed:
            return ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return data


def main():
    ap = argparse.ArgumentParser(description="Remove PowerPoint notes parts for maximum openability.")
    ap.add_argument("pptx")
    ap.add_argument("--out")
    args = ap.parse_args()
    source = Path(args.pptx).resolve()
    target = Path(args.out).resolve() if args.out else source
    with NamedTemporaryFile(delete=False, suffix=".pptx", dir=target.parent) as stream:
        temp = Path(stream.name)
    with ZipFile(source, "r") as zin, ZipFile(temp, "w", ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            name = item.filename
            if name.startswith("ppt/notesSlides/") or name.startswith("ppt/notesMasters/"):
                continue
            zout.writestr(item, clean_xml(name, zin.read(name)))
    shutil.move(temp, target)
    print(target)


if __name__ == "__main__":
    main()
