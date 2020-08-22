
# calc6.py

实现带括号的运算, 语法表达式如下

```shell script
expr: term ((PLUS|MINUS) term)*
term: factor ((MUL|DIV) factor)*
factor: INTEGER | LEFTPAREN expr RIGHTPAREN
```

测试：
```shell script
calc>3
3
calc>2+7*4
30
calc>7-8/4
5.0
calc>14+2*3-6/2
17.0
calc>calc>7 + 3 * (10 / (12 / (3 + 1) - 1))
22.0
calc>7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)
10.0
calc> 7 + (((3 + 2)))
12
```


