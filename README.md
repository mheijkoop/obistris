# Obistris
## A blocky game for your train

![An orange-on-black LED display showing a tetris-like game. An S-shaped block is currently falling sideways.](/../static/gameplay.jpeg)

## Running

You should be able to run the game with `pipenv run ./main.py`.

The came can be controlled with the arrow keys: up is rotate and down is accelerated dropping.
Left and right are left as an exercise to the reader. I'm sure you'll get it right.

You can pass the path to your rs-485 uart via `--port /dev/your-usb-tty`. If you've set a different bus id for your display with the jumpers, you can use `--device-id`.

## Requirements

These requirements should be installed automatically with `pipenv sync`.

### python 3.13


### focon-util
Excellent library by [@shiz@mastodon.social](https://mastodon.social/@shiz) from [RevSpace](https://revspace.nl) for controlling the Focon-branded displays used in various trains throughout Europe.

### sshkeyboard
I was surprised (in a bad way) by the poor state of getting keyboard input for something like this from the terminal in Python, especially on macOS.
Everything required the script to run as root, with accessibility permissions, with a GUI component, or any combination of the three.
For me, this was not an option for a silly game.
Thankfully there's [sshkeyboard](https://sshkeyboard.readthedocs.io/en/latest/), which just reads from stdin.


## Known Issues

* There's an out-of-bounds issue when rotating a block at the right end of the screen. I'll fix it. I'm just lazy.
* On the higher levels, the low-ish framerate becomes noticable and falling blocks appear to stutter.
* We're not using the full 'width' of the display, drawing an object 32 pixels wide returns an error but 30 seems to work.
* We're not using the full 'height' of the display, the larger the object, the slower the rendering gets, the current default setting is about the optimum for a non-overclocked display.
* You can't see your score on the display. That'll come! I promise!


## FAQ

### Why?
No reason. I had the display, I wanted something fun to do with it and it was a good opportunity to brush up on my python after more than a decade of not touching it (and never really having done something larger than a couple of lines with it).

### How do I get an ICMm display?
While supplies last, you can support charity and buy used surplus displays from scrapped Koplopers via [Stichting kaNScentraal](https://kanscentraal.nl/).
You will need to arrange your own transportation etc.
Please don't waste their time. They're doing this voluntarily for charity and to put a smile on hobbyists faces. Only contact them if you're seriously interested and willing to spend the money.

If you're part of a hacker space or some other collective, bulk purchasing options are available via afvalbestaatniet at ns dot nl.

#### What else would I need
You will need an RS-485 transceiver (aliexpress!) and a 100V DC power supply capable of delivering about 1A.

Be warned, 100VDC is not a safe voltage. Don't mess around with it if you're not comfortable around electronics with the potential (ha-ha) to kill you.

#### Does it work on other Focon displays
Maybe? I haven't tried.

### This game is not compliant with the Tetris Guideline as published by the Tetris Holding
I know.
It's not tetris!
It's just a blocky game.
Tetris is a very specific blocky game with set behaviors and rules and is trademarked and copyrighted by the Tetris Holding.
This is something else entirely.
Embrace it ;)

### This code sucks
I don't care, I did this for fun in a language I don't use for my dayjob.
I literally had to google the syntax for if-then-else. (`elif`? really? I thought you prefered verbosity, Guido!)
Also, I'm not gonna write unit tests for a fun project, writing tests is not my idea of fun.
And it might not be efficient, the actual sending bits to the display is the bottleneck so it doesn't matter.

### Why are you so defensive?
Because I'm a woman on the internet and men have made me this way.

### Why the name?
OBIS is the name of the system providing travel info in the Koploper trains.
I'm not sure it also controls the exterior displays but it sounded nice.

## AI
No AI was used in the development of this code.
Please don't propose pull requests written by AI.
