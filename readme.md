<h1 align="center">
    <img src="icon/brand_icon256.png" alt="Plugin's branch icon" width="200">
    <br/>
    AIMP Floating Lyrics Plugin
</h1>

> Also see [Post on AIMP Forum](https://aimp.ru/forum/index.php?topic=77574.0).

> What's this?  
> The repo provides AIMP-Floating-Lyrics-Plugin localization files.  
> As I'm from China, I only know about Chinese and English. If you are interested, you can help translate this plugin to other languages.

### About Plugin

Here I present my hand-made plugin: AIMP Floating Lyrics Player and Editor Plugin, as a software developer, this is my hobby project. If you have found any issue, it would be a great help to tell me :)!
It has these features:

1. It plays synchronized lyrics file(currently only supports ".lrc" file format with UTF-8 or ASCII encoding) for your song, it reads from your local lrc file alongside with your song file, or if your song file has synchronized lyrics embedded(like ID3v2 tag supported by AIMP), it will also play it;
2. For playing lyrics, you can style text color, text size, text shadow and more, I have written a preference window to configure these(and more configurations will be brought in the future updates);
3. For playing lyrics, currently I implemented 3 playing styles, one-line fade in fade out lyrics text, scroll horizontally and two-line;
4. You can make or edit your own ".lrc" file, just right click the playing lyrics window, choose "Make / Edit Lyrics". Or in AIMP playlist, right click playlist item(aka, songs in your library), choose "Send to - Lyrics Editor".
5. About the lyrics editor, when it opens, it will fill basic information automatically if possible, otherwise, you should input information yourself.
6. Some hint to use the lyrics editor: Currently I exposed 3 hotkeys to inert/replace/delete timestamp on active line, they are bound with F7/F8/F9 keys globally by default. You can always change these hotkeys in AIMP's "Hotkeys" configuration, but remember, local hotkeys won't work, because the lyrics editor is not recognized by AIMP as local window. The inserted or replaced timestamp is always the timestamp that AIMP is current playing at, so ideally you just play the song once and inserted timestamps all by yourself. There are also some handy buttons there, you can hover on them to see brief descriptions.

\*Tip: you can set lyrics playing window's background color to a totally transparent value, which looks fancy, however, even though it is transparent, it is not transparent for mouse clicks, which may cause some inconvenience. There is a workaround(since v1.3.0) when mouse hovers at that time, background will become less transparent. You can also enable click-through to prevent this.

### How to Install & Use

#### **Since v1.3.2:**

Plugin' file name looks like "aimp_floating_lyrics_x86_64_net[DOTNET_RUNTIME_VERSION]\_ver\_[VERSION].aimppack" since this version.

Be sure to install corresponding version of dotnet runtime(`DOTNET_RUNTIME_VERSION`) first (You only need to install one of the files listed below):

> .NET 8.0 Desktop Runtime (`DOTNET_RUNTIME_VERSION = net8.0`):
>
> - for AIMP x64: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.30-windows-x64-installer
> - for AIMP x86: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.30-windows-x86-installer
>
> .NET 10.0 Desktop Runtime (`DOTNET_RUNTIME_VERSION = net10.0`):
>
> - for AIMP x64: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-10.0.11-windows-x64-installer
> - for AIMP x86: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-10.0.11-windows-x86-installer

Plugin files are released as `.aimppack` format, you can easily install them with AIMP's built-in install button.

> .NET 8.0 releases may be removed in the future version if .NET 8 reaches end-of-life, so it is recommended to install .NET 10.0 Desktop Runtime from now on.

#### **Prior to v1.3.2:**

1. Download and install ".NET 8.0 Desktop Runtime":
    - for AIMP x64: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.30-windows-x64-installer
    - for AIMP x86: https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.30-windows-x86-installer

2. ~~Download and install "Visual C++ Redistributable 2012" from https://www.microsoft.com/en-us/download/details.aspx?id=30679, make sure to pick x86 or x64, which depends on AIMP x86 or x64 your are using. (a known issue listed below also mentions this runtime package, if you are not sure, I recommend you just download and install it);~~

You no longer need to install VC++ 2012 since v1.2.4, plugin has already included necessary files.

