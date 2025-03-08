# Create Figma Variables Automation (CFVA)

<img src="https://github.com/Dedo-Finger2/create-figma-variables-python/blob/master/images/figma-variables-cover.png?raw=true" />

---

## About

This project creates figma variables using PyautoGUI and a .txt file with your CSS variables. For now it only works with color variables, separating light from dark theme colors.
It's highly recommended to use Realtime Colors since this project was originally made to handle how THEY export css variables. If you want to make your own, follow this format:

```css
:root[data-theme="light"] {
  --variable-01: #fff;
  ...
}
:root[data-theme="dark"] {
  --variable-01: #000;
  ...
}
```

## How to use

1. Clone the project
```
git clone https://github.com/Dedo-Finger2/create-figma-variables-python.git
```
2. Install the dependencies
```
pip install -r requirements.txt
```
3. Change the variables inside the variables.txt to match your own
4. Run the main.py file
5. Create two collections: "Light" and "Dark" and leave the variables popover's sidebar open just like its shown in this project cover
6. Close the variables popover
7. Confirm/Close the python popover and leave the script to execute it's magic

## Troubleshoot
### Gnome-Screenshot problems
If you're using KDE Plasma with Wayland, switch to X11 and try again.
