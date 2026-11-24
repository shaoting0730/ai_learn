# 比较 LangChain 和 LlamaIndex

**User:** Anonymous  
**Created:** 11/22/2026 17:40:50  
**Updated:** 11/22/2026 17:42:07  
**Exported:** 11/22/2026 17:47:21  
**Link:** [https://chatgpt.com/c/6b02b8a2-15d4-83ea-acac-ce678c7a77bf](https://chatgpt.com/c/6b02b8a2-15d4-83ea-acac-ce678c7a77bf)  

## Prompt:
2026/11/22 17:41:54

**LangChain 和  LlamaIndex异同？**

## Response:
2026/11/22 17:41:56 · gpt-6

**LangChain 和 LlamaIndex 都是基于大语言模型（LLM）的应用开发框架。** 两者功能有重叠，但设计重点不同。

最核心的区别：

- **LangChain：侧重 LLM 应用编排，尤其是 Agent、工具调用和工作流。**
- **LlamaIndex：侧重数据接入、索引、检索，尤其是 RAG 和知识库。**

## 一、核心异同

| 对比维度 | LangChain | LlamaIndex |
|--------|--------|--------|
| 核心定位 | 大模型应用开发框架 | 大模型数据框架 |
| 主要用途 | 构建 AI 应用和 Agent | 构建知识库和 RAG |
| 模型接入 | 支持 | 支持 |
| Prompt 管理 | 支持 | 支持 |
| 文档加载 | 支持 | 支持 |
| 文档切分 | 支持 | 支持 |
| Embedding | 支持 | 支持 |
| 向量数据库 | 支持 | 支持 |
| RAG | 支持 | 核心优势 |
| Agent | 核心能力 | 支持 |
| 工作流 | LangGraph | Workflows |

## 二、各自的工作流程

### 1\. LangChain：构建 AI Agent

假设你开发一个可以查询天气、搜索网页、回答问题的 AI 助手。

[![LangChain Simplified: AI Orchestration for Builders | Subba Raju Sir Koraseeka posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/c2h_XTni6yRYIh9Hyqb9T6QMAwHllciH9T2wTDrHMcRbMFdS0fdZdktvNAihXKA4Zm_lGBLxIXf7sctS3xMhdst8TsZrV2STzJEAFmnMCAetPG6s3aVxRrDnW2CLqLt9aYHKUUwYgomRrKl6u8M99JNTETw9BwZYQnbkGNVYEPYR8wcRZ-uf8nau0G40Njcf?purpose=fullsize)](https://www.linkedin.com/posts/subbarajuk_langchain-generativeai-aiengineering-activity-7452981510468485121-wQU4)

主要工作流程：

1. 接收用户问题。
2. 大模型分析用户意图。
3. 决定调用哪个工具。
4. 执行工具。
5. 将结果交给大模型。
6. 返回最终答案。

核心是：**让大模型具备调用工具和执行任务的能力。**

### 2\. LlamaIndex：构建 RAG 知识库

假设你开发一个能够阅读企业内部 PDF、Word、Excel 的知识库助手。

[![Build Your First AI Application Using LlamaIndex! - DEV Community](https://images.openai.com/static-rsc-4/f-2QGM-UBlM-s-l1xUb7YOQdQlyT494n9HVaw2oRnyRM0TT_OX2unCjsjt-VbpMQ1SzKolMdkjmeaiONb9MIpNLDMzhWLM8RXAniY4hYBMQQAqRMrQ_NBBqWYogcNN-GZ0c7x_lyAWfxqPDsrQU9d1f5Ag5h5aX6T0rWYG9VcqubzbAt72Vvj3QI6nvw7rH4?purpose=fullsize)](https://dev.to/pavanbelagatti/build-your-first-ai-application-using-llamaindex-1f9)

主要工作流程：

1. 加载 PDF、Word 等文档。
2. 文档解析与切分（Chunking）。
3. 使用 Embedding 模型向量化。
4. 保存到向量数据库。
5. 用户提问时检索相关内容。
6. 将检索结果交给大模型生成答案。

核心是：**让大模型能够利用外部数据和知识回答问题。**

## 三、两者是什么关系？

它们不是竞争关系，而是可以组合使用的。

例如：

**用户提出问题**

**LangChain / LangGraph**

Agent 决策、任务编排、工具调用

**LlamaIndex**

文档检索、知识库查询、RAG

**向量数据库**

**大语言模型（LLM）**

**生成最终答案**

## 四、应该学习哪个？

我的建议：

| 你的目标 | 优先学习 |
|--------|--------|
| 理解 RAG 原理 | LlamaIndex |
| 开发企业知识库 | LlamaIndex |
| 开发 AI Agent | LangChain |
| 多 Agent 协作 | LangChain + LangGraph |
| 复杂 AI 工作流 | LangGraph |
| 完整 AI 应用 | 两者结合 |

**学习顺序建议：**

1. 先理解 RAG 的原理。
2. 学习 LlamaIndex，动手搭建一个知识库。
3. 学习 LangChain，掌握模型调用、工具调用。
4. 学习 LangGraph，构建复杂 Agent。

## 五、官方资源

- [LangChain 官方文档](https://docs.langchain.com/?utm_source=chatgpt.com)
- [LlamaIndex 官方文档](https://developers.llamaindex.ai/?utm_source=chatgpt.com)
- [LangChain GitHub](https://github.com/langchain-ai/langchain?utm_source=chatgpt.com)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index?utm_source=chatgpt.com)

**一句话记忆：**

LangChain 解决的是「如何让大模型完成任务」，LlamaIndex 解决的是「如何让大模型找到并利用外部知识」。



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)