3. Unzip "aimp_floating_lyrics_x[86\_or\_64]\_ver\_[VERSION].zip" and drop extracted "aimp_floating_lyrics" folder to "[your-AIMP-x86-or-x64-installation-folder]/Plugins";
4. Finally, open AIMP and check "Floating Lyrics" menu item in AIMP's main menu to show lyrics player window and let's roll!

### Troubleshooting

In some cases, AIMP might disable the plugin so you won't be able to use the plugin in AIMP, you can follow these steps to fix:

> i. Make sure to close AIMP instance before proceed;  
> ii. Open "AIMP.ini" file within "[your-AIMP-installation-directory]/Profile" directory, search and delete these lines (it may differ from your file, but should look similar):
>
> ```ini
> [Plugins]
> aimp_floating_lyrics.dll=0
>
> [Plugins.CachedInfo]
> aimp_floating_lyrics.dll=0|||||1552900961
> ```
>
> iii. If this still does not work, you can try to delete whole `[aimp_floating_lyrics_plugin]` section in "AIMP.ini" file, this will reset all configurations of my plugin.

Try launching AIMP after that, plugin should work now.

### Plugin Screenshots

![Floating lyrics Window](/screenshots/floating_window.png)
![Floating lyrics Window Context Menu](/screenshots/context-menu.jpg)
![Lyrics Editor](/screenshots/lyrics_editor.jpg)
![Preference Window](/screenshots/preference_window.jpg)
![Configuration Panel in AIMP](/screenshots/configuration_panel_in_AIMP.jpg)

### Change Logs

#### 1.3.4 (2026.08.16)

- Feat: Introduce dark/light theme for sub-windows(preference window and etc.), currently it follows AIMP's night mode preference
- Feat(windows 11 only): Sub-windows now set mica backdrop as default, on windows 10, it falls back to pure color
- Feat: Ever annoyed by the fact that lyrics playing window will reload after preference applied? Good news is, since this release, only partial preferences will trigger the reloading(which is necessary)
- Feat: Add "toggle click-through" on lyrics playing window's context menu
- Fix: Incorrect position calculation when two-line placement is "center"
- Fix: Plugin crashes if user closes lyrics playing window while preference window is also open
- Optimize: As automation tests go further, crash is spotted on a fresh new windows installation, that's because a basic Visual C++ Redistributable installation is still required, to get away trouble installing it, plugin has added required dlls(msvcp*.dll and vcruntime*.dll), for more details, please refer to https://learn.microsoft.com/en-us/cpp/windows/determining-which-dlls-to-redistribute?view=msvc-170
- Chore(dep): Upgrade "Microsoft.Web.WebView2" to 1.0.4129.50
- Chore: change lyrics playing window's default background to black, which in my opinion looks better
- Other minor optimizations and fixes

#### 1.3.3.1 (2026.08.10)

- Fix: Add back missing lyrics scroll window resizing resources before v1.3.3, they are accidentally removed by me while enhancing WPF.UI related resources in v1.3.3

#### 1.3.3 (2026.08.08)

> This is majorly a maintenance version which introduces UI automation tests, which helps identify bugs.

- Feat: Happy to announce that plugin's brand icon is finally added, which is designed by **杨桃 Yiting**
- Feat: Add about dialog, so there is a place to show plugin's icon and credits
- Feat: Preference window now adds "reset to default" buttons for each group
- Feat: Add localization file entries for Lyrics Editor
- Feat: Add a preference to configure text alignment for multi-language lyrics
- Feat: Add a preference to configure two-line placement(center, left-right or right-left) for Two-line play style, thus "two-line reverse" preference is dropped
- Feat: Aware of precise lyrics(or enhanced lyrics with A2 extension), precise timestamps will only be removed at current version, (in future version, karaoke mode will add support for it)
- Fix: Fade duration preference not being applied immediately when "Apply" button is clicked
- Optimize (Better with lyrics playing window positioning): reset itself back to edge of screen instead of center screen if its position is out of screen when startup
- Optimize (Preference Saving logic): Preference with default value no longer writes to "AIMP.ini"
- Other minor optimizations and fixes

