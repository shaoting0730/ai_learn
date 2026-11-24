# 比较三种 RAG!

**User:** Anonymous  
**Created:** 11/22/2026 17:25:28  
**Updated:** 11/22/2026 17:25:41  
**Exported:** 11/22/2026 17:27:21  
**Link:** [https://chatgpt.com/c/6b02b507-d650-83e9-a85c-2615d2effe93](https://chatgpt.com/c/6b02b507-d650-83e9-a85c-2615d2effe93)  

## Prompt:
2026/11/22 17:25:25

Native RAG 和 Advanced RAG 和 Modular RAG 的异同？

## Response:
2026/11/22 17:25:34 · gpt-6

> **已搜索 13 个网站**
>
> 
>
> 思考了 6s

Native RAG、Advanced RAG 和 Modular RAG 都是 **RAG（检索增强生成，Retrieval-Augmented Generation）** 的不同实现思路。

它们最核心的区别是：

- **Native RAG：** 基础型 RAG，解决如何让大模型从外部知识库获取信息。
- **Advanced RAG：** 增强型 RAG，重点解决如何让检索更准确、生成质量更高。
- **Modular RAG：** 模块化 RAG，重点解决如何灵活组合、替换和编排 RAG 的各个环节。

可以先记住一句话：

**Native 关注能不能检索，Advanced 关注检索得好不好，Modular 关注整个系统能不能灵活组合。**

## 一、三者的架构区别

**1\. Native RAG（基础 RAG）**

文档 / 知识库

文本切分 + 向量化

向量检索 Top-K

LLM + 检索结果 → 答案

---

**2\. Advanced RAG（增强 RAG）**

文档预处理 / 优化切分

Query 改写 / 扩展

混合检索（向量 + 关键词）

Rerank（重排序）

LLM + 优化后的检索结果 → 答案

---

**3\. Modular RAG（模块化 RAG）**

Query 模块

检索模块

排序模块

生成模块

知识库模块

评估模块

灵活组合、条件路由、循环检索、多路检索

LLM → 最终答案

以上是概念示意图，并非所有 RAG 系统都必须采用这些组件或固定流程。

## 二、三者详细对比

| 对比维度 | Native RAG | Advanced RAG | Modular RAG |
|--------|--------|--------|--------|
| 中文理解 | 原生/基础 RAG | 增强 RAG | 模块化 RAG |
| 核心思想 | 基础检索生成 | 优化检索质量 | 灵活组合模块 |
| 工作流程 | 固定顺序 | 增强型流水线 | 灵活编排 |
| Query 改写 | 通常没有 | 支持 | 可选模块 |
| 混合检索 | 通常没有 | 常见 | 可组合 |
| Rerank | 通常没有 | 常见 | 可组合 |
| 多路检索 | 通常没有 | 可以支持 | 灵活支持 |
| 循环检索 | 通常没有 | 部分支持 | 可以支持 |
| 系统复杂度 | 低 | 中 | 较高 |
| 灵活性 | 低 | 中 | 高 |

这里有个术语细节：学术文献中更常用的是 **Naive RAG**，而不是 Native RAG。你说的 Native RAG 如果指最基础的原生检索增强生成，可以按照 Naive RAG 来理解。

## 三、用一个实际案例理解

假设你正在开发一个企业内部 AI 客服系统。

用户提问：

> 公司春节期间的请假制度是什么？

知识库中存储着公司的员工手册。

**Native RAG：**

1. 将问题转换为向量。
2. 到向量数据库检索相似内容。
3. 找到 Top-K 文档片段。
4. 将片段和问题一起交给 LLM。
5. LLM 生成答案。

特点：简单直接。

**Advanced RAG：**

1. 改写问题，明确搜索春节期间的请假政策。
2. 使用关键词 + 向量混合检索。
3. 找出相关文档。
4. 使用 Rerank 对结果重新排序。
5. 将最相关的内容交给 LLM。
6. 生成答案。

特点：减少无关信息，提高答案准确性。

**Modular RAG：**

系统根据问题动态决定执行哪些模块：

1. Query 模块：分析用户意图。
2. Routing 模块：判断应该查询人事制度知识库。
3. Retrieval 模块：检索相关制度。
4. Rerank 模块：重新排序。
5. Generation 模块：生成答案。
6. Evaluation 模块：检查答案是否有依据。

如果第一次检索没有找到足够信息，还可以重新改写问题，再次检索。

特点：模块可以根据实际业务需求自由组合。

## 四、它们是什么关系？

可以用下面这张图理解：

**Native / Naive RAG**

基础检索 → 生成

增加检索优化策略

**Advanced RAG**

Query 优化 + 混合检索 + Rerank

进一步模块化和灵活编排

**Modular RAG**

模块拆分 + 灵活组合 + 动态执行

这是技术演进的概念示意，不代表严格的版本升级关系。

需要特别注意：Modular RAG 并不意味着一定比 Advanced RAG 答案准确。它主要提供架构灵活性，最终效果仍取决于模块设计、数据质量和检索策略。三者也不是互斥的，Advanced RAG 的优化策略完全可以放进 Modular RAG 中。\[[Journal Pre-proof](https://www.osti.gov/servlets/purl/2573185?utm_source=chatgpt.com); [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997?utm_source=chatgpt.com); [Chapter 6 · A Simple Guide to Retrieval Augmented Generation](https://www.manning.com/preview/a-simple-guide-to-retrieval-augmented-generation/chapter-6?utm_source=chatgpt.com)\]

## 五、应该怎么学习？

结合 RAG 的技术体系，我建议按这个顺序：

| 顺序 | 学习内容 | 重点掌握 |
|--------|--------|--------|
| 1 | Native RAG | Embedding、文本切分、向量数据库、Top-K |
| 2 | Advanced RAG | Query Rewrite、Hybrid Search、Rerank |
| 3 | Modular RAG | Router、模块编排、多路检索、循环检索 |

其中，建议先真正理解这几个概念：

- **Embedding**：把文本转换成向量。
- **Vector Database**：存储和检索向量。
- **Top-K**：取相似度最高的 K 个结果。
- **Rerank**：对初步检索结果重新评分和排序。
- **Query Rewrite**：让用户的问题更适合检索。

**我的建议：先把 Native RAG 的完整代码跑通，再学习 Advanced RAG，最后接触 Modular RAG。** 不要一开始就研究复杂的 Agentic RAG，否则容易把检索、向量数据库和 Agent 编排几个概念混在一起。

如果想深入研究原始分类，可以阅读这篇经典论文：

Retrieval-Augmented Generation for Large Language Models: A Survey（2024）。



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)