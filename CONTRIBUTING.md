# Contributing

1. Open an issue for a factual correction, UI issue or docs change before doing broad changes.
2. Keep product claims limited to behavior supported by source code or reproducible testing. Screenshots establish visual controls, not successful execution.
3. Keep screenshots local to the repo, use descriptive alt text and optimize large raster files.
4. Preserve the safety guidance for data wiping, bootloader changes, partitions and RAM optimization.
5. Run the static check before committing:

   ```bash
   python -m unittest discover -s tests -v
   ```

6. Make website changes in `website/index.html`, `website/styles.css` and `website/app.js`; avoid adding frameworks unless needed.
