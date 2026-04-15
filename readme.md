# AIMP-Floating-Lyrics-Plugin-Localization

> Also see [Post on AIMP Forum](https://aimp.ru/forum/index.php?topic=77574.0).

> What's this?  
> The repo provides AIMP-Floating-Lyrics-Plugin translations.  
> As I'm from China, I only know about Chinese and English. If you are interested, you can help translate this plugin to other languages.

### About Plugin

Here I present my hand-made plugin: AIMP Floating Lyrics Player and Editor Plugin, as a software developer, this is my hobby project. If you have found any issue, it would be a great help to tell me :)!
It has these features:

1. It plays synchronized lyrics file(currently only supports ".lrc" file format with UTF-8 or ASCII encoding) for your song, it reads from your local lrc file alongside with your song file, or if your song file has synchronized lyrics embedded(like ID3v2 tag supported by AIMP), it will also play it;
2. For playing lyrics, you can style text color, text size, text shadow and more, I have written a preference window to configure these(and more configurations will be brought in the future updates);
3. For playing lyrics, currently I designed 2 playing styles, one is to fade in fade out lyrics text, another style is to scroll lyrics horizontally;
4. You can make or edit your own ".lrc" file, just right click the playing lyrics window, choose "Make / Edit Lyrics". Or in AIMP playlist, right click playlist item(aka, songs in your library), choose "Send to - Lyrics Editor".
5. About the lyrics editor, when it opens, it will fill basic information automatically if it finds that, otherwise, you need to input information yourself.
6. Some hint to use the lyrics editor: Currently I exposed 3 hotkeys to inert/replace/delete timestamp on active line, they are bound with F7/F8/F9 keys globally by default. You can always change these hotkeys in AIMP's "Hotkeys" configuration, but remember, local hotkeys won't work, because the lyrics editor is not recognized by AIMP as local window. The inserted or replaced timestamp is always the timestamp that AIMP is current playing at, so ideally you just play the song once and inserted timestamps all by yourself. There are also some handy buttons there, you can hover on them to see brief descriptions.

\*Tip: you can set lyrics playing window's background color to a totally transparent value, which looks fancy, but it will make context menu harder to open, you can preview in my screenshots.

### How to Install & Use

To install and use this plugin,

1. Download and install ".NET 8.0 Desktop Runtime":
    - for AIMP x64: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.26-windows-x64-installer
    - for AIMP x86: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.26-windows-x86-installer
2. Download and install "Visual C++ Redistributable 2012" from https://www.microsoft.com/en-us/download/details.aspx?id=30679, make sure to pick x86 or x64, which depends on AIMP x86 or x64 your are using. (a known issue listed below also mentions this runtime package, if you are not sure, I recommend you just download and install it);
3. Unzip "aimp*floating_lyrics_x[86_or_64]\_ver*[VERSION].zip" and drop extracted "aimp_floating_lyrics" folder to "[your-AIMP-x86-or-x64-installation-folder]/Plugins";
4. Finally, open AIMP and check "Floating Lyrics" menu item in AIMP's main menu to show lyrics player window and let's roll!

### Plugin Screenshots

![Floating lyrics Window](/screenshots/floating_window.jpg)
![Floating lyrics Window Context Menu](/screenshots/context-menu.jpg)
![Lyrics Editor](/screenshots/lyrics_editor.jpg)
![Preference Window](/screenshots/preference_window.jpg)
![Configuration Panel in AIMP](/screenshots/configuration_panel_in_AIMP.jpg)

### Change Logs

#### 1.0.1 (2026.04.15)

- Now supports both AIMP 5 x86 and x64! Make sure to download corresponding zip file and install corresponding runtime packages (see "How to Install & Use" section below)
- Fix an issue causing lyrics editor to crash when user clears "offset" input
- Add option panel in AIMP's preference window, provides functionality to open plugin's preference window or reset lyrics playing window's position there
- Optimize code originally porting from .NET Framework to ensure better compatibility with .NET 8.0
- Update project dependencies: WPF.UI from 4.0.3 to 4.2.0; my dotnet-lrc-parser 0.3.0 to 0.3.1(minor changes concerning .NET 8.0)
- Other stability optimizations and adjustments

#### 1.0.0 (2026.04.12)

Original Release
