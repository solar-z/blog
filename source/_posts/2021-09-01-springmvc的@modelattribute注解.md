---
layout: post
cid: 26
title: springmvc的@modelattribute注解
slug: 26
date: 2021/09/01 23:19:00
updated: 2022/03/09 23:20:25
status: publish
author: solar-
categories: 
  - 默认分类
tags: 
  - springmvc
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


!!!
<h2 >springmvc @ModelAttribute注解</h2>
<h3 >放在方法前</h3>
<p>在每个handler方法执行之间，执行这个函数，并且把返回值作为value放入model，对应的key设置为注解的value属性，如果没有这个属性，则设置为返回值类型的小写。</p>
<h3 >放在方法参数前</h3>
<p>在执行这个方法之前，寻找model中有没有注解中value属性的key（没有value属性则使用参数类型名的全小写）（显然是被之前的某个有modelattribute注解的方法返回的），如果有则绑定到参数，然后寻找请求中有没有可以注入的对象（比如form表单提交的参数），如果有则注入并绑定model，覆盖之前的值。</p>
<p>其实这个注解可以通过很多种方式绑定参数，比较复杂，上述的只是常见两种的情况。</p>

!!!