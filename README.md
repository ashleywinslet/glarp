# Glarp Home Screen — Pixel-Accurate Clone (v2)

This version uses your actual screenshot as the UI, with the status bar
(time, dynamic island, wifi, battery) cropped off, and just two working
hotspots layered on top: **Send** and **+ Cash In**. Everything else
(Load, Transfer, Bills, tabs, promo banner, bottom nav, etc.) is part of
the static image, exactly as in your screenshot.

## Files
- `app.py` — Flask backend (balance stored in session)
- `templates/index.html` — the page: your screenshot + invisible clickable
  hotspots + two bottom-sheet modals
- `static/replacement.png` — your screenshot, cropped to remove the status bar

## Run instructions

```bash
pip install flask
python3 app.py
```

Open `http://127.0.0.1:5000` locally, or `http://<your-PC-IP>:5000` on your
iPhone (same Wi‑Fi — see earlier instructions for finding your IP and
allowing it through the firewall).

## How it works
- The screenshot is shown at full width as the entire background.
- A small rectangle the same blue as the balance panel sits exactly over
  the "2,516.04" text and displays the **live** balance in a matching bold
  font — so it updates in place without looking pasted on.
- Invisible buttons sit exactly over the eye icon, the **+ Cash In** pill,
  and the **Send** icon/label — same tap targets as the real app, but the
  artwork underneath never changes.
- **Send**: opens a bottom sheet → recipient + amount → deducts from
  balance (validates funds/amount).
- **+ Cash In**: opens a bottom sheet → amount → adds to balance.
- Eye icon toggles the balance between the number and `••••••`.
- All positions are percentage-based, so it scales correctly across
  iPhone screen sizes.

## Notes
- If you want to re-crop or replace the screenshot, swap
  `static/replacement.png` for a same-aspect-ratio image and the hotspot
  percentages in `index.html` should still line up closely — nudge the
  `left/top/width/height` percentages on `.balance-mask`, `#eyeToggle`,
  `#cashInBtn`, and `#sendBtn` if needed.
- Balance persists per-browser-session (Flask `session`), so it won't sync
  between your phone and a desktop browser tab.
