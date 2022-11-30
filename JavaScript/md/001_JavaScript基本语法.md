## 字符编码

JavaScript程序使用Unicode字符集编写。Unicode字符集中每个字符使用两个字节来表示，这意味着用户可以使用中文来命名JavaScript变量。

## 大小写区分

JavaScript严格区分大小写。为了避免输入错误，用户可以采用一致的字符大小写形式。例如，遵循习惯了所有字符都采用小写形式，这样可以有效减少输入错误。不过有两点例外。

- 定义JavaScript构造函数时,可以让函数名首字母大写。
- 如果变量名是多个词语连写，可以考虑部分字符大写。

## 标识符

标识符（identifier）表示名称的意思。JavaScript标识符主要包括变量名、函数名、参数名和属性名。合法的标识符命名应该注意如下几条规则，这些规则与C语系其他语言基本相同。

- 第一个字符必须是字母、下划线(_)或美元符号($)。
- 除了第一个字符外，其他位置的字符可以使用字母、数字、下划线、美元符号。
- 标识符名称不能与JavaScript关键字或保留字同名。
- 可以在标识符中使用Unicode转义序列。例如，标识符a可以写成”\u0061“（Unicode转义序列），然后就可以在变量中使用这个转义序列代替字符本身。

## 直接量

直接量（literal）是在程序中直接显示出来的值，如字符串、数值、布尔值、正则表达式、对象初始化、数组初始化等。

## 关键字

具有特定用途的关键字，这些关键字可用于表示控制语句的开始或结束，或者用于执行特定操作等。按照规则，关键字也是语言保留的，不能用作标识符。

关键字列表

- break
- delete
- function
- return
- typeof
- case
- do
- if
- switch
- var
- catch
- else
- in
- this
- void
- continue
- false
- instanceof
- throw
- while
- debugger
- finally
- new
- truc
- with
- default
- for
- null
- try

## 保留字

不能用作标识符的保留字。保留字就是在目前还没有任何特定的用途，但它们有可能在将来版本中被用作关键字。

保留字列表：

- abstract
- double
- goto
- native
- static
- boolean
- enum
- implements
- package
- super
- byte
- export
- import
- private
- synchronized
- char
- extends
- int
- protected
- throws
- class
- final
- interface
- public
- transient
- const
- float
- long
- short
- volatile

## 分隔符

空格、制表符、换行符、换页符等在JavaScript程序中被统称为分隔符，用来分隔代码中的各种记号（如标识符、关键字、直接量、注释等信息）。在解析时，JavaScript 会忽略这些分隔符。

## 注释

注释就是不被解析的语句行或段。JavaScript把位于“I”字符后一行内的所有字符视为注释信息，从而忽略掉。

- 多行注释：`/* 注释内容 换行 注释内容 */`
- 单行注释：`//注释内容`

## 转义序列

在有些计算机硬件和软件里，无法显示或输入Unicode字符全集。为了支持那些使用老旧技术的程序，JavaScript定义了一种特殊序列，使用6个ASCII字符来代表任意16位Unicode内码。
这些Unicode转义序列均以u为前缀，其后跟随4个十六进制数，即，使用数字以及大写或小写的字母A~F表示。这种Unicode转义写法可以用在JavaScript字符串直接量、正则表达式直接量和标识符中，但关键字除外。