#### 1.3.2.1 (2026.07.23)

- Fix(#10, AIMP6): Plugin's newly added gatekeeper layer failed to load underlying .NET plugin on AIMP6
- Feat(#9): Add Indonesian Localization (by @naturbrilian)

#### 1.3.2 (2026.07.19)

> Since this version, plugin will be mainly dispatched as `.aimppack` formats, to get plugin files without installation, rename it to `.zip`.

- Feat: Add a preference to control non-synchronized lyrics playing behavior, user can choose to stack such lyrics vertically(default behavior) or horizontally, play with current play style(old behavior), or even do not show them at all (Suggested by many people including Soolo and Kenji Wolfgang)
- Fix: Under karaoke mode, some font text gets incorrectly truncated at the edge, e.g. character `g`'s tail gets truncated on some fonts
- Fix: Incorrect theme color under AIMP 6
- Optimize: Lyrics Editor now reads non-synchronized lyrics
- Optimize: Add a gatekeeper layer which prevents plugin from crashing if corresponding .NET Desktop Runtime is not installed or plugin confliction occurs, a notification will be displayed at that time, which is friendly for new users
- Add(CI): As .NET 8 will soon reach its end-of-support date, plugin files targeting .NET 10 is added since this release. It is recommended to install .NET Desktop Runtime 10 and use corresponding plugin files
- Optimize: Dispose webview process completely if user closes lyrics playing window
- Other minor optimizations

#### 1.3.1 (2026.07.05)

- Feat(#7): Allow "Fade Animation Max Duration" preference of One Line Fade-In-Out play style able to be set down to 0, at that time, lyrics player acts like movie subtitle player (Suggested by **@The-Fae-Sorceress**)
- Feat: Add a preference to disable lyrics playing window always showing on top (Suggested by **Kenji Wolfgang** on AIMP forum)
- Fix: Letter spacing animation of One Line Fade-In-Out play style will not play the first line after user seeks playback
- Other minor optimizations

#### 1.3.0 (2026.07.04)

- Feat: Add Karaoke Mode alongside these features
    - Ability to style karaoke inactive parts' font color, shadow color and text stroke color, corresponding configurations appear on preference window when karaoke mode is enabled
    - Ability to change karaoke transition area width. If set to 0%, there is no transition area, which many people may prefer
    - Karaoke mode supports all 3 play styles
- Feat: Add an preference which enables outer text stroke, which in my opinion looks better than inner text stroke(the old one)
    - Limitation(s):
        - In karaoke mode, outer text stroke is always enabled
        - Outer text stroke does not support hollow text, i.e. if setting font color to a transparent value, text stroke inner part will not be transparent
- Feat: Enhance text shadow settings, add shadow implementation preference:
    - The default text shadow implementation does not look well when text stroke is enabled, so "stroke shadow" is introduced in this version, which looks better when text stroke is enabled
    - The default value of shadow implementation preference is "Automatic", which enables "stroke shadow" only when text stroke is enabled and is recommended
    - For advanced users, you can choose to enable one or both of them.
    - Limitation(s):
        - In karaoke mode, only "stroke" shadow implementation can be enabled, this preference has no effect under karaoke mode
- Feat: Allow negative value for letter spacing preference, because some font family is spotted to be very loose even if letter spacing is 0
- Optimize: Letter spacing animation in one line fade-in-out play style
- Feat: when user sets transparency of background color to a very small value, mouse hovers on lyrics floating window will make background less transparent, because transparent floating window is not transparent for mouse clicks(as Artem previously points out), which may confuse users. If you don't want this feature, just enable "click-through" preference.

#### 1.2.5.fix2 (2026.06.19)

- Fix an issue that Two-Line play style may not play the lyrics line whose preceding line duration is too small (bug reported by Soolo)
- Fix an issue that lyrics scroll window will not re-appear if user switches song quickly

#### 1.2.5.fix1 (2026.06.16)

- Fix Two-Line play style will not clean up stage if switching to a song without lyrics (bug reported by **Soolo**)
- Fix an issue that Two-Line play style may not play first lyrics line if its starting time is too small
- Make lyrics scroll window fades in/fades out if window is about to change visibility

#### 1.2.5 (2026.06.14)

- Implement Two-Line play style, which plays lyrics in two-line
- Optimize One-Line play style: when playback pauses/resumes, animations will also pause/resume
- Optimize animations when user starts/restarts/seeks/stops playback
- Add `Fade Duration` preferences for both One-Line and Two-Line play styles (note that they did not share same preferences)
- Optimize overall stability

#### 1.2.4 (2026.06.14)

- Optimize plugin's low native C++ layer to have better memory management
- Drop the necessity of installing VC++ 2012 runtime
- Optimize "edge feather width" preference implementation to prevent lyrics from being blocked by it
- Support playing non-synchronized lyrics in `.txt`/`.lrc` files or embedded tag (suggested by **Artem**)
- Fix .NET string formatting behaves inconsistently across different systems with different regional formats (bug reported by **Soolo**)

#### 1.2.3 (2026.06.04)

- Fix(#6): At the edge of playing lyrics, shadow effect may be blocked by an invisible area, this happens because lyrics playing area is not set to full width of owner window
- Fix inconsistent .NET `System.Convert` behavior among Windows OS with different regional format (Thanks for **Soolo** reporting the issue!)
- Fix some memory leak issues as **Artem** points out (Thank you AIMP creator!), and with the help of CRT Library, some native C++ code is refactored in this update to get away such issue as much as possible

#### 1.2.2 (2026.05.31)

- optimize(#6 related): Add lyrics window edge feather effect and a corresponding preference to set feather width
- Add a hotkey that allows to toggle lyrics window click-through behavior
- Make preference window layout responsive, alongside some minor adjustments
- Fix an issue happens when user toggles/restarts playing song, window would blink once when "Hide if No Lyrics" preference is enabled
- Other minor fixes and optimizations

#### 1.2.1.1 (2026.05.26)

- Fix an issue when "Hide if No Lyrics" preference is enabled, there is a chance lyrics window not showing even if playing song has lyrics
- Optimize option dialog implementation to embrace AIMP's Automatically Localization feature
- Add some localization entries

#### 1.2.1 (2026.05.20)

- Add a preference, when enabled, floating lyrics window will not appear on taskbar
- Add a preference, when enabled, floating lyrics window will be hidden when no lyrics are found
- Add text stroke preference, which means outlined/hollow text is supported now
- Font family picker now respects AIMP's language: font family name now displays as AIMP language if possible
- Preference window's size is remembered now in case some user's screen is too small
- Other minor bug fixes and optimizations, and modified some localization entries

#### 1.2.0 (2026.05.10)

- Migrate plugin's floating lyrics window implementation to Edge Webview2 to achieve better animation performance.
- Add letter spacing preference as web platform supports them out of the box.
- Add an experimental preference that allows you to animate letter spacing under "Fade In Out Play Style", which looks fancy.
- Other minor bug fixes and optimizations, and modified some localization entries.

#### 1.0.3 (2026.04.21)

- Support multi-language lrc file as 17hapi on AIMP forum suggests
- Change default font family to make UI look better
- Optimize lang files entries, enhance Chinese translations

#### 1.0.2 (2026.04.19)

- Re-write preference window user interface to make it have a modern look
- Add an option to enable/disable click-through lyrics playing window(note that when background is set to a transparent color, the click-through feature is always enabled)
- Fix an issue causing context menu's text and icon blurry
- Other minor stability optimizations and adjustments

#### 1.0.1 (2026.04.15)

- Now supports both AIMP 5 x86 and x64! Make sure to download corresponding zip file and install corresponding runtime packages (see "How to Install & Use" section below)
- Fix an issue causing lyrics editor to crash when user clears "offset" input
- Add option panel in AIMP's preference window, provides functionality to open plugin's preference window or reset lyrics playing window's position there
- Optimize code originally porting from .NET Framework to ensure better compatibility with .NET 8.0
- Update project dependencies: WPF.UI from 4.0.3 to 4.2.0; my dotnet-lrc-parser 0.3.0 to 0.3.1(minor changes concerning .NET 8.0)
- Other stability optimizations and adjustments

#### 1.0.0 (2026.04.12)

Original Release
