# Using Slugger

Slugger 1.0 — a Mac file-renaming utility

Open Slugger.app. Click Add Files or drag files into the window.
Review Original name, New name, and Status, then click Rename Files.

Example: My Summer Photo.JPG → my-summer-photo.JPG

• Handles a single file or a batch, including files from different folders.
• Preserves the final extension by default.
• Enable “Lowercase extensions” to lowercase every final
  extension and normalize .JPEG/.jpeg/.JPG to .jpg. This preference is saved
  between sessions. The checkbox is in the main window.
  The preview updates immediately. This renames files; it does not convert
  their contents. Undo restores the original extension too.
• Converts the filename stem to lowercase, removes accents, transliterates
  supported scripts to Latin, and replaces punctuation and spaces with hyphens.
• Preserves the leading dot on hidden files.
• Does not rename folders or follow symbolic links. Standard renaming stays local.
• Blocks conflicting names rather than adding numbers or overwriting files.
• Files remain in their original folders and their contents are unchanged.
• Undo Last Rename restores the last batch while the app remains open.
  Undo history is replaced by the next successful rename and lost on quitting.

Renaming can affect links or references to files. Use the preview to check names.

This app was built locally for Apple Silicon. You can keep it here or copy it
into Applications. Slugger.swift is the complete editable source.

Keyboard shortcuts: ⌘O adds files, Return renames the ready batch,
⌘Z undoes the last batch.

AI Agent Integration

Choose Claude or Codex under AI Agent, then click Suggest Names.
Review the proposed names before clicking Rename. Reset returns to ordinary
slugified names; choose Off to turn AI off. Cancel stops an active request.
Your provider choice is saved. AI supports up to 25 files per request.

The integration uses the installed Claude Code or Codex CLI and its active
sign-in. For subscription access, sign in with your Claude or ChatGPT account.
API-key sign-ins use API billing. Slugger does not extract, store, or transfer
your credentials. Usage is subject to your provider's allowance and limits.

One-time setup in Terminal:
• Claude Code: install from https://code.claude.com/docs/en/setup,
  run claude, and sign in.
• Codex: install from https://developers.openai.com/codex/cli/,
  then run codex login.
The Slugger → AI Setup… menu contains a short reminder.

Clicking Suggest Names sends the listed filenames, image previews, and bounded excerpts to
the selected provider. Up to 8,000 characters per file are included. Text
files and the first three PDF pages are supported. Images send a resized visual preview (up to 1536 pixels), with metadata
removed. AI can name the visible subject or scene. Files without readable text use filenames
only; Office files are not parsed.

The agent generates filename stems only. Your lowercase-extension preference
still applies. Conflicts and invalid suggestions are blocked. Files aren't
renamed until you click Rename; their contents are never changed. The CLI
runs in a temporary empty folder with agent customizations disabled. Claude
tools are disabled; Codex runs read-only with execution tools disabled.
