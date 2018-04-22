# Coq Homework

## Build

```sh
python3 config.py
make
make clean
python3 clean.py
```

## Coq -beautify

+ `coq -beautify Basics/Basics.v` would make the `Basics.v` failed in compilation.

```
File "./Basics/Basics.v", line 223, characters 20-33:
Error: Unknown interpretation for notation "_ || _".
```

+ I think the reason is that coq does not understand the meaning of `||` because it does not load some library. However, the `coq -beautify` would load these library by default. I guess the library should be `Coq.Init.Datatypes`, so I add `Require Import Coq.Init.Datatypes.` to the front of `Basics.v`, but it does not work. Then, I add:

```coq
Infix "||" := orb.
Infix "&&" := andb.
```

+ It does work, however the compiler throw error when it is parsing `nat`:

```
Error: Found a constructor of inductive type Datatypes.nat
 while a constructor of nat is expected.
```

+ Then, I think "add code" is not a good idea, I should load the library. But I do not know how to work this out.