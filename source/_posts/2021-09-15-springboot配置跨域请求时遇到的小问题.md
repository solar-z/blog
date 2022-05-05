---
layout: post
cid: 24
title: springboot配置跨域请求时遇到的小问题
slug: 24
date: 2021/09/15 23:17:00
updated: 2022/03/09 23:20:38
status: publish
author: solar-
categories: 
  - 默认分类
tags: 
  - springboot
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
<h2 >springboot  跨域请求</h2>
<p>registration类的allowCredentials函数，参数为Boolean，credential的翻译为证书，但这个函数的实际意义是是否允许前端跨域请求携带cookie（可以理解为在cookie中携带验证信息），只有后端设置为allowCredentials(true)且前端设置为withCredentials: true时，跨域请求才可以使用cookie。</p>
<p>&nbsp;</p>

!!!