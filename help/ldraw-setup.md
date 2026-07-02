# LDraw Setup

LEGO Builder needs an LDraw-compatible library folder before it can index part
metadata.

## Required Folders

A valid LDraw library folder must contain:

- `parts/`
- `p/`

The current validation only checks for these folders. It does not perform full
LDraw compliance checks.

## Managed LDraw Folder

If you created a LEGO Library, use `Use LEGO Library LDraw` to set the LDraw
path to the managed `ldraw/` folder.

## Existing LDraw Folder

You can also select an existing LDraw library folder manually. LEGO Builder does
not copy, download, or update LDraw files yet.
