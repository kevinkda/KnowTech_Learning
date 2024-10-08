# 学习记录文档

[toc]

## 一、Develop

### 1. Node.js 相关

#### nodeJS 的 npm 设置国内高速镜像之淘宝镜像的方法

1、我们知道 nodeJS 是老外搞出来的，服务器放在了国外，国内的小朋友访问起来会比较慢，阿里巴巴的淘宝给出了有力支持，现在我们就将 nodeJS 的镜像地址切换为国内的淘宝镜像。

2、查看当前的镜像地址：
　　`npm get registry`
　　得到
　　`https://registry.npmjs.org/`

3、在 CMD 中执行如下命令，配置注册的镜像地址为淘宝镜像：
　　`npm config set registry http://registry.npm.taobao.org/`
　　或
　　`yarn config set registry http://registry.npm.taobao.org/`

4、如果想换回来的话将淘宝镜像再换成 `https://registry.npmjs.org/` 即可：
　　`npm config set registry https://registry.npmjs.org/`

5、备注：
　　NPM = NodeJS Package Manager

#### 建议安装的包

- nrm：镜像源管理工具
- create-react-app：react项目创建工具
- vue-cli：Vue.js 开发的标准工具



### 2. Vue 学习

```bash
# 全局安装 vue-cli
$ cnpm install --global vue-cli
# 创建一个基于 webpack 模板的新项目
$ vue init webpack my-project
# 这里需要进行一些配置，默认回车即可
This will install Vue 2.x version of the template.

For Vue 1.x use: vue init webpack#1.0 my-project

? Project name my-project
? Project description A Vue.js project
? Author runoob <test@runoob.com>
? Vue build standalone
? Use ESLint to lint your code? Yes
? Pick an ESLint preset Standard
? Setup unit tests with Karma + Mocha? Yes
? Setup e2e tests with Nightwatch? Yes

   vue-cli · Generated "my-project".

   To get started:
   
     cd my-project
     npm install
     npm run dev
   
   Documentation can be found at https://vuejs-templates.github.io/webpack
```

```base
$ cd my-project
$ cnpm install
$ cnpm run dev
 DONE  Compiled successfully in 4388ms

> Listening at http://localhost:8080
```

#### 一些有用的依赖

- `npm config set registry https:*//registry**.npm**.taobao**.org*`  更换源至淘宝
- `npm install-g cnpm --registry=https://registry.npm.taobao.org ` 设置淘宝镜像
- `cnpm install express` express
- `cnpm install webpack -g` 安装webpack
- `cnpm install vue-cli -g` vue脚手架
- `cnpm install axios -S` axios
- `cnpm install element-ui -S` elementUI
- `cnpm install less less-loader --save-dev`
- `npm install vuex --save`
- `cnpm install babel-polyfill`  -- 解决白屏问题 
- `cnpm install ex6-promise`
- `npm install css-loader style-loader –save-dev`

#### 项目打包

`npm run build`
执行完后会在项目中下生成`dist`目录，一般包含 index.html 文件及 static 目录，static 目录包含了静态文件 js、css 以及图片目录 images。

#### 项目结构

| build        | 项目构建(webpack)相关代码                                    |
| ------------ | ------------------------------------------------------------ |
| config       | 配置目录，包括端口号等。我们初学可以使用默认的。             |
| node_modules | npm 加载的项目依赖模块                                       |
| src          | 这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：assets: 放置一些图片，如logo等。components: 目录里面放了一个组件文件，可以不用。App.vue: 项目入口文件，我们也可以直接将组件写这里，而不使用 components 目录。main.js: 项目的核心文件。 |
| static       | 静态资源目录，如图片、字体等。                               |
| test         | 初始测试目录，可删除                                         |
| .xxxx文件    | 这些是一些配置文件，包括语法配置，git配置等。                |
| index.html   | 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。       |
| package.json | 项目配置文件。                                               |
| README.md    | 项目的说明文档，markdown 格式                                |



### 3. 后端mod(%)取模运算符的算法

例如a % b

![image-20220909180024124](https://image.kevinkda.cn/md/image-20220909180024124.png)



### 4. Spring boot 和 Spring Cloud 各个版本对应关系

| spring cloud        | spring boot                                   |
| ------------------- | --------------------------------------------- |
| Finchley            | 2.0.x                                         |
| Finchley.SR1        | Spring Boot >=2.0.3RELEASE and <=2.0.9RELEASE |
| Finchley.SR4        | Spring Boot >=2.0.3RELEASE and <=2.0.9RELEASE |
| Greenwich           | 2.1.x                                         |
| Hoxton              | 2.2.x , 2.3.x(Starting with SR5)              |
| 2020.0.x aka Ilford | 2.4.x                                         |



### 5. 缓存技术之session缓存管控

​	Session是服务器端使用的一种记录客户端状态的机制，一般Session存储在服务器的内存中，tomcat的StandardManager类将session存储在内存中；客户端只保存sessionID到cookie中，而不会保存session，session销毁只能通过invalidate或超时（默认30分钟），关掉浏览器并不会关闭session。当程序需要为某个客户端的请求创建一个session时，服务器首先检查这个客户端的请求里是否包含一个session标识（即sessionID）。如果已经包含一个sessionID说明以前已经为此客户端创建过session，服务器就按照sessionID把这个session检索出来使用。

​	如果客户请求不包含sessionID，则为此客户创建一个session并且生成一个与此session相关的sessionID，这个sessionID将在本次响应中返回给客户端保存。

Session缓存优势明显，在日常开发过程中，大家基于这个优势，不可避免地存在session过度使用的情况，导致缓存未能正确清理，造成其他业务的误使用，从而引发一些业务问题，严重时可导致业务受理异常或业务数据不一致，比如下面的场景：

![img](https://image.kevinkda.cn/md/image017(10-31-18-03-18).jpg)

​	1、由于session缓存的生命周期较长，当操作员同时打开多个tab页时，A业务保存的缓存，B业务也能取到，被错误使用。只对某业务自己使用的信息，直接用同一个key来设值，被其他业务误用：

​	2、缓存使用完后未清理，或者在清理之前业务有异常导致未能正确清理缓存，会有多余的缓存信息残留，被其他业务错误使用。缓存使用完后应该及时清理，并且需要考虑在异常情况下是否也可以正确清理：

​	从使用session导致的问题看，严重时直接造成业务受理不正确，造成业务受理风险甚至生产故障，影响客户满意度。基于以上问题，在页面使用session的过程中，建议遵循以下原则：

​	1、只有页面全局通用的信息，再考虑是否有必要使用session缓存的方式来处理。

​	2、对于具体的业务菜单尽量不要使用，换其他的方式解决：

​		a) （推荐）本业务的所有信息都在handler里面处理，涉及到调用外部方法时，最安全的办法是使用Map传递值。

​		b) （不推荐）如果必须使用session缓存才能实现，缓存key值必须关联号码和菜单ID（建议的key格式XXXX_billId_menuId）。



### 6. 在Idea中打包项目

+ 打开Project Structure界面(快捷键是F4或者F12)  选择Artifacts一栏
+ 点击＋号后选择`Web Application: Exploded`下的From Modules
+ 点击＋号后选择 `Web Application: Archive`下的For ***
+ 在右侧Name：一栏中修改名字  点击Apply和OK
+ 选择菜单栏上的Build下的Build Artifacts
+ 选择后缀之后War的那一个，之后点击Build，等待完成
+ 再打开Project Structure界面，查看Output directory一栏后的War包所在路径



### 7. Java中正则的妙用 - 组

 *  PROCESSING_EMAIL_HTML_IMAGE_REGEX 常量中的每一个括弧为一个组
 *  PROCESS_EMAIL_HTML_IMAGE_REGEX_REPLACEMENT_PLACEHOLDER 常量中的$1 $3 $5代表上上面的第1个、第3个、第5个组
 *  processContentHTMLImageTag方法则是将 PROCESSING_EMAIL_HTML_IMAGE_REGEX 常量中的第1个、第3个、第5个组给摘出来，即删除第2、第4组

```java
public class Regular {
    public static final String PROCESSING_EMAIL_HTML_IMAGE_REGEX = "(src=\\\")(cid:)([\\w\\d]+\\.[A-Za-z]+)(@[A-Za-z0-9]+\\.[A-Za-z0-9]+)(\\\")";
    public static final String PROCESS_EMAIL_HTML_IMAGE_REGEX_REPLACEMENT_PLACEHOLDER = "$1$3$5";

    public String processContentHTMLImageTag(String contentText) {
        return contentText.replaceAll(
                MailConstants.PROCESSING_EMAIL_HTML_IMAGE_REGEX,
                MailConstants.PROCESS_EMAIL_HTML_IMAGE_REGEX_REPLACEMENT_PLACEHOLDER
        );
    }
}
```



### 8. Gradle学习

#### 常见的项目构建工具

- Ant: 
  - 优点: 使用灵活，速度快(快于 gradle 和 maven)
  - 缺点:Ant没有强加任何编码约定的项目目录结构,开发人员需编写繁杂 XML 文件构建指令,对开发人员是一个挑战
- Maven
  - 优点: 遵循一套约定大于配置的项目目录结构，使用统一的 GAV 坐标进行依赖管理,侧重于包管理
  - 缺点: 项目构建过程僵化,配置文件编写不够灵活、不方便自定义组件,构建速度慢于 gradle
- Gradle
  - 优点:集 Ant 脚本的灵活性+Maven 约定大于配置的项目目录优势,支持多种远程仓库和插件,侧重于大项目构建
  - 缺点: 学习成本高、资料少、脚本灵活、版本兼容性差等

