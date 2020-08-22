
# AST

AST vs ParseTree

我们之前实现的方式就是解析树，查看文章解释：[https://ruslanspivak.com/lsbasi-part7/](https://ruslanspivak.com/lsbasi-part7/)

* AST更简洁，紧凑
* 解析树非常冗余
* AST 通过树节点的层次来表示优先级，优先级越高的越低

然后是访问者模式：后序遍历AST

测试：
```shell script
calc>7 + 3 * (10 / (12 / (3 + 1) - 1))
22.0
calc>7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)
10.0
calc>7 + (((3 + 2)))
12
```

