
from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    ([mod], "b", lazy.spawn("firefox")),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    (
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),
    ([mod], "Return", lazy.spawn(terminal)),
    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod], "w", lazy.window.kill()),
    (
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        
    ),
    ([mod], "t", lazy.window.toggle_floating()),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control"], "q", lazy.shutdown()),

    ([mod], "m", lazy.spawn("rofi -show drun")),
    ([mod, "shift"], "m", lazy.spawn("rofi -show"))

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]]