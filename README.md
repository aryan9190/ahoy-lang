# 🏴‍☠️ Ahoy!

**Ahoy!** is a pirate-themed esolang. With its swashbuckling syntax and nautical nonsense, it's designed to be both entertaining and powerful. Write loops, functions, math, and even talk to a parrot - all in pirate speak.

---

##  Try It Online

 [**Playground**]()

---

##  Example

```
Parrot says Ahoy, world!
Add 5 to the booty!
Fire the cannon!
```

##  Language Concepts

| Concept           | Pirate Syntax                             | Description                         |
|-------------------|--------------------------------------------|-------------------------------------|
| Add               | `Add 3 to the booty!`                      | Adds a number to `booty`            |
| Subtract          | `Subtract 2 from the booty!`               | Subtracts from `booty`              |
| Multiply          | `Multiply booty by 4!`                     | Multiplies `booty`                  |
| Divide            | `Divide booty in 2 pieces!`                | Integer divides `booty`             |
| Print value       | `Fire the cannon!`                         | Prints current value of `booty`     |
| Print string      | `Parrot says Ahoy!`                        | Prints a literal string             |
| Push to stack     | `Stash the booty!`                         | Pushes `booty` onto the barrel      |
| Pop from stack    | `Grab from the barrel!`                    | Pops from barrel into `booty`       |
| Define variable   | `Name the booty treasure!`                 | Saves `booty` to `ledger` as `treasure` |
| Load variable     | `Ask for treasure from the ledger!`        | Loads `treasure` from ledger into `booty` |
| Loop start        | `Set sail if the booty be no 0!`           | Starts loop if `booty != 0`         |
| Loop end          | `Drop Anchor!`                             | Ends current loop                   |
| Input             | `Echo from the parrot!`                    | Gets input and stores in `booty`    |
| Function define   | `Raise the sails ye scallywag name!`       | Begins a function block             |
| Function end      | `Lower the sails!`                         | Ends a function block               |
| Call function     | `Call upon greet!`                         | Calls the defined function          |
| Reset booty       | `Swab the deck!`                           | Sets `booty = 0`                    |
| Exit              | `Walk the plank!`                          | Ends the program                    |
| Random booty      | `Drink rum!`                               | Sets `booty = random(1–100)`        |



##  CLI Usage
```
python cli.py examples/hello.ahoy
```

With debug output:
```
python cli.py examples/hello.ahoy --debug
```
