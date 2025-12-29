# Future Features

Ideas for extending the touch button application beyond its current SuperWhisper-specific use case.

## Context

The app runs on a dedicated 1080p touchscreen positioned as a secondary display. The goal is to create a customizable touch control surface for various applications.

## Planned Features

### Profile/Template System

- Support for multiple button layouts (profiles) for different contexts
- Examples: general productivity, Elite Dangerous, other complex applications
- Desktop shortcuts to launch specific profiles
- Ability to launch multiple buttons at once or a single configured layout

### Multi-Button Support

- Run multiple button instances simultaneously
- Each button can have its own shortcut, position, and appearance
- Profiles define which buttons appear and where

### Application Compatibility

#### Focus Preservation (Critical)
- Maintain the current `WS_EX_NOACTIVATE` behavior
- Buttons must never steal focus from the active application
- Essential for fullscreen games and uninterrupted workflows

#### Anti-Cheat Safe Input
- Keyboard simulation must use methods that don't trigger anti-cheat systems
- Current implementation uses pynput with standard Windows input APIs
- May need validation per game/application
- Goal is accessibility and convenience, not automation or cheating

## Use Cases

- **SuperWhisper**: Voice transcription trigger (current)
- **Elite Dangerous**: Quick access to complex keybinds
- **Other applications**: Streamlined controls for software with extensive keyboard shortcuts
