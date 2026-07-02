# Troubleshooting

## The LEGO Tab Is Missing

Confirm the extension is installed and enabled in Blender preferences. The tab
appears in the 3D View sidebar.

## LEGO Library Shows Not Configured

Open add-on preferences and choose a LEGO Library folder.

## LEGO Library Shows Incomplete

Use `Create LEGO Library` to create the expected folder structure and marker
file.

## LDraw Library Shows Invalid Path

Check that the selected LDraw folder exists and contains both `parts/` and `p/`.

## Refresh Library Does Not Index Parts

Confirm the LDraw path points at the library root, not directly at the `parts/`
folder. The root folder should contain `parts/` and `p/`.

## Preferences Reset After Reinstall

Blender may remove add-on preferences when an extension is uninstalled or
reinstalled. Re-select your LEGO Library and LDraw paths if needed.
