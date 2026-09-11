# COLORBOT SCRIPT



[![GitHub issues](https://img.shields.io/github/issues/red1gr/colorbot?style=for-the-badge)](https://github.com/red1gr/colorbot/issues)
[![GitHub license](https://img.shields.io/github/license/red1gr/colorbot?style=for-the-badge)](LICENSE) 


> ##  WARNING — READ BEFORE USE ⚠️
>
> **USING THIS SCRIPT IN ONLINE GAMES OR ANY MULTIPLAYER/COMPETITIVE ENVIRONMENT MAY RESULT IN YOUR ACCOUNT BEING PERMANENTLY BANNED.**
>
> Automated input tools such as this one violate the Terms of Service of most games and platforms. Anti-cheat systems are often able to detect this type of automation.
>
> **THE AUTHOR(S) AND CONTRIBUTOR(S) OF THIS PROJECT ARE NOT RESPONSIBLE FOR ANY BANS, SUSPENSIONS, LOSS OF ACCOUNT PROGRESS, OR OTHER CONSEQUENCES RESULTING FROM THE USE OF THIS SOFTWARE.**
>
> **USE ENTIRELY AT YOUR OWN RISK.**

## OVERVIEW

COLORBOT is an efficient AutoHotkey script designed to automate mouse clicks based on real-time pixel detection. It actively scans a user-defined area around the screen center for a specific target color. Upon detection, it triggers a rapid mouse click, making it ideal for tasks requiring quick reactions or repetitive input. The script offers flexible activation modes Toggle, Hold, and Off-controlled via customizable hotkeys, alongside a compact, always-on-top graphical user interface for easy configuration and monitoring.

## FEATURES

-   **Intelligent Pixel Scanning**: Scans pixels around the screen center to detect a user-defined target color.
-   **Optimized Input Speed**: Incorporates input optimization techniques for fast and responsive auto-clicking.
-   **Automated Clicking**: Performs an auto-click immediately upon target color detection.
-   **Multiple Operational Modes**: Switch between `Toggle` (on/off), `Hold` (active while hotkey is pressed), and `Off` modes using dedicated hotkeys.
-   **Minimal Always-On-Top GUI**: Provides a compact, non-intrusive interface for quick settings adjustments and status display.
-   **Sound Feedback**: Delivers auditory cues for mode changes or detection events.
-   **Fast-Click Option**: Includes a configurable option for ultra-rapid clicking.
-   **Customizable Target Color**: Easily set the specific color to be detected.
-   **Adjustable Scan Area**: Define the pixel radius around the screen center for detection.


## TECK STACK

[![AutoHotkey](https://img.shields.io/badge/AutoHotkey-1.1-green?style=for-the-badge&logo=autohotkey)](https://www.autohotkey.com/)

## QUICK START

### Prerequisites
To run this script, you need to have AutoHotkey installed on your Windows machine.

-   **AutoHotkey v1.1**: Download and install it from the [official AutoHotkey website](https://www.autohotkey.com/download/).

### INSTALLATION

1.  **Download the script**
    Download the `rd_macro.ahk` file directly from this repository:
    ```bash
    git clone https://github.com/red1gr/COLORBOT.git
    cd COLORBOT
    ```
    Alternatively, you can simply download the `rd_macro.ahk` file directly.

2.  **Run the script**
    Once AutoHotkey is installed, you can run the script by simply double-clicking `rd_macro.ahk`. The script will start running in the background, and its icon will appear in your system tray.

### CONFIGURATION & USAGE

Upon running `rd_macro.ahk`, a minimal GUI will appear, typically in an always-on-top fashion. You can use this GUI to:

-   **Set Target Color**: Input or select the hexadecimal color code that COLORBOT should detect.
-   **Adjust Scan Area**: Configure the width and height of the pixel scanning area around the screen center.
-   **Enable Fast-Click**: Toggle the fast-click option for quicker responses.

**Hotkeys:**
The script defines hotkeys to switch between its operational modes. You will need to examine the `rd_macro.ahk` file for the exact hotkey assignments. Common assignments are often `F1`, `F2`, `F3` etc., or custom combinations.

-   **Toggle Mode Hotkey**: Activates/deactivates the auto-clicking functionality.
-   **Hold Mode Hotkey**: Activates auto-clicking only while the hotkey is pressed.
-   **Off Mode Hotkey**: Completely disables the auto-clicking.

**To customize hotkeys or initial settings further, you can directly edit the `rd_macro.ahk` file in a text editor.** Look for variables and `Hotkey` commands near the top of the script.

## PROJECT SRUCTURE

```
COLORBOT/
├── README.md       # This documentation file
└── rd_macro.ahk    # The main AutoHotkey script containing all logic
```

## CONFIGURATION

The primary configuration for COLORBOT is handled directly within the `rd_macro.ahk` script file itself, as well as through its interactive GUI.

### SCRIPT BASED CONFIGURATION 
You can open `rd_macro.ahk` with any text editor (like Notepad, VS Code, or AutoHotkey Studio) to modify variables at the top of the file. This typically includes:

-   `TargetColor`: The hexadecimal color code to look for.
-   `ScanAreaWidth`, `ScanAreaHeight`: Dimensions for the pixel search area.
-   `FastClickEnabled`: A boolean (1 or 0) to enable or disable the fast-click feature.
-   `Hotkey` assignments: Change the keys used to toggle modes.

### GUI-BASED CONFIGURATION
The "always-on-top GUI" offers a convenient way to adjust critical settings on the fly without restarting the script. Any changes made through the GUI will take precedence over initial script settings for the current session.

## DEVELOPMENT

This project is a single AutoHotkey script. Development primarily involves:

-   **Editing**: Modifying the `rd_macro.ahk` file using an AutoHotkey-aware editor.
-   **Testing**: Running the script and observing its behavior in real-time.
-   **Debugging**: Utilizing AutoHotkey's built-in debugging features or simple `MsgBox` commands.




## CONTRIBUTING

- WE WELCOME CONTRIBUTIONS! IF YOU HAVE SUGGESTIONS FOR IMPROVEMENTS, FEATURE REQUESTS, OR BUG REPORTS, PLEASE OPEN AN ISSUE OR SUBMIT A PULL REQUEST ON OUR GITHUB REPOSITORY.

## LICENSE

THIS PROJECT IS LICENSED UNDER THE [APACHE LICENSE 2.0](LICENSE) - SEE THE [LICENSE](LICENSE) FILE FOR DETAILS.

## SUPPORT & CONTACT

- ISSUES:  [GITHUB ISSUES](https://github.com/red1gr/colorbot/issues)
- CONTACT: [SUPPORT CONTACT](mailto:mail@red1gr.dev)
