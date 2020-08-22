
# calc5.py

这一次要考虑乘除法和加减法的结合，需要做到：

* 左结合
* 优先级

形成语法规则如下：

```shell script
expr: term ((PLUS|MINUS) term)*
term: factor ((MUL|DIV) factor)*
factor: INTEGER
```

测试：
```shell script
calc>1+2
3
calc>2*3
6
calc>3/2
1.5
calc>1+3*7
22
calc>2*7/4
3.5
calc>2+3*7-6/2
20.0
```
