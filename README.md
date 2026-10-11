# Slugger

A native macOS utility for renaming one file or a batch into clean, consistent slugs.
Version **1.0**. Licensed under the [MIT license](LICENSE).

- Preview names, block conflicts, and undo the last batch.
- Keep extensions or optionally lowercase them and normalize JPEG to jpg.
- Optionally suggest names from text, PDFs, and image content through an installed Claude Code or Codex CLI.
- Standard renaming stays local; AI is off by default.

## Build

Requires macOS 14 or later, Apple Command Line Tools (or Xcode), and Python 3.
There are no third-party runtime libraries or package downloads.

```sh
python3 scripts/build.py
open build/Slugger.app
```

The script compiles for the current Mac architecture, builds the icon, signs the
app ad hoc, verifies its signature, and creates `build/Slugger.zip`. Use a
Developer ID signature and notarization for a public downloadable release.
The repository itself can be shared without publishing a compiled release.

## Test

```sh
build/Slugger.app/Contents/MacOS/Slugger --self-test
```

These local tests cover slug rules, extensions, renaming and undo, collision
handling, content preservation, AI response validation, cancellation, bounded
text extraction, and image metadata removal. They do not call an AI provider.
Live CLI integration depends on the installed provider version and sign-in.

## Privacy and usage

See [USAGE.md](USAGE.md) for instructions and what is sent when you choose AI.
Slugger uses the selected CLI's active sign-in; credentials are not bundled or
stored by Slugger. Provider subscriptions and API billing are separate from
this project's license. Review AI suggestions before applying a rename.

## Project layout

- `Sources/Slugger.swift`: AppKit interface, rename logic, optional AI integration, and local self-tests.
- `Resources/Info.plist`: application metadata.
- `Resources/AppIcon.png`: full square icon artwork; macOS renders its outer shape.
- `scripts/build.py`: portable local build and packaging script.

## Contributing

Keep changes focused, run the self-tests, and check the app's interface on macOS.
Do not include personal files, credentials, generated builds, or provider account
information in contributions.
