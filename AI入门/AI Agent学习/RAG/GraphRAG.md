# 比较三种 RAG!

**User:** Anonymous  
**Created:** 11/22/2026 17:25:28  
**Updated:** 11/27/2026 10:10:10  
**Exported:** 11/27/2026 10:12:55  
**Link:** [https://chatgpt.com/c/6b02b507-d650-83e9-a85c-2615d2effe93](https://chatgpt.com/c/6b02b507-d650-83e9-a85c-2615d2effe93)  

## Prompt:
2026/11/26 11:13:16

GraphRAG 具体解释

## Response:
2026/11/26 11:13:57 · gpt-6

# GraphRAG（图检索增强生成）是什么？

**GraphRAG = Graph + RAG，即知识图谱 + 检索增强生成。**

它是一种结合知识图谱（Knowledge Graph）和大语言模型（LLM）的 RAG 技术。

传统 RAG 主要通过向量相似度查找相关文本片段；GraphRAG 则进一步把文档中的实体、关系和事件组织成知识图谱，让 AI 不仅能找到相关信息，还能理解不同信息之间的关联。

简单理解：

- **普通 RAG：** 从大量文档中寻找相关内容。
- **GraphRAG：** 从大量文档中寻找实体，以及实体之间的关系。

它特别适合回答涉及多个实体、复杂关系、跨文档关联和全局总结的问题。

## 一、先理解普通 RAG 的局限

假设你有一个包含 1 万篇文档的企业知识库。

其中有以下内容：

- OpenAI 开发了 GPT 系列模型。
- GPT 模型使用 Transformer 架构。
- Transformer 最初由 Google 团队在 2017 年提出。
- Google 开发了 Gemini 模型。

用户提问：

> OpenAI 和 Google 在 Transformer 技术方面有什么关联？

普通 RAG 的工作方式：

用户问题

Embedding 向量化

向量数据库检索 Top-K

找到相关文本片段

LLM 生成答案

问题在于：

如果 OpenAI 和 Google 的信息分别存储在不同文档中，普通向量检索可能无法一次性找到所有需要的关联信息。

它主要依据语义相似度检索，不会天然维护一张完整的实体关系网络。

这就是 GraphRAG 想解决的问题。

## 二、GraphRAG 的核心原理

GraphRAG 会先把文档转换成一张知识图谱。

知识图谱由三个核心元素组成：

1. **实体（Entity）：** 人、公司、产品、技术等。
2. **关系（Relationship）：** 实体之间的关联。
3. **描述（Description）：** 对实体或关系的具体说明。

例如，把刚才的内容转换成知识图谱：

## 知识图谱示意

```svg
<svg viewBox="0 0 340 250" width="100%" xmlns="http://www.w3.org/2000/svg"><defs><marker id="arr" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#8B8B8B" stroke-width="1" /></marker></defs><g stroke="#8B8B8B" stroke-width="1.4" fill="none" marker-end="url(#arr)"><path d="M83 48 L128 48" /><path d="M205 48 L251 48" /><path d="M166 68 L166 166" /><path d="M273 68 L273 166" /></g><g fill="currentColor" font-size="9" text-anchor="middle"><text x="105" y="38">开发</text><text x="228" y="38">采用</text><text x="180" y="116">提出架构</text><text x="290" y="116">开发</text></g><g><rect x="9" y="29" width="74" height="38" rx="8" fill="#2563EB" fill-opacity=".15" stroke="#3B82F6" /><rect x="128" y="29" width="77" height="38" rx="8" fill="#16A34A" fill-opacity=".15" stroke="#16A34A" /><rect x="251" y="29" width="78" height="38" rx="8" fill="#9333EA" fill-opacity=".15" stroke="#9333EA" /><rect x="127" y="166" width="78" height="38" rx="8" fill="#D97706" fill-opacity=".15" stroke="#D97706" /><rect x="234" y="166" width="78" height="38" rx="8" fill="#9333EA" fill-opacity=".15" stroke="#9333EA" /></g><g fill="currentColor" font-size="11" font-weight="600" text-anchor="middle"><text x="46" y="53">OpenAI</text><text x="166" y="53">GPT</text><text x="290" y="53">Google</text><text x="166" y="190">Transformer</text><text x="273" y="190">Gemini</text></g></svg>
```

简化关系示意：真实知识图谱会包含更多实体、关系、来源和属性。图中不代表 Transformer 只由 OpenAI 和 Google 使用。

例如：

```text
OpenAI
  └── 开发 → GPT

GPT
  └── 使用 → Transformer

Transformer
  └── 最初由 Google 研究团队提出

Google
  └── 开发 → Gemini
```

这样，系统就不只是知道 GPT、Google、Transformer 这些关键词，还能知道它们之间的关系。

### GraphRAG 的主要处理流程

**原始文档**

PDF、Word、网页、数据库等

**文本切分**

将长文档拆分成文本片段

**LLM 实体和关系提取**

识别人名、公司、产品、技术及其关系

**构建知识图谱**

实体节点 + 关系边 + 属性

**社区发现（Community Detection）**

将关系紧密的实体划分成不同社区

**社区摘要（Community Reports）**

为不同主题的社区生成摘要

**用户提问 → 图谱检索 → LLM 生成答案**

这里有两个重要概念：

- **Community Detection：** 发现知识图谱中关系紧密的实体群体。
- **Community Reports：** 对这些群体进行总结，方便回答涉及大量文档的复杂问题。

这也是微软 GraphRAG 实现中的一个重要特点。

## 三、GraphRAG 有哪些检索方式？

GraphRAG 不只是沿着知识图谱查找关系，还可以根据问题选择不同的检索策略。

微软 GraphRAG 中比较重要的两种方式是：

### 1\. Local Search（局部搜索）

适合回答具体实体及其相关关系的问题。

例如：

> GPT 和 Transformer 有什么关系？

系统可以从 GPT 节点出发，查找与它相关的实体和关系，再结合原始文本片段生成答案。

[![Visualizing graph data with Neo4j Bloom](https://images.openai.com/static-rsc-4/x8O3mO-7UjYbiVipaQVx1uObgd6OEFyW8fjNuX4Zo4NpZ0HEz1s5aoo6m2kKnMy8xWEDDgCBY2S6J2qMeuILYym4WtDI24AkBHF2xLM7CDKQ325K_FJj3-9kJxRBinUCCfPOuqnt7W7HHLOzkEfH8MNEcfDZZQ9meHuaAp8p52UxAsxPY1J6GYKeYKmA_Ccl?purpose=fullsize)](https://neo4j.com/blog/developer/scoobygraph-3/)

### 2\. Global Search（全局搜索）

适合回答整个知识库层面的问题。

例如：

> 总结这 1 万篇 AI 文章中，人工智能领域的主要发展方向。

这种问题很难通过简单的 Top-K 向量检索解决，因为它需要综合大量不同文档的信息。

GraphRAG 可以利用社区摘要，对多个主题社区进行分层总结，再通过 Map-Reduce 思路综合生成答案。

[![Fraud detection using knowledge graph: How to detect and visualize fraudulent activities](https://images.openai.com/static-rsc-4/U1sLrw6szPj6ZCD0X3iL43idhAzSK_7QMqgrGTLs6LG9v0jXH2CtmQ4v6CTZf9ik9rDF3uzfs43ZZOlIiYwHUlZqC-5fqMdxO9lgRyyQVMjusDbTAhI8MBb0ilmX_Jvl0_tMn0cQToWpljTTqV4ZvJsoK8jOh8UR7uWkEaaDyMOfuG0pmOnX9HdUan0vrkFW?purpose=fullsize)](https://www.nebula-graph.io/posts/fraud-detection-using-knowledge-and-graph-database)

简单记忆：

| 搜索方式 | 适合回答的问题 |
|--------|--------|
| Local Search | 某个人、公司、产品与谁有什么关系？ |
| Global Search | 整个知识库有哪些共同主题、趋势和规律？ |

## 四、GraphRAG 和普通 RAG 有什么区别？

| 对比维度 | 普通 RAG | GraphRAG |
|--------|--------|--------|
| 核心技术 | 向量检索 | 知识图谱 + 检索 |
| 数据组织 | 文本片段、向量 | 实体、关系、文本 |
| 检索依据 | 语义相似度 | 实体关系、语义及图结构 |
| 关系理解 | 相对较弱 | 更擅长多实体关联 |
| 跨文档分析 | 有一定能力 | 更适合复杂关联分析 |
| 全局总结 | 相对困难 | 社区摘要辅助全局分析 |
| 构建成本 | 相对较低 | 相对较高 |
| 计算成本 | 相对较低 | 通常更高 |

注意：GraphRAG 并不是完全抛弃向量检索。实际系统可以同时使用向量检索、关键词检索和图谱检索。

## 五、GraphRAG 有什么优缺点？

**优点：**

1. 关系理解能力强：能够找到不同实体之间的关联。
2. 跨文档检索：能够关联分散在不同文档中的信息。
3. 全局分析能力：适合对大量文档进行主题总结。
4. 可解释性：可以通过实体和关系路径追溯信息来源。

**缺点：**

1. 构建成本高：需要提取实体、关系和构建图谱。
2. LLM 调用成本高：初次处理大量文档可能消耗较多 Token。
3. 更新维护复杂：文档更新后，需要考虑图谱的同步更新。
4. 可能产生错误关系：实体识别和关系提取依赖模型质量，需要验证。

## 六、GraphRAG 和其他 RAG 技术是什么关系？

把之前学过的技术放在一起：

## RAG 技术体系

**RAG（检索增强生成）**

**传统检索路线**

(文本检索)

- Native RAG
- Advanced RAG
- Modular RAG
- Sparse / Dense
- Hybrid Search
- Rerank

**图检索路线**

(关系检索)

- GraphRAG
- 知识图谱
- 实体提取
- 关系提取
- 社区发现
- Local / Global Search

**可以组合成 Hybrid GraphRAG**

向量检索 + 关键词检索 + 知识图谱检索

这里要注意：GraphRAG 是一种 RAG 架构思路，不是 Advanced RAG 的下一代版本，也不与 Modular RAG 互斥。它可以被设计成 Modular RAG 中的一个检索模块。

## 七、有哪些值得了解的 GraphRAG 项目？

[![GraphRAG auto-tuning provides rapid adaptation to new domains - Microsoft Research](https://images.openai.com/static-rsc-4/scxV9uQ7bDy7WmejZIuqkF-nv_hrZkDo1_4ctcerwYJ3OvcZ0-uHiRtmFKVidEsiqbyoIXkfuh32ImAw7IYIQp-e-b65WGCw-CyZpKM9QYA3NHnh175UA308zv7QjLNSx0ZZ_SxU1s7-fS7DeyK1Tqte1-MrAQbE_Z0VYDeO7ycroGP5jmcjfCX88zrz0eas?purpose=fullsize)](https://www.microsoft.com/en-us/research/blog/graphrag-auto-tuning-provides-rapid-adaptation-to-new-domains/)

**1\. Microsoft GraphRAG**

微软开源项目，比较经典，重点研究实体提取、知识图谱、社区发现和全局搜索。

[GitHub 源码](https://github.com/microsoft/graphrag?utm_source=chatgpt.com)

---

[![【GitHub每日速递 20251121】LightRAG：简单快速的检索增强生成工具，多项功能革新RAG领域！ - piggy侠 - 博客园](https://images.openai.com/static-rsc-4/Tr7SlZFhWD1fz83RWMVyCcJaiknKGR3ArXedAHQwxsAoXY4dhdEyirbdopcZ5n73ZjBr1IKVflKxc-nbW6ZJ_h8kArHpBk93iGgAvx_zxKCXV-VO8Z2ZO7iWyj-WqwDUo_VIb5vOA4ncJXBwHXTTaQ0J2WobTdQm2sc3n0IyJ2dDgnIxg_cgrZAJ1I5xGy58?purpose=fullsize)](https://www.cnblogs.com/freedom-w/p/19250311)

**2\. LightRAG**

HKUDS 开源项目，强调轻量化和高效检索，可以作为学习图增强 RAG 的另一个案例。

[GitHub 源码](https://github.com/HKUDS/LightRAG?utm_source=chatgpt.com)

---

[![Neo4j Logo Vector Download | Logowik](https://images.openai.com/static-rsc-4/_K4B9Jn-CXmA8hitZqoPMpvp2xQa2x7j93SZpMzoQ2jSrfQmSbpPldqZ1H2ir9hwk-i0cKli57Nqn8HBerND_-Pala6hebtftXUzGwwBinz4c2w0OsyAUgOL3z4WFS7pcueSs6fEeFC25jZ6Wgjq3e7RUzXF508cOPH-A6hLU3Hb3Su-8zoEniRvh_AvfyDq?purpose=fullsize)](https://logowik.com/neo4j-logo-vector-svg-pdf-ai-eps-cdr-free-download-16954.html)

**3\. Neo4j**

图数据库，可以用来存储和查询实体之间的关系，是构建知识图谱应用的重要工具。

[GitHub 源码](https://github.com/neo4j/neo4j?utm_source=chatgpt.com)

## 八、建议你的学习顺序

结合你目前正在学习的 Embedding、向量数据库、Sparse Retrieval、Dense Retrieval 和 Advanced RAG，我建议：

1. 先掌握普通 RAG 的完整流程。
2. 学习知识图谱（实体、关系、节点、边）。
3. 学习 GraphRAG 的实体提取和关系提取。
4. 学习 Local Search 和 Global Search。
5. 最后运行微软 GraphRAG 或 LightRAG 的代码。

**最重要的一点：**

普通 RAG 更像是在图书馆里找相关书页；GraphRAG 则是在找书页的同时，建立人物、公司、技术和事件之间的关系网络。

如果你的问题是「这段文档讲了什么」，普通 RAG 往往就够了。

如果你的问题是「这批文档中，不同公司、人物、技术之间究竟存在什么关系」，GraphRAG 就更值得考虑。



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)