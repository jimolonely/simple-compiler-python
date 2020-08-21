
# 语法表达式

对于表达式：
```shell script
expr: factor ((MUL|DIV) factor)*
factor: INTEGER
```

其转化为程序的对应关系：

* 语法规则(expr,factor): 对应程序的方法 R()
* (a1|a2|aN): 对应条件选择if-elif-else
* (...)*: 对应while循环
* 最终符号(INTEGER,DIV,MUL): 对应eat(T)方法

# calc4.py

将词法和语法拆分出来，按照上面的对应关系实现

```shell script
calc>1/2
0.5
calc>2*3/5
1.2
calc>45*32/67
21.492537313432837
```

