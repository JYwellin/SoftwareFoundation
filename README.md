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

## Basics:

+ `andb_true_elim2` is really intersting. I found two method:

```coq
Theorem andb_false : forall b : bool,
  andb b false = false.
Proof.
  (intros c). (destruct c).
    - reflexivity.
    - reflexivity.
Qed.

Theorem andb_true_elim2 : forall b c : bool,
  andb b c = true -> c = true.
Proof.
  (intros b c). destruct c.
  - intro H. reflexivity.
  - (rewrite andb_false). intro H. rewrite -> H. reflexivity.
Qed.
```

```coq
Theorem andb_true_elim2 : forall b c : bool,
  andb b c = true -> c = true.
Proof.
  (intros b c). (destruct b).
  { (destruct c).
    { reflexivity. }
    { simpl. intros H. rewrite -> H. reflexivity. } }
  { (destruct c).
    { simpl. intros H. rewrite <- H. reflexivity. }
    { simpl. intros H. rewrite <- H. reflexivity. } }
Qed.
```

+ best way of `andb_eq_orb` ?
  + My Answer is:

```coq
Theorem andb_eq_orb :
  forall (b c : bool),
  (andb b c = orb b c) ->
  b = c.
Proof.
  intros b c. destruct b.
  { destruct c.
    { reflexivity. }
    { simpl. intros H. rewrite <- H. reflexivity. } }
  { destruct c.
    { simpl. intros H. rewrite <- H. reflexivity. }
    { reflexivity. } }
Qed.
```
  + However, the author said: **You will probably need both `destruct` and `rewrite`, but destructing everything in sight is not the best way.**
  + So, What is the best way?

+ can I use `match` in `Inductive` ?
  + My definition of `bin` is:

```coq
Inductive bin : Type :=
  | B : bin
  | D : bin -> bin
  | N : bin -> bin.
```
  + `D B`, `D D B` and `B` as the same. I want to make all those format to be `B` in `Inductive`, but It seem that I could not use match in Inductive. What should I do?

+ How to use `fixpoint` in `Theorem` ?
  + As the book said, I want to proof S (bin_to_nat(b)) = bin_to_nat(incr(b)). However, I could not been satisfied by `Example`. So I try to proof:

```coq
Theorem bin_to_nat_incr: forall b:bin, S (bin_to_nat(b)) = bin_to_nat(incr(b)).
Proof.
  intros b. destruct b as [| b'| b''].
  - reflexivity.
  - reflexivity.
  - simpl. reflexivity.
Qed.
```

  + I was failed when the `b` is odd number(`b = N b''`). The compiler said: `bin_to_nat (incr b'') + bin_to_nat (incr b'')" with "S (S (bin_to_nat b'' + bin_to_nat b''))`. I cannot simpl this because there are different case depended on the value of `b''`. I have to use infinited step of `destruct b` to prove this. I found I have to recursion in this situation, but I dont know how.

## BasicsTest:

+ How to use this? I notice that there are some `abort.` in it. But when I remove them, it could not pass the compilation.