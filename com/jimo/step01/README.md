# calc.py

写一个实现 一位整数的加法解释器：

```python
calc>1+1
2
calc>23+12
Traceback (most recent call last):
  File calc.py, line 83, in <module>
    main()
  File calc.py, line 78, in main
    result = interpreter.expr()
  File calc.py, line 60, in expr
    self.eat(PLUS)
  File calc.py, line 51, in eat
    self.error()
  File calc.py, line 25, in error
    raise Exception('Error parsing input')
Exception: Error parsing input
```

# calc_exercise.py

实现一个支持多位数整数的加法和减法解释器

```shell script
calc>1+1
2
calc>12+12
24
calc>23+1
24
calc>1+34
35
calc>1-10
-9
calc>100-90
10
```