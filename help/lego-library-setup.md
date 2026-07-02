# LEGO Library Setup

The LEGO Library is the folder LEGO Builder uses for managed project data.

## Choose a Folder

In add-on preferences, select a folder for `LEGO Library Folder`. This can be a
new folder or an existing folder you want LEGO Builder to manage.

## Create the Folder Structure

Use `Create LEGO Library` to create the expected folders and marker file.

The current structure is:

```text
LEGO Library/
├── ldraw/
│   ├── parts/
│   ├── p/
│   ├── unofficial/
│   └── models/
├── cache/
│   ├── metadata/
│   ├── geometry/
│   └── thumbnails/
├── downloads/
├── projects/
├── logs/
└── lego_builder_library.toml
```

LEGO Builder creates missing folders without deleting or overwriting user files.

## Marker File

`lego_builder_library.toml` identifies the folder as a LEGO Builder library. It
does not store user-specific settings.
