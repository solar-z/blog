---
layout: post
cid: 32
title: 试图理解javascript
slug: 32
date: 2021/08/18 16:36:00
updated: 2022/03/09 23:33:58
status: publish
author: solar-
categories: 
  - 默认分类
tags: 
customSummary: 
mathjax: auto
noThumbInfoStyle: default
outdatedNotice: no
reprint: standard
thumb: 
thumbChoice: default
thumbDesc: 
thumbSmall: 
thumbStyle: default
---


前端好难
!!!
<h2 >函数对局部变量的捕获</h2>
<ul>
<li>在c++中，普通函数不会出现这个问题，lambda函数才会捕获局部变量。如果是值捕获，那么只在lambda定义时捕获一次值，之后便不再改变。如果是引用捕获，那c++会记住那个局部变量的地址，在运行时捕获它的值。（注意不是记住名字，所以即使后面调用的环境中有同名但不同地址的第二个变量，捕获的也还是原来定义时环境下的那个变量）</li>
<li>在javascript中，所有的函数都可以认为是c++中的lambda，也就是意味着函数本身也是可以用来赋值的变量。js中所有局部变量的捕获都是引用捕获。如果被捕获的局部变量不是this，而是普通变量，那么和c++中一样，都是记住变量的地址然后再运行时捕获它的值。如果被捕获的局部变量名字叫this，那么此时情况变得比较特别，javascript中认为this变量是一种”环境“，代表着函数运行时所处的环境，所以在不同对象中调用同一个函数时，其中的this变量的值会是不同的，具体情况如下：</li>

</ul>
<pre><code class='language-javascript' lang='javascript'>      var x={
        b:789342,
        fun(){
          console.log(this.b);
        }
      }
      var a={
        b:1,
        f:x.fun,
      };
      var c={
        b:2,
        f:x.fun,
      }
      a.f();
      c.f();
</code></pre>
<p>输出结果为1和2。显然a.f()中的this.b取了a中的b成员变量的值，也就是意味着此时的this为a。</p>
<pre><code class='language-javascript' lang='javascript'>      var b=1;
      var fun =function(){
        console.log(b);
      };
      var a=function(c){
        var b=2;
        console.log(&quot;fake&quot;+b);
        c();
      };
      a(fun);
</code></pre>
<p>输出结果为fake2和1。显然b一直都是fun定义时捕获的b，即使后来定义了同名b也一样。</p>

!!!