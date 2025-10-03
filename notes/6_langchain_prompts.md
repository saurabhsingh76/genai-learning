# LangChain Prompts - Complete Guide

A comprehensive guide to understanding and implementing prompts in LangChain for building robust conversational AI applications.

## Table of Contents

1. [Introduction to Prompts](#introduction-to-prompts)
2. [Understanding Temperature Parameter](#understanding-temperature-parameter)
3. [Static vs Dynamic Prompts](#static-vs-dynamic-prompts)
4. [Prompt Templates](#prompt-templates)
5. [Messages in LangChain](#messages-in-langchain)
6. [Chat Prompt Templates](#chat-prompt-templates)
7. [Message Placeholders](#message-placeholders)
8. [Best Practices](#best-practices)

## Introduction to Prompts

**What is a Prompt?**
A prompt is simply the message you send to a Large Language Model (LLM) to initiate an interaction. It's the input text that guides the AI's response.

**Why are Prompts Important?**
- LLM output is highly dependent and sensitive to prompt phrasing
- Small changes in prompts can significantly alter the AI's response
- Proper prompt engineering ensures consistent and reliable AI behavior
- Critical for building production-ready AI applications

**Types of Prompts:**
- **Text-based prompts**: Most common type (focus of this guide)
- **Multi-modal prompts**: Images, audio, video (brief mention)

## Understanding Temperature Parameter

The temperature parameter controls the randomness and creativity of LLM responses:

### Temperature = 0 (Deterministic)
- Same input always produces the same output
- Ideal for applications requiring consistency (factual queries, structured responses)
- Perfect for production systems where predictability is crucial

### Temperature = 1.5-2 (Creative)
- Same input produces varied, creative outputs
- Great for brainstorming, creative writing, generating diverse content
- Higher variability in responses

**When to Use Which:**
- **Low temperature (0-0.3)**: Customer support, data analysis, factual Q&A
- **High temperature (1.0-2.0)**: Content creation, brainstorming, artistic applications

## Static vs Dynamic Prompts

### Static Prompts - The Problem

**Definition:** Directly hardcoding prompts or allowing users complete control over prompt content.

**Issues:**
- **Inconsistent User Experience**: Different users phrase prompts differently
- **Quality Control**: Users might create ineffective or problematic prompts
- **Application Goals**: Hard to ensure specific output characteristics
- **Hallucination Risk**: Poorly constructed prompts can lead to inaccurate responses

**Example of Static Prompt:**
```
User input: "Write a summary of the Attention paper"
```

### Dynamic Prompts - The Solution

**Definition:** Using predefined templates with placeholders filled by structured user inputs.

**Benefits:**
- **Consistent Output Quality**: Template ensures standardized responses
- **Better User Experience**: Guided inputs reduce user confusion  
- **Application Control**: Maintain specific output characteristics
- **Reduced Errors**: Structured inputs minimize prompt-related issues

**Example Structure:**
Instead of free-form text, provide:
- **Dropdown 1**: Paper selection (pre-defined list)
- **Dropdown 2**: Explanation style (Simple, Math-heavy, Code-heavy)
- **Dropdown 3**: Length preference (Short, Medium, Long)

## Prompt Templates

### What are Prompt Templates?

LangChain's `PromptTemplate` class enables creation of dynamic prompts with placeholders that get filled at runtime.

### Key Features

**1. Template Structure:**
- Define template strings with placeholders: `{variable_name}`
- Specify input variables required
- Fill placeholders dynamically at runtime

**2. Validation (Optional):**
- `validate_template=True` parameter
- Automatically checks if all placeholders are provided
- Prevents runtime errors by catching issues during development

**3. Reusability:**
- Save templates as JSON files using `template.save("template.json")`
- Load templates using `load_prompt("template.json")`
- Share templates across different parts of application
- Keeps code clean and organized

**4. LangChain Integration:**
- Seamlessly works with LangChain Chains
- Can combine template + model into single operation
- Example: `chain = template | model`

### Advantages over F-strings

1. **Built-in Validation**: Catches missing variables early
2. **Serialization**: Save/load templates from files  
3. **Chain Integration**: Works with LangChain's ecosystem
4. **Error Handling**: Better debugging capabilities

### Example Template Structure

```
Template: "Please summarize the research paper titled {paper_input} with the following specifications:
- Explanation style: {style_input}  
- Explanation length: {length_input}

Requirements:
- Include relevant mathematical equations if present
- Explain concepts using simple, intuitive examples
- Add analogies where applicable
- If information is not available, state 'Insufficient information available'"

Input Variables: ["paper_input", "style_input", "length_input"]
```

## Messages in LangChain

### The Context Problem

Basic chatbots lose conversation context. When a user asks a follow-up question, the AI doesn't remember previous exchanges, leading to:
- Broken conversation flow
- Inability to reference prior context
- Poor user experience

### Solution: Message Types

LangChain provides three distinct message types to maintain conversation context:

### 1. SystemMessage
**Purpose:** Define the AI's role and behavior at conversation start
**Usage:** Set initial instructions, personality, or expertise domain

**Examples:**
- `"You are a helpful AI assistant"`
- `"You are a knowledgeable doctor. Answer medical queries efficiently"`
- `"You are a coding expert. Provide clear, well-commented code examples"`

### 2. HumanMessage  
**Purpose:** Represent messages sent by the user
**Usage:** All user inputs in conversation

**Examples:**
- `"Tell me about LangChain"`
- `"What's the capital of India?"`
- `"Explain machine learning"`

### 3. AIMessage
**Purpose:** Represent responses from the AI
**Usage:** Store AI's previous responses for context

**Examples:**
- AI's response to user queries
- Generated from `result.content` after LLM invocation

### Message Management

**Creating Message History:**
1. Initialize with `SystemMessage` for role definition
2. Add `HumanMessage` for user input
3. Get LLM response and convert to `AIMessage`
4. Append `AIMessage` to message history
5. Send complete message history for context-aware responses

**Benefits:**
- **Clear Role Identification**: Know who sent each message
- **Context Preservation**: Maintain conversation flow
- **Better AI Understanding**: AI can reference previous exchanges

## Chat Prompt Templates

### Purpose
Create dynamic lists of messages where individual messages contain placeholders, similar to how `PromptTemplate` handles single dynamic messages.

### When to Use
- System messages with dynamic roles: `"You are a helpful {domain} expert"`
- Dynamic user queries: `"Explain {topic} in simple terms"`
- Templates requiring multiple dynamic messages in conversation

### Key Features

**1. Message List Structure:**
- Takes list of message tuples: `(role, template_string)`
- Roles: "system", "human", "ai"
- Template strings can contain placeholders

**2. Dynamic Filling:**
- Use `.invoke({variables})` to fill all placeholders
- Generates properly labeled message objects
- Maintains message type structure

### Syntax Considerations
- Use tuple format `("system", "template")` rather than direct object instantiation
- Ensures placeholders are properly filled during template generation

## Message Placeholders

### Definition
Special placeholders within `ChatPromptTemplate` for dynamically inserting entire lists of messages (chat history) at runtime.

### Use Cases

**1. Returning User Conversations:**
- Customer service scenarios where users return with follow-ups
- Need to load previous conversation context
- Example: User asks for refund, gets confirmation, later asks "Where is my refund?"

**2. Session Management:**
- Load chat history from database/files
- Insert historical context into current conversation
- Maintain continuity across sessions

### Implementation Approach

**1. Structure:**
```
[SystemMessage] -> [MessagePlaceholder for history] -> [Current HumanMessage]
```

**2. Loading History:**
- Retrieve previous messages from storage
- Pass as list to placeholder variable
- LLM gets full conversational context

**3. Benefits:**
- **Complete Context**: AI understands entire conversation history
- **Better Responses**: More accurate and relevant answers
- **User Continuity**: Seamless experience across sessions

## Best Practices

### 1. Choose Right Prompt Type
- **Static prompts**: Only for simple, one-off interactions
- **Dynamic prompts**: For production applications requiring consistency
- **Chat prompts**: For conversational applications

### 2. Temperature Selection
- **Low (0-0.3)**: Factual queries, customer support, data analysis
- **Medium (0.4-0.8)**: General conversation, balanced creativity
- **High (0.9-2.0)**: Creative writing, brainstorming, artistic tasks

### 3. Template Design
- **Clear structure**: Well-defined placeholders and instructions
- **Validation**: Always use validation in development
- **Reusability**: Save complex templates as JSON files
- **Documentation**: Comment template purpose and variables

### 4. Message Management
- **Always use proper message types**: SystemMessage, HumanMessage, AIMessage
- **Maintain history**: Store complete conversation context
- **Clean old history**: Implement history truncation for long conversations
- **Handle edge cases**: Empty history, malformed messages

### 5. Context Management
- **System messages**: Define clear, specific roles
- **History limits**: Avoid sending too much history (token limits)
- **Relevant context**: Only include necessary historical messages
- **Performance**: Consider conversation summarization for very long chats

### 6. Error Handling
- **Template validation**: Catch missing variables early
- **Message structure**: Ensure proper message type usage
- **Fallback responses**: Handle LLM failures gracefully
- **User feedback**: Provide clear error messages to users

### 7. Testing and Optimization
- **Template testing**: Test various input combinations
- **Response consistency**: Verify outputs meet application requirements
- **Performance monitoring**: Track response times and quality
- **Iterative improvement**: Refine templates based on usage patterns

## Conclusion

Understanding LangChain's prompt system is crucial for building reliable AI applications. The progression from static to dynamic prompts, proper message management, and context preservation enables creation of sophisticated, production-ready conversational systems.

**Key Takeaways:**
- Prompts significantly impact AI behavior and output quality
- Dynamic prompts provide better control and consistency than static approaches
- Proper message types and history management enable context-aware conversations  
- Template reusability and validation improve development efficiency
- Temperature selection should match application requirements

