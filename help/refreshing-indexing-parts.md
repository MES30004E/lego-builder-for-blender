# Refreshing and Indexing Parts

`Refresh Library` scans the configured LDraw library and builds an in-memory
metadata index.

## What It Reads

The indexer scans `.dat` files under the LDraw `parts/` folder and records basic
metadata such as part number, filename, display name, and relative path.

## What It Does Not Do

Refreshing the library does not:

- Import geometry into Blender.
- Create meshes.
- Generate thumbnails.
- Download libraries.
- Clear caches.
- Validate full LDraw syntax.
- Add search or part browsing UI.

The index is stored in memory and resets when Blender reloads the extension.
