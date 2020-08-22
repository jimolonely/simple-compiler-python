
# 一元表达式

接下来允许数字前面带符号： `-3, --3, --+--3` 都是合法的。

语法规则如下

```shell script
expr: term ((PLUS|MINUS) term)*
term: factor ((MUL|DIV) factor)*
factor: (PLUS|MINUS) factor | INTEGER | LPAREN expr RPAREN
```

测试：

```shell script
calc>-3
-3
calc>+3
3
calc>5---+-3
8
calc>5---(3+4)-2
-4
```

