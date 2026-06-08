# Certificate Automation

A simple Python script that generates personalized certificates in bulk from an Excel sheet.

Instead of manually editing each certificate, just provide:

- A certificate template (`certificate.png`)
- An Excel file containing participant names

and the script will automatically generate certificates for everyone.

## How to Use

1. Place your certificate template as `certificate.png`
2. Add participant names to `test.xlsx` under a column named `Name`
3. Run:

```bash
python main.py
```

4. Generated certificates will be saved in the `output` folder.

## Customization

You can easily modify the script to match your certificate design:

```python
FONT_SIZE = 65
y = 750
```

- Change the font size
- Adjust the text position (X/Y coordinates)
- Use your own font file

No redesigning of certificates is required. Just update the template and Excel sheet.

## Tech Stack

- Python
- Pillow (PIL)
- Pandas

## Future Improvements

- PDF export
- Emailing certificates directly to participants
- Simple web interface