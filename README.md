# Assign selected items to net

This is a Kicad 9.0 plugin that lets you select whatever you want in PCB Editor and assign it to any existing net you have defined.

I use this for assigning nets to graphics objects that I imported from DXFs.I can design custom zones or coils in CAD then use them functionally in my PCBs.

Copy this Python file into your plugin directory, which for me is this on Linux: ~/.local/share/kicad/9.0/scripting/plugins. Kicad won't detect it if you put it in a subdirectory. After restarting or refreshing, you should find it in Tools > External Plugins.

To use:
1. Select any combination of pads, traces, vias, graphics on copper layers, etc.
2. Tools > External Plugins > Assign Net to Selection
3. Menu will pop up. Select the net from the drop-down and hit ok.
