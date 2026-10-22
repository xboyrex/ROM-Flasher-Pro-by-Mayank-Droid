from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "website"
class ProjectIntegrityTests(unittest.TestCase):
    def test_all_gallery_screenshots_exist(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        paths = set(re.findall(r'(?:src|data-lightbox)="(\./screenshots/\d+\.png)"', html))
        self.assertGreaterEqual(len(paths), 7)
        for item in paths:
            self.assertTrue((SITE / item.removeprefix("./")).is_file(), item)
    def test_local_assets_exist(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        for item in set(re.findall(r'(?:src|href)="(\./assets/[^\"]+)"', html)):
            self.assertTrue((SITE / item.removeprefix("./")).is_file(), item)
        self.assertIn("prefers-reduced-motion", (SITE / "styles.css").read_text(encoding="utf-8"))
        self.assertIn("data-workspace", (SITE / "app.js").read_text(encoding="utf-8"))
    def test_required_workspace_labels_present(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        for label in ["AOSP / Custom ROM", "HyperOS / MIUI", "Kernel & Recovery", "Terminal Console", "RAM Cleaner"]:
            self.assertIn(label, html)
    def test_readme_documents_safety_and_source_status(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("does **not** currently contain the original application source tree", readme)
        self.assertIn("Before you flash", readme)
        self.assertIn("RAM Cleaner", readme)
    def test_svg_assets_are_valid_xml(self):
        svgs = list((ROOT / "assets").rglob("*.svg")) + list((SITE / "assets").rglob("*.svg"))
        self.assertGreaterEqual(len(svgs), 20)
        for svg in svgs:
            self.assertEqual(ET.parse(svg).getroot().tag.split('}')[-1], "svg", str(svg))
    def test_deployed_site_has_no_parent_directory_doc_links(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('href="../docs/', html)
    def test_screenshot_files_match_docs_and_web_gallery(self):
        for n in range(1,8):
            self.assertTrue((ROOT/f"{n}.png").exists())
            self.assertTrue((ROOT/"docs/readme-screenshots"/f"{n}.png").exists())
            self.assertTrue((SITE/"screenshots"/f"{n}.png").exists())
if __name__ == "__main__": unittest.main()