![image-20230711223518153](https://image.kevinkda.cn/md/image-20230711223518153.png)

#### Gradle安装

​	[SpringBoot 官方文档](https://docs.spring.io/spring-boot/docs/2.5.0/gradle-plugin/reference/htmlsingle/#getting-started)明确指出,目前 SpringBoot 的 Gradle 插件需要 gradle6.8 版本及以上，所以我们这里选择 7x 版本

​	其中SpringBoot与Gradle存在版本兼容问题，Gradle与Idea也存在兼容问题，所以要选择Gradle6.8版本以及高于6.8版本的Gradle	

**Important Tips：**

- 打开Idea安装目录下的\plugins\gradle\lib，能查看Idea与Gradle相对应的Gradle版本号
- 选择Spring Boot时一定要注意Spinrg Boot 和JDK 的版本

具体安装步骤参考以下文档：

- [官方文档](https://gradle.org/install/)
- [Gradle环境配置](https://zhuanlan.zhihu.com/p/522238682)

#### Gradle和Maven项目结构

![image-20230711234024582](https://image.kevinkda.cn/md/image-20230711234024582.png)

#### 修改Maven下载源

​	我们可以在gradle的init.d目录下创建以.gradle结尾的文件，.gradle文件可以实现在build开始之前执行，所以可以在这个文件配置一些你要预先加载的操作

将以下内容复制到init.d目录下的init.gradle文件中：

- 项目所需要的架包会前往repositories中区下载
- 而buildscript是给build.gradle使用的
- mavenLocal() 即为maven本地仓库
- mavenCentral() 即为maven重要仓库

```groovy
allprojects {
    repositories {
        mavenLocal()
        maven { name "Alibaba"; url "https://maven.aliyun.com/repository/public"}
        maven { name "Bstek"; url "https://nexus.bsdn.org/content/groups/public"}
        mavenCentral()
    }
    
    buildscript {
        repositories {
        	maven { name "Alibaba"; url "https://maven.aliyun.com/repository/public"}
        	maven { name "Bstek"; url "https://nexus.bsdn.org/content/groups/public"}
        	maven { name "M2"; url "https://plugins.gradle.org/m2/"}
        }
    }
}
```

<h5>启用init.gradle文件的方法：</h5>

1. 在命令行指定文件，例如：`gradle -init-script yourdir/init,gradle -q taskName`。你可以多输入此命令来指定多个init文件
2. 把init.gradle文件放到 USER_HOME/.gradle/ 目录下（即放到C盘下的当前用户目录下的.gradle文件夹下）
3. 把以.gradle结尾的文件放到 USER_HOME/.gradle/init.d/ 目录下（即放到C盘下的当前用户目录下的.gradle文件夹下的init.d文件夹下）
4. 把以.gradle结尾的文件放到 GRADLE_HOME/init.d/ 目录下（即gradle安装目录下的init.d文件夹下）

​	如果以上四种方式，存在两种，那么gradle会按照上面的顺序从1到4依次执行，如果给定目录下存在多个init脚本，会按拼音a-z顺序执行这些脚本，每个init脚本都存在一个对应的gradle实例，你在这个文件中调用的所有方法和属性，都会委托给这个gradle实例，每个init脚本都实现了Script接口。

<h5>其他类型的Maven的Aliyun地址</h5>

[阿里云云效Maven](https://developer.aliyun.com/mvn/guide)

插件类的仓库地址，最好放到 `buildscript` 下 

<h5>Gradle.properties</h5>

```properties
# 开启守护进程，下一次构建的时候，会连接这个守护进程进行构建，而不是重新fork一个进程进行构建
org.gradle.daemon=true
# 设置JVM堆内存大小
org.gradle.jvmargs=-Xmx4096m -XX:MaxPermSize=1024m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
# 并行编译
org.gradle.parallel=true
# 按需加载
org.gradle.configureondemand=true
# 开启gradle缓存
org.gradle.caching=true
```





#### Gradle Wrapper

​	Gradle Wrapper 实际上就是对Gradle的一层包装，用于解决实际开发中可能会遇到的不同项目需要不同版本的Gradle问题，例如：把自己代码共享给别人，`发现别人的没有安装Gradle、或者别人的Gradle版本太老旧。`

<h5>如何使用Gradle Wrapper</h5>

![image-20230712142433089](https://image.kevinkda.cn/md/image-20230712142433089.png)

​	Gradle指令和Gradlew指令是不一样的，并且版本也有可能不一样。原因是因为Gradle指令使用的是本地安装的Gradle，Gradlew使用的是Gradle Wrapper中的Gradle，不过最终指令的使用方式是一样的。

​	对于Gradlew指令时，我们也可以用一些参数来控制Wrapper的生产，比如依赖的版本等：

| 参数名称                  | 参数说明                        | 参数示例                                                     |
| ------------------------- | ------------------------------- | ------------------------------------------------------------ |
| --gradle-version          | 用于指定使用的Gradle版本        | gradle wrapper --gradle-version=7.4.2                        |
| --gradle-distribution-url | 用于指定下载的Gradle发行版的url | gradle wrapper --gradle-version 7.4.2 --distribution-type all |
|                           |                                 |                                                              |

<h5>GradleWrapper执行流程</h5>

1.当我们第一次执行 ./gradlew build 命令的时候，gradlew 会读取 gradle-wrapper.properties 文件的配置信息

2.准确的将指定版本的 gradle 下载并解压到指定的位置GRADLE_USER HOME目录下的wrapper/dists目录中

3.并构建本地缓存(GRADLE_USER HOME目录下的caches目录中),下载再使用相同版本的gradle就不用下载了

4.之后执行的 ./gradlew 所有命令都是使用指定的 gradle 版本

![image-20230712144504200](https://image.kevinkda.cn/md/image-20230712144504200.png)

<h5>何时使用Gradle Wrapper</h5>

下载别人的项目或者使用操作以前自己写的不同版本的gradle项目时：用Gradle wrapper，也即：gradlew，什么时候使用本地gradle？新建一个项目时：使用gradle指令即可。

#### Groovy学习

Groovy 是 用于Java虚拟机的一种敏捷的动态语言，它是一种成熟的面向对象编程语言，既可以用于面向对象编程，又可以用作纯粹的脚本语言。使用该种语言不必编写过多的代码，同时又具有闭包和动态语言中的其他特性。

Groovy是JVM的一个替代语言（替代是指可以用 Groovy 在Java平台上进行 Java 编程），使用方式基本与使用 Java代码的方式相同，该语言特别适合与Spring的动态语言支持一起使用，设计时充分考虑了Java集成，这使 Groovy 与 Java 代码的互操作很容易。（注意：不是指Groovy替代java，而是指Groovy和java很好的结合编程。）

<h5><a href="http://www.groovy-lang.org/objectorientation.html#_modifiers_on_a_property">Groovy与Java的主要区别</a></h5>

- 没有可见性修饰符的类或方法自动是公共的(可以使用一个特殊的注释来实现包的私有可见性)
- 没有可见性修饰符的字段将自动转换为属性，不需要显式的 getter 和 setter 方法
- 如果属性声明为 fnal，则不会生成 setter
- 一个源文件可能包含一个或多个类（但是如果一个文件不包含类定义的代码，则将其视为脚本）。脚本只是具有一些特殊约定的类,它们的名称与源文件相同(所以不要在脚本中包含与脚本源文件名相同的类定义)。

<h5>安装配置</h5>

[Groovy下载地址](https://groovy.apache.org/download.html)

![image-20230712172907286](https://image.kevinkda.cn/md/image-20230712172907286.png)

![image-20230712172934787](https://image.kevinkda.cn/md/image-20230712172934787.png)

<h5>Groovy概要</h5>

![image-20230712232018904](https://image.kevinkda.cn/md/image-20230712232018904.png)

**类型转换**：当需要时，类型之间会自动发生类型转换：字符串（String）、基本类型如 （int）和类型的包装类（如 nteger）

**类说明**: 如果在一个 groovy 文件中没有任何类定义，它将**被当做 script 来处理**，也就意味着这个文件将被透明的转换为**一个Script 类型的类**，这个自动转换得到的类将使用原始的 groovy 文件名作为类的名字。groovy 文件的内容被打包进run 方法，另外在新产生的类中被加入一个 main 方法以进行外部执行该脚本。

<h5>Groovy字符串操作</h5>

Groovy使用字符串时，单引号、双引号使用起来有不同的效果

- 单引号：不支持变量引用，不支持换行操作
- 双引号：支持变量引用，不支持换行操作
- 单引号模板字符串：不支持变量引用，支持换行操作
- 双引号模板字符串：支持变量引用，支持换行操作

![image-20230713002157590](https://image.kevinkda.cn/md/image-20230713002157590.png)

<h5>Groovy三大语句结构</h5>

[官方文档](http://www.groovy-lang.org/semantics.html#_conditional_structures)

<h5>Groovy类型以及权限修饰符</h5>

1. 原生数据类型

| 原生    | 包装      |
| ------- | --------- |
| boolean | Boolean   |
| char    | Character |
| short   | Short     |
| int     | Integer   |
| long    | Long      |
| float   | Float     |
| double  | Double    |

2. 类、内部类、抽象类、接口
3. 注解
4. Trait：带有方法实现的接口
5. 权限修饰符：private、public、protected

<h5>Groovy集合操作</h5>

Groovy支持List、Map集合操作，并且拓展了Java中的API，具体参考[官方文档](http://www.groovy-lang.org/syntax.html#_number_type_suffixes)

![image-20230713162219072](https://image.kevinkda.cn/md/image-20230713162219072.png)

<h5>Groovy类导入</h5>

[官方文档](http://www.groovy-lang.org/structure.html#_imports)

<h5>Groovy异常处理</h5>

[官方文档](http://www.groovy-lang.org/semantics.html#_try_catch_finally)

<h5>Groovy闭包</h5>

[官方文档](http://www.groovy-lang.org/closures.html)

定义：是一个开放的、匿名的代码块，它可以接受参数、也可以有返回值。闭包可以引用其周围作用域中声明的变量。

语法：

```groovy
{ [closureParameters -> ] statemets }
```

调用：

1. 将闭包赋值给一个变量
2. 变量名()、变量名.call()

示例：

```groovy
def running = { who ->
    println("$who start")
}

running("code")
running().call("code")

//____________分割_______________
def running(Closure closure) {
    println("running start")
    println("running end")
}

running({println("running")})

//____________分割_______________
def caculate(num1,num2,Closure closure){
    closure(num1,num2)
}

caculate(10,15,{k,v -> println("$k + $v = ${k+v}")})
// 闭包作为方法的最后一个参数，那么闭包可以写在方法外边
caculate(10,15){k,v -> println("$k + $v = ${k+v}")}
//____________分割_______________
def caculate(Closure closure){
    def num1 = 10
    def num2 = 15
    closure(num1,num2)
}

caculate(){k,v -> println("$k + $v = ${k+v}")}
caculate{k,v -> println("$k + $v = ${k+v}")}
```

#### Gretty项目部署

[官网地址](http://akhikhl.github.io/gretty-doc/index.html)

Tips：Gradle 6.x版本以前对Gretty支持比较友好

Gretty核心功能：

- 底层支持jerry，tomcat等Servlet容器
- 支持热部署、Https、调试

<h5>具体使用</h5>

1. 项目引入Gretty

```groovy
plugins {
    id 'war'
    id 'org.gretty' version '2.2.0'
}
```

2. 指定maven仓库

```groovy
repositories {
    jcenter()
    mavenCentral()
}
```

3. Gretty 插件设置

```groovy
gretty {
	httpPort = 8888
    contextPath = "/web"
    debugPort = 5005
    debugSuspend = true
    httpsEnabled = true
    // 热部署
    manageClassReload = true
    // 如果不指定默认容器，则默认使用Jetty
    // servletContainer = 'tomcat'
    httpsPort = 4431
}
```

4. 执行命令：gradle appRun

#### Gradle项目生命周期

Gradle项目的生命周期分为三大阶段：Initialization -> Configuration -> Execution

![image-20230715000734926](https://image.kevinkda.cn/md/image-20230715000734926.png)

#### Gradle中的setting文件

作用：主要作用是在项目初始化阶段确定要引入那些工程，需要加入到项目构建中，为构建项目工程树做准备。

工程树：Gradle中有工程树的概念，类似于Maven中的Project和Module

![image-20230715001221629](https://image.kevinkda.cn/md/image-20230715001221629.png)

内容：里面主要定义了当前Gradle项目以及子Project的项目名称

位置：必须放在根工程下

名字：为setting.gradle文件，不能发生变化

对应实例：与org.gradle.api.initialization.Settings 实例是一一对应的关系。每个项目只有一个settings文件。

关注：只需关注文件中的 include 方法。

一个子工程只有再settings文件中配置了才会被gradle识别，构建时才会被包含

```groovy
// 根项目名称
rootProject.name = 'gradle_tree'
// 子模块名称
include 'sub_01'
include 'sub_02'
include 'sub_03'
// 包含的子工程下的子工程名称
include 'sub_01:subProject01'
include 'sub_02:subProject02'
```



#### Gradle的Task

```groovy
tasks.named('test') {
    // 任务配置段，在配置阶段执行
    println "this is task example"
    // 任务的行为：在执行阶段执行
    doFirst {
        println "task first task"
    }
    doLast {
        println "task last task"
    }
}
```

运行任务

```shell
gradle -i test
```

任务的doFirst、doLast都可以在任务的外部定义

```groovy
tasks.named('test') {
    // 任务配置段，在配置阶段执行
    println "this is task example"
}

test.doFirst {
	println "task first task"
}
test.doLast {
	println "task last task"
}
```

**底层原理解析**：无论是定义任务自身的 action，还是添加的 doLast、doFirst 方法，其实底层都被放入到一个 Action 的 List中了，最初这个action List 是空的，当我们设置了 ation[任务自身的行为]，它先将 actin 添加到列表中，此时列表中只有一个action，后续执行doFirst的时候 doFirst在 action 前面添加,执行 doLast 的时候 doLast 在 action 后面添加。doFirst永远添加在 actions List 的第一位，保证添加的 Action 在现有的 action List 元素的最前面；doLast 永远都是在 action List末尾添加，保证其添加的 Action 在现有的 ction List 元素的最后面。一个往前面添加一个往后面添加，最后这个 actionList 就按顺序形成了 doFirst、 doSelf、 doLast 三部分的 Actions,就达到 doFirst、 doSelf、doLast 二部分的 Actions 顺序执行的目的。

![image-20230716215239588](https://image.kevinkda.cn/md/image-20230716215239588.png)

Tips：其中<<代表dolast，在Gradle5.x版本之后就废弃了。

<h5>任务的依赖方式</h5>

- 参数方式依赖

```groovy
taks 'A' {
    doLast {
        println "task A"
    }
}

taks 'B' {
    doLast {
        println "task B"
    }
}

taks 'C'(dependsOn: ['A','B']) {
    doLast {
        println "task C"
    }
}
```

- 内部依赖

```groovy
taks 'C' {
    dependsOn = ['A','B']
    doLast {
        println "task C"
    }
}
// ==================
taks 'C' {
    doLast {
        println "task C"
    }
}
c.dependsOn = ['A','B']
```

- 外部依赖

```groovy
// subproject01 工程
taks 'A' {
    doLast {
        println "task A"
    }
}
// subproject02 工程
taks 'B' {
    dependsOn(":subproject01:A")
    doLast {
        println "task B"
    }
}
```

Tips1：当一个Task依赖多个Task的时候，被依赖的Task之间如果没有依赖关系，那么它们的执行顺序是随机的。

Tips2：重复依赖的任务只会执行一次，比如：



<h5>任务的执行</h5>

[官方文档](https://docs.gradle.org/current/userguide/command_line_interface.html#sec:command_line_executing_tasks)

语法：gradle [taskanme] [--option-name]

```shell
# 常见任务
gradle build：构建项目:编译、测试、打包等操作 
gradle run：运行一个服务,需要 application 插件支持，并且指定了主启动类才能运行
gradle clean：请求当前项目的 build 目录 
gradle init：初始化 gradle 项目使用 
gradle wrapper：生成 wrapper 文件夹的 
gradle wrapper 升级 wrapper 版本号：gradle wrapper -gradle-version=4.4 
gradle wrapper -gradle-version 5.2.1 --distribution-type all：关联源码用

# 项目报告
gradle projects：列出所选项目及子项目列表，以层次结构的形式显示 
gradle tasks：列出所选项目[当前 project,不包含父、子]的已分配给任务组的那些任务 
gradle tasks -all：列出所选项目的所有任务 
gradle tasks -group="build setup"：列出所选项目中指定分组中的任务 
gradle help -task someTask：显示某个任务的详细信息 
gradle dependencies：查看整个项目的依赖信息，以依赖树的方式显示 
gradle properties：列出所选项目的属性列表

# 调试选项
-h,--help：查看帮助信息 
-v,--version：打]印Gradle、Groovy、 AntJVM 和操作系统版本信息 
-S,-full-stacktrace：打印出所有异常的完整(非常详细)堆栈跟踪信息 
-s,-stacktrace：打印出用户异常的堆栈跟踪(例如编译错误)
-Dorg.gradle,daemon.debug=true：调试 Gradle 守护进程 
-Dorg.gradle.debug=true：调试 Gradle 客户端（非 daemon）进程 
-Dorg.gradle.debug.port=(port number)：指定启用调试时要侦听的端口号。默认值为 5005

# 性能选项
-build-cache,--no-build-cache：尝试重用先前版本的输出。默认关闭(off)。 
-max-workers：设置 Gradle 可以使用的 woker数。默认值是处理器数 
-parallel,-no-parallel：并行执行项目。有关此选项的限制，请参阅并行项目执行默认设置为关闭(off)

# 守护进程
-daemon,--no-daemon：使用守护进程运行构建。默认是 onGradle 
-foreground：在前台进程中启动 Gradle 守护进程 
-Dorg.gradle.daemon.idletimeout=(number of milliseconds)：Gradle Daemon 将在这个空闲时间的毫秒数之后停止自己。默认值为 1000000(3 小时)

# 日志选项
-Dorg.gradle.logging.level=(quiet,warn,lifecycle,info,debug)：通过 Gradle 属性设置日志记录级别。 
-q,-quiet：只能记录错误信息 
-w,--warn：设置日志级别为 warn 
-i,--info：将日志级别设置为 info 
-d,-debug：登录调试模式(包括正常的堆栈跟踪）

# 其他
-x:-x 等价于：-exclude-task:常见 gradle -x test clean build 
-rerun-tasks：强制执行任务，忽略up-to-date ,常见 gradle build -rerun-tasks 
-continue：忽略前面失败的任务.继续执行,而不是在遇到第一个失败时立即停止执行。每个遇到的故障都将在构建结束时报告，常见: gradle build -continue。 
gradle init -type pom：将 maven 项目转换为 gradle 项目(根目录执行） 
gradle [taskName]：执行自定义任务
```

Gradle默认各指令之间相互的依赖关系

![image-20230719004133258](https://image.kevinkda.cn/md/image-20230719004133258.png)

<h5>任务的定义方式</h5>

任务定义方式，总体分为两大类，一种是通过Project中的task方法，另一种是通过tasks对象的create或者register方法。

```groovy
task('A',{ // 任务名称，闭包都作为参数
    println "task a"
})

task('B'){ // 闭包作为最后一个参数可以直接从中括号中拿出来
    println "task b"
}

task C { // groovy语法支持省略方法括号
    println "taks c"
}
// 以上三种方法本质上是一种方法

def map = new HashMap<String,Object>();
map.put("aciton",{println "task d"})// action属性可以设置为闭包
taks(map,"D");

task.create("E"){ // 使用 task 的create方法
    println "task e"
}

task.register("F"){ // register执行是延迟创建，即只有当task被需要的时候才会创建
    println "task f"
}
```

<h5>任务的属性</h5>

| 配置项      | 描述                                           | 默认值      |
| ----------- | ---------------------------------------------- | ----------- |
| type        | 基于一个存在的task来创建，和java中的类继承相似 | DefaultTask |
| overwrite   | 是否替换一个存在的task，这个和type配合使用     | false       |
| dependsOn   | 用于配置任务的依赖                             | []          |
| action      | 添加到任务中的一个Action或者一个闭包           | null        |
| description | 任务的描述                                     | null        |
| group       | 任务的分组                                     | null        |

```groovy
// 1.F是任务名，以参数的方式指定任务的属性信息
task(grou: "alan", description: "this is task F","F")

// 2.H是任务名，任务定义的同时，直接在内部指定属性信息
task("H"){
    group("alan")
    description("this is task H")
}

// 3.Y是任务名，给已有的任务 在外部指定属性信息
task("Y"){}
y.group = "alan"
y.description = "this is task Y"
```







### 9. 将Maven项目配置并上传到JFrog

#### 相关链接

[从JFrog上传和下载制品](https://blog.csdn.net/weixin_40816738/article/details/121530665)

[Maven在settings.xml中存储加密密码](https://blog.csdn.net/it_freshman/article/details/125084861)

#### 1.生成配置

生成Artifactory仓库上传配置文件，选择仓库，点击‘Set Me Up’查看部署配置

![img](https://image.kevinkda.cn/md/acd89fe1071649fba4f319e2ba31e6ff.png)

![在这里插入图片描述](https://image.kevinkda.cn/md/cc07f3722c5a4ff39999ebc6e7882fa9.png)

#### 2.拷贝配置

拷贝配置到项目中的POM文件，添加配置DistributionManagement

注意id和url要配置正确, 与setting文件的一致. 如果不是使用虚拟库来部署, 这里的url就指定私库, 但是id要与setting中的server一致, 因为会通过id去找用户密码

![image-20230720010525432](https://image.kevinkda.cn/md/image-20230720010525432.png)

#### 3.配置settings.xml文件

将下图中的servers配置给写入settins.xml文件中，注意：下图中的id一项需要和第二步中的id一致

![image-20230720010655180](https://image.kevinkda.cn/md/image-20230720010655180.png)

#### 4.执行上传

执行命令

```shell
mvn deploy
```

或者

![在这里插入图片描述](https://image.kevinkda.cn/md/1ef2f535132149d8b67a9a4fcb69ae62.png)



### 10. Java Map Struts 技巧

#### 指定不同属性映射

```java
/**
 * 请求入参转为Alipay的业务Model
 * @param request
 * @return
 */
@Mappings({
    @Mapping(target = "totalAmount", source ="oraTotalAmount"),
    @Mapping(target = "price", source ="oraPrice"),
})
AlipayTradeAppPayModel requestToModel(AlipayAppRequest request);
```

#### 金额映射

```java
/**
 * 请求入参转为Alipay的业务Model
 * @param request
 * @return
 */
@Mappings({
        @Mapping(target = "totalAmount",
                expression = "java(com.api.business.alipay.utils.CurrencyUtils.changeF2Y(request.getOraTotalAmount()))")
})
AlipayTradeWapPayModel requestToModel(AlipayWapRequest request);

/**
 * 应答出参映射
 * @param model
 * @return
 */
@Mappings({
        @Mapping(target = "oraTotalAmount",
                expression = "java(com.api.business.alipay.utils.CurrencyUtils.changeY2F(request.getTotalAmount()))")
})
AlipayWapResponse modelToResponse(AlipayTradeWapPayResponse model);

/**
 * 请求对象中的集合，集合中的对象GoodsDetail的金额映射
 */
@Mappings({
        @Mapping(target = "price",
                expression = "java(com.api.business.alipay.utils.CurrencyUtils.changeF2Y(goodsDetail.getOraPrice()))")
})
com.alipay.api.domain.GoodsDetail goodsDetailToGoodsDetail(GoodsDetail goodsDetail);
```



### 11. xxl-job使用问题

#### 配置入参格式

代码中获取参数的方法为：

```java
public abstract class BaseJobHandler extends IJobHandler {
    public Map<String, String> getJobParams() {
        return getJobParams(XxlJobContext.getXxlJobContext().getJobParam());
    }

    public Map<String, String> getJobParams(String jobParam) {
        Map<String, String> param = new HashMap<>(8);
        if (StringUtil.isNonBlank(jobParam)) {
            Arrays.stream(jobParam.split(",")).forEach((s) -> {
                String[] arr = s.split("=");
                param.put(arr[0].trim(), arr[1].trim());
            });
        }
        return param;
    }
}
```

配置参数的格式为：

```java
param1=value1,param2=value2
例如：
RUN_DATE=2021-09-03,MAX_TRADE_DAY=-1
```



### 12. React加载完成后执行方法

 在React中，如果你希望在组件加载完成后执行某个方法，你可以使用生命周期方法或React的`useEffect`钩子（如果你正在使用函数组件）。以下是两种方法的示例：

**使用生命周期方法 (类组件)**：

在类组件中，你可以使用`componentDidMount`生命周期方法，它会在组件挂载后被调用。你可以在这个方法内执行你的操作。例如：

```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  componentDidMount() {
    // 在组件加载完成后执行你的方法
    this.myMethod();
  }

  myMethod() {
    // 在这里执行你的操作
  }

  render() {
    return (
      // JSX内容
    );
  }
}

export default MyComponent;
```

**使用 useEffect 钩子 (函数组件)**：

在函数组件中，你可以使用React的`useEffect`钩子来达到类似的效果。`useEffect`允许你在组件加载后执行副作用操作。以下是一个示例：

```javascript
import React, { useEffect } from 'react';

function MyComponent() {
  useEffect(() => {
    // 在组件加载完成后执行你的方法
    myMethod();
  }, []); // 空的依赖数组表示只在组件挂载时执行一次

  function myMethod() {
    // 在这里执行你的操作
  }

  return (
    // JSX内容
  );
}

export default MyComponent;
```

无论你选择使用类组件的`componentDidMount`方法还是函数组件的`useEffect`钩子，都可以在组件加载完成后执行你的方法。



### 13. NVM的使用

#### 常用命令

```shell
nvm off                     // 禁用node.js版本管理(不卸载任何东西)
nvm on                      // 启用node.js版本管理
nvm install <version>       // 安装node.js的命名 version是版本号 例如：nvm install 8.12.0
nvm uninstall <version>     // 卸载node.js是的命令，卸载指定版本的nodejs，当安装失败时卸载使用
nvm ls                      // 显示所有安装的node.js版本
nvm list available          // 显示可以安装的所有node.js的版本
nvm use <version>           // 切换到使用指定的nodejs版本
nvm v                       // 显示nvm版本
nvm install stable          // 安装最新稳定版
```



### 14. Elasticsearch数据同步方案

一般情况下，如果做查询搜索功能，使用ES来模糊搜索，但是数据是存放在数据库中里的，所以说我们需要把数据库中的数据和ES进行同步，保证数据一致（以数据库为主）。

#### 数据库->ES单向

首次安装完ES，把数据库全量同步到ES里，写一个单次脚本。

四种方式，首次全量同步 + 新数据增量同步

1. 定时任务：比如一分钟同步一次，找到数据库中过去几分钟内（至少是定时周期的两倍）发生改变的数据，然后更新到ES
   - 优点：简单易懂、占用资源少、不用引入第三方中间件
   - 缺点：有时间差
   - 应用场景：数据短时间内不同步影响不大、或者数据几乎不发生改变
2. 双写：写数据的是偶，也必须去写ES；更新或删除数据库数据时同理。（事务：建议先保证数据库写入成功，如果ES写失败，可以通过定时任务 + 日志 + 告警，进行检测和修复，俗称补偿）
3. Logstash中间件：用Elastic Stack中的Logstash中间件，但是一般要配合kafka消息队列 + beats采集器
4. Canal：通过订阅数据库流水的方式使用canal
   - 优点：实时同步，实时性非常强
   - 原理：数据库每次修改时，都会修改binlog文件，只要监听该文件的修改，就能第一时间得到消息并处理。Canal伪装成了MySQL的从节点，来接受主节点给的binlog



### 15. 正则的使用

Regex是正则表达式的简称（Regular Expression）。它便于匹配、查找和管理文本。

#### 基本匹配

##### 点 `.`：任何字符

`.` 允许匹配任何字符，包括特殊字符和空格。

```js
# 文本：abcABC123 .:!?
# 正则表达式：
/./g

# 题目：请编写表达式，匹配文本中所有字母、数字、空格和特殊字符。表达式必须匹配任何字符。
# 文本：az AZ 09 _- = !? ., :;
# 正则表达式：
/./g
```

##### 字符集`[abc]`

如果一个词中的字符可以是各种字符，我们就将所有的可选字符写进中括号`[]`中。我们需要编写表达式，在 [] 中相邻地输入字符 a、e、i、o、u。

```js
# 题目：查找文本中所有的单词
# 文本：bar ber bir bor bur
# 正则表达式：
/b[aeiou]r/g

# 题目：写出匹配文本中所有单词的表达式。单词首字母是唯一变化的字符。
# 文本：beer deer feer
# 正则表达式：
/[bdf]eer/g
```

##### 否定字符集`[^abc]`

为了查找下方文本的所有单词（ber 和 bor 除外），请在 [] 中的 ^ 后面并排输入 e 和 o。

```js
# 文本：bar ber bir bor bur
# 正则表达式：
/b[^eo]r/g

# 题目：请编写表达式，匹配除 beor 和 beur 以外的所有单词。要求使用否定字符集完成。
# 文本：bear beor beer beur
# 正则表达式：
/be[^ou]r/g
```

##### 字母范围`[a-z]`

为了查找指定范围的字母，我们需要将起始字母和结束字母写进 [] 中，中间用连字符 - 分隔。它区分大小写。

```js
# 题目：请编写表达式，匹配 e 和 o 之间所有的小写字母，包括它们本身。
# 文本：abcdefghijklmnopqrstuvwxyz
# 正则表达式：
/[e-o]/g

# 题目：请编写表达式，匹配 g 到 k 之间的所有字母，包括它们本身。
# 文本：abcdefghijklmnopqrstuvwxyz
# 正则表达式：
/[g-k]/g
```

##### 数字范围`[0-9]`

为了查找指定范围的数字，我们需要在 [] 中输入起始和结束数字，中间用连字符 - 分隔。

```js
# 题目：请编写表达式，匹配 3 到 6 之间的所有数字，包括它们本身。
# 文本：0123456789
# 正则表达式：
/[3-6]/g

# 题目：请编写表达式，匹配 2 到 7 之间的所有数字，包括它们本身。
# 文本：0123456789
# 正则表达式：
/[2-7]/g
```



#### 重复

一些特殊字符用来指定一个字符在文本中的重复次数。它们分别是`+`、`*`、`?`

##### 星号`*`

在字符后面加上 *，表示一个字符完全不匹配或可以匹配多次。

```js
# 题目：表示字母 e 在下方文本中不出现，只出现 1 次或者并排出现多次。
# 文本：br ber beer
# 正则表达式
/be*r/g

# 题目：请编写表达式，用 * 匹配下方文本中，没有或存在多个字母 e 的单词。
# 文本：dp dep deep
# 正则表达式
/de*p/g
```

##### 加号`+`

为了表示一个字符可以出现一次或多次，我们将 + 放在它后面。

```js
# 题目：表示 e 在下方文本中出现一次或多次。
# 文本：br ber beer
# 正则表达式：
/be+r/g

# 题目：请编写表达式，用 + 匹配下方文本中，字母 e 出现一次或多次的单词。
# 文本：dp dep deep
# 正则表达式：
/de+p/g
```

##### 问号`？`

为了表示一个字符是可选的，我们在它后面加一个 ?。

```js
# 题目：表示下方文本中的字母 u 是可选的。
# 文本：color, colour
# 正则表达式：
/colou?r/g

# 题目：请编写表达式，用 ? 表示字母 n 在文本中是可选的，使 a 和 an 都可以匹配到。
# 文本：a, an
# 正则表达式：
/an?/g
```

##### 大括号

- 为了表示一个字符出现的确切次数，我们在该字符的末尾，将它出现的次数写进大括号 {} 中，如 {n}。 

```js
# 题目：表表示下方文本中的字母 e 只能出现 2 次。
# 文本：ber beer beeer beeeer
# 正则表达式：
/be{2}r/g

# 题目：用 {} 编写表达式，匹配文本中，位数为 4 的阿拉伯数字。
# 文本：Release 10/9/2021
# 正则表达式：
/[0-9]{4}/g
```

- 为了表示一个字符至少出现多少次，我们在该字符的末尾，将它至少应出现的次数写进大括号 {} 中，并在数字后面加上逗号，如 {n, }。

```js
# 题目：表示下方文本中的字母 e 至少出现 3 次。
# 文本：ber beer beeer beeeer
# 正则表达式：
/be{3,}r/g
    
# 题目：用 {} 编写表达式，匹配文本中，位数至少为 2 的阿拉伯数字。
# 文本：Release 10/9/2021
# 正则表达式：
/[0-9]{2,}/g
```

- 为了表示一些字符出现的次数在某个数字范围内，我们在该字符的末尾，将它至少和至多出现的次数写进大括号 {} 中，中间用逗号 , 分隔，如 {x,y}。

```js
# 题目：匹配下方文本中，字母 e 出现 1 至 3 次的单词。
# 文本：ber beer beeer beeeer
# 正则表达式：
/be{1,3}r/g

# 题目：用 {} 编写表达式，匹配文本中，位数为 1 至 4 的阿拉伯数字。
# 文本：Release 10/9/2021
# 正则表达式：
/[0-9]{1,4}/g
```



#### 分组

##### 括号`()`

我们可以对一个表达式进行分组，并用这些分组来引用或执行一些规则。为了给表达式分组，我们需要将文本包裹在()中。

```js
# 题目：为下方文本中的 haa 构造分组。
# 文本：ha-ha,haa-haa
# 正则表达式：
/(haa)/g
```

##### 引用组

单词 ha 和 haa 分组如下。第一组用 \1 来避免重复书写。这里的 1 表示分组的顺序。

```js
# 题目：请在表达式的末尾键入 \2 以引用第二组。
# 文本：ha-ha,haa-haa
# 正则表达式：
/(ha)-\1,(haa)-\2/g
```

##### 括号(?:)：非捕获分组

您可以对表达式进行分组，并确保它不被引用捕获。例如，下面有两个分组，但我们用 \1 引用的第一个组实际上是指向第二个组，因为第一个是未被捕获的分组。

```js
# 文本：ha-ha,haa-haa
# 正则表达式：
/(?:ha)-ha,(haa)-\1/g
```



#### 零宽断言

如果我们希望正在写的词语出现在另一个词语之前或之后，我们需要使用「零宽断言」。

##### 正向先行断言: `(?=)`

例如，我们要匹配文本中的小时值。为了只匹配后面有 PM 的数值，我们需要在表达式后面使用正向先行断言 (?=)，并在括号内的 = 后面添加 PM。

```js
# 文本：Date: 4 Aug 3PM
# 正则表达式：
/\d+(?=PM)/g
```

##### 负向先行断言`(?!)`

例如，我们要在文本中匹配小时值以外的数字。我们需要在表达式后面使用负向先行断言`(?!)`，并在括号内的`!`后面添加PM，从而只匹配没有PM的数值

```js
# 文本：Date: 4 Aug 3PM
# 正则表达式：
/\d+(?!PM)/g
```

##### 正向后行断言`(?<=)`

例如，我们要匹配文本中的金额数。为了只匹配前面带有 $ 的数字。我们要在表达式前面使用正向后行断言 (?<=)，并在括号内的 = 后面添加 \$。

```js
# 文本：Product Code: 1064 Price: $5
# 正则表达式：
/(?<=\$)\d+/g
```

##### 负向后行断言`(?<!)`

例如，我们要在文本中匹配除价格外的数字。为了只匹配前面没有 $ 的数字，我们要在表达式前用负向后行断言 (?<!)，并在括号内的 ! 后面添加 \$。

```js
# 文本：Product Code: 1064 Price: $5
# 正则表达式：
/(?<!\$)\d+/g
```



#### 标志

标志改变表达式的输出。这就是标志也称为 修饰符 的原因。标志决定表达式是否将文本视作单独的行处理，是否区分大小写，或者是否查找所有匹配项。

##### 全局标志

全局标志使表达式选中所有匹配项，如果不启用全局标志，那么表达式只会匹配第一个匹配项。现在，请启用全局标志，以便匹配所有匹配项。

```js
# 文本：domain.com, test.com, site.com
# 正则表达式：
/\w+\.com/g
```

##### 多行标志

正则表达式将所有文本视作一行。但如果我们使用了多行标志，它就会单独处理每一行。这次，我们将根据每一行行末的规律来写出表达式，现在，请启用多行标志来查找所有匹配项。

```js
# 文本：
# domain.com
# test.com
# site.com
# 正则表达式：
/\w+\.com/gm
```

##### 忽略大小写标志

为了使我们编写的表达式不再大小写敏感，我们必须启用 不区分大小写 标志。

```js
# 文本：
# DOMAIN.COM
# TEST.COM
# SITE.COM
# 正则表达式：
/\w+\.com/gmi
```

##### 贪婪匹配

正则表达式默认执行贪婪匹配。这意味着匹配内容会尽可能长。请看下面的示例，它匹配任何以 r 结尾的字符串，以及前面带有该字符串的文本，但它不会在第一个 r 处停止匹配。

```js
# 文本：ber beer beeer beeeer
# 正则表达式：
/.*r/
```

##### 懒惰匹配

与贪婪匹配不同，懒惰匹配在第一次匹配时停止。下面的例子中，在 * 之后添加 ?，将查找以 r 结尾且前面带有任意字符的第一个匹配项。这意味着本次匹配将会在第一个字母 r 处停止。

```js
# 文本：ber beer beeer beeeer
# 正则表达式：
/.*?r/
```



#### 其他正则

##### 竖线`|`

竖线允许一个表达式包含多个不同的分支。所有分支用 | 分隔。和在字符层面上运作的字符集 [abc] 不同，分支在表达式层面上运作。

```js
# 题目：下面的表达式同时匹配 cat 和 rat。请在末尾添加另一个 |，并输入 dog 以匹配所有单词。
# 文本：cat rat dog
# 正则表达式：
/(c|r)at|dog/g
```

##### 转义字符

在书写正则表达式时，我们会用到 { } [ ] / \ + * . $^ | ? 这些特殊字符 。为了匹配这些特殊字符本身，我们需要通过 \ 将它们转义。

```js
# 题目：要匹配文本中的 . 和 *，我们需要在它们前面添加一个 \。
# 文本：(*) Asterisk.
# 正则表达式：
/(\.|\*)/g
```

##### 插入符`^`

`^`用来匹配字符串的开始，比如，我们用 [0-9] 查找数字，若仅查找行首的数字，请在表达式前面加上 ^。

```js
# 文本：
# Basic Omellette Recipe
# 1. 3 eggs, beaten
# 2. 1 tsp sunflower oil
# 3. 1 tsp butter
# 正则表达式：
/^[0-9]/gm
```

##### 美元符`$`

`$`用来匹配字符串的结束，让我们在 html 的后面添加 $，来查找仅在行末出现的 html。

```js
# 文本：
# https://domain.com/what-is-html.html
# https://otherdomain.com/html-elements
# https://website.com/html5-features.html
# 正则表达式：
/html$/gm
```

##### 单词字符`\w`

表达式 \w 用于查找字母、数字和下划线。让我们用表达式 \w 来查找文本中的单词字符。

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\w/g
```

##### 非单词字符`\W`

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\W/g
```

##### 数字字符`\d`

\d 仅用来匹配数字。

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\d/g
```

##### 非数字字符`\D`

\D 匹配除数字之外的字符。

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\D/g
```

##### 空白符`\s`

\s 仅匹配空白字符。

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\s/g
```

##### 非空白符`\S`

\S 仅匹配空白字符。

```js
# 文本：abcABC123 _.:!?
# 正则表达式：
/\S/g
```








## 二、Database

### 1. MySQL修改账号远程登陆权限

- 方法一：
  - `use mysql;`
  - `update user set host='%' where user='root';`
- 方法二：
  - `grant all privileges on *.* to 'root'@'%' identififed by '密码' with grant option;`

- 然后 `flush privileges;` 刷新权限



### 2. MySQL管理

#### 开发规范

**一、 命名规范**

1. 库名、表名、字段名必须使用小写字母并采用下划线分割

2. 库名、表名、字段名禁止超过 32 个字符，须见名知意；

3. 库名、表名、字段名支持最多 64 个字符，统一规范、易于辨识以及减少传输量不要超过 32 ；

4. 库名、表名、字段名禁止使用 MySQL 保留关键字（如果表名中包含关键字查询时，需要将其用单引号括起来）；

5. 临时库、临时表名必须以 tmp_ 为前缀并以日期为后缀；

6. 备份库、备份表名必须以 bak 为前缀并以日期为后缀；

7. 所有存储相同数据的列名和列类型必须一致（一般作为关联列，如果查询时关联列类型不一致会自动进行数据类型隐式转换，会造成列上的索引失效，导致查询效率降低）。

**二、 基本设计规范**

1. 所有表必须使用 Innodb 存储引擎
   - 没有特殊要求（即 Innodb 无法满足的功能如：列存储，存储空间数据等）的情况下，所有表必须使用 Innodb 存储引擎（ MySQL5.5 之前默认使用 Myisam ， 5.6 以后默认的为 Innodb ） Innodb 支持事务，支持行级锁，更好的恢复性，高并发下性能更好。

2. 数据库和表的字符集统一使用 utf8mb4( 5.5.3 版本以上支持 )
   - 兼容性更好，统一字符集可以避免由于字符集转换产生的乱码，不同的字符集进行比较前需要进行转换会造成索引失效；

3. 所有表和字段都需要添加注释
   - 使用 comment 从句添加表和列的备注 从一开始就进行数据字典的维护；

4. 尽量控制单表数据量的大小，建议控制在 1000 万以内
   - 1000 万并不是 MySQL 数据库的限制，过大会造成修改表结构，备份，恢复都会有很大的问题可以用历史数据归档（应用于日志数据），分库分表（应用于业务数据）等手段来控制数据量大小。

5. 谨慎使用 MySQL 分区表
   - 业务生命周期内，评估单表数据量是否在 1000 万以内，超出此范围需考虑分库分表可扩展性；分区表在物理上表现为多个文件，在逻辑上表现为一个表，谨慎选择分区键，跨分区查询效率可能更低，建议采用物理分表的方式管理大数据。

6. 尽量做到冷热数据分离，减小表的宽度
   - MySQL限制每个表最多存储 4096 列，并且每一行数据的大小不能超过 65535 字节 减少磁盘 IO, 保证热数据的内存缓存命中率（表越宽，把表装载进内存缓冲池时所占用的内存也就越大 , 也会消耗更多的 IO ） 更有效的利用缓存，避免读入无用的冷数据 经常一起使用的列放到一个表中（避免更多的关联操作）。

7. 禁止在表中建立预留字段
   - 预留字段的命名很难做到见名识义 预留字段无法确认存储的数据类型，所以无法选择合适的类型 对预留字段类型的修改，会对表进行锁定。

8. 禁止在数据库中存储图片，文件等大的二进制数据
   - 通常文件很大，会短时间内造成数据量快速增长，数据库进行数据库读取时，通常会进行大量的随机IO操作，文件很大时， IO 操作很耗时 通常存储于文件服务器，数据库只存储文件地址信息。

9. 禁止在线上做数据库压力测试

10. 禁止从开发环境，测试环境直接连接生成环境数据库。

**三、 字段设计规范**

1. 优先选择符合存储需要的最小的数据类型
   - 列的字段越大，建立索引时所需要的空间也就越大，这样一页中所能存储的索引节点的数量也就越少也越少，在遍历时所需要的 IO 次数也就越多， 索引的性能也就越差。建议：1 ）将字符串转换成数字类型存储，如：将 IP 地址转换成整形数据。2 ）对于非负型的数据（如自增 ID 、整型 IP ）来说，要优先使用无符号整型来存储因为：无符号相对于有符号可以多出一倍的存储空间， VARCHAR(N) 中的 N 代表的是字符数，而不是字节数使用 UTF8 存储 255 个汉字 Varchar(255)=765 个字节。过大的长度会消耗更多的内存。

2. 避免使用 TEXT 、 BLOB 数据类型

   - 最常见的 TEXT 类型可以存储 64k 的数据， 建议把 BLOB 或是 TEXT 列分离到单独的扩展表中。

   - MySQL内存临时表不支持 TEXT 、 BLOB 这样的大数据类型，如果查询中包含这样的数据，在排序等操作时，就不能使用内存临时表，必须使用磁盘临时表进行。

   - 且对于这种数据，MySQL还是要进行二次查询，会使 sql 性能变得很差，但是不是说一定不能使用这样的数据类型。

   - 如果一定要使用，建议把BLOB或是 TEXT 列分离到单独的扩展表中，查询时一定不要使用 select \* 而只需要取出必要的列，不需要 TEXT 列的数据时不要对该列进行查询。

   - 注意：TEXT或 BLOB 类型只能使用前缀索引，因为 MySQL 对索引字段长度是有限制的，所以 TEXT 类型只能使用前缀索引，并且 TEXT 列上是不能有默认值的。

3. 避免使用 ENUM 类型

   -  修改ENUM值需要使用 ALTER 语句

   - ENUM类型的 ORDER BY 操作效率低，需要额外操作

   - 禁止使用数值作为ENUM的枚举值

4. 尽可能把所有列定义为 NOT NULL

   - 原因：索引NULL列需要额外的空间来保存，所以要占用更多的空间；

   - 进行比较和计算时要对NULL值做特别的处理。

5. 使用 TIMESTAMP 存储时间
   - TIMESTAMP 存储的时间范围 1970-01-01 00:00:01 ~ 2038-01-19-03:14:07 。TIMESTAMP 使用 4 字节， DATETIME 使用 8 个字节，同时 TIMESTAMP 具有自动赋值以及自动更新的特性。

6. 财务相关的金额类数据必须使用 decimal 类型

   - 非精准浮点：float,double

   - 精准浮点：decimal

   - Decimal类型为精准浮点数，在计算时不会丢失精度。占用空间由定义的宽度决定，每 4个字节可以存储9位数字，并且小数点要占用一个字节。可用于存储比bigint更大的整型数据。

7. 用 DECIMAL 代替 FLOAT 和 DOUBLE 存储精确浮点数

   - 浮点数相对于定点数的优点是在长度一定的情况下，浮点数能够表示更大的数据范围；浮点数的缺点是会引起精度问题

   - 将字符转化为数字

   - 使用 TINYINT 来代替 ENUM 类型

   - 字段长度尽量按实际需要进行分配，不要随意分配一个很大的容量

8. 使用 UNSIGNED 存储非负整数
   - 同样的字节数，存储的数值范围更大。如 tinyint 有符号为 -128-127 ，无符号为 0-255 ；INT 类型固定占用 4 个字节存储

9. 使用 INT UNSIGNED 存储 IPV4

10. 使用 VARBINARY 存储大小写敏感的变长字符串

11. 禁止在数据库中存储明文密码

**四、索引设计规范**

建立索引的目的是：希望通过索引进行数据查找，减少随机 IO ，增加查询性能 ，索引能过滤出越少的数据，则从磁盘中读入的数据也就越少。

索引是一把双刃剑，可提高查询效率，但也会降低插入和更新的速度并占用磁盘空间。

1. 单张表中索引数量不超过 5 个
   - 限制每张表上的索引数量，建议单张表索引不超过 5 个索引；索引可以提高效率同样可以降低效率。索引可以增加查询效率，但同样也会降低插入和更新的效率，甚至有些情况下会降低查询效率。优化器在选择如何优化查询时，会根据统一信息，对每一个可以用到的索引来进行评估，以生成出一个最好的执行计划，如果同时有很多个索引都可以用于查询，会增加 MySQL 优化器生成执行计划时间，降低查询性能。

2. 禁止给表中的每一列都建立单独的索引
   - 5.6 版本之前，一个 sql 只能使用到一个表中的一个索引， 5.6 以后，虽然有了合并索引的优化方式，但远没有使用联合索引的查询方式效率高。

3. Innodb 表必须要有主键

   - Innodb是一种索引组织表：数据的存储的逻辑顺序和索引的顺序是相同的。

   - 每个表都可以有多个索引，但是表的存储顺序只能有一种 Innodb是按照主键索引的顺序来组织表的。不要使用更新频繁的列作为主键，不适用多列主键（相当于联合索引） 不要使用 UUID 、 MD5 、 HASH 、字符串列作为主键（无法保证数据的顺序增长）。

   - 主键建议使用自增ID值。

4. 单个索引中的字段数不超过 5 个

   - 对字符串使用前缀索引，前缀索引长度不超过10个字符；

   - 举例：如有一个 HAR(200) 列，在前 10 个字符内，多数值是唯一的，就可不要对整个列进行索引。对前 10 个字符进行索引能够节省大量索引空间，也可能会使查询更快。

5. 表主键建议

   - 表必须有主键，不使用更新频繁地列作为主键

   - 尽量不选择字符串列作为主键

   - 不使用 UUID 、 MD5 、 HASH 作为主键

   - 默认使用非空的唯一键

   - 主键建议选择自增或发号器重要的 SQL 必须被索引：

   - SELECT、 UPDATE 、 DELETE 语句的 WHERE 条件列 ORDER BY 、 GROUP BY 、 DISTINCT 的字段多表 JOIN 的字段

6. 区分度最大的字段放在索引前面

7. 核心 SQL 优先考虑覆盖索引
   - select 的数据列只用从索引中就能够取得，不必读取数据行，换句话说查询列要被所建的索引覆盖。

8. 避免冗余或重复索引

   - 合理创建联合索引（避免冗余），index(a,b,c)相当于 index(a) 、 index(a,b) 、 index(a,b,c)

   -  索引不是越多越好，按实际需要进行创建，每个额外的索引都要占用额外的磁盘空间，并降低写操作的性能

   - 不在低基数列上建立索引，例如 ‘性别’

   - 不在索引列进行数学运算和函数运算

9. 尽量避免使用外键约束
   - 不建议使用外键约束（ foreign key ），但一定要在表与表之间的关联键上建立索引；
   - 外键可用于保证数据的参照完整性，建议在业务端实现；
   - 外键会影响父表和子表的写操作从而降低性能。

10. 不使用 % 前导的查询，如 like “ %xxx ”，无法使用索引

11. 不使用反向查询，如 not in / not like
    - 无法使用索引，导致全表扫描，全表扫描导致 bufferpool 利用降低；

12. 索引列建议
    - 出现在 SELECT 、 UPDATE 、 DELETE 语句的 WHERE 从句中的列 ；
    - 包含在 ORDER BY 、 GROUP BY 、 DISTINCT 中的字段；
    - 多表 join 的关联列
    - 注意： 并不要将符合 1 和 2 中的字段的列都建立一个索引，通常将 1 、 2 中的字段建立联合索引效果更好

13. 如何选择索引列的顺序
    - 区分度最高的放在联合索引的最左侧（区分度 = 列中不同值的数量 / 列的总行数）；
    - 尽量把字段长度小的列放在联合索引的最左侧（因为字段长度越小，一页能存储的数据量越大， IO 性能也就越好）；
    - 使用最频繁的列放到联合索引的左侧（这样可较少的建立一些索引）。

14. 避免建立冗余索引和重复索引

    - 冗余 / 重复索引 会增加查询优化器生成执行计划的时间。

    - 重复索引示例：primary key(id) 、 index(id) 、 unique index(id)
    - 冗余索引示例：index(a,b,c) 、 index(a,b) 、 index(a)

15. 优先考虑覆盖索引

    - 对于频繁的查询优先考虑使用覆盖索引。

    - 覆盖索引：即 包含了所有查询字段 (where,select,ordery by,group by 包含的字段 ) 的索引 ， 覆盖索引的好处：
    - 避免 Innodb 表进行索引的二次查询
    - Innodb 是以聚集索引的顺序来存储的，对于 Innodb 来说，二级索引在叶子节点中所保存的是行的主键信息，如果是用二级索引查询数据，在查找到相应的键值后，还 需 通过主键进行二次查询才能获取我们真实所需要的数据。
    - 而在覆盖索引中，二级索引的键值中可以获取所有的数据，避免了对主键的二次查询 ，减少了 IO 操作，提升了查询效率。
    - 可以把随机 IO 变成顺序 IO 加快查询效率
    - 由于覆盖索引是按键值的顺序存储的，对于 IO 密集型的范围查找来说，对比随机从磁盘读取每一行的数据 IO 要少的多，因此利用覆盖索引在访问时也可以把磁盘的随机读取的 IO 转变成索引查找的顺序 IO 。

**五、SQL开发规范**

1. 建议使用预编译语句进行数据库操作
   - 预编译语句可以重复使用这些计划，减少 SQL 编译所需要的时间，还可以解决动态 SQL 所带来的 SQL 注入的问题 只传参数，比传递 SQL 语句更高效 相同语句可以一次解析，多次使用，提高处理效率。

2. 避免数据类型的隐式转换
   - 隐式转换会导致索引失效。

3. 充分利用表上已经存在的索引
   - 避免使用双 % 号的查询条件。
   - 如无前置 %, 只有后置 % ，是可以用到列上的索引的
   -  一个 SQL 只能利用到复合索引中的一列进行范围查询
   - 解说：有 a,b,c 列的联合索引，在查询条件中有 a 列的范围查询，则在 b,c 列上的索引将不会被用到，在定义联合索引时，如果 a 列要用到范围查找的话，就要把 a 列放到联合索引的右侧。使用 left join 或 not exists 来优化 not in 操作 ， 因 not in 也通常会使用索引失效。

4. 数据库设计时，应该要对以后扩展进行考虑

5. 程序连接不同的数据库使用不同的账号，进制跨库查询
   - 为数据库迁移和分库分表留出余地
   - 降低业务耦合度
   - 避免权限过大而产生的安全风险

6. 强烈不建议使用 SELECT\* ；推荐使用 SELECT < 字段列表 > 查询

   - 原因：消耗更多的 CPU 和 IO 以网络带宽资源

   - 无法使用覆盖索引
   - 可减少表结构变更带来的影响

7. 禁止使用不含字段列表的 INSERT 语句
   - 举例： insert into values ('a','b','c');
   - 应使用 insert into t(c1,c2,c3) values ('a','b','c');

8. 避免使用子查询，可把子查询优化为 join 操作

   - 通常子查询在 in 子句中，且子查询中为简单 SQL( 不包含 union 、 group by 、 order by 、 limit 从句 ) 时，才可以把子查询转化为关联查询进行优化。

   - 子查询性能差的原因：

   - 子查询的结果集无法使用索引，通常子查询的结果集会被存储到临时表中，不论是内存临时表还是磁盘临时表都不会存在索引，所以查询性能 会受到一定的影响；

   - 特别是对于返回结果集比较大的子查询，其对查询性能的影响也就越大；
   - 由于子查询会产生大量的临时表也没有索引，所以会消耗过多的 CPU 和 IO 资源，产生大量的慢查询。

9. 避免使用 JOIN 关联太多表
   - MySQL 最擅长的是单表的主键 / 二级索引查询， MySQL 存在关联缓存的，缓存的大小可以由 join_buffer_size 参数进行设置。在 MySQL 中，对于同一个 SQL 多关联（ join ）一个表，会多分配一个关联缓存，如果在一个 SQL 中关联的表越多，所占用的内存也就越大。
   - Join 消耗较多的内存，产生临时表；
   - 如程序中大量的使用了多表关联的操作，同时 join_buffer_size 设置的也不合理的情况下，就容易造成服务器内存溢出的情况，就会影响到服务器数据库性能的稳定性。
   - 同时对于关联操作来说，会产生临时表操作，影响查询效率。 MySQL 最多允许关联 61 个表，但业务生产环境中建议不超过 5 个 。

10. 减少同数据库的交互次数
    - 数据库更适合处理批量操作 合并多个相同的操作到一起，可以提高处理效率 。

11. 对应同一列进行 or 判断时，使用 in 代替 or
    - 不要超过 500 个 in 操作可以更有效的利用索引， or 大多数情况下很少能利用到索引。

12. 禁止使用 order by ， rand() 进行随机排序
    - 随机排序会把表中所有符合条件的数据装载到内存中，然后在内存中对所有数据根据随机生成的值进行排序，并且可能会对每一行都生成一个随机值，如果满足条件的数据集非常大，就会消耗大量的 CPU 和 IO 及内存资源。
    - 简单来说：order by ， rand() 会将数据从磁盘中读取，进行排序，会消耗大量的 IO 和 CPU 。
    - 推荐在程序中获取一个随机值，然后从数据库中获取 对应的 数据 。

13. WHERE 从句中禁止对列进行函数转换和计算
    - 对列进行函数转换或计算时会导致无法使用索引。

14. 在明显不会有重复值时使用 UNION ALL 而不是 UNION
    - UNION 会把两个结果集的所有数据放到临时表中后再进行去重操作 ；
    - UNION ALL 不会再对结果集进行去重操作。

15. 拆分复杂的大 SQL 为多个小 SQL
    - 大 SQL ：逻辑上比较复杂，需要占用大量 CPU 进行计算；
    - MySQL ：一个 SQL 只能使用一个 CPU 进行计算；
    - SQL 拆分后可以通过并行执行来提高处理效率。

16. 避免使用存储过程、触发器、 EVENTS 等
    - 降低业务耦合度，为分库分表 sacleout 、 sha rding 留点余地；
    - 改策略可有效规避 BUG 。

17. 避免在数据库中进行数学运算
    - 容易将业务逻辑和 DB 耦合在一起
    - MySQL 不擅长数学运算和逻辑判断
    - 无法使用索引

**六、 操作行为规范**

1. 超 100 万行的批量写（ UPDATE 、 DELETE 、 INSERT ）操作，要分批多次进行操作
1. 大批量操作可能会造成严重的主从延迟 。
   - 主从环境中，大批量操作可能会造成严重的主从延迟，大批量的写操作一般都需要执行一定长的时间，只有当主库上执行完成后，才会在其他从库上执行，会造成主库与从库长时间的延迟情况 。

3. binlog 日志为 row 格式时会产生大量的日志
   - 大批量写操作会产生大量日志，特别是对于 row 格式二进制数据而言，由于在 row 格式中会记录每一行数据的修改，一次修改的数据越多，产生的日志量也会越多，日志的传输和恢复所需要的时间也就越长，这也是造成主从延迟的一个原因。

4. 避免产生大事务操作

   - 大批量修改数据，一定是在一个事务中进行的，这会造成表中大批量数据进行锁定，导致大量的阻塞，阻塞会对 MySQL 的性能影响 很大 。尤其是 长时间的阻塞会占满所有数据库的可用连接，会使生产环境中的其他应用无法连接到数据库，因此一定要注意大批量写操作要进行分批。

   - 对于大表使用 pt-online-schema-change 修改表结构

   - 可避免大表修改产生的主从延迟

   - 可避免在对表字段进行修改时进行锁表

   - 生产环境中， 对大表数据结构的修改一定要谨慎，会造成严重的锁表操作 ；

   - pt-online-schema-change 首先建立一个与原表结构相同的新表，并且在新表上进行表结构的修改，然后再把原表中的数据复制到新表中，并在原表中增加一些触发器。

   - 把原表中新增的数据也复制到新表中，在行所有数据复制完成之后，把新表命名成原表，并把原来的表删除掉。把原来一个 DDL 操作，分解成多个小批次 作业 进行。

   - 这也是对表进行碎片整理 / 重组的一个常用方式。


5. 禁止程序使用的账号赋予 super 权限
   - 原因：当 MySQL 达到最大连接数限制时， 此刻还 运行 1 个有 super 权限的用户连接 ， super 权限只能留给 DBA 处理问题的账号使用。

6. 对于程序连接数据库账号，遵循权限最小原则程序
   - 使用数据库账号只能在一个 DB 下使用，不准跨库 程序使用的账号原则上不准有 drop 权限。

其他一些操作规范：

5. 任何数据库的线上操作，必须走工单

6. 禁止在主库上执行统计类的功能查询；

7. 有大规模市场推广、运营活动必须提前通知 DBA 进行流量评估；

8. 对单表的多次 alter 操作必须合并为一次操作；

9. 不在 MySQL 数据库中存放业务逻辑，即可创建存储过程；

10. 重大项目的数据库方案选型和设计必须提前通知 DBA 参与；

11. 数据必须有备份机制和定期的恢复演练；

12. 不在业务高峰期批量更新、查询数据库。

#### 优化相关建议

- MySQL会使用索引的操作符号

    - <,<=,>=,>,=,between
    - 不带%或者_开头的like
    
- 使用索引的缺点

    - 减慢增删改数据的速度；
    - 占用磁盘空间；
    - 增加查询优化器的负担；
    - 当查询优化器生成执行计划时，会考虑索引，太多的索引会给查询优化器增加工作量，导致无法选择最优的查询方案；
    
- 分析索引效率

  - 方法：在一般的SQL语句前加上explain；
  - 分析结果的含义：
    - table：表名；
    - type：连接的类型，(ALL/Range/Ref)。其中ref是最理想的
    - possible_keys：查询可以利用的索引名
    - key：实际使用的索引
    - key_len：索引中被使用部分的长度（字节）
    - ref：显示列名字或者"const"
    - rows：显示MySQL认为在找到正确结果之前必须扫描的行数
    - extra：MySQL的建议；
- 数据表使用较短的定长列
  - 尽可能使用较短的数据类型；
  - 尽可能使用定长数据类型；
    - 用char代替varchar，固定长度的数据处理比变长的快些；
    - 对于频繁修改的表，磁盘容易形成碎片，从而影响数据库的整体性能；
    - 万一出现数据表崩溃，使用固定长度数据行的表更容易重新构造。使用固定长度的数据行，每个记录的开始位置都是固定记录长度的倍数，可以很容易被检测到，但是使用可变长度的数据行就不一定了；
    - 对于MyISAM类型的数据表，虽然转换成固定长度的数据列可以提高性能，但是占据的空间也大；

- 使用not null和enum

  - 尽量将列定义为not null，这样可使数据的出来更快，所需的空间更少，而且在查询时，MySQL不需要检查是否存在特例，即null值，从而优化查询；

  - 如果一列只含有有限数目的特定值，如性别，是否有效或者入学年份等，在这种情况下应该考虑将其转换为enum列的值，MySQL处理的更快，因为所有的enum值在系统内都是以标识数值来表示的；


- 使用optimize table
  - 对于经常修改的表，容易产生碎片，使在查询数据库时必须读取更多的磁盘块，降低查询性能。
  - 具有可变长的表都存在磁盘碎片问题，这个问题对blob数据类型更为突出，因为其尺寸变化非常大。
  - 可以通过使用optimize table来整理碎片，保证数据库性能不下降，优化那些受碎片影响的数据表。 
  - optimize table可以用于MyISAM和BDB类型的数据表。实际上任何碎片整理方法都是用mysqldump来转存数据表，然后使用转存后的文件并重新建数据表；

- 使用procedure analyse()
  - 使用procedure analyse()显示最佳类型的建议，使用很简单，在select语句后面加上procedure analyse()就可以了；例如：
    - select * from students procedure analyse();
    - select * from students procedure analyse(16,256);
  - 第二条语句要求procedure analyse()不要建议含有多于16个值，或者含有多于256字节的enum类型，如果没有限制，输出可能会很长；

- 使用查询缓存
  - 查询缓存的工作方式：
    第一次执行某条select语句时，服务器记住该查询的文本内容和查询结果，存储在缓存中，下次碰到这个语句时，直接从缓存中返回结果；当更新数据表后，该数据表的任何缓存查询都变成无效的，并且会被丢弃。
  - 配置缓存参数：
    变量：query_cache _type，查询缓存的操作模式。有3中模式，0：不缓存；1：缓存查询，除非与 select sql_no_cache开头；2：根据需要只缓存那些以select sql_cache开头的查询； query_cache_size：设置查询缓存的最大结果集的大小，比这个值大的不会被缓存。

- 调整硬件
  - 在机器上装更多的内存；
  - 增加更快的硬盘以减少I/O等待时间；
    寻道时间是决定性能的主要因素，逐字地移动磁头是最慢的，一旦磁头定位，从磁道读则很快；
  - 在不同的物理硬盘设备上重新分配磁盘活动；
  - 如果可能，应将最繁忙的数据库存放在不同的物理设备上，这跟使用同一物理设备的不同分区是不同的，因为它们将争用相同的物理资源（磁头）。



#### MySQL命令

##### 系统相关

- 查询时间

```mysql
select now();
```

- 查询当前用户

```mysql
select user();
```

- 查询数据库版本：

```mysql
select version();
```

- 查询当前使用的数据库：

```mysql
select database();
```

- 查看sql查询效率

```mysql
explain select * from t3 where id=3952602;
```

- 列出数据库

```mysql
show databases;
```

- 选择数据库

```mysql
use databaseName;
```

- 列出表格

```mysql
show tables;
```



##### 查询相关

- 联合字符或者多个列(将列id与":"和列name和"="连接)

```mysql
select concat(id,':',name,'=') from students;
```

- limit：选出10到20条

```mysql
select * from students order by id limit 9,10;
```



##### 索引相关

- 创建索引

```mysql
alter table table1 add index ind_id (id);
create index ind_id on table1 (id);
-- 建立唯一性索引
create unique index ind_id on table1 (id);
```

- 删除索引

```mysql
drop index idx_id on table1;
alter table table1 drop index ind_id;
```



##### 用户相关

- 增加新用户

```mysql
-- 普通创建用户并设置连接方式
CREATE USER 'test1'@'localhost' IDENTIFIED BY 'test1';
-- 赋予账号管理员权限
grant all on *.* to 'weihu'@'%' with grant option;
-- 创建用户并赋予权限
grant select on 数据库.* to 用户名@登录主机 identified by "密码"

-- 增加一个用户test密码为123，让他可以在任何主机上登录， 并对所有数据库有查询、插入、修改、删除的权限。
grant select,insert,update,delete on *.* to test Identified by "123";
-- 增加一个管理员用户
-- 如果报错最好使用先创建普通用户，然后去赋予管理员权限的方式
grant all on *.* to user@localhost identified by "password";
-- 最后刷新权限
flush privileges;
```

- 修改密码

```mysql
-- 命令行方式
-- mysqladmin -u用户名 -p旧密码 password 新密码
-- sql的方式
update user set password=password('521') where user='root' and host='localhost';
```



##### 权限相关



##### 数据表相关

- 修改表名

```mysql
alter table t1 rename t2;
```

- 显示数据表结构

```mysql
desc test;
show columns from tableName;
```

- 创建数据表

```mysql
-- DEFAULT 1：设置字段默认值
create table test(
`id` int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT ‘主表id’,
`name` string NOT NULL COMMENT ‘名称’
`age` int NULL DEFAULT 18 COMMENT '年龄'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

- 创建临时表

```mysql
create temporary table test(name varchar(10));
```

- 创建表是先判断表是否存在

```mysql
create table if not exists students(name varchar(10));
```

- 复制表

```mysql
create table table2 select * from table1;
-- 复制表从已经有的表中复制表的结构
create table table2 select * from table1 where 1<>1;
```

- 删除数据表

```mysql
drop table test;
```

- 修改数据表名

```mysql
-- ALTER TABLE <旧表名> RENAME TO <新表名>；
alter talbe oldTableName reanme to newTalbeName；
```

- 清空数据表记录

```mysql
-- 这种方式不会重置自动递增的id
delete from test;
-- 这种方式则会重置自动递增的id
truncate table test;
```

- 增加字段

```mysql
-- 增加一个字段：
alter table tabelName add column fieldName dateType;
-- 增加多个字段：
alter table tabelName add column fieldName1 dateType,add columns fieldName2 dateType;
-- 增加一个字段并指定在哪个字段之后
-- FIRST 和 AFTER 为可选参数
-- FIRST：将新添加的字段设置为表的第一个字段
-- AFTER：将新添加的字段添加到指定的已存在的字段名的后面
alter table tableName add column fieldName1 dateType after fieldNmae2;
```

- 修改字段

```mysql
-- 修改列id的类型为int unsigned
alter table table1 modify id int unsigned;
-- 修改列id的名字为sid，而且把属性修改为int unsigned
alter table table1 change id sid int unsigned;
```

- 删除字段

```mysql
-- ALTER TABLE <表名> DROP <字段名>；
alter table tableName drop name;
```



##### 数据库相关

- 创建数据库

```mysql
create database test;
-- GBK
create database test DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
-- UTF8
CREATE DATABASE test2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

- 删除数据库

```mysql
drop database test;
```

- 修改数据库编码格式

```mysql
-- 如果要改变某个库的编码格式：在mysql提示符后输入命令 
alter database db_name default character set gbk;
```



##### 数据导入导出

- 用文本方式将数据装入数据库表中

```mysql
LOAD DATA LOCAL INFILE "/opt/data/mysql.txt" INTO TABLE test;
```

- 文本数据转到数据库中

```mysql
-- 文本数据应符合的格式：字段数据之间用`tab键`隔开，`null值`用来代替。例：
load data local infile "./mysql.txt" into table test;
```

- 导出数据库和表

```shell
mysqldump --opt news > news.sql

# 将数据库news中的author表和article表备份到author.article.sql文件， author.article.sql是一个文本文件，文件名任取。
mysqldump --opt news author article > author.article.sql

# 将数据库dbl和db2备份到news.sql文件
mysqldump --databases db1 db2 > news.sql
# 使用指定账号导出数据库
mysqldump --databases db1 db2 > news.sql -uroot -p

# 就是把host上的以名字user，口令pass的数据库dbname导入到文件file.dump中
mysqldump -h host -u user -p pass --databases dbname > file.dump

# 将所有数据库备份到all-databases.sql文件
mysqldump --all-databases > all-databases.sql
```

- 导入数据

```mysql
-- 在mysql命令下执行，可导入表
-- 导入数据库
mysql < all-databases.sql
-- 导入表
mysql > source news.sql;
```



##### Binlog相关

- 查看某一个binlog的某一个节点的数据

```shell
mysqlbinlog --no-defaults -v -v --base64-output=decode-rows ./mysql-bin.000062 | grep -A 30 "230666661" --color
```



### 3. Oracle管理

#### 相关链接

[Oracle官方文档](https://docs.oracle.com/database/121/DBSEG/users.htm#DBSEG99778)

[Oracle新特性](https://blog.csdn.net/weixin_31758621/article/details/116294855)

[OraclePDB管理](https://blog.csdn.net/xin_shou123/article/details/123879415)

#### 体系架构

![image-20230711164235043](https://image.kevinkda.cn/md/image-20230711164235043.png)

​	从Oracle数据库架构的本身，充分体现了数据库这种数据库管理机制中，引用程序与数据的独立性，同时也体现了在软件设计中，结构化，模块化，分层分工，重用，效率等基本问题的解决办法。

##### 实例 Instance

![image-20230711164630986](https://image.kevinkda.cn/md/image-20230711164630986.png)

- PGA（Process Global Area）：
  - 用于保存服务器进程的数据和控制信息。
  - 当用户进程要连接到Oracle数据库服务器时，会在实例中分配相应的服务器进程。
- SGA（System Global Area）：
  - 主要为了减少对磁盘的访问，提高计算机系统性能。
  - 系统全局区，分为一下三个部分；
  - Shared Pool（共享池）：
    - 大小由 SHARED_POOL_SIZE 决定
    - 库缓存（库高速缓存）：存储并共享经过分析的最近执行的SQL和PL/SQL程序代表。通过内存中缓存SQL，能有效降低执行一组应用语句的服务开销
    - 字典缓存（数据字典高速缓存）：在系统运行的过程中，不断查询与更新数据库数据字典信息。实例的字典缓存存储了最多使用的数据字典的信息，提高了系统内部操作性能。
  - Database Buffer Cache（数据块告诉缓存区）：
    - DB_BLOCK_BUFFERS：buffer的数目
    - DB_BLOCK_SIZE：每个buffer的大小
    - 是最大的服务器内存区，存储应用事务最近查询的数据库信息，读出来的数据、真实的数据缓存、索引
  - Redo Log Buffer（日志缓存区）：
    - LOG_BUFFER：每个buffer的大小
    - 加速日志写的进程，为了写日志的缓存
- 后台进程
  - SMON
  - PMON
  - DBWR
    - 数据库写进程
    - DBWR有搁置空闲（time out）
  - LGWR
  - CKPT
    - 周期性的数据库写进程执行一次检查点，将内存中全部修改数据写回到数据库的数据文件中
  - ARCH
  - RECO

##### 存储结构

物理存储结构：实际数据的存储单元

![image-20230711171048623](https://image.kevinkda.cn/md/image-20230711171048623.png)

- 参数文件

- 控制文件
  
  - 记录内容：数据文件信息，日志文件信息，数据库创建时间，SCN；控制文件数量和存储位置：一遍需要三个，分布在不通的硬盘上
  - 三个控制文件不是冗余的，任意一个坏了都要修复
  
- 数据文件

- 日志文件

  - 存储数据库改变的事务数据，DSL
  - 系统冲突或其它系统故障后，日志文件中的信息可用于恢复事务，是保护数据库的关键
  - 每个Oracle数据库至少有两个日志文件

  ![image-20230808173504256](https://image.kevinkda.cn/md/image-20230808173504256.png)

  日志文件组和成员

  ![image-20230808173533558](https://image.kevinkda.cn/md/image-20230808173533558.png)

逻辑结构和物理结构：

![image-20230808173703526](https://image.kevinkda.cn/md/image-20230808173703526.png)

- 段类型

![image-20230808174351337](https://image.kevinkda.cn/md/image-20230808174351337.png)![image-20230808174405099](https://image.kevinkda.cn/md/image-20230808174405099.png)

- 逻辑存储结构 - 数据块
  - 最小的磁盘存取单元，当操作一个数据库时，Oracle使用数据块存储和提取磁盘上的数据
  - 由一个或多个O/S块组成
  - 在数据库创建时设定大小，块大小必须等于O/S块大小或它的倍数

![image-20230808174703009](https://image.kevinkda.cn/md/image-20230808174703009.png)

![image-20230808174717958](https://image.kevinkda.cn/md/image-20230808174717958.png)

![image-20230808174817563](https://image.kevinkda.cn/md/image-20230808174817563.png)

- 索引（Index）
  - B-Tree索引

![image-20230808175115452](https://image.kevinkda.cn/md/image-20230808175115452.png)

![image-20230810110137012](https://image.kevinkda.cn/md/image-20230810110137012.png)

- 回滚段（RollBack）
- 临时段（TEMP）
  - 永久表空间上的临时段
    - 事务需要排序时创建
    - 过程执行完成后由SMON回收
  - 临时表空间上的临时段
    - 用作排序
    - 每个实例每个表空间只有一个段
    - 实例重启后第一次发生内存排序空间不够时创建
    - 根据Sort Extent Pool的信息，多个事务可以复用临时段
    - 数据库关闭时释放

![image-20230810110435590](https://image.kevinkda.cn/md/image-20230810110435590.png)

##### Oracle安装组件

常用组件

- Oracle rdbms
- TCP/IP Protocal Adapter
- SQL*NET
- PL/SQL
- Distrbution Server

#####  内存设置

- /etc/system里的参数设置
  - 设置最大的Share Memory为物理内存的3/4 ~ 4/5 其他想基本按照缺省配置
  - 设置swap区为2-4倍的物理内存

##### 创建数据库

- 定义唯一的实例、数据库名和字符集
- 设置操作系统环境变量
- 准备初始化参数文件
- 启动实例
- 创建数据库
- 运行脚本文件创建数据字典以及一些必要步骤

##### Cache Fusion体系结构

![image-20230810113936824](https://image.kevinkda.cn/md/image-20230810113936824.png)

##### SQL的执行过程

1. 运用HASH算法，得到一个HASH值，这个值可以通过VSSQLAREAHASH VALUE 查看
2. 到shared pool中的 library cache 中查找是否有相同的HASH值，如果存在，则无需硬解析，进行软解析
3. 如果shared pool不存在此HASH值，则进行语法检查，查看是否有语法错误
4. 如果没有语法错误，就进行语义检查，检查该SQL引用的对象是否存在该用户是否具有访问该对象的权限
5. 如果没有语义错误，对该SQL进行解析，生成解析树，执行计划
6. 生成ORACLE能运行的二进制代码，运行该代码并且返回结果给用户

##### 共享SQL语句

为了不重复解析相同的SQL语句，在第一次解析之后，Oracle将SQL语句存放在内存中。这块位于系统全局区域的SGA（System Global Area）的共享池（Shared Buffer Pool）中的内存可以被所有的数据库用户共享。因此，当你执行一个SQL语句时，如果它和之前执行过的语句完全相同，Oracle就能很快的获得已经被解析的语句以及最好的执行路径。Oralce的这个功能大大地提高了SQL执行的性能并节省了内存的使用。

##### 应该简索引列的特点

- 在经常需要搜索的列上，可以加快搜索的速度。

- 在作为主键的列上，强制该列的唯一性和组织表中数据的排列结构在经常用
- 在连接的列上，这些列主要是一些外键，可以加快连接的速度
- 在经常需要根据范围进行搜索的列上创建索引，因为索引已经排序，其指定的范围是连续的。
- 在经常需要排序的列上创建索引，因为索引已经排序这样查询可以利用索引的排序，加快排序查询时间。
- 在经常使用在WHERE子句中的列上面创建索引，加快条件的判断速度

- 经常由空值，经常修改，不太常用的字段不建议建索引

#### CDB与PDB

CDB与PDB是Oracle 12C引入的新特性，在ORACLE 12C数据库引入的多租用户环境（Multitenant Environment）中，允许一个数据库容器(CDB)承载多个可插拔数据库(PDB)。

CDB全称为Container Database，中文翻译为数据库容器，PDB全称为Pluggable Database，即可插拔数据库。

在ORACLE 12C之前，实例与数据库是一对一或多对一关系(RAC)：即一个实例只能与一个数据库相关联，数据库可以被多个实例所加载。

而实例与数据库不可能是一对多的关系。当进入ORACLE 12C后，实例与数据库可以是一对多的关系。

![image-20220828030404818](https://image.kevinkda.cn/md/image-20220828030404818.png)

和SQL Server相对照的话，CDB与PDB是不是感觉和SQL SERVER的单实例多数据库架构是一回事。像PDB$SEED可以看成是master、msdb等系统数据库，PDBS可以看成用户创建的数据库。而可插拔的概念与SQL SERVER中的用户数据库的分离、附加其实就是那么一回事。

#### CDB组件

- ROOT组件
  - ROOT又叫CDB$ROOT, 存储着ORACLE提供的元数据和Common User,元数据的一个例子是ORACLE提供的PL/SQL包的源代码，Common User 是指在每个容器中都存在的用户。
- SEED组件
  - Seed又叫PDB$SEED,这个是你创建PDBS数据库的模板，你不能在Seed中添加或修改一个对象。一个CDB中有且只能有一个Seed. 这个感念，个人感觉非常类似SQL SERVER中的model数据库
- PDBS
  - CDB中可以有一个或多个PDBS，PDBS向后兼容，可以像以前在数据库中那样操作PDBS，这里指大多数常规操作。

这些组件中的每一个都可以被称为一个容器。因此，ROOT(根)是一个容器，Seed(种子)是一个容器，每个PDB是一个容器。每个容器在CDB中都有一个独一无二的的ID和名称。

#### Oracle角色说明

- connect（连接角色）
  - 这种角色下只可以登录Oracle，不可用创建实体，也不可用创建数据库结构，即只能对其他人创建的表中的数据进行操作。

- resource(资源角色)
  - 该角色可以创建实体，但是不可以创建数据库结构。 可以创建表、序列（sequence）、运算符(operator)、过程(procedure)、触发器(trigger)、索引(index)、类型(type)和簇(cluster)。

- dba（数据库管理员权限）
  - 该角色拥有系统最高权限，只有DBA才可以创建数据库结构。包括无限制的空间限额和给其他用户授予各种权限的能力，system由dba用户拥有。
    对于普通用户来说，授予connect和resource权限即可，只对dba授予connect、resource和dba权限。

#### Oracle命令

##### 系统相关

- 查询oracle版本

```sql
select *
from V$VERSION;
```
- 查询oracle的SID

```sql
select instance_name from v$instance;
```

- 查询db_name

```sql
select name from v$database;
```

- 重启数据库

```sql
shutdown immediate;
startup;
```
- 当前连接数

```sql
select count(*) from v$process;
```
- 数据库允许的最大连接数

```
select value from v$parameter where name = 'processes';
```
- 修改最大连接数:

```sql
alter system set processes = 2000 scope = spfile;
```

- 数据库服务器配置`tnsnames`,方便后期运维操作
```shell
# 添加前最好先备份下,vim tnsnames.ora编辑文件，仔细检查，不要配置错误
cd $ORACLE_HOME/network/admin/
```
  - 格式如下
```ora
TESTRAC =
	(DESCRIPTION =
		(ADDRESS = (PROTOCOL = TCP)(HOST = scan域名)(PORT = 1521))
	(CONNECT_DATA =
	(SERVER = DEDICATED)
	(SERVICE_NAME = TESTRAC )
)
```

数据库告警阈值设定查看

```sql
select warning_value, critical_value
from dba_thresholds
where metrics_name='Tablespace Space Usage' and object_name is NULL;
```

数据库当前告警和可用的处理方法

```sql
select reason,SUGGESTED_ACTION
from dba_outstanding_alerts
where object_name='CDATA';
```

查看系统的编码格式

```sql
select userenv('language') from dual;
```



##### PDB相关

- 查看CDB信息

```sql
select name, cdb, open_mode, con_id
from v$database;
```
- 查看PDB实例

```sql
select name, con_id, open_mode
from V$PDBS;
```
- 查看已有pdb的tempfile文件

```sql
select name
from V$TEMPFILE;
```
- 查看已有的PDB的datafile

```sql
select name
from V$DATAFILE;
```
- 创建一个新的PDB

- 密码大小写是否敏感可以在CDB下查看该参数: show parameter sensitive

- `file_name_convert`参数参数格式：`/opt/oracle/oradata/${SID}/pdbseed, /opt/oracle/oradata/${SID}/${PDB_Name}`

```sql
create pluggable database dev admin user dev identified by 123 file_name_convert =('/opt/oracle/oradata/ORCLCDB/pdbseed','/opt/oracle/oradata/orcl_root_dev');
```
- 设置pdb自启动

`${pdb} save state`是对于某个pdb而言。即你想让哪个pdb随着cdb启动，就设置哪一个。

```sql
alter pluggable database all save state;
-- 查询自启动设置
select con_name, instance_name, state from dba_pdb_saved_states;
-- 取消自启动
alter pluggable database all discard state;
```

- 启动或关闭一个创建好的PDB

```sql
alter pluggable database dev open;
alter pluggable database pdb1 close;
-- 启动所有pdb
alter pluggable database all open;
```
- 切换到指定PDB

```sql
alter session set container=pdb1;
```
- 查看配置文件default

```sql
-- FAILED_LOGIN_ATTEMPTS --用户失败登录尝试次数
-- PASSWORD_LIFE_TIME--用户密码生命周期（按规定要求是配置3个月90天）
-- PASSWORD_VERIFY_FUNCTION--密码校验函数
-- PASSWORD_GRACE_TIME--密码失效宽容期限(30天的宽容期限)
select * from dba_profiles;
```

- 删除PDB

```sql
-- 关闭所有节点下的指定PDB，PDB处于关闭状态才能删除
show pdbs；
-- 首先在所有节点上停止实例（PDB）
alter pluggable database testrac close immediate;
-- 单节点执行删除命令
drop pluggable database testrac including datafiles;
```

- 查看profile

```sql
-- 查看profile
select profile,resource_name,limit from dba_profiles;
select * from dba_profiles where profile='PASSWORD_UNLIMIT_PROFILE';
```

- 创建profile

```sql
-- 创建profile
CREATE PROFILE "PASSWORD_UNLIMIT_PROFILE" LIMIT
 COMPOSITE_LIMIT UNLIMITED
 SESSIONS_PER_USER UNLIMITED
 CPU_PER_SESSION UNLIMITED
 CPU_PER_CALL UNLIMITED
 LOGICAL_READS_PER_SESSION UNLIMITED
 LOGICAL_READS_PER_CALL UNLIMITED
 IDLE_TIME UNLIMITED
 CONNECT_TIME UNLIMITED
 PRIVATE_SGA UNLIMITED
 FAILED_LOGIN_ATTEMPTS 10
 PASSWORD_LIFE_TIME	180
 PASSWORD_REUSE_TIME UNLIMITED
 PASSWORD_REUSE_MAX	UNLIMITED
 PASSWORD_VERIFY_FUNCTION NULL
 PASSWORD_LOCK_TIME 1
 PASSWORD_GRACE_TIME 7
 INACTIVE_ACCOUNT_TIME UNLIMITED;
```

- 修改profile密码过期策略

```sql
-- 修改profile密码过期时间
ALTER profile PASSWORD_UNLIMIT_PROFILE limit PASSWORD_LIFE_TIME UNLIMITED;
```



##### 表空间相关

- 查看OMF配置的`db_create_file_dest`

```sql
show parameter db_create_file_dest;
```

- 查看表空间

```sql
select name from v$tablespace;
-- 查看表空间大小
SELECT t.tablespace_name, round(SUM(bytes / (1024 * 1024)), 0) ts_size
FROM dba_tablespaces t, dba_data_files d
WHERE t.tablespace_name = d.tablespace_name
GROUP BY t.tablespace_name; 
```

- 查看表空间下的表

```sql
select TABLE_NAME,TABLESPACE_NAME from dba_tables where TABLESPACE_NAME='CDATA';
```

- 查看表空间使用情况

```sql
select sum(bytes) / (1024 * 1024) as free_space, tablespace_name
from dba_free_space
group by tablespace_name
-- 查看表空间使用情况(注：若表空间未使用或者占满，sys.sm$ts_used、sys.sm$ts_free可能为空)
SELECT a.tablespace_name,a.bytes total,b.bytes used,c.bytes free,(b.bytes * 100) / a.bytes "% USED ",(c.bytes * 100) / a.bytes "% FREE "
FROM sys.sm$ts_avail a, sys.sm$ts_used b,sys.sm$ts_free c 
WHERE a.tablespace_name = b.tablespace_name
AND a.tablespace_name = c.tablespace_name;
```

- 查看单个表空间使用情况

```sql
select df.tablespace_name tablespace, fs.bytes free,
df.bytes , fs.bytes *100/ df.bytes pct_free
from dba_data_files df ,dba_free_space fs
where df.tablespace_name = fs.tablespace_name
and df.tablespace_name = 'CDATA';
```

- 查看表空间是否可扩展

```sql
SELECT T.TABLESPACE_NAME, D.FILE_NAME,  D.AUTOEXTENSIBLE,   D.BYTES,  D.MAXBYTES,   D.STATUS
FROM DBA_TABLESPACES T,DBA_DATA_FILES D 
WHERE T.TABLESPACE_NAME = D.TABLESPACE_NAME
ORDER BY TABLESPACE_NAME, FILE_NAME;
```

- 设置表空间大小和是否可扩展

```sql
//设置表空间大小
alter database datafile '/opt/oracle/oradata/orclpdb3/ORCL/DAD5E8983D36442CE053BF38A8C0BB73/datafile/o1_mf_inventor_k4ykocb9_.dbf' resize 64M;
//设置表空间是否可扩展s
alter database datafile '/opt/oracle/oradata/orclpdb3/ORCL/DAD5E8983D36442CE053BF38A8C0BB73/datafile/o1_mf_inventor_k4ykocb9_.dbf' autoextend off;
```

- 创建表空间

```sql
-- 最基础的创建表空间
create tablespace 123;
-- 创建表空间，指定数据文件位置，指定文件大小，扩宽性，等
-- 创建表空间时需要保证指定的datafile目录是存在的
-- 参数说明：
-- datafile '${data file path}'：数据文件路径
-- size ${size}：数据文件大小
-- autoextend on next ${size}：下次自动扩展大小
-- maxsize unlimited：最大尺寸无限制
create tablespace 表空间 datafile '/opt/oracle/oradata/orcl/数据文件.dbf' size 200m autoextend on next 10m maxsize unlimited;
```

- 创建临时表空间

```sql
-- 创建临时表空间，指定数据文件位置，指定文件大小，扩宽性，等
-- 创建临时表空间时需要保证指定的datafile目录是存在的
-- 参数说明：
-- tempfile '${temp data file path}'：数据文件路径
-- size ${size}：数据文件大小
-- autoextend on next ${size}：下次自动扩展大小
-- maxsize unlimited：最大尺寸无限制
create temporary tablespace 表空间 tempfile '/opt/oracle/oradata/orcl/数据文件.dbf' size 200m autoextend on next 10m maxsize unlimited;
```

- 设置表空间自动扩展

```sql
alter database datafile '/opt/oracle/oradata/oradata/orcl/数据文件.dbf' autoextend on;
```

- 查看文件位置(表空间等一些文件的位置)

```sql
select name from v$datafile;
```

- 查看默认表空间

```sql
select property_name ,property_value from database_properties where property_name like 'DEFAULT_%TABLE%';
```

- 设置默认表空间

```sql
alter database default tablespace 123;
-- 默认临时表空间
alter database default temporary tablespace 123;
```

- 删除表空间

```sql
drop tablespace 123;
-- 如果表空间有数据，使用以下命令删除
drop tablespace 123 including contents and datafiles;
```



##### 表空间权限

建用户的时候通常都可以选择一个default tablespace，但是在没有授权的情况下该用户也无法往该表空间写数据，需要进行授权。

授权有全局授权和通过quota限制两种情况（quota配额可以防止某个用户过多使用某个表空间中的空间）

- 授予用户全局表空间权限 - 通过命令的方式

```sql
grant unlimited tablespace to username;
```

- 授予用户全局表空间权限 - 通过角色的方式

```sql
-- 查看resource角色底下带的权限，没有unlimited tablespace权限
SELECT * from Dba_Sys_Privs s WHERE s.grantee='RESOURCE';
-- 把resource角色授予用户
grant resource to username;
--查看用户拥有的权限，可以发现自己带上了unlimited tablespace（另外这个时候可以去看dba_ts_quotas，这样授权的用户没有体现出来）
SELECT * from Dba_Sys_Privs s WHERE s.grantee='USERNAME' ;
```

- 授予某个用户完全访问某个表空间权限

```sql
-- 授权
alter user ${username} quota unlimited on ${tablespace};
-- 在授予完权限后查看dba_ts_quotas表
-- max_bytes = -1，代表不受限制
SELECT * from Dba_Ts_Quotas z WHERE z.username='USERNAME';
```

- 授予某个用户有限的访问某个表空间权限

```sql
-- 授权
ALTER USER username QUOTA 1M ON rcat;
-- 在授予完权限后查看dba_ts_quotas表
-- max_bytes = 1M
SELECT * from Dba_Ts_Quotas z WHERE z.username='USERNAME';
```

- 删除用户表空间权限

```sql
-- 全局
revoke unlimited tablespace from username;
-- 个别表空间
ALTER USER username  QUOTA 0 ON rcat 
```



##### 角色相关

Oracle三种标准角色，connect role(连接角色)、resource role(资源角色)、dba role(数据库管理员角色)

1. connect role：临时用户，特指不需要建表的用户，通常只赋予他们connect role。

   connect是使用oracle简单权限，这种权限只对其他用户的表有访问权限，包括select/insert/update和delete等。

   拥有connect role 的用户还能够创建表、视图、序列(sequence)、簇(cluster)、同义词(synonym)、回话(session)和其他 数据的链(link)

2. resource role：更可靠和正式的数据库用户可以授予resource role。

   resource提供给用户另外的权限以创建他们自己的表、序列、过程(procedure)、触发器(trigger)、索引(index)和簇(cluster)。

3. dba role：dba role拥有所有的系统权限

   包括无限制的空间限额和给其他用户授予各种权限的能力。system由dba用户拥有

- 查看所有角色

```sql
select * from dba_roles;
```

- 查看当前用户被激活的全部角色

```sql
select * from session_roles;
```

- 查看当前用户被授予的角色和信息

```sql
select * from user_role_privs;
```

- 查看某个用户所拥有的角色

```sql
select * from dba_role_privs where grantee = 'username';
```

- 查看某个角色所拥有的权限

```sql
select * from dba_sys_privs where grantee = 'CONNECT';
```

- 创建角色

创建的角色可以由表或系统权限或者两者的组合构成

```sql
-- 创建角色
create role myRole;
-- 授权角色
-- 如使myRole获得了在mytable中使用select进行查询的权限
grant select on mytable to myRole;
-- 再比如为角色赋予创建会话的权限
grant create session to myRole;
-- 删除角色
drop role myRole;
```

- 授予用户角色

```sql
-- 切换到对应的PDB下
alter session set container=PDB1;
show pdbs;
-- 授予dba、resource、connect角色
grant dba,resource,connect to pdb1;
-- 收回某个用户的某个角色
revoke dba,resource,connect from pdb1;
-- 查看用户角色
select * from dba_role_privs where grantee = 'PDB1' and granted_role in ('DBA','RESOURCE','CONNECT')
```

- 授予角色权限

```sql
-- create seesion 用户登陆会话权限
-- create table 用户建表权限
-- create sequence 用户创建序列权限
-- create view 用户创建视图权限
-- create procedure 用户创建存储过程权限
-- create tablespace 用户创建表空间权限
grant create session,create table to role_name;
```

- 撤销角色权限

```sql
revoke create table from role_name;
```



##### 用户相关

- 查看所有用户信息

```sql
select * from all_users;
```

- 查看当前用户的信息

```sql
select * from user_users;
```

- 创建用户，对于普通用户名，用户创建的普通用户名必须以C##（或c##）开头。

```sql
create user c##svc_res identified by 123;
-- 创建用户并指定表空间
-- default tablespace ${tablespace}：默认表空间
-- temporary tablespace ${talbespace}：临时表空间
create user tssh identified by "XXXXX" default tablespace TSSH_15_DATA_MIN temporary tablespace TEMP;
```
- 更改用户密码

```sql
-- 如果密码带有字符需要加上双引号
alter user pdb identified by 321
```

- 查看当前用户

```sql
show user;
```
- 删除用户

```sql
-- cascade操作需要谨慎，cascade代表代表着联级删除用户名下所有的表和视图
drop user c##svc_res cascade;
```
- 创建一个模式

Oracle是不支持创建自定义模式的，想要创建模式的话只能新建一个用户，每个用户会有一个默认的和用户名相同的模式

```sql
CREATE SCHEMA "svc_bitbucket" AUTHORIZATION SYSTEM;
```

- 查看当前有哪些用户正在使用数据

```sql
SELECT osuser, a.username,cpu_time/executions/1000000||'s', sql_fulltext,machine
from v$session a, v$sqlarea b
where a.sql_address =b.address order by cpu_time/executions desc;
```
- 锁定与解锁用户

```sql
alter user itcast account lock;
alter user itcast account unlock;
```

- 开启密码校验

```sql
-- 开启PDB下的用户密码校验
@?/rdbms/admin/utlpwdmg.sql
```

- 设置用户空间

```sql
-- 设置用户的空间配额
-- quota 容量的意思
-- unlimited 无限制
alter user itcast quota unlimited on pdb1;
```

- 设置用户失效
  - 旨在要求使用方强制修改密码，提高密码安全性和复杂度，避免由我方运维人员知晓

```sql
alter user testrac password expire;
select username,account_status from dba_users where oracle_maintained='N';
```

- 查看用户所属的profile

```sql
SELECT username,PROFILE FROM dba_users;
```

- 查看指定概要文件(default)的密码有效期设置

```sql
SELECT * FROM dba_profiles s WHERE s.profile='DEFAULT' AND resource_name='PASSWORD_LIFE_TIME';
```

- 修改密码有效期

```sql
-- 影响所有用户
ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;
```

- 修改用户所属的profile

[8、修改ORACLE单个用户密码过期策略](###8、修改ORACLE单个用户密码过期策略)

```sql
-- 修改用户所属profile
-- 修改单个用户的密码有效期可以通过新建profile，然后修改用户所属的profile实现
ALTER user SVC_CONFLUENCE profile PASSWORD_UNLIMIT_PROFILE;
```



##### 权限相关

- 基本权限查询

```sql
--当前用户所拥有的全部权限
select * from session_privs;
--当前用户的系统权限
select * from user_sys_privs;
--当前用户的对象权限
select * from user_tab_privs;
--查询某个用户所拥有的系统权限
select * from dba_sys_privs where grantee='DBA';
--查看角色(只能查看登陆用户拥有的角色)所包含的权限
select * from role_sys_privs;
```

- 查看哪些用户有`sysdba`或`sysoper`系统权限(查询时需要相应权限)

```sql
select * from v$pwfile_users;
```

- 查询所有的用户级别权限

```sql
select *
from system_privilege_map
order by name;
```

- 授予用户权限

```sql
-- create seesion 用户登陆会话权限
-- create table 用户建表权限
-- create sequence 用户创建序列权限
-- create view 用户创建视图权限
-- create procedure 用户创建存储过程权限
-- create tablespace 用户创建表空间权限
-- unlimited teblespace 用户无限表空间使用权限
grant create session,create table to user_name;
```

- 查看Oracle提供的系统权限

```sql
select name from sys.system_privilege_map
```

- 查看一个用户的所有系统权限(包含角色的系统权限)

```sql
select privilege from dba_sys_privs where grantee='SCOTT'
union
select privilege from dba_sys_privs where grantee in (
	select granted_role from dba_role_privs where grantee = 'SCOTT'
);
```

- 查看当前用户可以访问的所有数据字典的视图

```sql
select * from dict where comments like '%grant%';
```

- 查看当前数据库全称

```sql
select * from global_name;
```



##### 日志相关


在Oracle数据库中，与日志（Log）相关的操作主要涉及到归档日志（Archive Logs）和重做日志（Redo Logs）。以下是一些与这些日志相关的常用操作：

归档日志操作：

1. 启用归档模式：

   ```sql
   ALTER DATABASE ARCHIVELOG;
   ```

2. 禁用归档模式：

   ```sql
   ALTER DATABASE NOARCHIVELOG;
   ```

3. 手动切换日志：

   ```sql
   ALTER SYSTEM ARCHIVE LOG CURRENT;
   ```

4. 手动归档日志文件：

   ```sql
   ALTER SYSTEM ARCHIVE LOG <log_sequence_number>;
   ```

5. 列出所有归档日志文件：

   ```sql
   SELECT * FROM V$ARCHIVED_LOG;
   ```

6. 删除过期的归档日志文件：

   ```sql
   DELETE EXPIRED ARCHIVELOG ALL;
   ```

重做日志操作：

1. 添加新的重做日志组：

   ```sql
   ALTER DATABASE ADD LOGFILE GROUP <group_number> ('path_to_logfile') SIZE <size>;
   ```

2. 切换到下一个重做日志组：

   ```sql
   ALTER SYSTEM SWITCH LOGFILE;
   ```

3. 强制切换到下一个重做日志组：

   ```sql
   ALTER SYSTEM SWITCH LOGFILE FORCE;
   ```

4. 强制归档当前重做日志组：

   ```sql
   ALTER SYSTEM ARCHIVE LOG CURRENT;
   ```

5. 查看当前活动的重做日志组：

   ```sql
   SELECT * FROM V$LOG;
   ```

6. 查看重做日志的内容：

   ```sql
   SELECT * FROM V$LOG_HISTORY WHERE <conditions>;
   ```

查询重做日志信息：

1. 查看当前活动的重做日志组：

   ```sql
   SELECT * FROM V$LOG;
   ```

2. 查看数据库的重做日志状态：

   ```sql
   SELECT * FROM V$LOGFILE;
   ```

3. 查看数据库的重做日志组及其文件信息：

   ```sql
   SELECT GROUP#, THREAD#, MEMBER FROM V$LOGFILE;
   ```

4. 查看重做日志的内容和顺序号：

   ```sql
   SELECT SEQUENCE#, FIRST_CHANGE#, NEXT_CHANGE# FROM V$LOG_HISTORY WHERE <conditions>;
   ```

5. 查看重做日志切换的历史：

   ```sql
   SELECT * FROM V$LOG_HISTORY WHERE <conditions>;
   ```

6. 查看某个时间段内的重做日志信息：

   ```sql
   SELECT * FROM V$ARCHIVED_LOG WHERE FIRST_TIME BETWEEN TO_DATE('start_date', 'yyyy-mm-dd hh24:mi:ss') AND TO_DATE('end_date', 'yyyy-mm-dd hh24:mi:ss');
   ```

7. 查看当前会话正在使用的重做日志信息：

   ```sql
   SELECT * FROM V$SESSION WHERE <conditions>;
   ```

8. 查看归档日志文件的信息：

   ```sql
   SELECT * FROM V$ARCHIVED_LOG;
   ```




##### RMAN相关

Oracle RMAN（Recovery Manager）是一个用于数据库备份和恢复的工具，具有丰富的命令集。以下是一些常用的RMAN命令，用于备份、恢复、检查和管理Oracle数据库：

备份操作：

1. 备份整个数据库：

   ```
   BACKUP DATABASE;
   ```

2. 备份特定表空间

   ```
   BACKUP TABLESPACE <tablespace_name>;
   ```

3. 备份特定数据文件

   ```
   BACKUP DATAFILE <file_number>;
   ```

4. 备份指定时间点之前的数据：

   ```
   BACKUP DATABASE UNTIL TIME 'YYYY-MM-DD:HH24:MI:SS';
   ```

恢复操作：

1. 恢复整个数据库：

   ```
   RECOVER DATABASE;
   ```

2. 恢复特定表空间**：**

   ```
   RECOVER TABLESPACE <tablespace_name>;
   ```

3. 应用指定日志序列号之前的归档日志：

   ```
   RECOVER DATABASE UNTIL SEQUENCE <sequence_number>;
   
   -- 查询恢复的归档日志号
   select * from v$log;
   -- 根据归档日志号恢复
   RUN {
     SET UNTIL SEQUENCE '07-AUG-23';
     RESTORE DATABASE;
     RECOVER DATABASE;
   }
   ```

4. 打开数据库并重做日志应用**：**

   ```
   ALTER DATABASE OPEN RESETLOGS;
   
   ALTER DATABASE OPEN NORESETLOGS;
   ```

备份和恢复控制文件：

1. 备份控制文件**：**

   ```
   BACKUP CURRENT CONTROLFILE;
   ```

2. 恢复控制文件**：**

   ```
   RESTORE CONTROLFILE FROM 'backup_location';
   ```

其他操作**：**

1. 列出数据库备份**：**

   ```
   LIST BACKUP;
   ```

2. 列出数据库的日志序列号和时间信息**：**

   ```
   LIST ARCHIVELOG ALL;
   ```

3. 删除过期备份**：**

   ```
   DELETE EXPIRED BACKUP;
   ```

4. 删除过期归档日志**：**

   ```
   DELETE EXPIRED ARCHIVELOG ALL;
   ```



##### 其他设置

- 查看表字段

```sql
#desc ${table_name}
```

- 命令行相关设置

```sql
-- 显示一行多少字符
show line
-- 设置一行多少字符
set linesize 1000
-- 设置是否显示报表标题
set hea on
-- 显示每页行数
show pages
-- 设置每页显示行数
set pages 50
-- 设置输出结果是否滚动
set pause on/off
-- 设置滚动时自定义的提示
set pause 'Press <Enter> to continue'

```



### 4. MySQL Explain详解(SQL调优)

#### Explain介绍

- 在select语句之前增加explain关键字，执行后MySQl就会返回执行计划的信息，而不是执行SQL。但是如果from中包含子查询，MySQL仍然会执行该子查询，并把子查询结果放入临时表中。

#### Explain详解

**1)** id列

​	id列的编号就是select的序列号，有几个select就有几个id，并且id是按照select出现的顺序增长的，id列的值越大优先级越高。id相同则是按照执行计划列从上往下执行，id为空则是最后执行

**2)** select_type列

​	表示对应行是简单查询还是复杂查询

- simple：不包含子查询和union的简单查询

![img](https://image.kevinkda.cn/md/2f768fa6e05f4d89ab95c3b27a2886d5.png)

- primary：复杂查询中最外层的select
- subquery：包含在select中的子查询，但是不在from的子句中

![img](https://image.kevinkda.cn/md/b14940b3b7cb49a796eeaad688d9fc88.png)

- derived：包含在from子句中的子查询，MySQL会将结果放入一个临时表中，此表也叫衍生表

![img](https://image.kevinkda.cn/md/a57be66c15684664add5f17aba02bbca.png)

- union：在union中的第二个和最后的select，UNION RESULT为合并的结果

![img](https://image.kevinkda.cn/md/78a6f4afee1346fb9176afcd684acd73.png)

**3)** table列

​	表示当前访问的是那张表。当from中有子查询时，table列的格式为`<derivedN>`，表示当前查询依赖id=N行的查询，所以首先执行id=N行的查询，如果上面select_type如上图union所示，当有union查询时，UNION RESULT的table列的值为`<union 1,2>`，1和2表示参与union的行id

**4)** partitions列

​	查询将匹配记录的区分。对于非分区表，该值为NULL。

**5)** type列

​	此列表示关联类型或访问类型。也就是MySQL决定如何查找表中的行。从优到差依次为：system > const > eq_ref > ref > range > index > all。

​	**NULL**：MySQL能在优化阶段分解查询语句，在执行阶段不用再去访问表或者索引。

![img](https://image.kevinkda.cn/md/b750ef4009b34fd6b4fb7f3b52243532.png)

​	**system、const**：MySQL对查询的某部分进行右滑并把其转化成一个常量（可以通过show warnings命令查看结果）。system是const的一个特例，表示表里只有一条元组匹配时为system。

![img](https://image.kevinkda.cn/md/f2f32d2468ae435d9d19c26284647c5d.png)

![img](https://image.kevinkda.cn/md/c85c851b0f50429b88cb60fd523afa77.png)

​	**eq_ref**：主键或唯一键索引被连接使用，最多只会返回一条符合条件的记录。简单的select查询不会出现这种type。

![img](https://image.kevinkda.cn/md/b9a94d9490df4a5ea55aaba5a8435d04.png)

​	**range**：通常出现在范围查询中，比如in、between、大于、小于等。使用索引来检索给定范围的行。

![img](https://image.kevinkda.cn/md/573979004689414d945f60538ccfbb62.png)

​	**index**：扫描全表索引拿到结果，一般是扫描某个二级索引，二级索引一般比较少，所以通常比ALL快。

![img](https://image.kevinkda.cn/md/9c220a48cb3e4a3f86bf9f1e1bbc0ba9.png)

​	**all**：全表扫描，扫描聚簇索引的所有叶子节点。

**6)** possible_keys列

​	此列显示在查询中可能用到的索引。如果该列为NULL，则表示没有相关索引，可以通过检查where子句看是否可以添加一个适当的索引来提高性能。

**7)** key列

​	此列显示MySQL在查询时实际用到的索引。在执行计划中可能出现possible_keys列有值，而key列为null，这种情况可能是表中数据不多，MySQL则认为索引对当前查询帮助不大而选择了全表查询。如果想要强制MySQL使用或忽视possible_keys列中的索引，在查询时可使用force index，ignore index。

**8)** key_len列

​	此列显示MySQL在索引里使用的字节数，通过此列可以算出具体使用了索引中的那些列。索引最大长度为768字节，当长度过大时，MySQL会做一个类似最左前缀处理，将前半部部分字符提取出做索引。当字段可以为null时，还需要一个字节去记录。

key_len计算规则：

1. 字符串：

   char(n)：n个数字或者字母占n个字节，汉字占3n个字节

   varchar(n)：n个数字或者字母占n个字节，汉字占3n+2个字节，+2字节用来存储字符串长度。

2. 数字类型：

   tinyyint：1字节

   smallint：2字节

   int：4字节

   bigint：8字节

3. 时间类型：

   date：3字节

   timestamp：4字节

   datetime：8字节

**9)** ref列

​	此列显示key列记录的索引中，表查找值时使用到的列或常量。常见的有const、字段名

**10)** rows列

​	此列是MySQL在查询中估计要读取的行数。不是结果集的行数。

**11)** Extra列

​	此列是一些额外信息。常见的重要值如下：

1.	Using index：使用覆盖索引（如果select后面查询的字段都可以从这个索引的树中获取，不需要通过辅助索引树找到主键，再通过主键去主键索引树里获取其他字段值，这种情况一般可以说是用到了覆盖索引）
2.	Using where：使用where语句来处理结果，并且查询的列未被索引覆盖。
3.	Using index condition：查询的列不完全被索引覆盖，where条件中是一个范围查询。
4.	Using temporary：MySQL需要创建一张临时表来处理查询。出现这种情况一般是要进行优化的。
5.	Using filesort：将使用外部排序而不是索引排序，数据较小时从内存排序，否则需要在磁盘完成排序。
6.	Select tables optimized away：使用某些聚合函数（max、min等）来访问存在索引的某个字段时。



### 5. 10个高级SQL写法

![image-20230320173713241](https://image.kevinkda.cn/md/image-20230321195750672.png)

#### ORDER BY FIELD() - 自定义排序逻辑

​	MySQL中的排序ORDER BY 除了可以用 ASC 和 DESC，还可以用 **ORDER BY FIELD(str,str1,…)** 来自定义字符串/数字来实现排序。

```sql
select * 
from order_diy 
order by field(title,'九阴真经', 
'降龙十八掌','九阴白骨爪','双手互博','桃花岛主',
'全真内功心法','蛤蟆功','销魂掌','灵白山少主')
```

​	如上，设置的自定义排序字段为 title，然后将自定义排序结果跟在title之后

#### CASE 表达式

​	**[ case when then else end ]** 表达式功能非常强大，可以帮助我们解决 **if else if** 这类问题。例如，在order_diy 表中加一列 level ，根据 money 判断大于 60 是高级，大于 30 是中级，其余为低级

```sql
select *,
case when money > 60 then ‘高级’
when money > 30 then '中级'
else '低级' end level
from order_diy
```

#### EXISTS 用法

​	exists 后面跟着的是一个子查询语句，他的作用是根据著查询的数据，每一行都放到子查询中做条件验证，根据验证结果(true or flase)，true的话这一行就会保留。

![image-20230320175651600](https://image.kevinkda.cn/md/image-20230320173713241.png)

​	例如，想要找到 emp 表中 dept_name 与 dept 表中 dept_name 对应不上的员工数据，也就是 emp 表中第二行记录

```sql
select *
from emp e
where exists (
	select *
    from dept p
    where p.dept_id = e.dept_id
    and p.dept_name != e.dept_name
);
```

​	通过 exists 语法将外层 emp 表全部数据放到子查询中一一与 dept 表中得全部数据进行比较，只要有一行记录返回true，主查询与子查询交互过程如下所示

![image-20230321195750672](https://image.kevinkda.cn/md/image-20230320175651600.png)

- 第一条记录与子查询比较时，全部返回false。所以第一行不展示。
- 第二行记录与子查询比较时，发现 `销售部们` 与 dept 表中第二行 `销售部` 对应不上，返回true，所以这条主查询得记录会返回。
- 后面得记录同样执行以上得步骤

#### GROUP_CONCAT(expr) - 组连接函数

​	组连接函数可以返回分组后指定字段得字符串连接形式，并且可以指定排序逻辑，以及连接字符串，默认为英文逗号连接。

```mysql
select name,group_conncat(title order by id desc separator '-')
from order_diy
group by name
order by null;
```

​	查询结果：

![image-20230324144611148](https://image.kevinkda.cn/md/image-20230324144611148.png)

​	通过 `group_conncat(title order by id desc separator '-')` 语句，指定分组链接title字段，并且按照 id 排序，设置连接字符串为 `-`

#### 自连接查询

​	自连接查询是比较常用的查询，可以轻松解决很多问题。这里具体的表结构和数据如下。

![image-20230403104806400](https://image.kevinkda.cn/md/image-20230403105701095.png)

​	tree 表中通过 pid 和 id 进行父子级关联。如果现在需要按照父子级层级将 tree 表数据转换成 `一级职位 二级职位 三级职位` 三个列名进行展示，sql如下：

```sql
select t1.job_name '一级职位',
	   t2.job_name '二级职位',
	   t3.job_name '二级职位'
from tree t1 join tree t2 on t1.id = t2.pid
     left join tree t3 on t2.id = t3.pid
where t1.pid = 0;
```

![image-20230403105701095](https://image.kevinkda.cn/md/image-20230403143617384.png)

​	通过 `tree t1 join tree t2 on t1.id = t2.pid` 自连接 展示 `一级职位 二级职位`，再用 `left join tree t3 on t2.id = t3.pid` 自连接展示 `二级职位 三级职位`，最后通过 `where t1.pid = 0` 过滤非一级职位的展示。

#### 更新 emp 表和 dept 表关联数据

​	数据继续使用上面的 emp 表和 dept 表

![image-20230403114927979](https://image.kevinkda.cn/md/image-20230403114927979.png)

​		从表数据中可以看到 emp 表中的 jack 的部门名称和 dept 表中的部门名称不相符，现有需求需要将 jack 的部门名称更新成 dept  表中正确的名称，sql如下。

```sql
update emp, dept set emp.dept_name = dept.dept_name where emp.dept_id = dept.id;
```

![image-20230403142157376](https://image.kevinkda.cn/md/image-20230403160059275.png)

​	sql中直接关联 emp 表和 dept 表并设置关联条件，然后更新 emp 表的 dept_name 为 dept 表中的 dept_name。

#### ORDER BY - 空值 NULL 排序

​	order by 子句中可以跟要排序的字段名称，但是当字段中存在 null 值得时候，会对排序结果造成影响。我们可以通过 `order by if(isnull(title), 1, 0)` 语法将 null 值转换成0或者1，来达到将null值放到最前面还是最后面进行排序的效果。这里继续用 order_diy 表举例，sql 如下：

```sql
select * from order_diy order by if(isnull(title), 1, 0), money
```

![image-20230403143617384](https://image.kevinkda.cn/md/image-20230403104806400.png)

#### with rollup - 分组统计数据的基础上再进行统计汇总

​	MySQL 中使用 with rollup 再分组统计数据的基础上再进行统计汇总，即用来得到 group by 的汇总信息，这里数据继续使用 order_diy 表举例，sql如下

![image-20230403161717626](https://image.kevinkda.cn/md/image-20230403142157376.png)

```mysql
select name, sum(money) as money
from order_diy group by name with rollup;
```

![image-20230403160059275](https://image.kevinkda.cn/md/image-20230403161717626.png)

​	通过 `group by name with rollup` 语句，查询结果最后一列显示了分组统计的汇总结果。但是 name 字段汇总后显示为 null，我们可以通过 `coalesce(value…)` 比较函数，返回第一个非空参数。

```mysql
select coalesce(name, '总金额') name, sum(money) as money
from order_diy group by name with rollup;
```

![image-20230403160250104](https://image.kevinkda.cn/md/image-20230403160250104.png)

#### with as - 提取临时表别名

​	with as 语法需要 MySQL 8.0+ 以上的版本，其作用主要是提取子查询，方便后续共用，更多的使用在数据分析的场景上。

​	如果一整个查询语句中，多个子查询都需要使用同一个子查询的结果，那么就可以用 with as，将共用的子查询语句提取出来，加上别名。后续的查询语句可以直接使用，对于大量复杂的sql起到了优化作用。这里继续使用 order_diy 表进行举例，sql如下。

![image-20230403161709749](https://image.kevinkda.cn/md/image-20230403161709749.png)

```mysql
with t1 as (select * from order_diy where money > 30)
     t2 as (select * from order_diy where money > 60)
select * from t1
where t1.id not in (select id from t2) and t1.name = '周伯通';
```

![image-20230403161835692](https://image.kevinkda.cn/md/image-20230403161835692.png)

​	这个sql查询的是 order_diy 表中 money 大于 30 但是小于 60 之间并且 name 是周伯通的数据。

#### 存在就更新，不存在就插入

MySQL 中通过 `on duplicate key update` 语法来是实现存在就更新，不存在就插入的逻辑。插入或者更新时，他会根据**表中主键索引或者唯一索引进行判断**，**如果主键索引或者唯一索引有冲突**，就会执行 `on duplicate key update` 后面的复制语句。这里通过 news 表距离，结构和数据如下，news_code 字段有唯一索引：

![image-20230403164809819](https://image.kevinkda.cn/md/image-20230403164809819.png)

```mysql
-- 第一次执行添加语句
insert into `news` ('news_title', 'news_auth', 'news_code')
values ('新闻3', '小花', 'wx-003')
on duplicate update news_title = '新闻3'
-- 第二次执行修改语句
insert into `news` ('news_title', 'news_auth', 'news_code')
values ('新闻4', '小花', 'wx-003')
on duplicate update news_title = '新闻4'
```

![image-20230403170326150](https://image.kevinkda.cn/md/image-20230403170326150.png)



### 6. 修改ORACLE单个用户密码过期策略

#### 相关链接

[修改ORACLE密码过期策略](https://blog.csdn.net/weixin_42609714/article/details/124457520)

#### 方案

```sql
-- ################ 修改单个用户密码过期策略
-- 查看profile
select profile,resource_name,limit from dba_profiles;
select * from dba_profiles where profile='PASSWORD_UNLIMIT_PROFILE';
-- 查看用户所属profile
select username,profile from dba_users;
-- 创建profile
CREATE PROFILE "PASSWORD_UNLIMIT_PROFILE" LIMIT
 COMPOSITE_LIMIT UNLIMITED
 SESSIONS_PER_USER UNLIMITED
 CPU_PER_SESSION UNLIMITED
 CPU_PER_CALL UNLIMITED
 LOGICAL_READS_PER_SESSION UNLIMITED
 LOGICAL_READS_PER_CALL UNLIMITED
 IDLE_TIME UNLIMITED
 CONNECT_TIME UNLIMITED
 PRIVATE_SGA UNLIMITED
 FAILED_LOGIN_ATTEMPTS 10
 PASSWORD_LIFE_TIME	180
 PASSWORD_REUSE_TIME UNLIMITED
 PASSWORD_REUSE_MAX	UNLIMITED
 PASSWORD_VERIFY_FUNCTION NULL
 PASSWORD_LOCK_TIME 1
 PASSWORD_GRACE_TIME 7
 INACTIVE_ACCOUNT_TIME UNLIMITED;
-- 修改profile密码过期时间
ALTER profile PASSWORD_UNLIMIT_PROFILE limit PASSWORD_LIFE_TIME UNLIMITED;
-- 修改用户所属profile
ALTER user SVC_CONFLUENCE profile PASSWORD_UNLIMIT_PROFILE;
```



### 7. MySQL免安装版初始化

#### 相关链接

[MySQL免安装版配置](https://juejin.cn/post/6854573215290359821)

[MySQL8.0.33免安装版下载地址](https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.33-winx64.zip)

#### 安装流程

##### 安装目录下新建my.ini文件

- 安装目录为`mysql`文件夹的顶级目录，安装目录下不要新建`data`文件夹，后续的服务配置会生成
- 安装目录下新建`my.ini`文件，写入以下内容（记得修改其中的路径）

```ini
[client]
# 设置mysql客户端默认字符集
default-character-set=utf8
 
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=D:\my_tool\mysql-8.0.21-winx64\mysql-8.0.21-winx64
# 设置 mysql数据库的数据的存放目录
datadir=D:\my_tool\mysql-8.0.21-winx64\mysql-8.0.21-winx64\data
# 允许最大连接数
max_connections=20
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```

##### 配置环境变量

- 配置环境变量 `path` ，将安装目录下的 `bin` 目录配置到 `path` 中。
- 即，例如 `mysql` 安装目录为 `D:\mysql` ，那么则配置成 `D:\mysql\bin`

##### 启动CMD

- 进入mysql安装目录下的bin目录

```powershell
cd D:\mysql\bin
```

- 将MySQL加入到Windows的服务中

```shell
mysqld --install
```

- 初始化数据库(初始化成功后会创建data文件夹、最后一行是生成的初始用户名和密码)

```shell
mysqld --initialize --user=root --console
```

- 启动mysql服务

```shell
net start mysql
```

- 进入MySQL修改初始密码



### 8. MySQL开启慢日志

开启慢查询日志，可以让MySQL记录下查询超过指定时间的语句，通过定位分析性能的瓶颈，才能更好的优化数据库系统的性能。

#### 参数

slow_query_log 慢查询开启状态
slow_query_log_file 慢查询日志存放的位置（这个目录需要MySQL的运行帐号的可写权限，一般设置为MySQL的数据存放目录）
long_query_time 查询超过多少秒才记录

#### 步骤

**查看慢查询相关参数**

```mysql
mysql> show variables like 'slow_query%';
+---------------------------+----------------------------------+
| Variable_name             | Value                            |
+---------------------------+----------------------------------+
| slow_query_log            | OFF                              |
| slow_query_log_file       | /mysql/data/localhost-slow.log   |
+---------------------------+----------------------------------+

mysql> show variables like 'long_query_time';
+-----------------+-----------+
| Variable_name   | Value     |
+-----------------+-----------+
| long_query_time | 10.000000 |
+-----------------+-----------+
```

**设置参数**

方法一：全局变量设置
将 slow_query_log 全局变量设置为“ON”状态

```
mysql> set global slow_query_log='ON'; 
```

设置慢查询日志存放的位置

```
mysql> set global slow_query_log_file='/usr/local/mysql/data/slow.log';
```

查询超过1秒就记录

```
mysql> set global long_query_time=1;
```

方法二：配置文件设置
修改配置文件my.cnf，在[mysqld]下的下方加入

```
[mysqld]
slow_query_log = ON
slow_query_log_file = /usr/local/mysql/data/slow.log
long_query_time = 1
```

3.重启MySQL服务

```
service mysqld restart
```

4.查看设置后的参数

```
mysql> show variables like 'slow_query%';
+---------------------+--------------------------------+
| Variable_name       | Value                          |
+---------------------+--------------------------------+
| slow_query_log      | ON                             |
| slow_query_log_file | /usr/local/mysql/data/slow.log |
+---------------------+--------------------------------+

mysql> show variables like 'long_query_time';
+-----------------+----------+
| Variable_name   | Value    |
+-----------------+----------+
| long_query_time | 1.000000 |
+-----------------+----------+
```



### 9. Elasticsearch操作

#### 新增

- 新增索引

```elm
PUT /system_log
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "Type": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "Time": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "User": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "Event": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  }
}
```



### 10. 记录一次服务器宕机后恢复Oracle的操作

#### 经过

- 某一日9点，发现微信没有收到某个服务器的定时任务的执行的信息，然后打开各种服务的网页发现打开都很慢并且无法登录，经过排查以后发现是NAS宕机，导致服务器所有的服务的数据文件丢失。恢复并重启NAS以后，启动数据库服务时发现Oracle无法正常启动，报错redo02.log中有错误，有写入丢失，无法启动

#### 恢复

- 查看oracle的alert日志

```shell
tail -200 $ORACLE_BASE/diag/rdbms/orcl01/ORCL01/trace/alert_ORCL01.log
```

- 进入数据库查看重做日志

```sql
-- 发现数据都在mounted状态，如果不在这个状态，建议调整到这个状态
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       MOUNTED
         3 DEMO                           MOUNTED
         4 DEV                            MOUNTED
         5 SVCRES                         MOUNTED
SQL> set lines 300 pages 300
SQL> col member for a40
-- 通过`select * from v$logfile` 查看了重做日志
SQL> select * from v$logfile;

    GROUP# STATUS  TYPE    MEMBER                                   IS_     CON_ID
---------- ------- ------- ---------------------------------------- --- ----------
         3         ONLINE  /opt/oracle/oradata/ORCL01/redo03.log    NO           0
         2         ONLINE  /opt/oracle/oradata/ORCL01/redo02.log    NO           0
         1         ONLINE  /opt/oracle/oradata/ORCL01/redo01.log    NO           0
-- 通过`select * from v$log` 查看了重做日志的详细信息，包括了后续恢复到出错前要用到的归档日志序列号`SEQUENCE#`，或者恢复时间点`FIRST_TIM`
SQL> select * from v$log;

    GROUP#    THREAD#  SEQUENCE#      BYTES  BLOCKSIZE    MEMBERS ARC STATUS           FIRST_CHANGE# FIRST_TIM NEXT_CHANGE# NEXT_TIME     CON_ID
---------- ---------- ---------- ---------- ---------- ---------- --- ---------------- ------------- --------- ------------ --------- ----------
         1          1        367  209715200        512          1 NO  INACTIVE              58854455 07-AUG-23     59036643 07-AUG-23          0
         3          1        366  209715200        512          1 NO  INACTIVE              58673242 06-AUG-23     58854455 07-AUG-23          0
         2          1        368  209715200        512          1 NO  CURRENT               59036643 07-AUG-23   1.8447E+19                    0
-- 然后通过转换查看这些重做日志的具体时间
SQL> select SEQUENCE#,to_char(first_time,'yyyy-mm-dd hh24:mi:ss') from v$log;
 SEQUENCE# TO_CHAR(FIRST_TIME,
---------- -------------------
       367 2023-08-07 01:00:53
       366 2023-08-06 21:10:26
       368 2023-08-07 05:00:34
```

- 使用RMAN工具进行恢复

```shell
# 进入rman工具
rman target /

# 使用以下两种方式进行恢复
RUN
{
  SET UNTIL TIME '${FIRST_TIM}';
  RESTORE DATABASE;
  RECOVER DATABASE;
}

RUN
{
  SET UNTIL SEQUENCE '${SEQUENCE#}';  -- 替换 n 为目标序列号
  RESTORE DATABASE;
  RECOVER DATABASE;
}

# 成功以后，可能需要应用额外的归档日志文件或者重做日志文件。使用以下命令来完成此步骤：
RECOVER DATABASE USING BACKUP CONTROLFILE UNTIL CANCEL;

# 最后，尝试打开数据库
# 以下命令，如果你已经执行了数据库恢复操作，并希望从这个点开始一个全新的日志序列，你可以使用 RESETLOGS 选项来打开数据库。这将创建一个新的日志序列，并且旧的归档日志将被标记为无效。
ALTER DATABASE OPEN RESETLOGS;
# 以下命令，如果你希望保留之前的日志序列，并希望继续使用这些日志进行数据库操作，你可以使用 NORESETLOGS 选项来打开数据库。这样可以保留之前的归档日志序列，但在某些情况下可能会导致数据不一致。
ALTER DATABASE OPEN NORESETLOGS;
```



### 11. MySQL主从同步

#### 参考信息

[MySQL主从同步以及常见问题](https://www.cnblogs.com/cfas/p/16733598.html#autoid-4-0-0)

#### 环境信息

- 主库：10.21.0.1，sync/123456
- 从库：10.21.0.2

#### 配置信息

```cnf
# 修改主从库的my.cnf文件
# 主库从库的server-id需要为不同的id
server-id=1
binlog_format=ROW
log_bin_trust_function_creators=ON
log_bin=/var/log/mysql-bin
log_error=/var/log/mysql-error.log

# 如果需要设置只同步某些数据库可以在从库的my.cnf中加上此配置
replicate_wild_do_table = 要同步的数据库名.%
replicate_wild_ignore_table = 要忽略的数据库名.%
```

#### 用户准备

```sql
mysql> CREATE USER sync IDENTIFIED BY '123456';
mysql> GRANT SELECT, SHOW VIEW, REPLICATION SLAVE, REPLICATION CLIENT ON . TO 'sync'@'%';
mysql> FLUSH PRIVILEGES;
```

#### 数据拉平

使用此方式进行数据导入时，保证目标数据库中数据表与源数据库中数据表一致，同时，目标数据库中数据表保证为空表

```shell
mysqldump --default-character-set=utf8mb4 --host=192.168.91.131 -uroot -p123456 --opt --set-gtid-purged=OFF 从库需要导入数据的数据库名 | mysql --host=从库IP地址 --port=3306 -uroot -p123456 --default-character-set=utf8mb4 -C 从库需要导入数据的数据库名
```

#### 主库设置

```sql
-- 获取主库的binlog文件和当前位置，即查询结果的 File、Position 字段，例如：File字段值为 binlog.XXXXXXXX，Position 字段值为 YYYYYYYY
show master status\G;
-- 刷新log日志，自此刻开始产生一个新编号的binlog日志文件
flush logs;
```

#### 从库设置

```sql
-- 设置同步的信息
CHANGE MASTER TO MASTER_HOST = '10.21.0.1', MASTER_USER = 'sync',MASTER_PASSWORD = '123456', MASTER_PORT = 3306, MASTER_LOG_FILE='binlog.000014',MASTER_LOG_POS=178;
-- 开启同步
start slave;
-- 查看同步情况
show slave status\G;
-- 停止同步
stop slave;
```



 

## 三、Linux

[VMwear安装Centos7](https://www.jianshu.com/p/ce08cdbc4ddb?utm_source=tuicool&utm_medium=referral)

### 1、Linux或Git查看二进制文件

1、vim -b (需要修改的二进制文件名称)

2、`:%!xxd`

3、输入vim的修改指令，然后修改编辑二进制文件

4、编辑完后按ESC键回到指令模式

5、`:%!xxd -r`

6、输入vim的保存指令



### 2、Linux根据日期删除文件

#### find命令参数说明

```shell
# 最后一次访问发生在 n分钟 之内
-amin -n
# 最后一次访问发生在距离当前时间 n分钟 至 (n+1)分钟
-amin n
# 最后一次访问发生在 (n+1)分钟 之外
-amin +n
# 最后一次访问发生在 n天 之内
-atime -n
# 最后一次访问发生在 n天 至 (n+1)天
-atime n
# 最后一次访问发生在 (n+1)天 之外
-atime +n
# 最后一次文件状态修改发生在 n分钟 之内
-cmin -n
# 最后一次文件状态修改发生在 n分钟 至 (n+1)分钟
-cmin n
# 最后一次文件状态修改发生在 (n+1)分钟 之外
-cmin +n
# 最后一次文件状态修改发生在 n天 之内
-ctime -n
# 最后一次文件状态修改发生在 n天 至 (n+1) 天
-ctime n
# 最后一次文件状态修改发生在 (n+1)天 之外
-ctime +n
# 最后一次文件内容修改发生在 n分钟 之内
-mmin -n
# 最后一次文件内容修改发生在 n分钟 至 (n+1)分钟
-mmin n
# 最后一次文件内容修改发生在 (n+1)分钟 之外
-mmin +n
# 最后一次文件内容修改发生在 n天 之内
-mtime -n
# 最后一次文件内容修改发生在 n天 至 (n+1)天
-mtime n
# 最后一次文件内容修改发生在 (n+1)天 之外
-mtime +n
```

**例子**

```shell
# 找到两天以外的文件
find /home/xxx/pyscripts/AutoCreate/rg_task/files/ -name "*" -mtime +2 
```

```shell
# 找到两天以外的文件并删除 利用 -exec参数，如果查找有返回，可在exec参数后加上需要操作的命令，查找结果用{}来代替
find /home/xxx/pyscripts/AutoCreate/rg_task/files/ -name "*" -mtime +2 -exec rm -rfv {} \;
```



### 3、Systemctl 常用命令

查看全部服务命令：

```sh
systemctl list-unit-files --type service
```

查看服务：

```sh
systemctl status name.service
```

增加开机启动：

```sh
systemctl enable name.service
```

启动服务：

```sh
systemctl start name.service
```

停止服务：

```sh
systemctl stop name.service
```

重启服务：

```sh
systemctl restart name.service
```

删除开机启动：

```sh
systemctl disable name.service
```



### 4、Tomcat

- 日志类
  - `nohup ./startup.sh`  用nohup启动tomcat
  - `./catalina.sh run` tomat启动后显示控制台

#### 如何访问Tomcat页面上得manager app

- 首先进入系统中tomcat所在文件夹下的`conf`中

- 编辑`tomcat-users.xml`

- 输入以下内容，编辑好后保存退出

  ```xml
   <role rolename="manager-gui"/>
   <user username="admin" password="Hyq0901." roles="manager-gui"/>
  
    <role rolename="tomcat"/>
    <user username="tomcat" password="Hyq0901." roles="tomcat"/>
  
    <role rolename="manager-script"/>
    <user username="script" password="Hyq0901." roles="manager-script"/>
  
    <role rolename="manager-jmx"/>
    <user username="jmx" password="Hyq0901." roles="manager-jmx"/>
  
    <role rolename="manager-status"/>
    <user username="status" password="Hyq0901." roles="manager-status"/>
  
    <role rolename="admin-gui"/>
    <user username="adminGui" password="Hyq0901." roles="admin-gui"/>
  ```

- 再进入`webapps/manager/META-INF/`下编辑文件`context.xml`，将以下内容注释

  ```xml
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
           allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
  ```

- 重启tomcat

#### 修改Tomcat项目访问路径名

- 进入tomcat所在文件夹下得conf文件夹中

- 修改`server.xml`文件，再文件底部输入以下内容

  ```XML
  <Context path="/store" docBase="store-0.0.1/" reloadble="true"/>
  ```

  - `path`代表用浏览器访问的时候的的路径，如http://localhost:8080/web来访问path=”/web”
  - `docBase`为你的项目的路径，这里同样既可以用相对路径，也可以用绝对路径。设置好了之后就会把项目自动映射到ROOT
  - `reloadable`，如果这个属性设为true，tomcat服务器在运行状态下会监视在WEB-INF/classes和WEB-INF/lib目录下class文件的改动，如果监测到有class文件被更新的，服务器会自动重新加载Web应用

- 保存退出并重启tomcat




### 5、Docker 设置elasticsearch密码

| 序号 | 账号                   | 密码     |
| ---- | ---------------------- | -------- |
| 1    | elastic                | Hyq0901. |
| 2    | apm_system             |          |
| 3    | kibana_system          |          |
| 4    | logstash_system        |          |
| 5    | beats_system           |          |
| 6    | remote_monitoring_user |          |

- 在 `elasticsearch.yml` 中添加一下代码

```yaml
xpack.security.enabled: true
xpack.license.self_generated.type: basic
xpack.security.transport.ssl.enabled: true
```

- 在进入docker中的elasticsearch下的bin目录

```shell
docker exec -it elasticsearch /bin/bash
cd bin
```

- 输入以下内容

```shell
elasticsearch-setup-passwords interactive
```



### 6、设置命令全局的别名

#### 全局(所有用户所有终端)

```shell
# 打开系统文件
vim /etc/bashrc
# 将光标移动到文件最后一行后面，按下小o
# 粘贴或输入赋予别名的命令 
# alias [别名]='原命令'
alias grep='grep --color=auto'
# 保存文件并退出
# 重载文件
source /etc/bashrc
```

#### 局部(针对某个用户)

```shell
# 打开系统文件
vim ~/.bashrc
# 将光标移动到文件最后一行后面，按下小o
# 粘贴或输入赋予别名的命令 
# alias [别名]='原命令'
alias grep='grep --color=auto'
# 保存文件并退出
# 重载文件
source ~/.bashrc
```

#### 临时(当前终端当前用户)

```shell
# alias [别名]='原命令'
alias grep='grep --color=auto'
```



### 7、Linux设置类似$HOME的目录的快捷目录

- 第一步打开 `/etc/default/useradd` 这个文件
- 然后在最后一行写下 `名字=/目录`
- 按下ESC输入`:wq`保存并退出
- 最后输入 `source /etc/default/useradd` 或者 `source useradd`



### 8、Linux防火墙以及开放端口管理

```shell
# 查看防火墙是否开启
systemctl status firewalld
# 若没有开启则是开启状态,关闭则是 stop
systemctl start firewalld
# 查看所有开启的端口
firewall-cmd --list-ports

# 防火墙开启端口访问
# --zone 作用域 --add-port=80/tcp 添加端口 端口/通讯协议 --permanent  永久生效
firewall-cmd --zone=public --add-port=80/tcp --permanent
#关闭端口
firewall-cmd --zone=public --remove-port=5672/tcp --permanent

# 重启防火墙
firewall-cmd --reload
# 查看防火墙状态 是否是running
firewall-cmd --state
# 列出支持的zone
firewall-cmd --get-zones
# 列出支持的服务 服务是放行的
firewall-cmd --get-services
# 查看ftp服务是否支持，返回yes or no
firewall-cmd --query-service ftp
#永久移除ftp服务
firewall-cmd --remove-service=ftp --permanent
# 查看以开放的端口
firewall-cmd --zone=public --list-ports
# 查看监听端口
netstat -Inpt
# 检查端口被那个进程占用
netstat -Inpt |grep 5672
#查看进程的详细信息
ps 6832
# 终止进程
kill -9 6832
```



### 9、Iptables防火墙

#### Iptables防火墙介绍

- Linux系统内核集成了网络访问控制的功能，通过netfilter模块来实现，是内核的一部分（内核空间）
- 用户层（用户空间）可以通过iptables程序对netfilter进行控制管理，进而实现网络的访问控制
- TCP_Wrappers 也是一个网络访问控制的一个工具，作用在应用层（7层防火墙）

总结

- netfilter模块		内核空间，是内核一部分 
- iptables组件  用户空间，提供管理防火墙的手段，它主要作用在传输层（4层防火墙）

#### Iptables基本语法

- iptables [-t 表名] 命令选项 ［链名］ [规则号码] ［条件匹配］ ［-j 目标动作]

- 如果不指定表名，默认操作filter表

- 说明：
  表名和链名：用于指定 iptables命令所操作的表和链；
              命令选项：用于指定管理iptables规则的方式（比如：插入、增加、删除、查看等）；
  规则号吗：用于指定规则的编号；
  条件匹配：用于指定对符合什么样条件的数据包进行处理（比如：什么协议、出入网卡等）；
  目标动作：用于指定数据包的处理方式（比如：允许通过、拒绝、丢弃等）

- 示例

  ```shell
  iptables -L
  iptables -t filter -L
  iptables -t nat -L
  iptables -t raw -L
  iptables -t mangle -L
  ```

- 启停命令

  ```shell
  # 临时停止|启动|查看状态|重新加载|重新启动
  service iptables stop|start|status|reload|restart	
  # 开机是否自启动
  chkconfig iptables off|on
  # 永久保存规则
  vim	/etc/sysconfig/iptables
  ```

- 常用命令

  ```shell
  常见的命令选项：
  -L								查看
  -A								追加，放置最后一条
  -I								插入，默认插入成第一条
  -D								删除
  -F								清空flush
  -P     						    设置默认策略policy
  
  处理动作：
  filter表:
  -j ACCEPT				允许
  -j DROP					丢弃，没有任何提示信息
  -j REJECT				拒绝，有提示信息
  -j LOG					写日志     /var/log/messages    然后将数据包传递给下一条规则
  
  nat表:
  -j SNAT						源地址转换 POSTROUTING
  -j DNAT						目标地址转换 PREROUTING
  ```


#### Filter表

示例：

- 全部允许/拒绝/丢弃

```shell
# 添加规则，丢弃所有进来的数据包
iptables -t filter -A INPUT -j DROP
# 添加规则，允许所有进来的数据包
iptables -t filter -A INPUT -j ACCEPT

# 指定位置插入规则，允许所有进来的数据包第1条规则
iptables -t filter -I INPUT 1 -j ACCEPT
# 添加规则，丢弃所有出去的数据包
iptables -t filter -A OUTPUT -j DROP

# 指定位置插入规则，拒绝所有进来的数据包为第3条规则
iptables -t filter -I INPUT 3 -j REJECT	  
# 查看规则编号
iptables -t filter -L --line-numbers
# 覆盖已有规则
iptables -t filter -R INPUT 1 -j ACCEPT
# 删除INPUT链的第3条规则
iptables -t filter -D INPUT 3
# 清空filter表的所有规则
iptables -t filter -F
# 增加规则，先写日志，然后将数据包传递给下一条规则
iptables -A INPUT -j LOG
iptables -I INPUT 2 -j DROP
# 设置链上的默认规则
iptables -t filter -P INPUT DROP
iptables -D INPUT 1
```

- 根据源和目标地址匹配

```shell
# 匹配条件
# -s 192.168.1.1/24	源地址
# -d 192.168.1.2		目标地址
# -p tcp|upd|icmp		协议
# -i lo				input从lo接口进入得数据包
# -o eth0				output从eth0出去的数据包
# -p tcp --dport 80 	目标端口是80，需和-p tcp|upd|icmp连用
# -p udp --dport 53	目标端口是53，协议是udp
  
# 允许源地址为10.1.1.3进入
iptables -t filter -A INPUT -s 10.1.1.3 -j ACCEPT
# 不允许源地址为10.1.1.3进入
iptables -t filter -A INPUT ! -s 10.1.1.3 -j ACCEPT
# 拒绝源地址为10.1.1.3进入
iptables -t filter -A INPUT -s 10.1.1.3 -j DROP
# 丢弃到达目标地址为10.1.1.3的包
iptables -t filter -A OUTPUT -d 10.1.1.3 -j DROP
# 丢弃到达目标地址为10.1.1.3的包
iptables -t filter -A OUTPUT ! -d 10.1.1.3 -j ACCEPT
# 丢弃所有到目标地址10.1.1.2的包	
iptables -t filter -A INPUT -d 10.1.1.2 -j DROP
# 源地址为10.1.1.2出去的包全部允许
iptables -t filter -A OUTPUT -s 10.1.1.2 -j ACCEPT
```

  

### 10、Vim 的使用

![image-20220828030503848](https://image.kevinkda.cn/md/image-20220828030503848.png)

#### VIM 中的替换操作

##### 语法：

- `[range]s/目标字符串/替换字符串/[option]`
- s是substitute的简写，代表执行替换字符操作

###### [range]

- range 的值表示搜索范围，默认表示当前行
- range的值如果为`1,10`表示从第一行到第10行
- %表示整个文件,也可以写成`1,$`
- $表示从当前行到本文件末尾

###### [option]

表示操作类型，默认只对第一个匹配的字符串进行替换

- option字段值g(global)表示全局替换
- c(comfirm)表示操作时需要确认
- i(ignorecase)表示不区分大小写

##### 例子：

- `$s/Vim/vim/gc` 会出现提示`replace with foo(y/n/a/q/l/^E/^Y)?`，询问是否确认执行
  - 待选择操作的含义包括：
  - y:确认执行这个替换将将所有Vim替换成vim;
  - n:取消这个本交Vim替换命令的操作;
  - a:执行本次所有替换字符串操作且不再询问;
  - q:退出当前vim字符串替换操作而不做任何改动;
  - l:替换完当前匹配点后退出(last)
  - Ctrl + E:向上翻滚一行
  - Ctrl + Y:向下翻滚一行



### 11、在Windows环境下安装docker

1. 首先进入[官网](https://docs.docker.com/desktop/install/windows-install/)下载安装包
2. 然后不要直接安装下载的安装包，需要根据文档提示下载并启用WSL服务
3. 进入Microsoft的[WSL安装教程网](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)，根据文档提示安装
4. 最后安装第一步下载的安装包



### 12、Oracle Database Docker 镜像制作

#### 相关网址

[oracle/dockerimages](https://github.com/oracle/docker-images)

##### 下载

1. 首先先前往[官网下载](https://github.com/oracle/docker-images)docker-images

##### 上传

1. 将下载的docker-images中的OracleDatabase目录上传至linux上
   1. OracleDatabase目录下的RAC应该是集群
   2. SingleInstance是单节点
   3. 根据需求进入对应目录中的dockerfiles目录下

##### 讲解

1. dockerfiles目录下包含了`11.2.0.2、``12.1.0.2、``12.2.0.1、``18.3.0、``18.4.0、``19.3.0、``21.3.0` 七个Oracle版本的文件夹
2. `buildContainerImage.sh` 用于构建镜像的脚本
3. 执行 `.buildContainerImage.sh -h` 可以看到他的帮助文档，或者前往[官网](https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance)
4. 每个目录对应不通的版本，将你从官网下载的oracle版本放入到对应的目录，然后按照buildContainerImage.sh脚本的帮助文档 执行对应的命令和添加对应的参数

```
Usage: buildContainerImage.sh -v [version] -t [image_name:tag] [-e | -s | -x] [-i] [-o] [container build option]
Builds a container image for Oracle Database.

Parameters:
   -v: version to build
       Choose one of: 11.2.0.2  12.1.0.2  12.2.0.1  18.3.0  18.4.0  19.3.0  21.3.0

   -t: image_name:tag for the generated docker image
   -e: creates image based on 'Enterprise Edition'
   -s: creates image based on 'Standard Edition 2'
   -x: creates image based on 'Express Edition'
   -i: ignores the MD5 checksums
   -o: passes on container build option

* select one edition only: -e, -s, or -x

LICENSE UPL 1.0

Copyright (c) 2014,2021 Oracle and/or its affiliates.
```

##### 躲坑

![image-20220828030531150](https://image.kevinkda.cn/md/image-20220828030531150.png)

1. 第一个红圈说明了在执行 `buildContainerImage.sh` 脚本来构建每个版本的镜像时跟的参数，比如11g是-x，12c可以是-e也可以是-s

2. 第二个红圈要特别注意，需要将下载下来额Oracle包的名字改成 `linuxx64__database.zip` 这种格式，19c不需要，直接在官网下载 `Linux x86-64` 这个版本就ok，但是12c和11g不一样，如果遇到下载下来的包名字不对或者在执行脚本时报错找不到包，则需要仔细核查包名字然后修改

3. 其中 18c XE 和 21c XE 的不用下载镜像，其余版本都需要自行下载镜像

4. 11g的版本不能用 `linuxx64__database.zip` 这种格式的包，而是需要 `oracle-xe-11.2.0-1.0.x86_64.rpm.zip` 这个格式的包。

5. 每个包都需要放到对应版本的目录下

6. 以上关于 `包名字` 相关的都可以进入 `每个版本文件夹` 下，然后去查看其中的 `DockerFile` 文件

   ![image-20220828030544357](https://image.kevinkda.cn/md/image-20220828030544357.png)

##### 提醒

1. oracle11g 需要的是 oracle-xe-11.2.0-1.0.x86_64.rpm.zip 这个安装包。

2. 在镜像制作完成后 docker run的时候 要加上 --shm-size="2g" 来设置容日的内存，如果不设置可能会导致容器启动失败

3. sqlplus 出现 `ORA-12547: TNS:lost contact`

   `执行 chmod 6751 $ORACLE_HOME/bin/*`



### 13、Docker部署Oracle19c

#### 相关链接

[Oracle Database Docker 镜像制作](https://confluence.kevinkda.cn:2100/pages/viewpage.action?pageId=1900685)

[docker-compose](https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance)

#### 构建工具

docker-compose

#### 构建步骤

##### 1、拉取镜像

```shell
执行命令：docker pull registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-19c-ee
```

##### 2、创建Copy镜像

```shell
docker run -d -p 1522:1522 --name oracle registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-18.4x
```

##### 3、复制Copy镜像中的文件到本地并赋权

```shell
# 复制Copy镜像中的文件到本地
docker cp oracle:/opt/oracle/oradata /mnt/remote/data/db/oracle/oracle_env_01/oradata
docker cp oracle:/opt/oracle/scripts/startup /mnt/remote/data/db/oracle/oracle_env_01/scripts/
docker cp oracle:/opt/oracle/scripts/setup /mnt/remote/data/db/oracle/oracle_env_01/scripts
# 赋权
chmod 777 oradata/ scripts/
```

##### 4、使用docker-compose启动镜像

```
version: '3.9'
services:
  oracle_env_01:
    container_name: oracle_env_01
    image: registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-19c-ee
    # restart: none
    restart: always
    privileged: true
    hostname: oracle_18x
    network_mode: bridge
    # command: sleep 36000
    # network_mode: host
    # env_file:
    #   - /mnt/remote/docker_compose/env/wiki.js.mysql.env
    environment:
      TZ: 'Asia/Shanghai'
      # ORACLE_SID: ORCLCDB
      # ORACLE_PDB: ORCLPDB1
      ORACLE_PWD: avKtYefWD@X6H3tg
    ports:
      - 1521:1521
      - 5502:5500
    volumes:
      - /etc/localtime:/etc/localtime
      # - /mnt/remote/data/db/oracle/oracle_env_01/oracle:/opt/oracle
      # - /mnt/remote/data/db/oracle/oracle_env_01/init:/docker-entrypoint-initdb.d
      - /mnt/remote/data/db/oracle/oracle_env_01/oradata:/opt/oracle/oradata
      - /mnt/remote/data/db/oracle/oracle_env_01/scripts/startup:/opt/oracle/scripts/startup
      - /mnt/remote/data/db/oracle/oracle_env_01/scripts/setup:/opt/oracle/scripts/setup
    deploy:
      resources:
        limits:
          cpus: '30.0'
          memory: 2g 
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
```

##### 5、查看启动日志

执行命令：**docker logs -f oracle**

##### 6、oracle初始化

**连接oracle，执行命令：**docker exec -it oracle /bin/bash**
连接sysdba，执行命令：**sqlplus / as sysdba**
显示初始化的数据库，执行命令：**show pdbs**
修改 system 的密码，执行命令：**alter user system identified by system;**
修改 sys 的密码，执行命令：**alter user sys identified by sys;**
设置修改的密码永不过期，执行命令：**alter profile default limit password_life_time unlimited;**

##### 额外知识

如果需要解锁某个用户并用该用户的数据库

给某用户授予管理员权限，执行命令：**grant dba to 用户;**
更改密码，执行命令：**alter user 用户 identified by 密码;**
设置密码永不过期，执行命令：**alter profile default limit password_life_time unlimited;**
解锁用户，执行命令：**alter user 用户 account unlock**



### 14、Linux下创建swap文件

1. 创建一个足够大的文件

   `dd if=/dev/sdb1 of=/www/swapfile bs=1024 count=4096000`

   (count的值等于1024 x 你想要的文件大小, 4096000是4G)

2. 把这个文件变成swap文件.

   `mkswap /www/swapfile`

3. 启用这个swap文件

   `swapon /www/swapfile`

4. 在每次开机的时候自动加载swap文件, 需要在 /etc/fstab 文件中增加一行

   `/www/swapfile swap swap defaults 0 0`

5. 查看swap

   `cat /proc/swaps`



### 15、docker设置镜像加速器

```shell
#修改/etc/docker/daemon.json文件
vi /etc/docker/daemon.json
#输入以下内容
{
  "registry-mirrors": [
    "https://emt7vast.mirror.aliyuncs.com",
    "https://docker.mirrors.ustc.edu.cn/",
    "https://hub-mirror.c.163.com/"
  ]
}
```



### 16、Linux安装docker-compose

​	[官网地址](https://docs.docker.com/compose/install/)

1. 安装docker-compose之前，服务器上必须安装好docker。

2. docker-compose安装步骤

   ```shell
   # 国内加速安装
   curl -L https://get.daocloud.io/docker/compose/releases/download/v1.24.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
   # 对二进制文件应用可执行权限
   sudo chmod +x /usr/local/bin/docker-compose
   # 测试安装结果
   docker-compose --version
   ```

3. 安装结果截图

![image-20220907010519845](https://image.kevinkda.cn/md/image-20220907010519845.png)



### 17、Linux环境下网络测速的方法

1. #### 下载安装包进行测试

   1. 使用wget命令下载一个安装包(例如npm包)

      ```shell
      wget http://soft.vpser.net/lnmp/lnmp1.7-full.tar.gz
      ```

      ![image-20220913111903074](https://image.kevinkda.cn/md/image-20220913112232872.png)

2. #### 安装Speedtest进行测试

   Speedtest 是一个用 Python 编写的轻量级 Linux 命令行工具，可基于 Speedtest.net 的基础架构来测量linux服务器网络的上/下行速率！

   1. 安装

      ```shell
      wget https://raw.github.com/sivel/speedtest-cli/master/speedtest.py
      chmod a+rx speedtest.py
      mv speedtest.py /usr/local/bin/speedtest
      chown root:root /usr/local/bin/speedtest
      ```

   2. 运行检测

      1. speedtest

      ```shell
      speedtest
      ```

      ![image-20220913112232872](https://image.kevinkda.cn/md/image-20220913111903074.png)

      2. speedtest --share

      ```shell
      speedtest --share
      ```

      ![image-20220913112447891](https://image.kevinkda.cn/md/image-20220913112447891.png)
      
      打开 speedtest 测试结果的连接，可以显示测试结果的图示
      
      ![image-20220913112621876](https://image.kevinkda.cn/md/image-20220913112621876.png)



### 18、Linux下使用curl发送get/post请求

curl是一个非常实用的、用来与服务器之间传输数据的工具；支持的协议包括 (DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, TELNET and TFTP)，curl设计为无用户交互下完成工作；curl提供了一大堆非常有用的功能，包括代理访问、用户认证、ftp上传下载、HTTP POST、SSL连接、cookie支持、断点续传。

- 发送get请求

```shell
# 不带参数
curl ${url}
# 带参数
curl ${url}?a=1&b=2
```

- 发送post请求

```shell
# 普通请求
curl -X POST -d 'a=1&b=2' ${url}
# 发送json格式请求
curl -H "Content-Type: application/json" -X POST -d '{"abc":123,"bcd":"nihao"}' URL
curl -H "Content-Type: application/json" -X POST -d @test.json URL
```

其中，-H代表header头，-X是指定什么类型请求(POST/GET/HEAD/DELETE/PUT/PATCH)，-d代表传输什么数据。这几个是最常用的。

- 查看所有curl命令： `man curl或者curl -h`
- 请求头：`H,A,e`
- 响应头：`I,i,D`
- cookie：`b,c,j`
- 传输：`F(POST),G(GET),T(PUT),X`
- 输出：`o,O,w`
- 断点续传：`r`
- 调试：`v,--trace,--trace-ascii,--trace-time`



### 19、Redis

- Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

#### Redis 常用命令集

##### 系统相关

```shell
# 将数据同步保存到磁盘
save
# 将数据异步保存到磁盘
bgsave
# 返回上次成功将数据保存到磁盘的Unix时戳
lastsave
# 将数据同步保存到磁盘，然后关闭服务
shundown
############### 远程服务控制
# 提供服务器的信息和统计
info
# 实时转储收到的请求
monitor
# 改变复制策略设置
slaveof
# 在运行时配置Redis服务器
config
############### 安全相关
# 查看是否设置了密码
CONFIG get requirepass
# 设置密码
CONFIG set requirepass "***"
# 查看密码
CONFIG get requirepass
# 验证密码
AUTH ***
```

##### 数据库相关

```shell
# 选择数据库
select 1
# 查看所有keys
keys *
# 查看前缀为"prefix_"的所有keys
keys prefix_*
# 清除当前数据库的所有keys
flushdb
# 清除所有数据库的所有keys
flushall
# 移动当前数据库中的key到dbindex数据库
move(key, dbindex)
# 返回当前数据库中key的数目
dbsize
```

##### 订阅命令

```shell
# 订阅一个或多个符合给定模式的频道
PSUBSCRIBE pattern [pattern ...]
# 查看订阅与发布系统状态。
PUBSUB subcommand [argument [argument ...]]
# 将信息发送到指定的频道。
PUBLISH channel message
# 退订所有给定模式的频道。
PUNSUBSCRIBE [pattern [pattern ...]]
# 订阅给定的一个或多个频道的信息。
SUBSCRIBE channel [channel ...]
# 指退订给定的频道。
UNSUBSCRIBE [channel [channel ...]]
```

##### 事务命令

```shell
# 取消事务，放弃执行事务块内的所有命令。
DISCARD
# 执行所有事务块内的命令。
EXEC
# 标记一个事务块的开始。
MULTI
# 取消 WATCH 命令对所有 key 的监视。
UNWATCH
# 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。
WATCH key [key ...]
```

##### 脚本命令

```shell
# 执行Lua脚本
EVAL script numkeys key [key ] arg [arg ]
# 执行Lua脚本
EVALSHA sha1 numkeys key [key ...\] arg [arg ...]
# 查看指定脚本
SCRIPT EXISTS script [script ...]
# 从脚本缓存中一处所有脚本
SCRIPT FLUSH
# 杀死所有脚本
SCRIPT KILL
# 将脚本添加到脚本缓存中，但不执行
SCRIPT LOAD script
```

##### Redis GEO

- Redis GEO 主要用于存储地理位置信息，并对存储的信息进行操作，该功能在 Redis 3.2 版本新增。

```shell
# 添加地理位置的坐标。
geoadd
# 获取地理位置的坐标。
geopos
# 计算两个位置之间的距离。
geodist
# 根据用户给定的经纬度坐标来获取指定范围内的地理位置集合。
georadius
# 根据储存在位置集合里面的某个地点获取指定范围内的地理位置集合。
georadiusbymember
# 返回一个或多个位置对象的 geohash 值。
geohash
```

##### 对key和value的操作

```shell
# 确认一个key是否存在
exists(key)
# 删除一个key
del(key)
# 返回值的类型
type(key)
# 返回满足给定pattern的所有key
keys(pattern)
# 随机返回key空间的一个
randomkey
# 重命名key
keyrename(oldname, newname)
# 设定一个key的活动时间（s）
expire
# 获得一个key的活动时间
ttl
# 按索引查询
select(index)
```

##### String

- String 是 redis 最基本的类型，一个 key 对应一个 value。
- 一个键最大能存储 512MB。

```shell
# 给数据库中名称为key的string赋予值value
set(key, value)
# 返回数据库中名称为key的string的value
get(key)
# 给名称为key的string赋予上一次的value
getset(key, value)
# 返回库中多个string的value
mget(key1, key2,…, key N)
# 添加string，名称为key，值为value
setnx(key, value)
# 向库中添加string，设定过期时间time
setex(key, time, value)
# 批量设置多个string的值
mset(key N, value N)
# 如果所有名称为key i的string都不存在
msetnx(key N, value N)
# 名称为key的string增1操作
incr(key)
# 名称为key的string增加integer
incrby(key, integer)
# 名称为key的string减1操作
decr(key)
# 名称为key的string减少integer
decrby(key, integer)
# 名称为key的string的值附加value
append(key, value)
# 返回名称为key的string的value的子串
substr(key, start, end)
```

##### Hash

- Redis hash 是一个键值(key=>value)对集合。
- Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
- 每个 hash 可以存储 232 -1 键值对（40多亿）。

```shell
# 向名称为key的hash中添加元素field
hset(key, field, value)
# 返回名称为key的hash中field对应的value
hget(key, field)
# 返回名称为key的hash中field i对应的value
hmget(key, (fields))
# 向名称为key的hash中添加元素field 
hmset(key, (fields))
# 将名称为key的hash中field的value增加integer
hincrby(key, field, integer)
# 名称为key的hash中是否存在键为field的域
hexists(key, field)
# 删除名称为key的hash中键为field的域
hdel(key, field)
# 返回名称为key的hash中元素个数
hlen(key)
# 返回名称为key的hash中所有键
hkeys(key)
# 返回名称为key的hash中所有键对应的value
hvals(key)
# 返回名称为key的hash中所有的键（field）及其对应的value
hgetall(key)
```

##### List 

- Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
- 列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。

```shell
# 在名称为key的list尾添加一个值为value的元素
rpush(key, value)
# 在名称为key的list头添加一个值为value的 元素
lpush(key, value)
# 返回名称为key的list的长度
llen(key)
# 返回名称为key的list中start至end之间的元素
lrange(key, start, end)
# 截取名称为key的list
ltrim(key, start, end)
# 返回名称为key的list中index位置的元素
lindex(key, index)
# 给名称为key的list中index位置的元素赋值
lset(key, index, value)
# 删除count个key的list中值为value的元素
lrem(key, count, value)
# 返回并删除名称为key的list中的首元素
lpop(key)
# 返回并删除名称为key的list中的尾元素
rpop(key)
# lpop命令的block版本
blpop(key1, key2,… key N, timeout)
# rpop的block版本
brpop(key1, key2,… key N, timeout)
# 返回并删除名称为srckey的list的尾元素，并将该元素添加到名称为dstkey的list的头部
rpoplpush(srckey, dstkey)
```

##### Set

- Redis 的 Set 是 string 类型的无序集合。
- 集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
- 若sadd了一个数据两次，根据集合内元素的唯一性，第二次插入的元素将被忽略
- sadd命令
  - 添加一个 string 元素到 key 对应的 set 集合中，成功返回 1，如果元素已经在集合中返回 0。
  - sadd key member

```shell
# 向名称为key的set中添加元素member
sadd(key, member)
# 删除名称为key的set中的元素member
srem(key, member)
# 随机返回并删除名称为key的set中一个元素
spop(key)
# 移到集合元素
smove(srckey, dstkey, member)
# 返回名称为key的set的基数
scard(key)
# member是否是名称为key的set的元素
sismember(key, member)
# 求交集
sinter(key1, key2,…key N)
# 求交集并将交集保存到dstkey的集合
sinterstore(dstkey, (keys))
# 求并集
sunion(key1, (keys))
# 求并集并将并集保存到dstkey的集合
sunionstore(dstkey, (keys))
# 求差集
sdiff(key1, (keys))
# 求差集并将差集保存到dstkey的集合
sdiffstore(dstkey, (keys))
# 返回名称为key的set的所有元素
smembers(key)
# 随机返回名称为key的set的一个元素
srandmember(key)
```

##### Zset

- Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

- 不同的是每个元素都会关联一个double类型的分数。
- Redis正是通过分数来为集合中的成员进行从小到大的排序。

- zset的成员是唯一的,但分数(score)却可以重复。
- zrange根据索引序列查询，zrangebyscore根据score值查询。

- zadd命令
  - 添加元素到集合，元素在集合中存在则更新对应score
  - zadd key score member 



#### Redis 性能测试

##### 语法

redis 性能测试的基本命令如下：

```
redis-benchmark [option] [option value]
```

##### redis 性能测试工具参数

| 序号 | 选项               | 描述                                       | 默认值    |
| :--- | :----------------- | :----------------------------------------- | :-------- |
| 1    | -h                 | 指定服务器主机名                           | 127.0.0.1 |
| 2    | -p                 | 指定服务器端口                             | 6379      |
| 3    | -s                 | 指定服务器 socket                          |           |
| 4    | -c                 | 指定并发连接数                             | 50        |
| 5    | -n                 | 指定请求数                                 | 10000     |
| 6    | -d                 | 以字节的形式指定 SET/GET 值的数据大小      | 2         |
| 7    | -k                 | 1=keep alive 0=reconnect                   | 1         |
| 8    | -r                 | SET/GET/INCR 使用随机 key, SADD 使用随机值 |           |
| 9    | -P                 | 通过管道传输 <numreq> 请求                 | 1         |
| 10   | -q                 | 强制退出 redis。仅显示 query/sec 值        |           |
| 11   | --csv              | 以 CSV 格式输出                            |           |
| 12   | -l（L 的小写字母） | 生成循环，永久执行测试                     |           |
| 13   | -t                 | 仅运行以逗号分隔的测试命令列表。           |           |
| 14   | -I（i 的大写字母） | Idle 模式。仅打开 N 个 idle 连接并等待。   |           |



### 20、Linux日志审计

#### 相关连接

[Linux日志审计系统命令](https://javaforall.cn/230931.html)

[Linux系统加固](https://blog.csdn.net/qq_37561898/article/details/125359226)

#### Linux中常见日志以及位置

| 位置              | 名称                          |
| ----------------- | ----------------------------- |
| /var/log/cron     | 记录了系统定时任务相关的日志  |
| /var/log/auth.log | 记录验证和授权方面的信息      |
| /var/log/secure   | 同上，区别是系统不同          |
| /var/log/btmp     | 登录失败记录，使用lastb查看   |
| /var/log/wtmp     | 登录成功记录，使用last查看    |
| /var/log/lastlog  | 最后一次登录，使用lastlog查看 |
| /var/run/utmp     | 使用w、who、users命令查看     |

​	/var/log/auth.log、/var/log/secure记录验证和授权方面的信息，只要涉及账号和密码的程序都会记录，比如SSH登录，su切换用户，sudo授权，甚至添加用户和修改用户密码都会记录在这个日志文件中

#### 常用审计命令

```shell
# 定位多少IP在爆破root账号
grep "Failed password for root" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more  

# 定位有多少IP在爆破
grep "Failed password" /var/log/secure|grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"|uniq -c

# 爆破用户名的字典是什么
grep "Failed password" /var/log/secure|perl -e 'while($_=<>){ /for(.*?) from/; print "$1\n";}'|uniq -c|sort -nr

# 查看登录成功的IP有哪些
grep "Accepted " /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more

# 登录成功的日志、用户名、IP
grep "Accepted " /var/log/secure | awk '{print $1,$2,$3,$9,$11}' 
```



### 21、chmod命令详解

#### 简介

​	chmod命令主要用于修改、设置文件权限，chmod修改文件权限主要用两种方式：字母法和数字法

#### 字母法

##### 语法

```shell
# (u g o a)
# u user 表示该文件所有者
# g group 表示与该文件的所有者属于同一组者，即用户组
# o other 表示其他用户组
# a all 表示以上三者皆是

# (+ - =)
# + 增加权限
# - 撤销权限
# = 设定权限

# (r w x)
# r read 表示可读取，对于一个目录，如果没有r权限，那么就意味着不能通过ls查看这个目录的内容。
# w write 表示可写入，对于一个目录，如果没有w权限，那么就意味着不能在目录下创建新的文件。
# x excute 表示可执行，对于一个目录，如果没有x权限，那么就意味着不能通过cd进入这个目录。
chmod (u g o a) (+ - =) (r w x) (文件名)
```

##### 用法

```shell
# 设置模式：要分别对u(user), g(group), o(other)设置权限。
# chmod u+rwx, g+rwx, o+rwx filename 改命令说明对filename文件， 赋予user、group、other均有read、write、excute的权限
chmod + 设置模式 + 文件名
```

#### 数字法

数字法是基于字母法的表示

##### 用法

```shell
# 数字组合一般包含三个数字
# 第一个数字对应字母法的用户u（user）
# 第二个数字对应字母法的用户g（group）
# 第三个数字对应字母法的用户o（other）

# r (read) ----------------> 4
# w (write) ----------------> 2
# x (excute) ----------------> 1
chmod + 数字组合 + 文件名
```

##### 示例

```shell
# 数字法：
chmod 777 文件名 
# 对应字母法： 
chmod u+rwx, g+rwx, o+rwx 文件名

# 第一个数字7：代表用户 u 的权限 rwx， 4 ® + 2 (w) + 1 (x) = 7
# 第二个数字7：代表用户 g 的权限 rwx, 4 ® + 2 (w) + 1 (x) = 7
# 第三个数字7：代表用户 o 的权限 rwx, 4 ® + 2 (w) + 1 (x) = 7

# 举例说明：
# 数字法：
chmod 755 filename 
# 对应字母法： 
chmod u+rwx, g+rx, o+rx filename

# 数字法：
chmod 751 filename 
# 对应字母法： 
chmod u+rwx, g+rx, o+x filename

# 数字法：
chmod 765 filename 
# 对应字母法： 
chmod u+rwx, g+rw, o+rx filename
```



### 22、Docker运行Java项目挂载使用外部配置文件

#### 问题

- 打包好的`Java`项目编译成`Docker`镜像，当你的配置文件需要做改动，这个时候你就需要在本地更新配置文件重新打包成`Docker`镜像

#### 解决方案

在Dockerfile的入口点加上`--spring.config.additional-location=/config/application.yml`

**例如**

```dockerfile
FROM openjdk:8-jre-slim
MAINTAINER AlanHuang

ENV PARAMS="--spring.config.additional-location/config/application.yml"

ENV TZ=PRC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./store*.jar /app.jar

ENTRYPOINT ["sh","-c","java -jar $JAVA_OPTS /app.jar $PARAMS"]
```



### 23、Docker固定容器IP

#### 为已存在的容器固定IP

如果需要为已经存在的容器指定IP地址，则可以通过以下步骤操作：

1. 创建一个新的固定IP网络

首先，需要使用以下命令创建一个新的固定IP网络。在这个例子中，我们将网络名设置为 "mynetwork"，IP地址范围为 "172.100.0.2/16"，默认网关为 "172.100.0.1"：

```shell
docker network create --subnet=172.100.0.0/16 --gateway=172.100.0.1 --ip-range=172.100.0.0/16 -d bridge container-network
```

2. 将容器加入新网络

然后，将需要指定IP地址的容器加入这个新网络。使用以下命令将容器 "mycontainer" 加入到 "mynetwork" 网络中，并分配IP地址 "192.168.0.100"：

```shell
docker network connect --ip=192.168.0.100 mynetwork mycontainer
```

现在，容器 "mycontainer" 将在 "mynetwork" 网络中，它的IP地址为 "192.168.0.100"。

请注意，如果容器已加入一个Docker网络中，则必须首先将其从该网络中删除，然后再将其加入到新网络中。使用以下命令将容器从当前Docker网络中删除：

```shell
docker network disconnect bridge mycontainer
```

然后再使用上面的命令将容器加入新网络中。

最后，如果不再需要旧网络，则可以使用以下命令删除它：

```shell
docker network rm old_network
```

#### Docker Compose中定义容器的IP地址

使用networks设置固定IP地址

可以使用Docker Compose的networks设置容器的固定IP地址。例如，使用以下配置文件定义一个名为myapp的服务，并将其IP地址设置为192.168.0.100：

```yml
version: '3'
services:
  myapp:
    build: .
    networks:
      mynetwork:
        ipv4_address: 192.168.0.100
networks:
  mynetwork:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 192.168.0.0/24
```

在这个配置文件中，使用了Docker Compose的networks设置一个名为mynetwork的网络，并将其IP地址设置为192.168.0.100。然后，在myapp服务中，将networks参数设置为mynetwork，将myapp容器加入到这个网络中，并设置它的IP地址为192.168.0.100。最后，IPAM（IP地址管理）配置了一个IP地址段为192.168.0.0/24的子网，以供该网络使用。

#### Dockerfile中设置IP地址

另一种设置容器IP地址的方法是，在Dockerfile中设置IP地址。可以使用ENV命令设置容器的IP地址变量，然后以这个变量为参数启动容器。例如：

Dockerfile:

```dockerfile
FROM ubuntu
ENV MY_IP 192.168.0.100
CMD ["/bin/bash", "-c", "echo My IP address is $MY_IP"]
```

docker-compose.yml:

```yml
version: '3'
services:
  myapp:
    build: .
    command: /bin/bash -c "echo My IP address is $MY_IP"
```

在这个例子中，Dockerfile中定义了一个名为MY_IP的变量，并设置为192.168.0.100。然后，在docker-compose.yml文件中，使用command参数启动容器，并将MY_IP变量替换到命令中。这样，在容器启动时就可以看到应该输出的IP地址了。

#### 使用命令指定容器IP

地址，可以使用Docker的--ip参数指定容器的IP地址。例如，使用以下命令运行一个名为mycontainer的容器，并将其IP地址设为192.168.0.100：

```shell
docker run -d --name=mycontainer --ip=192.168.0.100 myimage
```

请注意，此选项仅在使用Docker网络时才有效。如果容器未连接到Docker网络，则无法使用--ip选项指定IP地址。



### 24、为Linux系统配置静态IP地址

#### 详细步骤

```shell
# 编辑的配置文件需要对应到网卡
# 即你要固定ens33这张网卡的ip，那么就把下方命令替换成vim /etc/sysconfig/network-scripts/ifcfg-ens33
vim /etc/sysconfig/network-scripts/ifcfg-{网卡名}
```

#### 配置文件内容

```properties
# 修改：将dhcp修改为static，修改后为BOOTPROTO=static
BOOTPROTO="static"
# 修改为yes, 网卡开机自启动
ONBOOT=yes
# 新增：配置静态IP地址，按需配置
IPADDR="xxx.xxx.xxx.xxx"
# 新增：配置子网掩码
NETMASK="255.xxx.xxx.xxx"
# 新增：配置网关
GATEWAY="xxx.xxx.xxx.xxx"
# 新增：配置DNS
DNS1="xxx.xxx.xxx.xxx"
```



### 25、使用OpenSSL生成各类证书

#### 相关连接

[OpenSSL官网](https://www.openssl.org/)

#### 生成私钥

```shell
# 该命令将使用RSA算法生成一个私钥，并将其保存到名为`private.key`的文件中。您可以根据需要选择不同的算法和文件名。
openssl genpkey -algorithm RSA -out private.key
```

#### 包含 SSL 证书和私钥的 Keystore 文件

1.生成私钥和证书签署请求（CSR）：

- 生成私钥：
   ```bash
   openssl genpkey -algorithm RSA -out private.key
   ```
- 生成证书签署请求（CSR）：
   ```bash
   openssl req -new -key private.key -out csr.csr
   ```

在生成私钥和 CSR 时，您需要提供一些相关信息，如组织名称、常用名称（通常为域名）等。

2.通过自签名颁发机构（CA）或受信任的 CA 签署证书：您有两个选择来签署证书：  

- a. 自签名证书（仅用于测试和开发）：
  - 使用私钥和 CSR 生成自签名证书：
```bash
 openssl x509 -req -in csr.csr -signkey private.key -out certificate.crt
```
- b. 使用受信任的 CA 颁发机构签署证书：
  - 将 CSR 提交给受信任的 CA 颁发机构，并按照他们的指示获得由 CA 签署的证书。

3.创建 Keystore 文件：

- 将私钥和证书合并到 PKCS12 文件中：
```bash
openssl pkcs12 -export -in certificate.crt -inkey private.key -out keystore.p12 -name "Alias"
```

在上述命令中，将 "Alias" 替换为您要为 Keystore 文件指定的别名。

设置 Keystore 密码：在创建 Keystore 文件时，您需要设置一个密码来保护 Keystore。根据提示输入密码，并记住它



## 四、工具

### 1、Postman客户端中文设置

+ 下载对应版本的 [app.zip](https://gitee.com/hlmd/PostmanCn/releases)
+ 进入 Postman安装目录/版本/resources 目录
+ 将app.zip 复制解压到resources中
+ 重启Postman

### 2、windows环境的Redis启动

- 命令行窗口输入`redis-server.exe redis.windows.conf`
- `Redis-cli.exe`用于连接客户端

### 3、Git统计代码行数

```shell
git log --pretty=tformat: --numstat | awk '{add += $1; subs += $2;loc+=$1 - $2} END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add,subs,loc}'
```

### 4、Git分支介绍及管理

项目采用git flow开发规范

#### main(生产分支)

​	main分支是仓库的主分支，这个分支包含最近发布到生产环境的代码，最近发布的release，这个分支只能从其他分支合并，不能在这个分支直接修改。

#### develop(开发分支)

​	这个分支是我们的主开发分支，包含所有要发布到下一个release的代码，这个主要合并与其他分支，比如feature分支。

#### feature(功能分支)

​	feature分支主要是用来开发一个新的功能，一旦开发完成，直接合并回dev分支进入下一个release。

#### release(发布分支)

​	当你需要发布一个新功能的时候，要基于dev分支创建一个release分支，在release分支测试并修复bug，完成release后，把release合并到main和develop分支。

#### hotfix(补丁分支)

​	当我们在生产环境发现新的bug的时候，我们需要基于main分支创建一个hotfix分支，然后在hotfix分支上修复Bug，完成hotfix后，我们把hotfix分支合并回main和dev分支。

#### 具体使用细节

​	当我们新建git仓库之后，默认会创建一个主分支也就是main分支，由于main分支是用于发布生产环境，所有必须保证main上代码的稳定性，所以我们不能直接在main分支上修改提交。

​	我们要基于main分支创建一个dev分支，dev分支用于保存开发好的相对稳定的功能，main分支和dev分支是仓库的常驻分支，一直会保留在仓库中;
​	当新的开发任务来了之后，就要编写代码了，我们尽量不要在dev分支上写代码，要保证dev分支的相对稳定，所以这时我要就要基于dev 分支创建一个临时的开发分支 (feature)，然后在开发分支上编写代码等功能开发完之后我们再把开发分支合并到dev上;
​	新功能合并到dev分支之后，我们想把新功能发布到生产环境，首先基于dev分支创建release分支，然后在release分支测试完成之后 (修复完上线前的bug)，把release分别合并到main分支和dev分支;release分支合并到main分支之后，在main分支上打标签用于发布;我们把代码发布到了生产环境，用户在使用的时候给我们反馈了一个bug，这时我们需要基于main分支创建一个hotfix 分支，用于修复bug，bug修好之后，把hotfix 分支分别合并到main分支和dev分支

### 5、查看Windows电脑电池使用报告

- 以管理员方式运行CMD
- 执行命令`powercfg /batteryreport /output C:/Users/AlanHuang/Desktop/battery_report.html`
- 前往桌面查看battery_report.html文件



## 五、中间件

### 1、Nginx中前端请求不在同一个主机上后端无法跳转或报错

现象：前端部署到Docker1的Nginx中，后端部署到Docker2中，当访问前端时，只能访问登录页面，登录成功后的跳转始终无法跳转。

原因：这可能是由于跨域请求问题导致的。需要确保在Nginx中配置允许跨域请求，并且后端服务的CORS（跨域资源共享）设置正确。

解决：

1. 在后端配置正确的CORS
2. 在Nginx配置中添加以下内容

```nginx
location / {
    # 由于后端和nginx不在同一个主机上，这会导致请求存在跨域问题
    # 增加一下内容以解决跨域问题
    add_header 'Access-Control-Allow-Origin' '*';
    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
    add_header 'Access-Control-Allow-Headers' 'DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
    add_header 'Access-Control-Allow-Credentials' 'true';
}
```

